from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import BookingForm
from .models import Booking
from django.http import JsonResponse
from .models import ContactMessage
from datetime import datetime
from django.db import IntegrityError


# Create your views here.

def index (request):

    
    return render (request, 'index.html')

# def booking (request):

#         return render(request, 'booking.html')

def mission(request):
    return render(request, 'mission.html')  


def vision(request):
    return render(request, 'vision.html')  


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Ensure the username is not only numeric
        if username.isnumeric():
            messages.info(request, 'Username cannot be only numbers. Please choose a valid username.')
            return redirect('register')

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')

            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
            except IntegrityError:
                messages.info(request, 'Username already exists. Try another.')
                return redirect('register')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')



def login (request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            messages.info(request, 'Invalid credentials')
            return render (request, 'login.html')

    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')
    

# def book_room(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('booking_success.html')
#         else:
#             return render(request, 'booking.html', {'form': form})

#     else:
#         form = BookingForm()
#         # Provide initial choices for available rooms
#         form.fields['rooms'].queryset = Booking.objects.none()
#         return render(request, 'booking.html', {'form': form})

# def booking_success(request):
#     return render(request, 'booking_success.html')



# def available_rooms(request):
#     room_type = request.GET.get('room_type')
#     checkin_date = request.GET.get('checkin_date')
#     checkout_date = request.GET.get('checkout_date')

#     if room_type and checkin_date and checkout_date:
#         available_rooms = Booking.available_rooms(room_type, checkin_date, checkout_date)
#         return JsonResponse({'available_rooms': list(available_rooms)})
#     return JsonResponse({'error': 'Invalid data'}, status=400)

def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
        else:
            return render(request, 'booking.html', {'form': form})

    else:
        form = BookingForm()
        return render(request, 'booking.html', {'form': form})

def booking_success(request):
    return render(request, 'booking_success.html')

def available_rooms(request):
    room_type = request.GET.get('room_type')
    checkin_date = request.GET.get('checkin_date')
    checkohhut_date = request.GET.get('checkout_date')

    if room_type and checkin_date and checkout_date:
        try:
            checkin_date = datetime.strptime(checkin_date, '%Y-%m-%d').date()
            checkout_date = datetime.strptime(checkout_date, '%Y-%m-%d').date()
        except ValueError:
            return JsonResponse({'error': 'Invalid date format'}, status=400)

        available_rooms = Booking.available_rooms(room_type, checkin_date, checkout_date)
        return JsonResponse({'available_rooms': list(available_rooms)})
    return JsonResponse({'error': 'Invalid data'}, status=400)



def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone", "")  # Optional
        message_content = request.POST.get("message")

        # Save to the database
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message_content
        )
        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")  # Redirect to the same page or another page

    return render(request, "contact.html")

def service_details(request, service_name):
    services ={
        'food-service':{
            'title': 'Food Service / Food Runner',
            'description': ('Details about our food service and food runner options... '
            'Exceptional dining experiences begin with us! Our food service and '
            'food runner team is committed to delivering your meals with promptness '
            'and care. Whether it’s a lavish dinner or a casual snack, we ensure every '
            'plate is served fresh, hot, and delicious. Let us turn every meal into a '
            'delightful memory. Experience premium dining'),


            'image': '/static/assets/images/3629845.jpg',
        },

        'refreshment': {
            'title': 'Refreshment',
            'description': (
        'Take a break and rejuvenate with our refreshing beverages and snacks. '
        'From poolside drinks to energy-packed refreshments, we cater to your '
        'relaxation needs. Dive into a world of flavors and unwind in style – because '
        'you deserve nothing but the best. Feel refreshed!'
      ),
            'image': '/static/assets/images/customer-banner.jpg', 
        },
       'housekeeping': {
    'title': 'Housekeeping',
    'description': (
        'A clean and welcoming environment is our promise. Our dedicated housekeeping '
        'staff ensures your space is spotless, cozy, and hygienic. From tidying up your room '
        'to ensuring every corner sparkles, we strive to make your stay as comfortable as possible. '
        'Your comfort, our priority.'
    ),
    'image': '/static/assets/images/afro-woman-holding-bucket-with-cleaning-items.jpg',  # Add a placeholder
},

'room-security': {
    'title': 'Room Security',
    'description': (
        'Your safety is our utmost priority. With state-of-the-art room security measures, '
        'we ensure you have peace of mind throughout your stay. Our team works tirelessly to create '
        'a secure environment, so you can focus on enjoying your time with us. '
        'Stay safe and sound.'
    ),
    'image': '/static/assets/images/modern-technology-controls-secure-domestic-room-indoors-generated-by-ai.jpg',  # Add a placeholder
},
    }

    service = services.get(service_name,{
        'title': 'Service Not Found',
        'description': 'The service you are looking for does not exist.',
    })
    
    return render(request, 'service_details.html', {'service': service})
