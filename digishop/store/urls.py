from django.urls import path
from .views import home, about, contact_us, test


urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact-us/', contact_us),
    path('test/', test)
]