# Sistema de Gestión de Menú de Restaurante 

**Estudiante:** Edisson Valentin Vera Gamboa  
**Asignatura:** Programación Orientada a Objetos   
**Paralelo:** E              
**Semana:** 6  

---

## 1. Descripción del Sistema
Este sistema representa una organización modular destinada a la administración del menú de un restaurante utilizando los principios fundamentales de la Programación Orientada a Objetos (POO): herencia, encapsulación y polimorfismo. El programa modela un catálogo heterogéneo que discrimina de forma lógica entre comidas sólidas y líquidos, controlando sus datos sensibles y exponiendo un comportamiento polimórfico limpio.

---

## 2. Estructura del Proyecto
El diseño modular sigue una arquitectura limpia distribuida en capas:

```text
restaurante_app/
├── modelos/                  
│   ├── __init__.py
│   ├── producto.py           
│   ├── platillo.py          
│   └── bebida.py             
├── servicios/                
│   ├── __init__.py
│   └── restaurante.py        
└── main.py                   