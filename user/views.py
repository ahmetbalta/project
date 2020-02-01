#from django.shortcuts import render
#from django.http import Http404
# Create your views here.
from user.meal_maker import MakeMeal
from django.template.response import TemplateResponse

from user.admin import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views import generic

def Home(request):
    body_type_custom_cal = MakeMeal(180, min_cal=12, max_cal=14, body_type='ectomorph')
    meal = body_type_custom_cal.daily_requirements()
    return TemplateResponse(request, 'home.html', {'meal': meal})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'







