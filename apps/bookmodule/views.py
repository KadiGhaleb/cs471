from django.shortcuts import render
def index(request):
    return render(request, 'bookmodule/index.html') #it will be in template folder
