# ui-automation-selenium-python

## Descripción

Este proyecto es una plantilla completa para la automatización de pruebas de interfaces gráficas (UI) utilizando Selenium 4 y Python, implementando el patrón de diseño Page Object Model (POM). Su objetivo principal es servir como guía y referencia para quienes desean aprender o mejorar sus habilidades en automatización de pruebas con Python y Selenium.

**¿Qué es Page Object Model (POM)?**
POM es un patrón de diseño que promueve la organización del código de automatización separando la lógica de interacción con la interfaz de usuario en clases llamadas "Page Objects". Esto facilita el mantenimiento, la reutilización y la escalabilidad de los tests.

**¿Qué incluye este repositorio?**
- Ejemplo de estructura de carpetas profesional para proyectos de automatización.
- Implementación de Page Objects para diferentes páginas del sitio de pruebas.
- Ejemplo de pruebas automatizadas usando Pytest.
- Instrucciones detalladas para la configuración del entorno y ejecución de pruebas.

**¿Para quién es útil este proyecto?**
- Personas que están aprendiendo Selenium con Python.
- QA Engineers que buscan una base para sus propios frameworks.
- Desarrolladores que desean automatizar pruebas de UI de manera estructurada y mantenible.

Con este proyecto podrás entender cómo estructurar, escribir y ejecutar pruebas automatizadas de manera profesional y escalable en Python.

## Setup inicial

### 1. Crear un entorno virtual con Python

Abre una terminal en la raíz del proyecto y ejecuta el siguiente comando según tu sistema operativo:

- **Windows:**
  ```powershell
  python -m venv venv
  ```
- **Linux/Mac:**
  ```bash
  python3 -m venv venv
  ```

Esto creará una carpeta llamada `venv` con el entorno virtual.

Para activarlo:

- **Windows PowerShell:**
  ```powershell
  .\venv\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

Para desactivarlo (en cualquier sistema operativo):

```powershell
deactivate
```

### 2. Instalar dependencias

Si ya tienes un archivo `requirements.txt`, instala las dependencias con:

```powershell
pip install -r requirements.txt
```

### 3. Generar el requirements.txt (opcional)

Si agregas nuevas dependencias, puedes actualizar el archivo `requirements.txt` con:

```powershell
pip freeze > requirements.txt
```

Esto guardará todas las dependencias instaladas en el entorno virtual.


### 4. Ejecutar pruebas

Para ejecutar las pruebas automatizadas con pytest, asegúrate de tener el entorno virtual activado y ejecuta uno de los siguientes comandos según tu sistema operativo:

- **Windows (PowerShell o CMD):**
  ```powershell
  pytest
  ```

- **Linux/Mac:**
  ```bash
  pytest
  ```

Esto buscará y ejecutará automáticamente todos los archivos que comiencen con `test_` o terminen con `_test.py` dentro de la carpeta `tests`.

Si quieres ejecutar un archivo de prueba específico, por ejemplo `registerUser.py`, usa:

- **Windows:**
  ```powershell
  pytest tests/registerUser.py
  ```
- **Linux/Mac:**
  ```bash
  pytest tests/registerUser.py
  ```

**Nota:** Puedes agregar la opción `-v` para ver un reporte más detallado:
```bash
pytest -v
```

Si tienes problemas de importación, asegúrate de ejecutar el comando desde la raíz del proyecto (donde está este README).

