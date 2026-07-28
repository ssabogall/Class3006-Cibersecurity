from flask import Flask, request, render_template
app = Flask(__name__, template_folder="template")

def Decifrar_cesar_dinamico(texto, clave):
    #input_text = input("Ingrese el texto a descifrar (solo letras mayúsculas): ").upper()
    #K = int(input("Ingrese la clave dinámica (un número entero rango 0-25): "))
    #clave = K
    resultado = ""
    for char in texto:
        if char.isalpha():
            C = ord(char) - ord('A')
            P = (C - clave) % 26
            resultado += chr(P + ord('A'))
        else:
            resultado += char
    return resultado


def cifrar_cesar_dinamico(texto, clave):
    #input_text = input("Ingrese el texto a cifrar (solo letras mayúsculas): ").upper()
    #K = int(input("Ingrese la clave dinámica (un número entero rango 0-25): "))
    #clave = K % 26  # Asegurar que la clave esté en el rango [0, 25]
    resultado = ""
    
    for char in texto:
        if char.isalpha():
            P = ord(char) - ord('A')
            C = (P + clave) % 26
            resultado += chr(C + ord('A'))
        else:
            resultado += char
    return resultado

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        texto = request.form.get("texto", "").strip().upper()
        clave_raw = request.form.get("clave", "").strip()

        if not texto:
            resultado = ""
        else:
            try:
                clave = int(clave_raw) % 26 if clave_raw else 0
            except ValueError:
                clave = 0

            accion = request.form.get("accion")
            if accion == "cifrar":
                resultado = cifrar_cesar_dinamico(texto, clave)
            elif accion == "descifrar":
                resultado = Decifrar_cesar_dinamico(texto, clave)

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)