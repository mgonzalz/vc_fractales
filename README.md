# Variable Compleja: Generador de Fractales.
Este proyecto es una aplicación gráfica para la generación de fractales, desarrollada en Python con el uso de Tkinter. Se ha diseñado bajo principios avanzados de programación orientada a objetos (POO), integrando una interfaz gráfica interactiva que permite la exploración detallada de diversos tipos de fractales.

## Repositorio.
Este proyecto ha sido desarrollado por:
- [Cantos Burgos, Lucía](https://github.com/luciacantos)
- [García González, Martina](https://github.com/martinagg7)
- [González García, María](https://github.com/mgonzalz)
- [Sánchez Escribano, José Antonio](https://github.com/josean9)
- [Serrano Catalina, Alejandro](https://github.com/seerraa16)

El código fuente del proyecto está disponible en el repositorio oficial: GitHub - [Variable Compleja: Fractales](https://github.com/mgonzalz/vc_fractales).

## Funcionalidades Principales.
- Generación de fractales matemáticos como Mandelbrot, Julia, entre otros.
- Interfaz gráfica intuitiva y dinámica implementada con Tkinter.
- Configuración avanzada de parámetros para personalizar la visualización y las características de los fractales.
- Exportación de fractales generados a formato de imagen.
- Código altamente modular y escalable, diseñado bajo principios sólidos de programación orientada a objetos (POO), garantizando un mantenimiento eficiente y facilidad para futuras ampliaciones.

## Estructura del Proyecto.
```plaintext
├── app
│   ├── assets              # Archivos de recursos como íconos.
│   ├── fractal_ui          # Módulos relacionados con la interfaz gráfica.
│   │   ├── __init__.py
│   ├── types_fractals.py
│   └── ui.py
├── modules
│   ├── fractal_types       # Implementación de tipos de fractales.
│   └── fractal_base.py
├── .gitignore             # Archivos y carpetas ignorados por Git.
├── main.py                # Archivo principal para ejecutar la aplicación.
├── README.md              # Documentación del proyecto.
├── requirements.txt       # Dependencias necesarias para el proyecto.
```

## Exportación a `.exe`.

La aplicación ha sido empaquetada en un archivo ejecutable (.exe) empleando PyInstaller, con el propósito de facilitar su distribución y ejecución en entornos Windows sin necesidad de instalaciones adicionales de Python. Este ejecutable está disponible en el directorio `dist` y ha sido diseñado para garantizar su funcionalidad óptima en sistemas compatibles.
