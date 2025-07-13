# ui-automation-selenium-python

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