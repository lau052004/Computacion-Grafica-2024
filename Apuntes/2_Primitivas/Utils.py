# current_min y current_max: Definen el rango actual en el que se encuentra el valor.
# new_min y new_max: Definen el nuevo rango al que quieres mapear el valor.
# value: Es el valor dentro del rango actual que quieres convertir al nuevo rango.
def map_value(current_min, current_max, new_min, new_max, value):
    current_range = current_max - current_min
    new_range = new_max - new_min
    return new_min + new_range * ((value - current_min) / current_range)

# Calcula el rango actual (current_range): Resta current_min de current_max para encontrar el rango de valores
# actual. Calcula el nuevo rango (new_range): Resta new_min de new_max para encontrar el rango de valores deseado.
# Normaliza el valor: Resta current_min de value y luego divide por current_range para normalizar el valor a un rango
# de 0 a 1, donde 0 representa current_min y 1 representa current_max. Escala al nuevo rango: Multiplica el valor
# normalizado por new_range para escalarlo al nuevo rango de valores. Ajusta al nuevo mínimo: Suma new_min al valor
# escalado para ajustarlo al nuevo rango de valores, asegurándote de que new_min sea efectivamente el mínimo del
# nuevo rango.


# EJEMPLO: Supongamos que tienes un sensor que mide temperatura en el rango de 0°C a 50°C, pero quieres mapear esa
# medida a un rango de 0 a 100 para mostrarla en una barra de progreso en una interfaz gráfica. Si el sensor lee
# 25°C, puedes usar map_value(0, 50, 0, 100, 25) para convertirlo al valor 50 en el nuevo rango, lo que indica que la
# temperatura está a la mitad del rango de medición del sensor.