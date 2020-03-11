from django.shortcuts import render

def Home(request):
    return render(request, 'olora_frontend/index.html')
