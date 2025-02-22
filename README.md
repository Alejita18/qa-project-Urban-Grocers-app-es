# Proyecto Urban Grocers 

## Nombre completo y Cohort
- **Nombre**: Ruby Alejandra Carmona
- **Cohort**: 19

## Descripcion

Este proyecto permite crear usuarios y kits a travez de una API. Incluye pruebas automatizadas par verificar la creacion de nuevos kits con diferentes valores

## Documentacion del proyecto

Tecnologías utilizadas:
- **Python**: Lenguaje principal para le desarrollo de las pruebas.
- **Requests**: Libreria para realizar solicitudes HTTP.
- **Pytest**: Framework utilizado para escribir y ejecutar pruebas automatizadas.
- **ApiDoc**: Para la documentacion de los endpoints.
- **Git*: Control de versiones.

### Prubas implementadas

Se desarrollaron 9 pruebas, siguiendo la lista de comprobaciones:

### Pruebas positivas
1. **Nombre mínimo valido (1 caracter)**: verifica que un nombre de kit con 1 carácter sea aceptado.
2. **Nombre maximo valido (511 carcteres)**: verifica que un nombre de kit con 511 caracteres sea aceptado.
3. **Uso de carácteres especiales**: verifica que nombres con caracteres especiales sean aceptados.
4. **Uso de espacios**: verifica que nombres con espacios sea aceptados.
5. **Uso de números**: verifica que nombres compuestos con números sean aceptados.

#### Pruebas negativas
6. **Nombre vacio**: verifica que un kit con nombre vacio no sea aceptado.
7. **Nombre excede el limite (512 caracteres)**: verifica que un kit con nombre superior a 511 caracteres no sea aceptado.
8. **Parametro 'name' no se pasa en la solicitud**: verifica que la ausencia de ccaracteres en el campo 'name' no sea aceptado.
9. **Tipo de dato incorrecto para 'name'**: verifica que un nombre de kit con tipo de dato incorrecto(ejemplo, números) no sea aceptado.
