from django.shortcuts import render
from django.http import JsonResponse
from fingerprints.models import Fingerprint
import hashlib


def create_fingerprint(request):
    if request.method == "POST":
        curr_user = request.user
        
        canvas = request.POST.get("canvas")
        webgl = request.POST.get("webgl")
        
        combined = f"{webgl}{canvas}"
        
        hashed = hashlib.sha256(combined.encode()).hexdigest()
        
        if not Fingerprint.objects.filter(user=curr_user, hashed=hashed).exists():
                
            fingerprint = Fingerprint()
            fingerprint.hashed = hashed
            fingerprint.user = curr_user
        
            fingerprint.save()
        
        return JsonResponse({"code": 200})
    
    return JsonResponse({"code": 405})
# Create your views here.