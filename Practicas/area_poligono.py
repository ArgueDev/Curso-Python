'''
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
 '''

"""
Triángulo: Área = (base x altura) / 2
Cuadrado: Área = lado x lado
Rectángulo: Área = base x altura
"""

def calcular_area(poligono):
  """
  Función que calcula el área de un polígono.

  Parámetros:
    poligono (dict): Diccionario que representa el polígono. Debe contener las claves "tipo" y los datos necesarios para calcular el área según el tipo de polígono.

  Retorno:
    float: El área del polígono.
  """

  if poligono["tipo"] == "triangulo":
    base = poligono["base"]
    altura = poligono["altura"]
    area = (base * altura) / 2
  elif poligono["tipo"] == "cuadrado":
    lado = poligono["lado"]
    area = lado * lado
  elif poligono["tipo"] == "rectangulo":
    base = poligono["base"]
    altura = poligono["altura"]
    area = base * altura
  else:
    raise ValueError(f"Tipo de polígono no válido: {poligono['tipo']}")

  return area


triangulo = {
  "tipo": "triangulo", 
  "base": 5,
  "altura": 4
}

cuadrado = {
  "tipo": "cuadrado",
  "lado": 3
}
rectangulo = {
  "tipo": "rectangulo",
  "base": 6,
  "altura": 4
}

print(f"Área del triángulo: {calcular_area(triangulo)}")
print(f"Área del cuadrado: {calcular_area(cuadrado)}")
print(f"Área del rectángulo: {calcular_area(rectangulo)}")

