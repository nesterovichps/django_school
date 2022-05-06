from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError


# Create your views here.

def main_view(request):
    return render(request, 'index.html')


def departure_view(request, departure):
    return render(request, 'departure.html')


def tour_view(request, id):
    return render(request, 'tour.html')


def custom_handler_404(request, exception):
    return HttpResponseNotFound('Not Found')


def custom_handler_500(request, exception):
    return HttpResponseServerError('Server dead')
