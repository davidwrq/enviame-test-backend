# Enviame backend test

Enviame Backend test



# Estructura de archivos 

La estructura base del proyecto es la siguente:

```bash
├── project-enviame (Main API REST empresas)
├── app
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── Dockerfile
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
│   └── schemas.py
├── db
│   └──  init.sql
├── Exercises
│   ├── exercise_3
│   │   ├── exercise_3.py
│   │   └── README.md
│   ├── exercise_4
│   │   ├── exercise_4.py
│   │   └── README.md
│   ├── exercise_5
│   │   ├── exercise_5.py
│   │   └── README.md
│   ├── exercise_6
│   │   └── exercise_6.py
│   │   └── README.md
│   └── exercise_7
│   │   ├── exercise_7.py
│   │   └── README.md
├── docker-compose.yml
├── README.md
└── .gitignore
```
dentro de cada carpeta  de exercise hay un readme para cada caso.


# Ejercicio 1: Docker  + Ejercicio 2: API REST + CRUD


## Comenzando 🚀

API Rest creada con

- Fastapi REST-API
- Swagger (Documentación)
- peewee (ORM)
- Uvicorn - is a lightning-fast ASGI server implementation


### Pre-requisitos 📋



```
Docker >= (version 20.10.1)
docker-compose >= (version 1.26.0)
```

### Instalación 🔧


```
docker-compose build
docker-compose up
```
## Correr servidor
El servidor quedara corriendo en el puerto 5000
```
http://0.0.0.0:5000
```

TODO: Script con data fake

Documentación


Para la documentación se implemento mediante Fastapi con swagger. 
ir a la siguente url:



```
http://0.0.0.0:5000/docs
```