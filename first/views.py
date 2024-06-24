from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
import random
import razorpay
# Create your views here.

def wishlist(request):
    return render(request,"wishlist.html")
def error(request):
    return render(request,"404.html")
def about(request):
    teams = teamDetails.objects.all()
    news = NewsDetails.objects.all()
    clientfeedback = clientFeedback.objects.all()
    services = ServiceDetails.objects.filter(Service_Title__in=["Home-Buying", "Home-Selling"])
    data = {
        'teams': teams,
        'news': news,
        'services':services,
        'clientfeedback':clientfeedback
    }
    return render(request,"about.html",{'data':data})
def account(request):
    return render(request,"account.html")
def addlisting(request):
    return render(request,"add-listing.html")
def appointment(request):
    return render(request,"appointment.html")
def comingsoon(request):
    return render(request,"coming-soon.html")
def contact(request):
    if request.method == "POST":
        Name = request.POST.get("name")
        Email = request.POST.get("email")
        Number = request.POST.get("number")
        Message = request.POST.get("message")
        formData = contactForm(name=Name, email=Email, number=Number, message=Message)
        formData.save()
    return render(request,"contact.html")
def faq(request):
    faq_details = Frequentlyaskedquestions.objects.all()
    return render(request,"faq.html",{'faq_details':faq_details})
def area(request, subarea):
    property_by_location = PropertyDetails.objects.all().filter(property_subarea=subarea)
    return render(request,"Area.html",{'property_by_location':property_by_location})
def index(request):
    news = NewsDetails.objects.all()
    clientfeedback = clientFeedback.objects.all()
    services = ServiceDetails.objects.filter(Service_Title__in=["Home-Buying", "Home-Selling"])
    Property_Details = PropertyDetails.objects.all()
    property_by_location = PropertyDetails.objects.all()
    teams = teamDetails.objects.all()
    index = {
       'clientfeedback':clientfeedback,
       'news':news,
       'services':services,
       'Property_Details':Property_Details,
       'teams':teams,
       'property_by_location':property_by_location
    }
    return render(request,"index-3.html",{'index':index})
# def login(request):
#     return render(request,"login.html")
def porfoliodetails(request,portfolioname):
    porfolio_details = PortfolioDetails.objects.all().filter(portoflio_title=portfolioname)
    return render(request,"portfolio-details.html",{'porfolio_details':porfolio_details})
def porfolio(request):
    porfolio_details = PortfolioDetails.objects.all()
    return render(request,"portfolio.html",{'porfolio_details':porfolio_details})
# def register(request):
#     return render(request,"register.html")
def shoplist(request):
    return render(request,"shop-list.html")
def changepassword(request):
    return render(request,"change-password.html")
def shoprightsidebar(request):
    return render(request,"shop-right-sidebar.html")
def shops(request):
    return render(request,"shop.html")
def headerfooter(request):
    return render(request,"header-footer.html")
def property(request):
    TeamData = teamDetails.objects.all()
    random_team = random.choice(TeamData)
    if request.method == 'POST':
        query = request.POST.get('search')
        if query and query != '':
            Property_Details = PropertyDetails.objects.filter(property_name__icontains=query)
        else:
            Property_Details = PropertyDetails.objects.all()
    else:
        Property_Details = PropertyDetails.objects.all()
    # Property_Details = PropertyDetails.objects.all()
    pt_data = {
        'property':Property_Details,
        'teamData':random_team
    }
    return render(request,"shop-grid.html", pt_data)
