from django.shortcuts import render
from .models import User
# Create your views here.
def home(request):
    user_data = User.objects.all()
    return render(request, "e_commerce/home.html",{"user_data":user_data})
