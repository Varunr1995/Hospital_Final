from django.urls import path
from Main_Content.views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('services/', services, name= "services"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('elements/', elements, name="elements"),
    path('news/', news, name="news"),
    path('appointmentform/', appointmentform, name="appointmentform"),
    # path('appointment/', AppointmentView, name='appointmentform'),
]
