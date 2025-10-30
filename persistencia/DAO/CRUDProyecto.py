from persistencia.DAO.conexion import Conexion
# Definimos los datso para conexión a la Base de datos
host = 'localhost'
user = 'usuarioEmpresa'
password = 'usuarioEmpresa'
db = 'empresa'

def agregar(c):
    try:
        con = Conexion(host, user, password, db)
        sql = "Insert into proyecto set nombre='{}',descripcion='{}',fecha_inicio='{}',participantes='{}',director='{}',id_proyecto='{}'".format(c.nombre,c.des)
        # ejecuta la query
        con.ejecuta_query(sql)
        # actualizamos la db
        con.commit()
        # mensaje de exito
        input("el proyecto fue agregado con exito")
        # desconectar
        con.desconectar()
    except Exception as e:
        con.rollback()
        input("Se ha generado un error al agregar un proyecto:\n{}".format(e))

def editar(c_list):#c_list debe recibir una lista con los nuevos datos del proyecto
    #NUNCA OLVIDAR QUE ESTO COMIENZA CON TRY-EXCEPTION
    try:
        #1. Creamos la Conexión a la BD
        con=Conexion(host,user,password,db)
        #2. Creamos la Query a utilizar
        sql="Update proyecto set id_proyecto='{}', nombre='{}', empleados='{}' where gerente='{}'".format()
        #3. Ejecutar la Query
        con.ejecuta_query(sql)
        #4. Actulizamos la BD
        con.commit()
        #5. Opcional.... Enviamos mensaje de éxito
        input("El proyecto fue Modificado con éxito :)")
        #6. NOS DESCONECTAMOS
        con.desconectar()
    except Exception as e:
        con.rollback()
        input("Se ha generado un error al Modificar un proyecto:\n{}".format(e))


#Creamos la Función para Eliminar
def eliminar(id_proyecto):
    #NUNCA OLVIDAR QUE ESTO COMIENZA CON TRY-EXCEPTION
    try:
        #1. Creamos la Conexión a la BD
        con=Conexion(host,user,password,db)
        #2. Creamos la Query a utilizar
        sql="Delete from proyecto where id_proyecto={}".format(id_proyecto)
        #3. Ejecutar la Query
        con.ejecuta_query(sql)
        #4. Actulizamos la BD
        con.commit()
        #5. Opcional.... Enviamos mensaje de éxito
        input("El proyecto fue Eliminado con éxito :)")
        #6. NOS DESCONECTAMOS
        con.desconectar()
    except Exception as e:
        con.rollback()
        print("Se ha generado un error al Elimnar un proyecto:\n{}".format(e))

#Creamos la función para Mostrar todos los datos o registros de la BD
def mostrarTodos():
    try:
        #1. Crear la conexión hacia la BD
        con=Conexion(host,user,password,db)
        #2. Crear la SQL
        sql="Select * from proyecto"
        #3. Ejecutamos la Query (SQL)
        cursor=con.ejecuta_query(sql)
        #4. Bajamos los datos del limbo (desde el cursor)
        datos=cursor.fetchall()
        #5. Nos Desconetamos
        con.desconectar()
        #6. Retornamos los datos a quien solicito la busqueda o carga de datos
        return datos
    except Exception as e:
        print("Error al Solicitar Todos los Registros de la Tabla proyecto: {}".format(e))