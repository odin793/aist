from django.shortcuts import get_object_or_404
from annoying.decorators import render_to
from aist_app.models import *
# Create your views here.

def paginate(cur_page, N):
    pages_list = []
    margin = 3
    min_gap = 2
    if N <= 20:
        return range(1, N + 1) 

    if (cur_page - margin) - (margin + 1) > min_gap:
        # first pages, gap and middle (or last) pages
        pages_list.extend(range(1, (margin + 1) + 1))
        pages_list.append(0)
        pages_list.extend(range(cur_page-margin, min((cur_page + margin) + 1,
            N + 1)))
    else:
         # very first pages
        pages_list.extend(range(1, (cur_page + margin) + 1))
    
    if (N - margin) - (cur_page + margin) > min_gap:
        # last pages after gap
        pages_list.append(0)
        pages_list.extend(range(N-margin, N + 1))
    else:
        # last pages without gap
        pages_list.extend(range(cur_page + margin + 1, N + 1))
        
    return pages_list


def organize_in_lists(obj_list, l):    # return list of lists of l objects
    result = []
    for i in range(0, len(obj_list), l):
        el = list(obj_list)[i: i+l]  # (0, 1), (2, 3) and so on, for l=2
        result.append(el)
    return result

@render_to('index.html')
def index_page(request):
    company_text = CompanyText.objects.all()[0]
    header, hello_text = (company_text.header, company_text.hello_text)
    index_pictures = organize_in_lists(IndexPicture.objects.all(), 3)
    return {
    	'header': header,
    	'hello_text': hello_text,
    	'index_pictures': index_pictures,
    }

@render_to('contacts.html')
def contacts(request):
    contacts = Contacts.objects.all()[0].contacts
    return {'contacts': contacts,}


@render_to('about.html')
def about(request):
	company_text = CompanyText.objects.all()[0]
	about, activity = (company_text.about, company_text.activity)
	manufacturers = Manufacturer.objects.all()
	certificates = Certificate.objects.all()
	documents = Document.objects.all()
	return {
		'about': about,
		'activity': activity,
		'manufacturers': manufacturers,
		'certificates': certificates,
		'documents': documents,
	}


@render_to('services.html')
def services(request):
	services = Service.objects.all()
	return locals()


@render_to('news.html')
def news_page(request):
    news_per_page = 8
    try:
        # if someone trying to hack, page arg can be anytings,
        # so limit it to length 10. enough for page number
        cur_page = int(request.GET.get('page', '1')[:10])
    except:
        cur_page = 1

    N = int(New.objects.count() / float(news_per_page))
    if cur_page > N and N: # can have db error if cur_page, somehow, is too large
        cur_page = N
    obj_list = New.objects.all()
    lower, upper = ((cur_page - 1) * news_per_page, cur_page * news_per_page)
    obj_for_cur_page = obj_list[lower:upper]
    links_list = paginate(cur_page, N)
    return {
        'obj_list': obj_for_cur_page,
        'cur_page': cur_page,
        'links_list': links_list,
    }

@render_to('exact_new.html')
def exact_new(request, new_id):
    new = get_object_or_404(New, pk=int(new_id))
    pictures_list = list(new.pictures_list.all())
    #files_list = organize_in_lists(pictures_list, 6)
    return {
        'new': new,
        'pictures_list': pictures_list,
    }