from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.
import socket


def home(request):
    return render(request, 'baseApp/home.html')

requestToSocket="None"
def new(request):
    global requestToSocket

    host = '192.168.0.101' 
    port = 80

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    # print("dsafadsfadsfdasfdsafadsfds--------------------------------------")
    # print(requestToSocket)
    client_socket.sendall(bytes(requestToSocket, 'utf-8'))

    data = client_socket.recv(1000).decode()

    

    # print("data : ",data)
    # print("data2 : ",data2)
    client_socket.close()  # close the 
    requestToSocket="None"
    return HttpResponse(data)



def control(request):
    global requestToSocket
    btnValue = request.POST['waterPumpBtnValue']
    response = btnValue
    if btnValue == 'ON':
        requestToSocket="waterPumpON"
    else:
        requestToSocket="waterPumpOFF"
        
    return HttpResponse(response)
