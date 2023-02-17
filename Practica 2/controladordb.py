import psycopg2
# creacion de la conexion
conect = psycopg2.connect(
    database="ejemplodb",
    user="docker",
    password="docker",
    host="0.0.0.0"
)

# Inicialisando la conexion del cursor
cur = conect.cursor()
# Insersion de Datos /Usando el INSERT INTO para introducir datos/
cur.execute("")  # INSERT INTO Estudiantes


# Ejecucion del curosr
cur.execute("SLECT * FROM Estudiantes")
colums = cur.fetchall()

if not len(colums):
    print("Colum navacia")
else:
    for colum in colums:
        print(colum)

# carranado el cursor y la conexion
cur.close()
conect.close()
