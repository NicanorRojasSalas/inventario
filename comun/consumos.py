from requests import request
import json

from comun.esquemas import EscribirPrdct

base_url = "https://localhost:8080/"


def login():
    url = base_url + "login"

    auth = {
        'email': 'admin@farmaciadelsur.com',
        'password': 'Carmen123'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = request("POST", url, headers=headers, data=auth)
    if(response.status_code == 200):
        return response.json()['data']['token']

    raise Exception(response.json()['error'])


def print_response(response):
    print(response.text)
    print(response.json())
    print(response.status_code)
    print(response.headers)




def get_task_by_id(id):

    url = base_url + f"tasks/{id}"

    headers = {
        'Authorization': login()
    }

    response = request("GET", url, headers=headers)

    print_response(response)
    

def AgregarProducto(Producto : EscribirPrdct):
    url = base_url + "productos"

    payload = json.dumps(Producto)

    headers = {
        'Authorization':  login(),
        'Content-Type': 'application/json'
    }

    response = request("POST", url, headers=headers, json=payload)

    print_response(response)
    
def ObtenerProductos():
    url = base_url + "productos"

    headers = {
        'Authorization':  login(),
        'Content-Type': 'application/json'
    }

    response = request("GET", url, headers=headers)

    return response.json()




    
