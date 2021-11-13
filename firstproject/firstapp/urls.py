from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView, name='home'),
    path('add/', views.Addlaptopview, name='add'),
    path('show/', views.Showlaptopview, name='show'),
    path('updt/<int:update>', views.Updatelaptopview, name='updt'),
    path('del/<int:delete>', views.Deletelaptopview, name='del'),
    path('listing/',views.listing,name='listing'),
]
