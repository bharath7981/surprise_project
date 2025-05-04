from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def main(request):
    return render(request, 'main.html')

def third(request):
    return render(request, 'third.html')
def fourth(request):
    return render(request, 'fourth.html')
def fifth(request):
    return render(request, 'fifth.html')


# Create your views here.
