import datetime

# Datos de la factura
nombre_empresa = 'CarolaTex'
numero_factura = 'PED-001'
fecha = datetime.date.today()

# Datos del los productos
polo = 7.00
cantidad_polo = 3
buzo = 3.50
cantidad_buzo = 4
chompa = 15.00
cantidad_chompa = 2

# Valores finales
total_polo = polo * cantidad_polo
total_buzo = buzo * cantidad_buzo
total_chompa = chompa * cantidad_chompa
iva = 0.19

total = total_polo + total_buzo + total_chompa
total_iva =  total * iva
total_neto = total_iva + total

# Mensaje en consola
print(f'''
Empresa: {nombre_empresa}
Fecha: {fecha}
La Factura: {numero_factura}

Tiene un Subtotal de: {total}
Con IVA del 19%: {total_iva}
Total Final Pagar de: {total_neto}
''')