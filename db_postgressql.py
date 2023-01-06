
import psycopg2

def get_connection():
    try:
        return psycopg2.connect(
            database="testdb",
            user="consultants",
            password="WelcomeItc@2022",
            host="ec2-13-40-49-105.eu-west-2.compute.amazonaws.com",
            port=5432,
        )
    except:
        return False

conn = get_connection()

# CREATE A CURSOR USING THE CONNECTION OBJECT
curr = conn.cursor()

# EXECUTE THE SQL QUERY
curr.execute("SELECT * FROM test;")

# FETCH ALL THE ROWS FROM THE CURSOR
data = curr.fetchall()

# PRINT THE RECORDS
for row in data:
    print(row)

# CLOSE THE CONNECTION
conn.close()

if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print("Connection to the PostgreSQL encountered and error.")








