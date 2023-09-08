from django.urls import path
import views

urlpatterns = [
    # path('', views.landing_page, name='landing_page'),
    path('save_contact/', views.save_contact, name='save_contact'),
    path('get_contacts/', views.get_contacts, name='get_contacts'),
]
