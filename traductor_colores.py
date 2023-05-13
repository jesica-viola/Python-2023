from googletrans import Translator

def traducir_color(color):
    translator = Translator(service_urls=['translate.google.com'])
    resultado = translator.translate(color, src='en', dest='es')
    return resultado.text

# Ejemplo de traducción de colores
colores_ingles = ['red', 'blue', 'green', 'yellow']
colores_espanol = []

for color in colores_ingles:
    color_traducido = traducir_color(color)
    colores_espanol.append(color_traducido)

# Imprimir los colores en inglés y su traducción al español
for i in range(len(colores_ingles)):
    print(colores_ingles[i], "->", colores_espanol[i])
