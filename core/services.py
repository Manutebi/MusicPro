from django.http import response
import requests
import json
from requests.api import request
from requests.models import Response


#consumo de api tbk
def generate_request_tbk(url, body):
    try:
        response = requests.post(url, body, headers = { "Tbk-Api-Key-Id": "597055555532", "Tbk-Api-Key-Secret": "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C", "Content-Type": "application/json"}, timeout=None)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.ConnectionError as e:
        response = "No hay respuesta" 
        return response
        
def get_initTrxTBK(monto):

    body = json.dumps({"buy_order": "ordencompra", "session_id": "sesion1234557545", "amount": monto , "return_url": "http://localhost:8000/tbkRes/" })
    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.0/transactions"
    response = generate_request_tbk(url, body)
    if response:
       return response

def get_status_trx(url, token_ws):
    try:
        response = requests.get(url+"/"+token_ws,  headers = { "Tbk-Api-Key-Id": "597055555532", "Tbk-Api-Key-Secret": "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C", "Content-Type": "application/json"}, timeout=None)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.ConnectionError as e:
        response = "No hay respuesta"
        return response

def get_statusTBK(request):

    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.0/transactions/"
    token = request.POST['token_ws']
    response = token 
    try : 
        header = {'Tbk-Api-Key-Id': '597055555532',
            'Tbk-Api-Key-Secret': '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C',
            'Content-Type': 'application/json'}
        autorizar = requests.put(url+token,headers=header).json()
        respuesta = requests.get(url+token,headers=header).json()
        resTrans = respuesta['vci']
        if (resTrans == 'TSY'):
            resTrans = 'Transacción Aprobada'
            resBool = True
        elif (resTrans == 'TSN'):
            resTrans = 'Transaccion Fallida'
            resBool = False
        elif (resTrans == 'TO'):
            resTrans = 'Tiempo máximo excedido para autenticación'
            resBool = False
        elif (resTrans == 'Autenticación abortada'):
            resTrans = 'Autenticación Fallida'
            resBool = False
        elif (resTrans == 'U3'):
            resTrans = 'Error interno en la autenticación'
            resBool = False
        elif (resTrans == 'NP'):
            resTrans = 'No Participa: Probable tarjeta extranjera'
            resBool = False
        elif (resTrans == 'ACS2'):
            resTrans = 'Autenticación fallida extranjera con tarjeta extranjera'
            resBool = False
        else:
            resTrans = 'Ha ocurrido un error con la autenticación'
            resBool = False
        status = respuesta ['status']
        idCompra = respuesta['buy_order']
        response = {'status':status,'idCompra':idCompra,'response':resTrans}

    except: 
        response = "Error: ah ocurrido un problema :c"

    #response = get_status_trx(url, request.POST['token_ws'])
    if response:
       return response



#Consumo de apis Django
def generate_request(url, params={}):
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.ConnectionError as e:
        response = "Error: No existe respuesta del servidor"
        return response

def get_productos():
    response = generate_request("http://127.0.0.1:8000/api/producto/?all.json")
    if response:
        return response

def get_categoria():
    response = generate_request("http://127.0.0.1:8080/api/categoria/?all.json=&format=json")
    if response:
        return response

def get_categoria_id(id):
    url="http://127.0.0.1:8080/api/categoria/"
    payload = {"id": id}
    response = requests.get(url, json=payload)
    if response.status_code == 200:
         return response

def post_categoria(nombre):
    url="http://127.0.0.1:8080/api/categoria/"
    payload = {"nombre": nombre}
    response = requests.post(url, json=payload)
    if response.status_code == 201:
         return response

def delete_categoria(id):
    url="http://127.0.0.1:8080/api/categoria/"
    payload = {"id": id}
    response = requests.delete(url, json=payload)
    if response.status_code == 200:
         return response

def put_categoria(id,nombre):
    url="http://127.0.0.1:8080/api/categoria/"
    payload = {"id": id, "nombre":nombre}
    response = requests.put(url, json=payload)
    print(response)
    if response.status_code == 200:
         return response

#proveedor

def get_proveedor():
    response = generate_request("http://127.0.0.1:8085/api2/proveedor/?all.json=&format=json")
    if response:
        return response

def get_proveedor_id(id):
    url="http://127.0.0.1:8085/api2/proveedor/"
    payload = {"id": id}
    response = requests.get(url, json=payload)
    if response.status_code == 200:
         return response

def post_proveedor(nombre):
    url="http://127.0.0.1:8085/api2/proveedor/"
    payload = {"nombre": nombre}
    response = requests.post(url, json=payload)
    if response.status_code == 201:
         return response

def delete_proveedor(id):
    url="http://127.0.0.1:8085/api2/proveedor/"
    payload = {"id": id}
    response = requests.delete(url, json=payload)
    if response.status_code == 200:
         return response

def put_proveedor(id,nombre):
    url="http://127.0.0.1:8085/api2/proveedor/"
    payload = {"id": id, "nombre":nombre}
    response = requests.put(url, json=payload)
    print(response)
    if response.status_code == 200:
         return response