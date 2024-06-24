from django.contrib import admin
from .models import *

class contactFormAdmin(admin.ModelAdmin):
    list_display = ['name','email','number','message']
class teamDetailsAdmin(admin.ModelAdmin):
    list_display = ['team_profile','team_name','designation','experience','phone','email','starting_content']
class propertydetailsAdmin(admin.ModelAdmin):
    list_display = ['property_img','property_name','property_type','property_location','property_price','property_description','property_status','type']
class newdetailsAdmin(admin.ModelAdmin):
    list_display = ['News_Title','News_type','News_By','News_Date','News_paragraph']
class servicedetailsAdmin(admin.ModelAdmin):
    list_display = ['Service_Title','Service_img','Service_Description','Service_gallery','Service_galleries']
class portfoliodetailsAdmin(admin.ModelAdmin):
    list_display = ['portoflio_title','portfolio_small_description','portfolio_image','Portfolio_card_image','portfolio_caption']

# Register your models here.
admin.site.register(contactForm,contactFormAdmin)
admin.site.register(teamDetails, teamDetailsAdmin)
# admin.site.register(properties)
admin.site.register(PropertyDetails,propertydetailsAdmin)
admin.site.register(NewsDetails,newdetailsAdmin)
admin.site.register(ServiceDetails,servicedetailsAdmin)
admin.site.register(PortfolioDetails,portfoliodetailsAdmin)
admin.site.register(CommercialDetails)
admin.site.register(UserProfile)
admin.site.register(Frequentlyaskedquestions)
admin.site.register(clientFeedback)