import sys
import re

DEPARTAMENTOS_VALIDOS = ['VEN', 'ADM', 'TEC', 'LOG', 'RHH']
SERIES_VALIDAS = ['A', 'B', 'C', 'D', 'E']

def detectar_tipo(codigo):
    """Detecta el tipo de codigo por su estructura general."""
    if re.match(r'^[A-Za-z]{3}-\d{4}-[A-Za-z]{2}$', codigo):
        return "producto"
    if re.match(r'^ENV-\d{4}-\d{2}-\d{2}-\d{6}$', codigo):
        return "envio"
    if re.match(r'^EMP-[A-Za-z]{3}-\d{4}$', codigo):
        return "empleado"
    if re.match(r'^FAC-[A-Za-z]-\d{6}$', codigo):
        return "factura"
    return "desconocido"

def validar_producto(codigo):
    """Valida que categoria y pais sean mayusculas."""
    # Regex estricta: solo mayusculas
    return bool(re.match(r'^[A-Z]{3}-\d{4}-[A-Z]{2}$', codigo))

def validar_envio(codigo):
    """Valida rangos de fecha (año 2020-2030, mes 01-12, dia 01-31)."""
    m = re.match(r'^ENV-(\d{4})-(\d{2})-(\d{2})-\d{6}$', codigo)
    if m:
        anio, mes, dia = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if (2020 <= anio <= 2030) and (1 <= mes <= 12) and (1 <= dia <= 31):
            return True
    return False

def validar_empleado(codigo):
    """Valida departamento valido y numero no empieza con 0."""
    m = re.match(r'^EMP-([A-Z]{3})-(\d{4})$', codigo)
    if m:
        depto = m.group(1)
        num = m.group(2)
        # Departamento en lista y numero no empieza con 0
        if depto in DEPARTAMENTOS_VALIDOS and not num.startswith('0'):
            return True
    return False

def validar_factura(codigo):
    """Valida serie A-E en mayuscula."""
    m = re.match(r'^FAC-([A-Z])-\d{6}$', codigo)
    if m:
        serie = m.group(1)
        return serie in SERIES_VALIDAS
    return False

def validar_codigo(codigo):
    """Detecta tipo y valida. Retorna (tipo, es_valido)."""
    tipo = detectar_tipo(codigo)
    if tipo == "producto":
        return tipo, validar_producto(codigo)
    elif tipo == "envio":
        return tipo, validar_envio(codigo)
    elif tipo == "empleado":
        return tipo, validar_empleado(codigo)
    elif tipo == "factura":
        return tipo, validar_factura(codigo)
    else:
        return "desconocido", False

def main():
    print("codigo,tipo,valido")
    for linea in sys.stdin:
        codigo = linea.strip()
        if not codigo:
            continue
        tipo, es_valido = validar_codigo(codigo)
        print(f"{codigo},{tipo},{'VALIDO' if es_valido else 'INVALIDO'}")

if __name__ == "__main__":
    main()
    