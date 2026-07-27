# metodo de criptografia de cesar con clave dinamica
# formula a usar sera: C = (P + K) mod 26
# variables: C = letra cifrada
#            P = letra original
#            K = clave dinamica
# Formula para descifrar: P = (C - K) mod 26


def main():
    opcion = input("Ingrese 'C' para cifrar o 'D' para Descifrar: ").lower()
    if opcion == 'C':
        cifrar_cesar_dinamico()
    elif opcion == 'D':
        Decifrar_cesar_dinamico()
    else:
        print("Opción no válida.")

def Decifrar_cesar_dinamico():
    input_text = input("Ingrese el texto a descifrar (solo letras mayúsculas): ").upper()
    K = int(input("Ingrese la clave dinámica (un número entero rango 0-25): "))
    clave = K % 26  # Asegurar que la clave esté en el rango [0, 25]
    resultado = ""
    
    for char in input_text:
        if char.isalpha():
            C = ord(char) - ord('A')
            P = (C - clave) % 26
            resultado += chr(P + ord('A'))
        else:
            resultado += char
    print(resultado)


def cifrar_cesar_dinamico():
    input_text = input("Ingrese el texto a cifrar (solo letras mayúsculas): ").upper()
    K = int(input("Ingrese la clave dinámica (un número entero rango 0-25): "))
    clave = K % 26  # Asegurar que la clave esté en el rango [0, 25]
    resultado = ""
    
    for char in input_text:
        if char.isalpha():
            P = ord(char) - ord('A')
            C = (P + clave) % 26
            resultado += chr(C + ord('A'))
        else:
            resultado += char
    
    print(resultado)

if __name__ == "__main__":
    main()
