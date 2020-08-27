from django.shortcuts import render
from django.http import HttpResponse
from .forms import Contact_info, emp_details

def index(request):
    return HttpResponse("Mission Successful")

def details(request):

    if request.method == 'POST':
        form = Contact_info(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']

            print(name, email, number)
            # return HttpResponse("You form is submitted successfully")
    form = Contact_info()
    return render(request,"form_app/form.html", {'form' : form})

def modform(request):
    if request.method == 'POST':
        form = emp_details(request.POST)
        if form.is_valid():
           form.save()
           print("Done")
            # return HttpResponse("You form is submitted successfully")
    form = emp_details()
    return render(request, "form_app/form.html", {'form': form})