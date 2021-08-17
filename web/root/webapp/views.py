from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from webapp.models import Command

import logging
import json


@csrf_exempt
def index(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            direction = Command.Direction(data["direction"])
            logging.warning(direction)
            return JsonResponse({}, status=200)
        except:
            logging.warning("boom!!!")
            return JsonResponse({}, status=500)

    return render(request, 'index.html')
