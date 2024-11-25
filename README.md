# REST Backend

Este proyecto es un template para un servicio REST utilizando Python, FastAPI y Cassandra. Proporciona una estructura organizada y modular para facilitar el desarrollo y mantenimiento de aplicaciones backend.

## Tecnologías

- **Python**: Lenguaje de programación utilizado para desarrollar el backend.
- **FastAPI**: Framework web moderno y de alto rendimiento para construir APIs con Python 3.6+ basado en estándares como OpenAPI y JSON Schema.
- **Cassandra**: Base de datos NoSQL distribuida y altamente escalable, ideal para manejar grandes cantidades de datos.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- `app/`: Contiene el código principal de la aplicación FastAPI.
    - `main.py`: Punto de entrada de la aplicación.
    - `routers/`: Módulos de enrutamiento para diferentes endpoints.
    - `models/`: Definiciones de los modelos de datos.
    - `schemas/`: Esquemas Pydantic para validación de datos.
    - `services/`: Lógica de negocio y servicios.
- `tests/`: Pruebas unitarias y de integración.

## Instalación

1. Clona el repositorio:
     ```bash
     git clone https://github.com/maopaa/maopaa-rest-template.git
     cd maopaa-rest-template
     ```

2. Crea un entorno virtual y activa:
     ```bash
     python -m venv env
     source env/bin/activate  # En Windows usa `env\Scripts\activate`
     ```

3. Instala las dependencias:
     ```bash
     pip install -r requirements.txt
     ```

## Uso

Para iniciar el servidor de desarrollo, ejecuta:
```bash
uvicorn app.main:app --reload
```

El servidor estará disponible en `http://127.0.0.1:8000`.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.
