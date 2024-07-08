
Gestor de Eventos
Descripción
El proyecto Gestor de Eventos es una plataforma web desarrollada para facilitar la gestión de eventos. Permite a los usuarios crear, inscribirse y administrar eventos de manera eficiente. Este proyecto fue realizado como parte de la asignatura de Programación Orientada a Objetos en la universidad.

Diseño de la Base de Datos
La base de datos del sistema Gestor de Eventos se compone de tres principales modelos: Usuario, Evento, e Inscripción. A continuación, se describe el diseño de la base de datos:

Usuario
email: Correo electrónico del usuario (único y requerido)
nombre: Nombre del usuario
is_active: Indica si el usuario está activo.
is_admin: Indica si el usuario es administrador.
Evento
nombre: Nombre del evento.
descripcion: Descripción del evento.
ubicacion: Ubicación del evento.
fecha_hora: Fecha y hora del evento.
creador: Referencia al usuario que creó el evento (relación ForeignKey con Usuario).
inscritos: Lista de usuarios inscritos en el evento (relación ManyToMany con Usuario).
Inscripción
evento: Referencia al evento en el que el usuario se inscribe (relación ForeignKey con Evento).
usuario: Referencia al usuario que se inscribe en el evento (relación ForeignKey con Usuario).
fecha_inscripcion: Fecha y hora en que el usuario se inscribe en el evento.
Diagrama de la Base de Datos
[Inserta aquí el diagrama de la base de datos si lo tienes]

Guía de Usuario
Navegación y uso de la aplicación
1. Página de Inicio
Descripción: Presenta una bienvenida y permite navegar a otras secciones.
Acciones Disponibles:
Home: Redirige a la página de inicio.
Eventos: Muestra la lista de eventos disponibles.
Crear Evento: Permite crear un nuevo evento (requiere inicio de sesión).
Iniciar Sesión / Registrarse: Permite a los usuarios iniciar sesión o registrarse.
2. Lista de Eventos
Descripción: Muestra todos los eventos disponibles con opción de búsqueda.
Acciones Disponibles:
Ver Detalles del Evento: Acceso a la página de detalles de cada evento.
Paginación: Navegación entre páginas de eventos.
3. Detalle del Evento
Descripción: Muestra información detallada sobre un evento específico.
Acciones Disponibles:
Editar Evento: Permite editar el evento (solo para el creador del evento).
Eliminar Evento: Permite eliminar el evento (solo para el creador del evento).
Inscribirse: Permite inscribirse al evento.
Cancelar Inscripción: Permite cancelar la inscripción al evento.
4. Crear Evento
Descripción: Formulario para crear un nuevo evento.
Acciones Disponibles:
Crear Evento: Envía el formulario y crea el evento.
5. Mis Eventos Inscritos
Descripción: Muestra una lista de eventos en los que el usuario está inscrito.
Acciones Disponibles:
Ver Detalles del Evento: Acceso a la página de detalles de cada evento inscrito.
Instrucciones de Configuración y Despliegue
Requisitos previos
Python 3.11 o superior
PostgreSQL instalado y configurado
Git instalado
Pasos de configuración
Clonar el repositorio

bash
Copiar código
git clone https://github.com/LeonardoLoor/gestor_eventos.git
cd gestor_eventos
Instalar dependencias

bash
Copiar código
pip install -r requirements.txt
Configurar la base de datos

Crear la base de datos PostgreSQL llamada db_gestor_eventos.
Configurar las credenciales de la base de datos en settings.py

python
Copiar código
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_gestor_eventos',
        'USER': 'postgres',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Realizar Migraciones

bash
Copiar código
python manage.py makemigrations
python manage.py migrate
Crear un superusuario si no lo tienes

bash
Copiar código
python manage.py createsuperuser
Iniciar el Servidor de Desarrollo

bash
Copiar código
python manage.py runserver
Este proyecto aún está en proceso y pronto lo mejoraré y ampliaré para que sea una aplicación web completa. ¡Espero que encuentren útil este proyecto y estoy ansioso por recibir sus comentarios y sugerencias!

¡Gracias por tu interés en el proyecto Gestor de Eventos!
