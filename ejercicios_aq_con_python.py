# ==============================================================================
# Ejercicio de práctica: Clasificación aplicando AQ con Python
# ==============================================================================

# ------------------------------------------------------------------------------
# EJERCICIO 1: Concesionaria de Vehículos (Compra de Auto Eléctrico)
# ------------------------------------------------------------------------------

# Dataset
positivos_autos = [
    {"edad": "Joven", "ingreso": "Alto", "tiene_garaje": "Si", "distancia_trabajo": "Corta"},
    {"edad": "Adulto", "ingreso": "Medio", "tiene_garaje": "Si", "distancia_trabajo": "Media"},
    {"edad": "Mayor", "ingreso": "Alto", "tiene_garaje": "Si", "distancia_trabajo": "Larga"}
]

negativos_autos = [
    {"edad": "Joven", "ingreso": "Alto", "tiene_garaje": "No", "distancia_trabajo": "Corta"},
    {"edad": "Adulto", "ingreso": "Medio", "tiene_garaje": "No", "distancia_trabajo": "Media"},
    {"edad": "Mayor", "ingreso": "Bajo", "tiene_garaje": "No", "distancia_trabajo": "Larga"}
]

def clasificar_compra_auto(cliente):
    """
    Regla inducida mediante algoritmo AQ:
    SI tiene_garaje == 'Si' ENTONCES Compra_Auto_Electrico = 'Sí'
    """
    if cliente.get("tiene_garaje") == "Si":
        return "Sí"
    else:
        return "No"

# Validación de la regla Ejercicio 1
def probar_ejercicio_1():
    print("=== VALIDACIÓN EJERCICIO 1: Concesionaria de Autos ===")
    
    # Probar que cubre todos los positivos
    todos_pos_ok = all(clasificar_compra_auto(c) == "Sí" for c in positivos_autos)
    # Probar que excluye todos los negativos
    todos_neg_ok = all(clasificar_compra_auto(c) == "No" for c in negativos_autos)
    
    print(f"¿Cubre todos los ejemplos positivos?: {'Sí' if todos_pos_ok else 'No'}")
    print(f"¿Excluye todos los ejemplos negativos?: {'Sí' if todos_neg_ok else 'No'}")
    print(f"Estado de la regla: {'VÁLIDA' if (todos_pos_ok and todos_neg_ok) else 'INVÁLIDA'}\n")


# ------------------------------------------------------------------------------
# EJERCICIO 2: Inferir qué significa ser Socio Activo de un Gimnasio
# ------------------------------------------------------------------------------

# Dataset
positivos_gym = [
    {"edad": 25, "frecuencia": "frecuente", "plan": "premium"},
    {"edad": 32, "frecuencia": "frecuente", "plan": "premium"},
    {"edad": 45, "frecuencia": "frecuente", "plan": "premium"}
]

negativos_gym = [
    {"edad": 25, "frecuencia": "ocasional", "plan": "básico"},
    {"edad": 32, "frecuencia": "ocasional", "plan": "estándar"},
    {"edad": 38, "frecuencia": "rara", "plan": "básico"}
]

def clasificar_socio_activo(socio):
    """
    Regla inducida mediante algoritmo AQ:
    SI frecuencia == 'frecuente' Y plan == 'premium' ENTONCES Socio_Activo = 'Sí'
    """
    if socio.get("frecuencia") == "frecuente" and socio.get("plan") == "premium":
        return "Sí"
    else:
        return "No"

# Validación de la regla Ejercicio 2
def probar_ejercicio_2():
    print("=== VALIDACIÓN EJERCICIO 2: Socio Activo de Gimnasio ===")
    
    # Probar que cubre todos los positivos
    todos_pos_ok = all(clasificar_socio_activo(s) == "Sí" for s in positivos_gym)
    # Probar que excluye todos los negativos
    todos_neg_ok = all(clasificar_socio_activo(s) == "No" for s in negativos_gym)
    
    print(f"¿Cubre todos los ejemplos positivos?: {'Sí' if todos_pos_ok else 'No'}")
    print(f"¿Excluye todos los ejemplos negativos?: {'Sí' if todos_neg_ok else 'No'}")
    print(f"Estado de la regla: {'VÁLIDA' if (todos_pos_ok and todos_neg_ok) else 'INVÁLIDA'}\n")


# ------------------------------------------------------------------------------
# Ejecución Principal
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    probar_ejercicio_1()
    probar_ejercicio_2()