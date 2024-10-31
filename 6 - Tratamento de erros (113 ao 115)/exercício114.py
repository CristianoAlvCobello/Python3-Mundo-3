import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('O Site está indisponivel')
else:
    print('O Site está disponivel')
    