from django.shortcuts import render
from django.views import generic
from .models import Car
from .forms import CarForm, UploadPic
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.core.mail import send_mail


@api_view(['POST'])
def send_email(request):
    rider = self.request.query_params.get('rider', None)
    balance = self.request.query_params.get('balance', None)
    pays_on = self.request.query_params.get('pays_on', None)
    date = self.request.query_params.get('date', None)
    
    
    



class CarsList(generic.ListView):
    # model = Car
    paginate_by = 10
    queryset = Car.objects.order_by('-pk')

class CarDetail(generic.DetailView):
    model = Car
    slug_field = 'slugy'

class CarCreate(LoginRequiredMixin, generic.CreateView):
    login_url = 'home'
    model = Car
    form_class = CarForm

    def form_valid(self, form):
        form.instance.by = self.request.user
        return super().form_valid(form)

class DeleteCar(LoginRequiredMixin, generic.DeleteView):
    model = Car
    slug_field = 'slugy'
    success_url = reverse_lazy('home')

class UpdateCar(LoginRequiredMixin, generic.UpdateView):
    model = Car
    slug_field = 'slugy'
    form_class = CarForm
