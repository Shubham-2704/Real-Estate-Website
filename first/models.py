from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    bio = models.TextField()
    email = models.EmailField()
    birthdate = models.DateField(blank=True, null=True)
    contact = models.CharField(max_length=10)
    gender = models.CharField(max_length=20)
    address = models.TextField()

    def str(self): 
        return f"{self.fname,self.lname,self.email}"

class contactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=10)
    message = models.TextField()

class teamDetails(models.Model):
    team_profile = models.ImageField(upload_to='profileimages')
    team_name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    starting_content = models.CharField(max_length=500)
    positions = models.CharField(max_length=30)
    experience = models.IntegerField()
    location = models.CharField(max_length=25)
    practiceArea = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    fax = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    content = models.CharField(max_length=500)
    ending_content = models.CharField(max_length=500)

# class properties(models.Model):
    
#     property_type = models.CharField(max_length=30)
#     property_name = models.CharField(max_length=30)
#     property_location = models.CharField(max_length=30)
#     bedroom = models.IntegerField(default=2)
#     bathroom = models.IntegerField(default=2)
#     area = models.IntegerField(default=2000)
#     property_price = models.IntegerField(default=100000)

# class CustomerDetails(models.Model):
#     client_img = models.ImageField(upload_to='Customer-img')
#     customer_name = models.CharField(max_length=30)
#     customer_designation = models.CharField(max_length=30)

class PropertyDetails(models.Model):
    property_videos = models.URLField(max_length=2000, null=True, default="property video")
    property_img = models.ImageField(upload_to='properties-img',default="agent")
    property_agent_img = models.ImageField(upload_to='propertyagent',default="agent")
    type = models.CharField(max_length=30)
    property_type = models.CharField(max_length=30, default="Buy")
    property_name = models.CharField(max_length=30)
    property_location = models.CharField(max_length=30)
    property_description = models.TextField(max_length=300)
    property_description_2 = models.TextField(max_length=3000, null=True)
    property_id = models.CharField(max_length=100,null=True)
    property_area = models.CharField(max_length=25,null=True)
    property_rooms = models.CharField(max_length=30,null=True)
    property_baths = models.CharField(max_length=30,null=True)
    property_year = models.CharField(max_length=30,null=True)
    property_lots_area = models.CharField(max_length=4,null=True)
    property_dimentions = models.CharField(max_length=20,null=True)
    property_bed = models.CharField(max_length=20,null=True)
    property_price = models.CharField(max_length=15,null=True)
    property_status = models.CharField(max_length=15,null=True)
    property_living_room = models.CharField(max_length=15,null=True)
    property_Garage = models.CharField(max_length=15,null=True)
    property_dinning_area = models.CharField(max_length=15,null=True)
    porperty_bathroom = models.CharField(max_length=15, default="Bathroom")
    property_gym = models.CharField(max_length=15,default="Gym")
    property_garden = models.CharField(max_length=15,default="Garden")
    property_parking = models.CharField(max_length=15,default="parking")
    property_gallery = models.ImageField(upload_to='properties-img',default="gallery")
    property_gallery_2 = models.ImageField(upload_to='properties-img',default="gallery")
    property_gallery_3 = models.ImageField(upload_to='properties-img',default="gallery")
    property_amenities = models.CharField(max_length=15,default="Amenities")
    property_air_conditioner = models.CharField(max_length=15,default="Air-conditioner")
    property_Microwave = models.CharField(max_length=15,default="Microwave")
    property_swimmingpool = models.CharField(max_length=15,default="swimmingpool")
    property_wifi = models.CharField(max_length=15,default="Air-conditioner")
    property_laundry = models.CharField(max_length=15,default="laundry")
    property_indoorgames = models.CharField(max_length=15,default="indoorgames")
    property_outdoorgames = models.CharField(max_length=15,default="outdoorgames")
    property_clubhouse = models.CharField(max_length=15,default="clubhouse")
    property_security = models.CharField(max_length=15,default="24x7 security")
    property_firesafety = models.CharField(max_length=15,default="Fire safety")
    property_basement_parking = models.CharField(max_length=20,default="Basement Parking")
    property_lift = models.CharField(max_length=15,default="Lift")
    number_of_properties = models.CharField(max_length=150, default="25 Properteis")
    property_subarea = models.CharField(max_length=50, default="Gota")
    property_map_location = models.CharField(max_length=1500, null=True)
    # pdf_file = models.FileField(upload_to='pdfs/', null=True, default="E-Broucher")     
    

