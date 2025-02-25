import sender_stand_request
import data


# Función para cambiar el valor del parámetro firstName en el cuerpo de la solicitud
def post_kit_body(name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body

# Función de prueba positiva
def positive_assert_kit_body(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    user_body = post_kit_body(kit_body)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    user_response = sender_stand_request.post_new_client_kit(user_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor

    assert user_response.json()["name"] == user_body["name"]



# Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
def negative_assert_code_400(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    user_body = post_kit_body(kit_body)

   # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(user_body)

    # Comprueba si el código de estado es 400
    assert response.status_code == 400

    # Comprueba que el atributo code en el cuerpo de respuesta es 400

    # Comprueba el atributo message en el cuerpo de respuesta



# Prueba 1.
# El parámetro name contiene 1 caracter
def test_create_kit_body_1_caracter_in_name():
    positive_assert_kit_body("a")

# Prueba 2.
# El parametro name contiene 511 caracteres
def test_create_kit_body2_511_caracteres_in_name():
    positive_assert_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Prueba 3.
# Error. El parámetro name contiene 0 carácter
def test_create_kit_body3_o_caracteres_in_name():
    negative_assert_code_400("")


# Prueba 4. Error.
# Error. El parámetro name contiene 512 caracteres
def test_create_kit_body4_512_caracteres_in_name():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Prueba 5.
# El parámetro name contiene un string de caracteres especiales
def test_create_kit_body5_caracteres_espaciales_in_name():
    positive_assert_kit_body("№%@")

# Prueba 6.
# El parámetro name contiene espacios
def test_create_kit_body6_con_espacios_in_name():
    positive_assert_kit_body(" A Aaa")

# Prueba 7.
# El parámetro name contiene numeros
def test_create_kit_body7_con_numeros_in_name():
    positive_assert_kit_body("123")

# Prueba 8.
# Error. Falta el parámetro name en la solicitud
def test_create_kit_body8_sin_parametros_en_la_solicitud():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "kit_body"
    kit_body = data.kit_body.copy()
    # El parámetro "name" se elimina de la solicitud
    kit_body.pop("name")
    # Comprueba la respuesta
    negative_assert_code_400(kit_body)


# Prueba 9
# . Error. El tipo del parámetro name: número
def test_create_kit_body9_con_numeros_in_name():
    negative_assert_code_400(123)