def sortedproperty(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        if query and query != '':
            Property_Details = PropertyDetails.objects.filter(property_name__icontains=query)
        else:
            Property_Details = PropertyDetails.objects.all()
    else:
        Property_Details = PropertyDetails.objects.all()
    # Property_Details = PropertyDetails.objects.all()
    return render(request,"shop-grid.html",{'property':Property_Details})
def sortedproductdetails(request, name):
    Property_Details = PropertyDetails.objects.all().filter(property_name=name)
    news = NewsDetails.objects.all()
    clientfeedback = clientFeedback.objects.all()
    Property_Detailss = PropertyDetails.objects.all()
    TeamData = teamDetails.objects.all()
    random_team = random.choice(TeamData)
    propertydetails_page = {
        'Property_Details':Property_Details,
        'news':news,
        'clientfeedback':clientfeedback,
        'Property_Detailss':Property_Detailss,
        'teamData':random_team,
    }
    return render(request,"product-details.html",{'propertydetails_page':propertydetails_page})
def sort_by_buy_property(request):
    Property_Details = PropertyDetails.objects.filter(property_type='Buy').order_by('property_name')
    if request.method == 'POST':
        query = request.POST.get('search')
        if query and query != '':
            Property_Details = PropertyDetails.objects.filter(property_name__icontains=query)
        else:
            Property_Details = PropertyDetails.objects.filter(property_type='Buy').order_by('property_name')
    else:
        Property_Details = PropertyDetails.objects.filter(property_type='Buy').order_by('property_name')
    return render(request, 'sortedproperty.html', {'property': Property_Details})
def sort_by_sell_property(request):
    Property_Details = PropertyDetails.objects.filter(property_type='Sell').order_by('property_name')
    if request.method == 'POST':
        query = request.POST.get('search')
        if query and query != '':
            Property_Details = PropertyDetails.objects.filter(property_name__icontains=query)
        else:
            Property_Details = PropertyDetails.objects.filter(property_type='Sell').order_by('property_name')
    else:
        Property_Details = PropertyDetails.objects.filter(property_type='Sell').order_by('property_name')
    return render(request, 'sortedproperty.html', {'property': Property_Details})
def productdetails(request, name):
    Property_Details = PropertyDetails.objects.all().filter(property_name=name)
    news = NewsDetails.objects.all()
    clientfeedback = clientFeedback.objects.all()
    Property_Detailss = PropertyDetails.objects.all()
    TeamData = teamDetails.objects.all()
    random_team = random.choice(TeamData)
    propertydetails_page = {
        'Property_Details':Property_Details,
        'news':news,
        'clientfeedback':clientfeedback,
        'Property_Detailss':Property_Detailss,
        'teamData':random_team,
    }
    return render(request,"product-details.html",{'propertydetails_page':propertydetails_page})
def commercial(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        if query and query != '':
            commercialdetails = CommercialDetails.objects.filter(commercial_name__icontains=query)
        else:
            commercialdetails = CommercialDetails.objects.all()
    else:
        commercialdetails = CommercialDetails.objects.all()
    # commercialdetails = CommercialDetails.objects.all()
    return render(request, "commercial.html",{'commercialdetails':commercialdetails})
    
def commercialdetail(request, commercial_name):
    commercialdetails = CommercialDetails.objects.all().filter(commercial_name=commercial_name)
    news = NewsDetails.objects.all()
    Property_Details = PropertyDetails.objects.all()
    TeamData = teamDetails.objects.all()
    random_team = random.choice(TeamData)
    commercialdetails_page = {
        'commercialdetails':commercialdetails,
        'news':news,
        'Property_Details':Property_Details,
        'teamData':random_team,
    }
    return render(request, "commercial-details.html",{'commercialdetails_page':commercialdetails_page})
    
def team(request):
    teams = teamDetails.objects.all()
    return render(request,"team.html",{'teams':teams})
def teamdetail(request, agent_name):
    teams = teamDetails.objects.all().filter(team_name=agent_name)
    return render(request,"team-details.html",{'teams':teams})
def blogdetails(request, news_name):
    news = NewsDetails.objects.all().filter(News_Title=news_name)
    newss = NewsDetails.objects.all()
    Property_Details = PropertyDetails.objects.all()
    TeamData = teamDetails.objects.all()
    random_team = random.choice(TeamData)
    blogs_details= {
        'news':news,
        'newss':newss,
        'Property_Details':Property_Details,
        'teamData':random_team,
    }
    return render(request,"blog-details.html",{'blogs_details':blogs_details})
def blog(request):
    news = NewsDetails.objects.all()
    return render(request,"blog-grid.html",{'news':news})
def servicedetails(request,service_name):
    services = ServiceDetails.objects.all().filter(Service_Title=service_name)
    return render(request,"service-details.html",{'services':services})
def service(request):
    services = ServiceDetails.objects.all()
    news = NewsDetails.objects.all()
    srvcsdtl = {
        'services':services,
        'news':news
    }
    return render(request,"service.html",{'srvcsdtl':srvcsdtl})
def forgotpassword(request):
    return render(request,"forgot-password.html")
def Booknowform(request):
    return render(request,"Booknow_form.html")
def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('profile')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Invalid Login, Try Again."))
            return redirect('login.html')
    
    else:
        return render(request,'login.html', {})
    
@login_required
def logout_user(request):
    logout(request)
    messages.success(request, ("Logout Successfull !!"))
    return redirect('login.html')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, ("Registration Successfull !!"))
            return redirect('profile')
    else:
        form = RegisterUserForm()
    return render(request,'register.html', {'form':form,})


@login_required
def profile_user(request):
    messages.success(request, ("Login successfull"))
    return render(request,'account.html')

@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'editprofile.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # To keep the user logged in
            # messages.success(request, ("Password Changed successfull"))
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change-password.html', {'form': form})

def booking(request):
    error_message = None
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        propertyselection = request.POST.get('propertyselection')
        amount = request.POST.get('amount')

        print("Amount:", amount)  # Debug print to see the value of 'amount'

        # Check if 'amount' is empty or non-numeric
        if not amount or not amount.isdigit():
            error_message = "Invalid amount. Please enter a valid number."
            return render(request, 'booknow_form.html', {'error_message': error_message})

        try:
            amount_int = int(amount)  # Convert 'amount' to an integer
        except ValueError:
            error_message = "Invalid amount. Please enter a valid number."
            return render(request, 'booknow_form.html', {'error_message': error_message})

        client = razorpay.Client(
            auth=('rzp_test_VQhEfe2NCXbbwI', '2ibreCYL78DA3kjOhobCvz0f'))

        razorpay_payment = client.order.create(
            dict(amount=amount_int * 100, currency='INR'))

        order_id = razorpay_payment['id']

        book = Booking.objects.create(
            name=name,
            number=number,
            email=email,
            propertyselection=propertyselection,
            amount=amount_int,
            order_id=order_id
        )
        book.save()

        razorpay_payment['name'] = name
        razorpay_payment['amount'] = amount_int
        razorpay_payment['order_id'] = order_id
        form = Booking(request.POST or None)
        return render(request, 'booknow_form.html', {'razorpay_payment': razorpay_payment})

    form = Booking()
    return render(request, 'booknow_form.html', {'form': form, 'error_message': error_message})


from django.core.mail import send_mail

def success(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature'],
    }

    client = razorpay.Client(
        auth=('rzp_test_VQhEfe2NCXbbwI', '2ibreCYL78DA3kjOhobCvz0f'))

    try:
        status = client.utility.verify_payment_signature(params_dict)
        razorpay_save = Booking.objects.get(
            order_id=response['razorpay_order_id'])
        razorpay_save.razorpay_payment_id = response['razorpay_payment_id']
        razorpay_save.paid = True
        razorpay_save.save() 
        
        if razorpay_save.paid:
            email = razorpay_save.email  # Getting the email from the saved booking
            client_name = razorpay_save.name  # Assuming 'name' is the client's name
            # You can customize the email message as needed
            subject = 'Payment Successful'
            message = f"Dear {client_name},\n\n" \
                      f"We are writing to inform you that your payment for the booking has been successfully processed. Thank you for choosing us!\n\n" \
                      f"Best regards,\n" \
                      f"Your Wedding Spell Team"
            sender_email = 'flutterer.dev90@gmail.com'  # Replace with your sender email address
            recipient_email = [email]  # Convert to list if needed

            send_mail(subject, message, sender_email, recipient_email, fail_silently=False)

            return render(request, 'success.html')
    except Exception as e:
        # Handle exceptions, for example, logging the error
        print(f"Error occurred: {str(e)}")
        return render(request, 'success.html', {'status': False})
    
def book(request):
    error_message = None
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        coselection = request.POST.get('coselection')
        amount = request.POST.get('amount')
        client = razorpay.Client(
                auth=('rzp_test_VQhEfe2NCXbbwI', '2ibreCYL78DA3kjOhobCvz0f'))

        razorpay_payment = client.order.create(
                dict(amount=amount, currency='INR'))

        order_id = razorpay_payment['id']

        book = Bookco.objects.create(
            name=name,
            number=number,
            email = email,
            coselection = coselection,
            amount = amount,
            order_id = order_id

        )
        book.save()
        razorpay_payment['name'] = name
        razorpay_payment['amount']= amount 
        razorpay_payment['order_id'] = order_id
        form = Bookco(request.POST or None)
        return render(request, 'bookcom.html', {'razorpay_payment': razorpay_payment})
    form = Bookco()
    return render(request,'bookcom.html', {'form': form, 'error_message':error_message})

from django.core.mail import send_mail

def successco(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature'],
    }

    client = razorpay.Client(
        auth=('rzp_test_VQhEfe2NCXbbwI', '2ibreCYL78DA3kjOhobCvz0f'))

    try:
        status = client.utility.verify_payment_signature(params_dict)
        razorpay_save = Bookco.objects.get(
            order_id=response['razorpay_order_id'])
        razorpay_save.razorpay_payment_id = response['razorpay_payment_id']
        razorpay_save.paid = True
        razorpay_save.save()
        
        if razorpay_save.paid:
            email = razorpay_save.email  # Getting the email from the saved booking
            client_name = razorpay_save.name  # Assuming 'name' is the client's name
            # You can customize the email message as needed
            subject = 'Payment Successful'
            message = f"Dear {client_name},\n\n" \
                      f"We are writing to inform you that your payment for the booking has been successfully processed. Thank you for choosing us!\n\n" \
                      f"Best regards,\n" \
                      f"Your Wedding Spell Team"
            sender_email = 'dpoza8125@gmail.com'  # Replace with your sender email address
            recipient_email = [email]  # Convert to list if needed

            send_mail(subject, message, sender_email, recipient_email, fail_silently=False)

            return render(request, 'success.html', {'status': True})
    except Exception as e:
        # Handle exceptions, for example, logging the error
        print(f"Error occurred: {str(e)}")
        return render(request, 'success.html', {'status': False})
