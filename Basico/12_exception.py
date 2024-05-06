# Excepciones #

numero1 = 5
numero2 = 1
numero2 = '1'

# --- Try Except --- #
try:
    print(numero1 + numero2)
    print('No se ha producido ningun error')
except:
    # Se ejecuta si se produce una excepcion
    print('Se ha producido un error')



# --- Try Except ELse --- #
try:
    print(numero1 + numero2)
    print('No se ha producido ningun error')
except:
    # Se ejecuta si se produce una excepcion
    print('Se ha producido un error')
else:
    # Se ejecuta si no se produce una excepcion
    print('La ejecucion continua correctamente')



# --- Try Except ELse Finally --- #
try:
    print(numero1 + numero2)
    print('No se ha producido ningun error')
except:
    # Se ejecuta si se produce una excepcion
    print('Se ha producido un error')
else:
    # Se ejecuta si no se produce una excepcion
    print('La ejecucion continua correctamente')
finally:
    # Se ejecuta siempre
    print('La ejecucion continua')


# --- Excepciones por tipo --- #
try:
    print(numero1 + numero2)
    print('No Se ha producido un error')
except ValueError:
    print('Se ha producido un ValueError')
except Exception as err:
    print(f'Se ha producido un error de tipo: {err}')