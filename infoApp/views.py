from django.shortcuts import render
from django.http import JsonResponse 

# Create your views here.

def info(request):
    """
    """
    name= request.GET.get("name", "Guest")
    clientIp = request.META.get("REMOTE_ADDR", "Unknown IP")
    location = "Nigeria" 
    response = {
        "client_ip": clientIp,
        "location": location,
        "greeting": f"Hello, {name}! The temperature is 45 degrees Celsius in {location}.",
    }

    return JsonResponse(response)
