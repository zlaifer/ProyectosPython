''' 
► Enunciado:
Comprobar si una clave dada ya existe en el diccionario.

► Entrada:
dictionary = {'es':'Spain','tw':'Taiwan','sg':'Singapore'}
is_key_present('sg')
is_key_present('uk')

► Salida:
La clave 'sg' se encuentra en el diccionario.
La clave 'uk' no se encuentra en el diccionario.
'''

diccionario = {'es':'Spain','tw':'Taiwan','sg':'Singapore'}

def is_key_present(key: str) -> None:
    if key in diccionario:
        print(f"La clave '{key}' se encuentra en el diccionario.")
    else:
        print(f"La clave '{key}' no se encuentra en el diccionario.")

is_key_present('sg')
is_key_present('uk')