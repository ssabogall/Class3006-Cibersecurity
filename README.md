# Class3006-Cibersecurity

Aplicacion educativa de criptografia para el curso de Ciberseguridad. El proyecto implementa el cifrado Cesar con una interfaz web desarrollada en Flask.

## Funcionalidades

- Cifrar texto usando una clave numerica.
- Descifrar texto previamente cifrado.
- Normalizar el texto ingresado a mayusculas.
- Mantener espacios y caracteres que no sean letras.
- Aplicar claves de cualquier valor entero reduciendolas al rango `0-25`.

## Requisitos

- Python 3.10 o superior.
- `pip`.
- Flask.

## Instalacion

1. Clona el repositorio y entra en la carpeta del proyecto:

	```powershell
	git clone <URL_DEL_REPOSITORIO>
	cd Class3006-Cibersecurity
	```

2. Crea un entorno virtual:

	```powershell
	python -m venv venv
	```

3. Activa el entorno virtual en Windows PowerShell:

	```powershell
	.\venv\Scripts\Activate.ps1
	```

	En Linux o macOS:

	```bash
	source venv/bin/activate
	```

4. Instala Flask:

	```bash
	pip install flask
	```

## Ejecucion

Con el entorno virtual activo, ejecuta:

```bash
python app.py
```

Abre `http://127.0.0.1:5000` en el navegador. La aplicacion se ejecuta en modo debug durante el desarrollo.

## Uso

1. Escribe el texto que deseas procesar.
2. Ingresa una clave numerica.
3. Selecciona **Cifrar** o **Descifrar**.
4. Consulta el resultado mostrado en la pagina.

El cifrado utiliza las siguientes formulas:

```text
C = (P + K) mod 26
P = (C - K) mod 26
```

Donde `P` es la letra original, `C` es la letra resultante y `K` es la clave.

## Estructura del proyecto

```text
Class3006-Cibersecurity/
├── app.py                 # Aplicacion web Flask
├── punto4.py              # Implementacion por consola del ejercicio
├── README.md              # Documentacion del proyecto
└── template/
	 └── index.html         # Interfaz web
```

## Notas

- La interfaz convierte automaticamente el texto a mayusculas.
- La clave se ajusta con `clave % 26`, por lo que claves mayores que 25 tambien son validas.
- Para un entorno de produccion se debe utilizar un servidor WSGI y desactivar `debug=True`.
