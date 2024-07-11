import random

cMax = "QWERTYUIOPASDFGHJKLZXCVBNM"
cMin = "qwertyuiopasdfghjklzxcvbnm"
num = "0123456789"
cEsp = "!@#$%&*"

composicao = cMax + cMin + num + cEsp
digito = 20

senha = "".join(random.sample(composicao,digito))

print("Senha: " + senha)