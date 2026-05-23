# Reto Semana 6: Validador de Códigos con Expresiones Regulares

Alumno: David Emiliano Rodriguez Anduiza
Materia: Programación para Ciencia de Datos
Profesor: Mario Augusto Ramirez

## Descripción
Sistema automatizado para la validación de códigos de logística (productos, envíos, empleados y facturas) desarrollado en Python. El programa utiliza expresiones regulares (RegEx) para la detección de estructuras y validación lógica de reglas de negocio específicas.

## Estructura del Proyecto

reto-semana-06/
├── main.py              # Script principal de validación
├── README.md            # Documentación del proyecto
├── .gitignore           # Archivos ignorados por Git
└── test/
├── codigo.txt       # Casos de prueba (Entrada)
└── salida_esperada.txt # Resultados esperados (Salida)

## Especificaciones Técnicas
- **Entrada:** `stdin` (lectura línea por línea).
- **Salida:** `stdout` (formato CSV).
- **Validaciones implementadas:**
  - **Producto:** Estructura `AAA-9999-AA` (Mayúsculas obligatorias).
  - **Envío:** Fecha válida (Año 2020-2030, Mes 01-12, Día 01-31).
  - **Empleado:** Departamentos permitidos (VEN, ADM, TEC, LOG, RHH) y número > 1000.
  - **Factura:** Serie permitida (A-E) en mayúsculas.

## Instrucciones de Uso

### Requisitos
- Python 3.12+ instalado.

### Ejecución
Para procesar el archivo de pruebas y generar el archivo de resultados, utiliza el siguiente comando en tu terminal (PowerShell):

powershell
Get-Content test/codigo.txt | python main.py > test/salida_esperada.txt

1. El flujo de procesamiento
El programa funciona como una línea de ensamblaje industrial:

Entrada: sys.stdin lee el archivo línea a línea. Esto es eficiente porque no carga todo el archivo en la memoria (importante para volúmenes grandes de datos).

Detección de Tipo: Usamos detectar_tipo() con un regex "flexible". Este regex solo pregunta: "¿Tiene la forma general de este código?". Por ejemplo, para un producto, le da igual si las letras son minúsculas, solo busca que haya 3 letras, un guion, 4 dígitos, un guion y 2 letras.

Validación Estricta: Si el tipo fue detectado, el código entra a su función específica (como validar_producto()). Aquí es donde usamos un regex más estricto o validaciones lógicas para verificar que se cumplan las reglas de negocio (mayúsculas, rangos de fechas, listas permitidas, etc.).

Salida: Se construye un CSV con los resultados obtenidos.

2. ¿Cómo funcionan las Expresiones Regulares (RegEx) aquí?
Las RegEx son el corazón del reto. Se dividen en dos tipos de patrones que implementamos:

Patrones de Estructura (Anclados con ^ y $):

Usamos ^ para indicar el inicio del texto y $ para el final. Esto asegura que el código sea exactamente del formato esperado, evitando que se cuelen caracteres basura al principio o final.

Grupos de Captura ():

En funciones como validar_envio() o validar_factura(), usamos paréntesis para "recortar" partes del código. Por ejemplo, en el envío: ENV-(\d{4})-(\d{2})-(\d{2})-\d{6}. Al capturar el año, mes y día en grupos (group(1), group(2), etc.), podemos convertirlos a números enteros (int()) y compararlos matemáticamente (2020 <= anio <= 2030).

3. La lógica de los validadores
Producto y Factura: Usamos comparaciones directas de mayúsculas y pertenencia a listas (serie in SERIES_VALIDAS).

Envío: Es la más compleja porque requiere lógica de rangos. El regex asegura que haya números, pero el programa asegura que esos números sean fechas válidas en el calendario (no puedes tener mes 13).

Empleado: Aquí combinamos una lista permitida (DEPARTAMENTOS_VALIDOS) con una condición lógica sobre los dígitos (not num.startswith('0')).

4. La arquitectura del código (Clean Code)
Para sacar los 5 puntos de "Código limpio", estructuramos el programa en funciones independientes:

Modularidad: Cada tipo de código tiene su propia función (validar_producto, validar_envio, etc.). Si mañana el formato de factura cambia, solo tienes que editar esa función sin romper el resto del programa.

Main centralizado: La función main() actúa como un orquestador, manteniendo el ciclo de lectura simple y llamando a validar_codigo() para cada línea.

Resumen del proceso
Todo se hizo siguiendo este orden:

Definición de constantes: Listas de departamentos y series válidas para evitar "hardcodear" valores dentro de las funciones.

Detección: detectar_tipo clasifica el caos de la entrada.

Validación: Cada función aplica el "filtro fino".

Salida: print con formato f-string para cumplir el estándar CSV.
