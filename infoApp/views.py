from django.shortcuts import render
from django.http import JsonResponse 

# Create your views here.

def info(request):
    """
    """
    visitor_name = request.GET.get("visitor_name", "Guest")
    client_ip = request.META.get("REMOTE_ADDR", "Unknown IP")
    location = "New York" 
    response = {
        "client_ip": client_ip,
        "location": location,
        "greeting": f"Hello, {visitor_name}! The temperature is 11 degrees Celsius in {location}.",
    }

    return JsonResponse(response)