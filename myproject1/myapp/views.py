# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .forms import logger_forms
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Count




def register(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            return redirect('login')  # Replace 'home' with your desired redirect URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('logger_view')  # Replace 'home' with your desired redirect URL
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def base(request):
    scholarships = UserScholarship.objects.values('scholarship__scheme_name').annotate(user_count=Count('user')).order_by('-user_count')
    return render(request, 'base.html', {'scholarships': scholarships})    


def login_page(request):
    data=Scholarship.objects.all()

    return render(request,'scrape.html',{'data':data})


from .models import *
from .models import Scholarship


# Create your views here.
def home(request):
    return  HttpResponse(Scholarship.objects.all())
# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse

def scrape_scholarship_data(request):

    
    data=Scholarship.objects.all()

    data=Scholarship.objects.all()
    


    return render(request,'new.html',{'data':data})
        #else:
           # return None    

'''def logger_view(request):
    scholarships = Scholarship.objects.all()
    if request.method == 'POST':
        selected_scholarships_ids = request.POST.getlist('is_selected')
        for scholarship_id in selected_scholarships_ids:
            UserScholarship.objects.update_or_create(
                user=request.user,
                scholarship_id=scholarship_id,
                defaults={'is_selected': True},
            )
        # Delete UserScholarship objects that were not selected
        UserScholarship.objects.filter(user=request.user).exclude(scholarship_id__in=selected_scholarships_ids).delete()

    user_scholarships = UserScholarship.objects.filter(user=request.user)
    selected_scholarship_ids = [us.scholarship.id for us in user_scholarships if us.is_selected]

    return render(request, 'logger.html', {
        'scholarships': scholarships,
        'selected_scholarship_ids': selected_scholarship_ids,
    })'''


def logger_view(request):
    scholarships = Scholarship.objects.all()
    if request.method == 'POST':
        selected_scholarships_ids = request.POST.getlist('is_selected')
        for scholarship_id in selected_scholarships_ids:
            user_scholarship, created = UserScholarship.objects.update_or_create(
                user=request.user,
                scholarship_id=scholarship_id,
                defaults={'is_selected': True},
            )
            
        # Delete UserScholarship objects that were not selected
        UserScholarship.objects.filter(user=request.user).exclude(scholarship_id__in=selected_scholarships_ids).delete()

    user_scholarships = UserScholarship.objects.filter(user=request.user)
    selected_scholarship_ids = [us.scholarship.id for us in user_scholarships if us.is_selected]

    return render(request, 'logger.html', {
        'scholarships': scholarships,
        'selected_scholarship_ids': selected_scholarship_ids,
        'username': request.user.username,
    })



def save_logger(request):
    form=logger_forms(request.POST)
    if form.is_valid():
        select_values=request.GET.getlist('is_selected')
        for i in select_values:
            i.save()
    return render(request,'logger')


from django.contrib.auth.decorators import login_required

@login_required
def selected_schemes_view(request):
    user_scholarships = UserScholarship.objects.filter(user=request.user, is_selected=True)
    selected_scholarships = [us.scholarship for us in user_scholarships]
    return render(request, 'selected_schemes.html', {'selected_scholarships': selected_scholarships})


from .forms import ImageForm
from .models import Image


