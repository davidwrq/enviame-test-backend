# Enviame backend test

Enviame Backend test

## Comenzando 🚀

API Rest creada con

- Fastapi REST-API
- peewee (ORM)
- Uvicorn - is a lightning-fast ASGI server implementation


### Pre-requisitos 📋



```
docker
docker-compose
```

### Instalación 🔧


```
docker-compose build
docker-compose up
```

TODO: Script con data fake
## Ejecutando las pruebas ⚙️

Los tests corren en el mismo contenedor 

```
docker-compose run app test
```

Documentación


Para la dumentación se usa swagger, ir a la ruta descrita abajo. 

```
http://0.0.0.0:5000/docs
```