"""Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto y devuelva el valor del producto con un aumento del 5%. Realizar la llamada desde el main.
"""

    
def aplicarAumento(precio:float)->float:
    aumento = (precio*5)/100
    precio_final = precio+aumento
    return precio_final

Final = aplicarAumento(200)

#print(Final)

"""" Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro, un carácter como segundo y otro carácter  como tercero,  
la misma deberá reemplazar cada ocurrencia del segundo parámetro por el tercero y devolver la cantidad de veces que se reemplazo ese carácter  en la cadena
"""
def reemplazarCaracteres(texto:str,carac_1:str,carac_2:str):
    cadena_reemplazada = texto.replace(carac_1,carac_2)
    contador = 0
    for i in texto:
        if(i == carac_1):
            contador+=1

    return cadena_reemplazada,contador



#cadena = "Hoy es un buen diaoo"


#Cadena_Final = reemplazarCaracteres(cadena,"o","s")

#print(Cadena_Final)

"""""Crear una función que se llame ordenarCaracteres que reciba una cadena de caracteres como parámetro  y su responsabilidad es ordenarlos caracteres de manera ascendente dentro de la cadena. 
Ejemplo si le pasamos "algoritmo" la deja como "agilmoort"

 """

def ordenarCaracteres(texto:str):
   
   texto_ordenado = "".join(sorted(texto))
   

   

   return texto_ordenado

cadena = "algoritmo"

Cadena_final = ordenarCaracteres(cadena)
print(Cadena_final)
