from django.shortcuts import redirect, render,HttpResponse

from training.models import Training
from .forms import TrainingForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,"index.html")

def training(request):
    trainings = Training.objects.filter(trainer = request.user)
    context = {
        "trainings":trainings
    }
    return render(request, "training.html",context)

def dashboard(request):
    return render(request,"dashboard.html")

def addtraining(request):
    form = TrainingForm(request.POST or None)

    if form.is_valid():
        training = form.save(commit= False)
        training.trainer = request.user
        training.save()

        messages.success(request, "Training created successfully")
        return redirect("index")

    return render(request,"addtraining.html", {"form":form})