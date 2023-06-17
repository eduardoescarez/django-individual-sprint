# README

## Requisitos básicos

Los requisitos básicos para que este proyecto funcione son:

- Python >3.9
- Django 4.2.1
- asgiref 3.7.2
- certifi 2023.5.7
- charset-normalizer 3.1.0
- idna 3.4
- requests 2.31.0
- sqlparse 0.4.4
- tzdata 2023.3
- urllib3 2.0.2


## Estructura del proyecto

La aplicación de WebConstructores se encuentra en el directorio **mainapp** y las carpetas que lo contienen son:

- migrations : contiene las migraciones de Django
- static : contiene los archivos estáticos del sistema y se divide en:
    - images : contiene las imágenes
    - styles : contiene las hojas de estilo
- templates : contiene las plantillas y se compone en:
    - components : contiene partes del sistema como el carrusel, navbar y footer
    - home : contiene las paginas disponibles a todo el público, como index, formulario de contacto, lista de usuarios, crear usuario y login
    - interno : contiene las paginas de acceso restringido de la aplicación
    - base.html : Es la pagina con la plantilla general del sitio
- views.py : contiene las vistas de cada pagina
- models.py : contiene los modelos de la aplicación
- forms.py : contiene los formularios de la aplicación

En el directorio **website** se encuentran dos archivos que se usaron en el desarrollo:

- settings.py : contiene las configuraciones de la aplicación
- urls.py : contiene las rutas de la aplicación

## Como usar la aplicación

Para usar la aplicación, una vez descargada una copia del repositorio, necesita de un entorno virtual de Python, y configurarlo para que tenga todos los componentes necesarios.

Para ello en Windows use las siguientes instrucciones en la línea de comandos, una vez ubicado en el directorio principal de la aplicación:

```
python -m venv .venv

.venv\scripts\activate

(.venv) pip install -r requirements.txt

(.venv) cd website

(.venv) python manage.py runserver

```

Con eso crea el entorno virtual, lo activa, instala los componentes requeridos y ejecuta el servidor web.

## Acceso al sitio interno

Para acceder a las paginas internas vía la opción **Iniciar sesión** en el sitio web, puede usar la siguiente combinación de usuario y contraseña:

```
nombre de usuario : isantamaria
contraseña        : PUDAHUEL23
```

Para acceder al panel de administración de Django, el superusuario disponible es:

```
nombre de usuario : administrador
contraseña        : CajaVecina23
```

## Añadido Individual 06

- Se han creado tres grupos : **administradores**, **trabajadores**, **clientes**. Las razones de los permisos otorgados son:
    - **administradores**: requieren los permisos para administrar todos los elementos del sistema
    - **trabajadores**: requieren tener permisos limitados para acceder a algunas partes del sistema, como los formularios de contacto o de asistencia
    - **clientes**: requieren permisos para realizar menos acciones como acceder al formulario de asistencia

- La pagina dinámica de creación de usuarios (/nuevousuario) ha sido mejorada para capturar los siguientes datos adicionales
    - Nombre
    - Apellido