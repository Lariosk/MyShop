import random
import secrets

NOMBRES = ["carlos", "maria", "juan", "ana", "luis", "sofia", "pedro", "lucia", "diego", "valeria"]
APELLIDOS = ["garcia", "lopez", "martinez", "hernandez", "perez", "ramirez", "torres", "flores"]
TELEFONO =["1234567890", "0987654321", "5555555555", "1112223333", "4445556666"]
EDAD = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
DOMINIOS = ["example.com", "gmail.com", "utn.org"]


def generate_user_data(num_users):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    users = []

    for _ in range(num_users):
        username = f"{random.choice(NOMBRES)}.{random.choice(APELLIDOS)}{random.randint(1, 999)}"
        password = ''.join(secrets.choice(caracteres) for _ in range(8))
        email = f"{username}@{random.choice(DOMINIOS)}"
        phone = random.choice(TELEFONO)
        age = random.choice(EDAD)
        users.append((username, password, email, phone, age))

    return users


if __name__ == "__main__":
    for user in generate_user_data(50):
        print(user)