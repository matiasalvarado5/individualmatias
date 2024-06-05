#activar nuestro ambiente virtual con flask en desarrollo

#Establecer configuraciones y variables de entorno(siempre con venv activado)

set flask_app=main.py (Estableciendo archivo el cual se encargara de correr flask)
set flask_debug=1 (Estableciendo modo depurador, para ver cambios sin ncesidad de parar el servidor)
set flask_env=development
set database_user=nombre de usuario en el serividor de bd (Fijando variable de user)
set database_password=contraseña de el usuario de el servidor de bd (Fijando variable de user)
set database_host=localhost (Fijando variable de host)
set database=nombre de la base de datos (Fijando variable de bd)
flask run (Corriendo nuestra app)

(SIEMPRE QUE QUERRAMOS CORRER NUESTRA APLICACION, ES OBLIGATORIO ESTABLECER LAS VARIABLES DE ENTORNO ANTERIORES.)