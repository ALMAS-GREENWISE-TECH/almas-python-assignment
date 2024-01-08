from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def result(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        # Perform any processing on user_input here
        return HttpResponse(f'Result: {user_input}')
