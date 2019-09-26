from django.contrib import admin
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin

from greencare.models import Ourteam, ContactDetails, Comment, News, ServicesDeals, TermsAndConditions, Service, \
    Experience


class OurteamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'picture')
    list_display_links = ('name', 'position', 'picture')
    search_fields = ('name', 'position',)
    list_per_page = 10


class OurContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email')
    list_display_links = ('phone', 'email')
    search_fields = ('phone', 'email')
    list_per_page = 10



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    list_display_links = ('name', 'email', 'message',)
    search_fields = ('name', 'email', 'subject', 'message')
    list_per_page = 10


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('newsheading', 'newscontent', 'newsdate', 'newspicture')
    list_display_links = ('newsheading', 'newscontent', 'newsdate', 'newspicture')
    search_fields = ('newsheading', 'newscontent', 'newsdate', 'newspicture')
    list_per_page = 10


class ServicesDealsAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('fullName', 'nameofservice', 'phoneNumber', 'email', 'description', 'accepttermsconditions', )
    list_display_links = ('nameofservice', 'fullName', 'phoneNumber', 'email', 'description',)
    search_fields = ('nameofservice', 'fullName', 'phoneNumber', 'email', 'description',)
    list_filter = ('accepttermsconditions', 'nameofservice', )
    list_per_page = 10


class TermsAndConditionsAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('nameofservice', )
    list_display_links = ('nameofservice', )
    search_fields = ('nameofservice', )
    list_per_page = 10


class ServiceAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('service_name', 'slug', 'button_text')
    list_display_links = ('service_name', )
    search_fields = ('service_name',)
    list_per_page = 10
    prepopulated_fields = {'slug': ('service_name',)}


class ExperienceAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('heading', 'imageattached')
    list_display_links = ('heading', 'imageattached')
    search_fields = ('heading', )
    list_per_page = 10



admin.site.unregister(Group)
admin.site.register(Ourteam, OurteamAdmin)
admin.site.register(ContactDetails, OurContactAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(ServicesDeals, ServicesDealsAdmin)
admin.site.register(TermsAndConditions, TermsAndConditionsAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Experience, ExperienceAdmin)


