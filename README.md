# Invera ToDo-List Challenge (Python/Django Jr-SSr)

El propósito de esta prueba es conocer tu capacidad para crear una pequeña aplicación funcional en un límite de tiempo. A continuación, encontrarás las funciones, los requisitos y los puntos clave que debés tener en cuenta durante el desarrollo.

## Qué queremos que hagas:

- El Challenge consiste en crear una aplicación web sencilla que permita a los usuarios crear y mantener una lista de tareas.
- La entrega del resultado será en un nuevo fork de este repo y deberás hacer una pequeña demo del funcionamiento y desarrollo del proyecto ante un super comité de las más grandes mentes maestras de Invera, o a un par de devs, lo que sea más fácil de conseguir.
- Podes contactarnos en caso que tengas alguna consulta.

## Objetivos:

El usuario de la aplicación tiene que ser capaz de:

- Crear una tarea
- Eliminar una tarea
- Marcar tareas como completadas
- Poder ver una lista de todas las tareas existentes
- Filtrar/buscar tareas por fecha de creación y/o por el contenido de la misma

## Qué evaluamos:

- Desarrollo utilizando Python, Django. No es necesario crear un Front-End, pero sí es necesario tener una API que permita cumplir con los objetivos de arriba.
- Calidad y arquitectura de código. Facilidad de lectura y mantenimiento del código. Estándares seguidos.
- [Bonus] Manejo de logs.
- [Bonus] Creación de tests (unitarias y de integración)
- [Bonus] Unificar la solución propuesta en una imagen de Docker por repositorio para poder ser ejecutada en cualquier ambiente (si aplica para full stack).

## Requerimientos de entrega:

- Hacer un fork del proyecto y pushearlo en github. Puede ser privado.
- La solución debe correr correctamente.
- El Readme debe contener todas las instrucciones para poder levantar la aplicación, en caso de ser necesario, y explicar cómo se usa.
- Disponibilidad para realizar una pequeña demo del proyecto al finalizar el challenge.
- Tiempo para la entrega: Aproximadamente 7 días.



## Readme del código propuesto para el challenge

Archivo .env a modo de prueba

```
DATABASE_HOST="127.0.0.1"
DATABASE_USER="root"
DATABASE_PASSWORD="secret"
DATABASE_NAME="todo"
DATABASE_PORT=5432
```

Tener configurada una base de datos en PostgreSQL, los parámetros para conectarse a la misma están en el archivo "todoapp/.env". Pueden usarse los valores literales de dicho archivo o configurar los mismos como variables de entorno

Ejemplo: 

Linux

```
export DATABASE_HOST=192.168.0.10
```

Windows

```
$env:DATABASE_HOST="192.168.0.5"
```

1. Una vez clonado el repo, instalar las dependencias:

```
pip install -r .\requirements.txt
```

2. Realizar las migraciones

```
python manage.py makemigrations app
python manage.py migrate
```

3. Correr servicios

```
py manage.py runserver 0.0.0.0:8000
```

Los endpoints son los siguientes:

- app/tasks/ (GET) -> Obtener lista de los tasks creados

- app/tasks/create (POST) -> Via in body JSON creamos un task via los siguientes campos:
    - title: string para definir el título de la tarea.
    - task: Cuerpo de la tarea en sí.
    - completed: Booleano que define si la tarea está completa o no

Ejemplo:

```
curl --location --request POST 'localhost:8000/app/tasks/create' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "task2020",
    "task": "gotta do this very important thing before X",
    "completed": false
}'
```

- app/tasks/delete (POST) -> Via un body JSON, señalando solo el campo title, se elimina la tarea.

Ejemplo:

```
curl --location --request POST 'localhost:8000/app/tasks/delete' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "task1"
}'
```

- app/tasks/complete (POST) -> Via un body JSON, señalando solo el campo title, se marca una tarea como completada (el campo "completed" pasa a True)

Ejemplo:

```
curl --location --request POST 'localhost:8000/app/tasks/complete' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "task2020"
}'
```

- app/tasks/search??taskbody=piece_of_string_to_match&timecreated=year-month-day-hour-minute (GET) -> Via los Query String propuestos luego del "search" se pueden filtrar tareas que coincidan con el pedazo de texto o bien con una fecha de creación calculada en el minuto
Ejemplo:

```
curl --location --request GET 'localhost:8000/app/tasks/search?taskbody=a&timecreated=2022-06-30-12-15'
```

Las pruebas unitarias actualmente componen las acciones de Crear una tarea, eliminarla, marcarla como completa y listarlas

La imagen de Docker puede ser construida y ejecutada de la siguiente forma:

```
docker build -t "todoapp-challenge" .


docker container run -it --rm -p 8000:8000 -e DATABASE_HOST=192.168.0.5 -e DATABASE_USER=root -e DATABASE_PASSWORD=secret -e DATABASE_PORT=5432 -e DATABASE_NAME=todo --name todoapp-challenge todoapp-challenge
```


