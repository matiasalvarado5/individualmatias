#activar nuestro ambiente virtual con flask en desarrollo

#Establecer configuraciones y variables de entorno(siempre con venv activado)

#Crear un archivo ".env" donde se encuentre las variables de entorno para que estas puedas ser cargadas automaticamentes al correr la app
#ejemplo: dentro del arhivo ".env" definir: database_user=nombre de usuario en el serividor de bd
                                            database_password=contraseña de el usuario de el servidor de bd 
                                            database_host=localhost
                                            database=nombre de la base de datos


set flask_app=main.py (Estableciendo archivo el cual se encargara de correr flask)
set flask_debug=1 (Estableciendo modo depurador, para ver cambios sin ncesidad de parar el servidor)
flask run (Corriendo nuestra app)
