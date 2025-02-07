from django.shortcuts import render
from .models import User
# Create your views here.
def home(request):
    user_data = User.objects.all()
    return render(request, 'home.html',{"user_data":user_data})