class CommercialDetails(models.Model):
    commercial_img = models.ImageField(upload_to='commercial-img',default="agent")
    commercial_agent_img = models.ImageField(upload_to='commercialagent',default="agent")
    type = models.CharField(max_length=30)
    commercial_type = models.CharField(max_length=30, default="Buy")
    commercial_name = models.CharField(max_length=30)
    commercial_location = models.CharField(max_length=30)
    commercial_description = models.TextField(max_length=3000)
    commercial_id = models.CharField(max_length=100)
    commercial_area = models.CharField(max_length=25)
    commercial_year = models.CharField(max_length=30)
    commercial_lots_area = models.CharField(max_length=4)
    commercial_dimentions = models.CharField(max_length=20)
    commercial_price = models.CharField(max_length=15)
    commercial_status = models.CharField(max_length=15)
    commercial_reception_area = models.CharField(max_length=15, default="20 X 16 sqrt")
    commercial_dinning_area = models.CharField(max_length=15, default="20 X 16 sqrt")
    commercial_washroom = models.CharField(max_length=15, default="20 X 16 sqrt")
    commercial_gym = models.CharField(max_length=15, default="20 X 16 sqrt")
    commercial_parking = models.CharField(max_length=15, default="20 X 16 sqrt")
    commercial_gallery = models.ImageField(upload_to='commercial-img',default="gallery")
    commercial_gallery_2 = models.ImageField(upload_to='commercial-img',default="gallery")
    commercial_gallery_3 = models.ImageField(upload_to='commercial-img',default="gallery")
    commercial_amenities = models.CharField(max_length=30,default="Amenities")
    commercial_air_conditioner = models.CharField(max_length=30,default="Air-conditioner")
    commercial_powerbackup = models.CharField(max_length=30,null= True,default="Microwave")
    commercial_Rain_Harvesting = models.CharField(max_length=30,default="Rain Harvesting")
    commercial_waterstorage = models.CharField(max_length=30,default="Water Storage")
    commercial_maintainance_staff = models.CharField(max_length=30,default="Maintainance Staff")
    commercial_earthquake_resistant = models.CharField(max_length=30,default="Earthquake Resistant")
    commercial_resevedparking = models.CharField(max_length=30,default="Reserved Parking")
    commercial_visitor_parking = models.CharField(max_length=30,default="Visitor Parking")
    commercial_security = models.CharField(max_length=30,default="24x7 security")
    commercial_firesafety = models.CharField(max_length=30,default="Fire safety")
    commercial_power_backup = models.CharField(max_length=30,default="Power Backup")
    commercial_lift = models.CharField(max_length=30,default="Lift")
    commercial_premium_brandedfitting = models.CharField(max_length=30, default="Premium Branded Fitting")


class NewsDetails(models.Model):
    News_type = models.CharField(max_length=30, default="REAL ESTATE")
    News_Title = models.CharField(max_length=150)
    News_By = models.CharField(max_length=20, default="ADMIN")
    News_Date = models.DateField()
    News_paragraph = models.CharField(max_length=1500)
    News_paragraph_2 = models.CharField(max_length=1500)
    News_img = models.ImageField(upload_to='news-images',default="newsimages")
    News_Sub_Title = models.CharField(max_length=150)
    News_paragraph_3 = models.CharField(max_length=1500)
    News_Sub_Title_2 = models.CharField(max_length=150)
    News_paragraph_4 = models.CharField(max_length=1500)
    News_paragraph_5 = models.CharField(max_length=1500)
    Img_news = models.ImageField(upload_to='news-images',default="newsimages")
    News_paragraph_6 = models.CharField(max_length=1500)
    News_paragraph_7 = models.CharField(max_length=1500)
    
    
class ServiceDetails(models.Model):
    Service_Title = models.CharField(max_length=150)
    Service_Description = models.CharField(max_length=350)
    Service_img = models.ImageField(upload_to='Service-images',default="servicesimages")
    Service_Descp_1 = models.CharField(max_length=2500)
    Service_Descp_2 = models.CharField(max_length=2500)
    Service_gallery = models.ImageField(upload_to='Service-images',default="servicesimages")
    Service_galleries = models.ImageField(upload_to='Service-images',default="servicesimages")
    Service_Descp_3 = models.CharField(max_length=2500)
    Service_Descp_4 = models.CharField(max_length=2500)

