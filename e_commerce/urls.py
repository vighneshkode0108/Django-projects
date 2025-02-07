from django.urls import path
from e_commerce import views
urlpatterns = [
    path('admin/', views.home,name='home'),
]