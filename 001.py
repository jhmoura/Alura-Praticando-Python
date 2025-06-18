import re
# -*- coding: utf-8 -*-

texto = str(input("Nome do produto: "))

# Verifica se o texto contém apenas letras, números e espaços
texto2 = texto.lower()  # Converte o texto para minúsculas
texto3 = texto2.strip() # Retira os espaços

print(texto3)