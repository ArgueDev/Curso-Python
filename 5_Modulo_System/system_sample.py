# Import sys
import sys
from datetime import datetime

print('Hola Mundo')
sys.stdout.write('Hola Mundo desde std out\n')
sys.stderr.write('Tenemos un error!\n')

try:
    date_event = datetime.strptime('2026-09-18', '%Y-%m-%d')
    print(date_event)
except ValueError:
    sys.stderr.write(f'Error con el formato de fecha {ValueError}')
    sys.exit(1)


print('Otra tarea a ejecutar!')