import sqlite3
import pandas as pd

miConexion = sqlite3.connect("Base de Datos Libros", isolation_level=None, detect_types= sqlite3.PARSE_COLNAMES)

db_df = pd. read_sql_query("SELECT * FROM LIBROS", miConexion)

db_df.to_csv('bdLibros.csv', index=False)

