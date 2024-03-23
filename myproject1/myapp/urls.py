from django.contrib import admin
from django.urls import path,include
from .views import*
urlpatterns = [
    path('',base,name='base'),
    path('login',user_login,name='login'),
    path('signup',register,name='signup'),
    path('base',base,name='base'),
    path('login_page',login_page,name='login_page'),
    path('scrape',scrape_scholarship_data,name='display_scraped_data'),
    path('logger', logger_view, name='logger_view'),
    path('save_logger',save_logger,name='save_logger'),
    path('selected_schemes/', selected_schemes_view, name='selected_schemes'),
]