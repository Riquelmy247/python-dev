import requests

link = "https://www.youtube.com/"
resultado = requests.get(link)

print(resultado.text)