import pyodbc
import pandas as pd


def get_courses():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=najahai;"
        "Trusted_Connection=yes;"
    )
    query = "SELECT * FROM Course"  
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def get_courses_arabic():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=najahai;"
        "Trusted_Connection=yes;"
    )
    query = "SELECT * FROM CourseTranslation"  
    df = pd.read_sql(query, conn)
    conn.close()
    return df


