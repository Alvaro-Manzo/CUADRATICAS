# 🧮 Solucionador de Ecuaciones Cuadráticas

**Herramienta simple y eficiente para resolver ecuaciones cuadráticas desarrollada por Álvaro Manzo**

## 📐 Descripción

Programa en Python que resuelve ecuaciones cuadráticas de la forma **ax² + bx + c = 0** utilizando la fórmula general (fórmula cuadrática). Soporta soluciones reales y complejas.

## ✨ Características

- ✅ Resuelve ecuaciones cuadráticas completas
- ✅ Maneja números complejos automáticamente
- ✅ Interfaz de línea de comandos simple e intuitiva
- ✅ Validación de entrada (a ≠ 0)
- ✅ Cálculo preciso usando la biblioteca `cmath`
- ✅ Muestra ambas soluciones (x₁ y x₂)

## 📋 Requisitos

```bash
Python 3.x
```

No requiere instalación de dependencias externas (usa bibliotecas estándar de Python).

## 🚀 Instalación y Uso

### Ejecución Directa

```bash
# Navegar al directorio
cd CUADRATICAS

# Ejecutar el programa
python main.py
```

### Ejemplo de Uso

```bash
$ python main.py

Resuelve la ecuación cuadrática de la forma ax^2 + bx + c = 0
Ingresa el valor de a (no puede ser 0): 1
Ingresa el valor de b: -5
Ingresa el valor de c: 6

Las soluciones son: (3+0j) y (2+0j)
               by: Alvaro Manzo
```

## 📊 Ejemplos de Ecuaciones

### Ejemplo 1: Soluciones Reales
```
Ecuación: x² - 5x + 6 = 0
Valores: a=1, b=-5, c=6
Resultado: x₁ = 3, x₂ = 2
```

### Ejemplo 2: Soluciones Complejas
```
Ecuación: x² + 2x + 5 = 0
Valores: a=1, b=2, c=5
Resultado: x₁ = -1+2j, x₂ = -1-2j
```

### Ejemplo 3: Raíz Doble
```
Ecuación: x² - 4x + 4 = 0
Valores: a=1, b=-4, c=4
Resultado: x₁ = 2, x₂ = 2
```

## 🔬 Fórmula Matemática

El programa utiliza la **fórmula general** para ecuaciones cuadráticas:

```
x = (-b ± √(b² - 4ac)) / 2a
```

Donde:
- **a** = coeficiente del término cuadrático
- **b** = coeficiente del término lineal
- **c** = término independiente
- **Δ = b² - 4ac** = discriminante

## 🧪 Casos Especiales

### Discriminante Positivo (Δ > 0)
Dos soluciones reales distintas

### Discriminante Cero (Δ = 0)
Una solución real doble (dos raíces iguales)

### Discriminante Negativo (Δ < 0)
Dos soluciones complejas conjugadas

## 📁 Estructura del Proyecto

```
CUADRATICAS/
├── main.py      # Programa principal
└── README.md    # Documentación (este archivo)
```

## 💡 Características Técnicas

- **Lenguaje**: Python 3
- **Biblioteca**: `cmath` (números complejos)
- **Método**: Fórmula cuadrática general
- **Precisión**: Punto flotante de Python
- **Tipo de números**: Reales y complejos

## 🎓 Uso Educativo

Esta herramienta es perfecta para:
- 📚 Estudiantes de matemáticas y álgebra
- 👨‍🏫 Profesores para verificar resultados
- 🧑‍💻 Aprendizaje de programación en Python
- 🔬 Práctica de resolución de ecuaciones

## ⚠️ Notas Importantes

- El valor de **a** no puede ser 0 (de lo contrario no sería una ecuación cuadrática)
- Los resultados se muestran en formato complejo incluso para soluciones reales
- Para soluciones reales, la parte imaginaria será `0j`

## 🛠️ Desarrollado por

**Álvaro Manzo**  
Software Engineer

---

📧 Para sugerencias o mejoras: contacto via GitHub

🌟 Si te resultó útil, ¡dale una estrella al proyecto!
