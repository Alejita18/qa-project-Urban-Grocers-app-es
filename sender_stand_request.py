import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados



def post_new_client_kit(kit_body):
    current_headers = data.headers.copy()  #referenciar y copiar los headers
    response = post_new_user(data.user_body)
    token = response.json()['authToken']
    current_headers["Authorization"] = f"Bearer {token}" #llamar el current y agrega la nueva llave authtoken
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS,
                         json=kit_body,
                         headers=current_headers)


