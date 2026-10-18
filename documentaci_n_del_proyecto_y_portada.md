# Ejercicio de práctica: Clasificación aplicando AQ con Python

**Asignatura:** Procesamiento de Aprendizaje Automático

**Objetivo:** Inducción de reglas de clasificación utilizando el algoritmo **AQ** a partir de conjuntos de ejemplos positivos (+) y negativos (-), e implementación de sus soluciones en Python.

## 📌 Estructura del Proyecto

```
.
├── README.md           # Portada principal, documentación y conclusiones teóricas.
└── ejercicios_AQ.py    # Script ejecutable en Python con los datasets y reglas inducidas.

```

## 💻 Ejercicio 1: Concesionaria de Vehículos (Automóviles Eléctricos)

### 1. Enunciado y Atributos

Identificar qué características tienen los clientes que compran un automóvil eléctrico.

* **Atributos:** `edad`, `ingreso`, `tiene_garaje`, `distancia_trabajo`

### 2. Análisis mediante Algoritmo AQ

Al realizar la comparación atributo por atributo entre ejemplos positivos y negativos:

* **`edad`**, **`ingreso`** y **`distancia_trabajo`**: Presentan solapamiento de valores entre ejemplos positivos y negativos, por lo que no discriminan la clase.

* **`tiene_garaje`**: Todos los ejemplos positivos poseen el valor `"Si"`, mientras que todos los negativos poseen el valor `"No"`.

### 3. Regla Inducida

```
SI tiene_garaje = Si
ENTONCES Compra_Auto_Electrico = Sí

```

## 🏋️ Ejercicio 2: Inferir qué significa ser Socio Activo de un Gimnasio

### 1. Enunciado y Atributos

Diferenciar a las personas que son socios activos de un gimnasio frente a quienes no mantienen una actividad regular.

* **Atributos:** `edad`, `frecuencia` (frecuencia de asistencia), `plan` (plan contratado)

### 2. Análisis mediante Algoritmo AQ

* **`edad`**: Los valores `25` y `32` aparecen tanto en el conjunto positivo como en el negativo, descartándose como condición discriminante directa.

* **`frecuencia`**: En los ejemplos positivos es siempre `"frecuente"`, mientras que en los negativos toma valores como `"ocasional"` o `"rara"`.

* **`plan`**: En los ejemplos positivos es siempre `"premium"`, mientras que en los negativos es `"básico"` o `"estándar"`.

### 3. Regla Inducida

```
SI frecuencia = "frecuente" Y plan = "premium"
ENTONCES Socio_Activo = Sí

```

## 🔍 Conclusiones Generales

1. **Eficiencia del Algoritmo AQ:** El algoritmo permite encontrar explicaciones simples y comprensibles a partir de datos estructurados, buscando la cobertura completa de ejemplos positivos y la exclusión estricta de ejemplos negativos.

2. **Relevancia de Atributos Discriminantes:** No todos los atributos tienen el mismo impacto inductivo. El análisis demuestra la importancia de aislar variables dependientes con alto poder de separación (como `tiene_garaje` en el primer caso y la combinación de `frecuencia` + `plan` en el segundo) para evitar sobreajustar la regla con datos irrelevantes (como la edad).

## 🚀 Instrucciones de Ejecución

Para verificar las reglas inducidas mediante la suite de pruebas automatizada, ejecute en la terminal:

```
python ejercicios_AQ.py

```