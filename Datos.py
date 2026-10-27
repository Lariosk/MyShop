import random
import secrets

NOMBRES = ["Carlos", "Maria", "Juan", "Ana", "Luis", "Sofia", "Pedro", "Lucia", "Diego", "Valeria"]
APELLIDOS = ["Garcia", "Lopez", "Martinez", "Hernandez", "Perez", "Ramirez", "Torres", "Flores"]
DOMINIOS = ["example.com", "gmail.com", "utn.org"]


def generate_user_data(num_users):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    users = []

    for _ in range(num_users):
        username = f"{random.choice(NOMBRES)}.{random.choice(APELLIDOS)}{random.randint(1, 999)}"
        password = ''.join(secrets.choice(caracteres) for _ in range(8))
        email = f"{username}@{random.choice(DOMINIOS)}"
        users.append((username, password, email))

    return users


if __name__ == "__main__":
    for user in generate_user_data(50):
        print(user)