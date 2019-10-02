from django.shortcuts import render
from pyfirmata import Arduino


# Configurando Arduino

board = Arduino('/dev/ttyACM0')


# Create your views here.


def home(request):
    return render(request, 'index.html')


def led_on(request):
    state = "ON"
    board.digital[13].write(1)
    return render(request, 'index.html', {'state': state})


def led_off(request):
    state = "OFF"
    board.digital[13].write(0)
    return render(request, 'index.html', {'state': state})
