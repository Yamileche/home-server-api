# Home Server API

## Descripción

**home-server-api** es una API backend desarrollada con **FastAPI** cuyo objetivo es gestionar servicios de un servidor doméstico mediante endpoints HTTP.

El proyecto centraliza distintas funcionalidades del sistema en una sola API, permitiendo interactuar con ellas de forma estructurada y extensible.

La aplicación está diseñada siguiendo una arquitectura modular que separa responsabilidades en distintas capas, facilitando la mantenibilidad y escalabilidad del sistema.

---

## Arquitectura del proyecto

La estructura del proyecto sigue una separación por capas:

```
app/
 ├── routes/        # Definición de endpoints HTTP
 ├── services/      # Lógica de negocio
 ├── repositories/  # Acceso a datos
 ├── models/        # Modelos y esquemas de datos
 └── core/          # Configuración, middlewares y utilidades
```

Esta organización permite desacoplar las distintas responsabilidades del sistema, haciendo el código más fácil de mantener y extender.

---

## Funcionalidades principales

### API REST

La aplicación expone endpoints HTTP para interactuar con los recursos del sistema.

---

### Logging estructurado

Se implementa un sistema de logging estructurado que incluye un **request_id** único por cada petición.  
Esto permite:

- rastrear solicitudes
- depurar errores
- analizar el comportamiento de la API

---

### Middleware de métricas

Cada request registra información relevante como:

- método HTTP
- ruta solicitada
- tiempo de respuesta
- código de estado
- dirección IP del cliente

Estos datos pueden utilizarse para monitoreo y análisis de rendimiento.

---

### Manejo global de errores

La API incluye un **global exception handler** que captura errores inesperados y devuelve respuestas estructuradas, evitando exponer trazas internas del servidor.

---

### Autenticación

El sistema utiliza **JWT (JSON Web Tokens)** para autenticar usuarios y proteger endpoints.

---

## Objetivo del proyecto

El objetivo de **home-server-api** es servir como una plataforma backend para gestionar y automatizar distintos servicios dentro de un servidor doméstico.

Además, el proyecto funciona como un entorno de aprendizaje para implementar prácticas comunes del desarrollo backend moderno, como:

- arquitectura por capas
- middlewares personalizados
- autenticación con tokens
- logging estructurado
- monitoreo de solicitudes

---

## Tecnologías utilizadas

- Python
- FastAPI
- Pydantic
- Uvicorn

---

## Estado del proyecto

El proyecto se encuentra en desarrollo y se utiliza como base para experimentar con diferentes patrones y herramientas del ecosistema backend, con el objetivo de construir una infraestructura personal extensible para un servidor doméstico.