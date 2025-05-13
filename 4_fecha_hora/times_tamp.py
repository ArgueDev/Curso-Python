from datetime import datetime
import time

start = time.time()
print(start)

# time.sleep(3)
for i in range(100000000):
    pass

end = datetime.now().timestamp()
print(end)
print(f'Tiempo total transcurrido: {end - start:.2f} segundos')