class PortfolioDetails(models.Model):
    portoflio_title = models.CharField(max_length=150)
    portfolio_small_description = models.CharField(max_length=350)
    portfolio_image = models.ImageField(upload_to='Portfolio-images',default="portfolioimages")
    portfolio_Descriptiion = models.CharField(max_length=3000)
    Portfolio_card_image = models.ImageField(upload_to='Portfolio-images',default="portfolioimages")
    portfolio_caption = models.CharField(max_length=180)
    portfolio_author_img = models.ImageField(upload_to='Portfolio-images',default="portfolioimages")
    portfolio_author = models.CharField(max_length=100)
    portofolio_founder = models.CharField(max_length=100)
    Portfolio_card_two = models.ImageField(upload_to='Portfolio-images',default="portfolioimages")
    portfolio_caption_two = models.CharField(max_length=180)
    portfolio_author_img_two = models.ImageField(upload_to='Portfolio-images',default="portfolioimages")
    portfolio_author_two = models.CharField(max_length=100)
    portofolio_founder_2 = models.CharField(max_length=100)
    portfolio_Heading_1 = models.CharField(max_length=100)
    portfolio_description_1 = models.CharField(max_length=1500)
    portfolio_Heading_2 = models.CharField(max_length=100)
    portfolio_description_2 = models.CharField(max_length=1500)
    portfolio_Heading_3 = models.CharField(max_length=100)
    portfolio_description_3 = models.CharField(max_length=1500)
    portfolio_Heading_4 = models.CharField(max_length=100)
    portfolio_description_4 = models.CharField(max_length=1500)
    portfolio_Heading_5 = models.CharField(max_length=100)
    portfolio_description_5 = models.CharField(max_length=1500)
    portfolio_Heading_6 = models.CharField(max_length=100)
    portfolio_description_6 = models.CharField(max_length=1500)
    portfolio_Heading_7 = models.CharField(max_length=100)
    portfolio_description_7 = models.CharField(max_length=1500)
    portoflio_Gallery_1 = models.ImageField(upload_to='Portfolio-images',default="portfolioimages")
    portoflio_Gallery_2 = models.ImageField(upload_to='Portfolio-images',default="portfolioimages")
    portfolio_description_end = models.CharField(max_length=2500, default="description ends here")

class Frequentlyaskedquestions(models.Model):
    Faq_question = models.CharField(max_length=300)
    Faq_description = models.CharField(max_length=3000,null=True)
    faq_help = models.CharField(max_length=300)
    faq_contact = models.CharField(max_length=13)
    faq_image = models.ImageField(upload_to='Faq-images',default="faq")
    faq_total_area_sq = models.CharField(max_length=100, default="560")
    faq_apartment_sold = models.CharField(max_length=100, default="197K+")
    faq_constrution = models.CharField(max_length=100, default="200")
    faq_rooms = models.CharField(max_length=500, default="250")

class clientFeedback(models.Model):
    Testimonial = models.CharField(max_length=60,default="Our Testimonial")
    Client_Feedbacks = models.CharField(max_length=60,default="CLIENTS FEEDBACK")
    Client_Feedback = models.CharField(max_length=1500,default="Hello this is feedback")
    Client_image = models.ImageField(upload_to="client_Feeback",default="client-img")
    Client_name = models.CharField(max_length=60,default="Jigar Desai")
    Client_designation = models.CharField(max_length=60,default="Buyer")

class Booking(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    number =models.CharField(max_length=10)
    email = models.EmailField()
    propertyselection = models.CharField(max_length=20)
    amount = models.IntegerField()
    order_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
 
    def __str__(self):
        if self.paid == True:
            return self.fname + " paid"
        else:
            return self.fname + " not paid"
        
class Bookco(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    number =models.CharField(max_length=10)
    email = models.EmailField()
    coselection = models.CharField(max_length=20,null=True)
    amount = models.IntegerField()
    order_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
 
    def __str__(self):
        if self.paid == True:
            return self.fname + " paid"
        else:
            return self.fname + " not paid"