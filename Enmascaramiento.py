import random

# 1. Enmascarar un correo electrónico
def enmascarar_correo(correo):
    usuario, dominio = correo.split("@")

    if len(usuario) <= 2:
        usuario_oculto = usuario[0] + "*"
    else:
        usuario_oculto = usuario[:2] + "*" * (len(usuario) - 2)

    return usuario_oculto + "@" + dominio


# 2. Enmascarar un número telefónico
def enmascarar_telefono(telefono):
    if len(telefono) <= 4:
        return "*" * len(telefono)

    return telefono[:2] + "*" * (len(telefono) - 4) + telefono[-2:]


# 3. Enmascarar un nombre
def enmascarar_nombre(nombre):
    palabras = nombre.split()
    resultado = []

    for palabra in palabras:
        if len(palabra) == 1:
            resultado.append("*")
        else:
            resultado.append(palabra[0] + "*" * (len(palabra) - 1))

    return " ".join(resultado)


# 4. Enmascarar una edad (¡Nueva función añadida!)
def enmascarar_edad(edad):
    # Convierte la edad a texto y oculta el primer dígito o pon asteriscos
    edad_str = str(edad)
    return "*" + edad_str[1:] if len(edad_str) > 1 else "*"


# 5. Generar datos de ejemplo
def generar_usuario():
    nombres = ["Ana García López", "Carlos Pérez Ruiz", 
               "María Torres Díaz", "Luis Hernández Soto"]

    # Añadimos la edad correspondiente a cada tupla (correo, teléfono, edad)
    usuarios = [
        ("ana.garcia@gmail.com", "5512345678", 28),
        ("carlos.perez@gmail.com", "5587654321", 34),
        ("maria.torres@gmail.com", "5545678912", 22),
        ("luis.hernandez@gmail.com", "5523456789", 40)
    ]

    indice = random.randrange(len(nombres))

    nombre = nombres[indice]
    correo, telefono, edad = usuarios[indice]

    return {
        "nombre": nombre,
        "correo": correo,
        "telefono": telefono,
        "edad": edad,
    }


# 6. Ejecutar el programa
usuario = generar_usuario()

print("DATOS ORIGINALES")
print("Nombre:", usuario["nombre"])
print("Correo:", usuario["correo"])
print("Teléfono:", usuario["telefono"])
print("Edad:", usuario["edad"])

print("\nDATOS ENMASCARADOS")
print("Nombre:", enmascarar_nombre(usuario["nombre"]))
print("Correo:", enmascarar_correo(usuario["correo"]))
print("Teléfono:", enmascarar_telefono(usuario["telefono"]))
print("Edad:", enmascarar_edad(usuario["edad"]))