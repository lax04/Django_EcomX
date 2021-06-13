from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('about', views.about, name = "AboutUs"),
    path('contact', views.contact, name = "ContactUs"),
    path('tracker', views.tracker, name = "TrackingUs"),
    path('search', views.search, name = "Search"),
    path('prodView/<str:slu>', views.prodView, name = "productView"),
    path('checkout/<str:slug>', views.checkout, name = "CheckUs"),
    path('men',views.men, name="men"),
    path('women',views.women,name="women"),
    path('cart',views.cart,name="cart"),
    path('track_info/<int:o_id>',views.track_info,name="track_info"),
    
]
