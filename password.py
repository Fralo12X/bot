import random
def get_password(loingitud):
    
   
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    password = ""
    for i in range(loingitud):
        password += random.choice(caracteres)
    return password
