# Listas que contienen las representaciones en letras de las unidades, decenas y centenas.
UNIDADES = (
    'cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve'
)

DECENAS = (
    'diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve'
)

DIEZ_DIEZ = (
    'cero', 'diez', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa'
)

CIENTOS = (
    '', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 
    'seiscientos', 'setecientos', 'ochocientos', 'novecientos'
)

# Función principal que convierte un número a letras.
def numero_a_letras(numero):
    # Convierte el número a un entero para evitar decimales.
    numero_entero = int(numero)
    
    # Si el número es negativo, añade la palabra "menos" antes de la conversión a letras.
    if numero_entero < 0:
        negativo_letras = numero_a_letras(abs(numero))
        return f"menos {negativo_letras}"
    
    # Dependiendo del rango del número, selecciona la función adecuada para convertirlo a letras.
    if numero_entero <= 99:
        resultado = leer_decenas(numero_entero)
    elif numero_entero <= 999:
        resultado = leer_centenas(numero_entero)
    elif numero_entero <= 999999:
        resultado = leer_miles(numero_entero)
    elif numero_entero <= 999999999:
        resultado = leer_millones(numero_entero)
    elif numero_entero <= 999999999999:
        resultado = leer_millardos(numero_entero)
    elif numero_entero <= 999999999999999:
        resultado = leer_billones(numero_entero)
    else:
        resultado = leer_trillones(numero_entero)
    
    # Corrección para cambiar "uno mil" a "un mil".
    resultado = resultado.replace('uno mil', 'un mil')
    
    # Elimina espacios innecesarios.
    resultado = resultado.strip()
    resultado = resultado.replace(' _ ', ' ')
    resultado = resultado.replace('  ', ' ')
    
    return resultado

# Función que convierte números menores a 100 en letras.
def leer_decenas(numero):
    if numero < 10:
        return UNIDADES[numero]
    
    # Separa el número en decenas y unidades.
    decena, unidad = divmod(numero, 10)
    
    # Para los números entre 10 y 19, se usan palabras específicas.
    if numero <= 19:
        resultado = DECENAS[unidad]
    
    # Maneja los números entre 21 y 29, por ejemplo, veintidós.
    elif 21 <= numero <= 29:
        resultado = f"veinti{UNIDADES[unidad]}"
    
    # Para otras decenas, se usa el formato "decena y unidad".
    else:
        resultado = DIEZ_DIEZ[decena]
        if unidad > 0:
            resultado = f"{resultado} y {UNIDADES[unidad]}"
    
    return resultado

# Función que convierte números entre 100 y 999 en letras.
def leer_centenas(numero):
    centena, decena = divmod(numero, 100)
    
    # Si es exactamente 100, se escribe "cien".
    if decena == 0 and centena == 1:
        resultado = 'cien'
    else:
        resultado = CIENTOS[centena]
        if decena > 0:
            decena_letras = leer_decenas(decena)
            resultado = f"{resultado} {decena_letras}"
    
    return resultado

# Función que convierte números entre 1,000 y 999,999 en letras.
def leer_miles(numero):
    millar, centena = divmod(numero, 1000)
    resultado = ''   
    # Si es exactamente 1,000, no se escribe el "uno" antes de "mil".
    if millar == 1:
        resultado = ''
    elif (millar >= 2) and (millar <= 9):
        resultado = UNIDADES[millar]
    elif (millar >= 10) and (millar <= 99):
        resultado = leer_decenas(millar)
    elif (millar >= 100) and (millar <= 999):
        resultado = leer_centenas(millar)

    # Solo se agrega "mil" si el millar es mayor que 0
    if millar > 0:
        resultado = f"{resultado} mil"

    # Si hay una parte en las centenas, se añade también.
    if centena > 0:
        centena_letras = leer_centenas(centena)
        resultado = f"{resultado} {centena_letras}"
    
    return resultado.strip()


# Función que convierte números entre 1,000,000 y 999,999,999 en letras.
def leer_millones(numero):
    millon, millar = divmod(numero, 1000000)
    resultado = ''
    
    # Si es exactamente 1 millón.
    if millon == 1:
        resultado = ' un millón '
    
    # Si es más de 1 millón, se convierte esa parte.
    if (millon >= 2) and (millon <= 9):
        resultado = UNIDADES[millon]
    elif (millon >= 10) and (millon <= 99):
        resultado = leer_decenas(millon)
    elif (millon >= 100) and (millon <= 999):
        resultado = leer_centenas(millon)
    
    # Se agrega la palabra "millones" si es mayor a uno.
    if millon > 1:
        resultado = f"{resultado} millones"
    
    # Se convierte la parte de los miles si es necesario.
    if (millar > 0) and (millar <= 999):
        centena_letras = leer_centenas(millar)
        resultado = f"{resultado} {centena_letras}"
    elif (millar >= 1000) and (millar <= 999999):
        miles_letras = leer_miles(millar)
        resultado = f"{resultado} {miles_letras}"
    
    return resultado

# Función para números entre 1,000,000,000 y 999,999,999,999.
def leer_millardos(numero):
    millardo, millon = divmod(numero, 1000000000)
    # Se convierte la parte de los millardos y millones.
    miles_letras = leer_miles(millardo)
    millones_letras = leer_millones(millon)
    return f"{miles_letras}  mil  {millones_letras}"

# Función que convierte números entre billones.
def leer_billones(numero):
    billon, millardo = divmod(numero, 1000000000000)
    resultado = ''
    
    # Si es exactamente 1 billón.
    if billon == 1:
        resultado = 'un billón'
    
    # Si es más de 1 billón, se convierte la parte del billón.
    elif billon > 1:
        resultado = f"{leer_millones(billon)} billones"
    
    # Si hay parte de millardos, también se convierte.
    if millardo > 0:
        millardo_letras = leer_millardos(millardo)
        resultado = f"{resultado} {millardo_letras}"
    
    return resultado

# Función para números en el rango de los trillones.
def leer_trillones(numero):
    trillon, billon = divmod(numero, 1000000000000000000)
    resultado = ''
    
    # Si es exactamente 1 trillón.
    if trillon == 1:
        resultado = 'un trillón'
    
    # Si es más de 1 trillón, se convierte la parte del trillón.
    elif trillon > 1:
        resultado = f"{leer_millones(trillon)} trillones"
    
    # Si hay parte de billones, también se convierte.
    if billon > 0:
        billon_letras = leer_billones(billon)
        resultado = f"{resultado} {billon_letras}"
    
    return resultado

# Ejemplo de uso:
numero = int(input("Ingresa un número: "))  # Conversión de entrada a entero.
resultado = numero_a_letras(numero)  # Convierte el número a letras.
print(f"El número {numero} en letras es: {resultado}")  # Muestra el resultado.
