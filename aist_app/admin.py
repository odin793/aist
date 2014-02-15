from django.contrib import admin
from aist_app.models import *
# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')


class PictureInline(admin.TabularInline):
    model = Picture


class ManufacturerAdmin(admin.ModelAdmin):
    pass


class NewAdmin(admin.ModelAdmin):
    inlines = (PictureInline,)
    list_display = ('title', 'date_added')


class CompanyTextAdmin(admin.ModelAdmin):
    list_display = ('header',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name',)


class IndexPictureAdmin(admin.ModelAdmin):
    list_display = ('name', 'position',)
    #list_editable = ('name', 'position',)
    #list_display_links = ()


class ContactsAdmin(admin.ModelAdmin):
    pass



class QuestionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Document, DocumentAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(CompanyText, CompanyTextAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(IndexPicture, IndexPictureAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Question, QuestionAdmin)