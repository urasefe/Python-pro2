import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

a = int(input("parola için belirli bir uzunluk belirleyin"))
b = ""


for i in range(a):
    b += random.choice(characters)

print("şifreniz", b)
