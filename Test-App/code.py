from flask import Flask
import pymysql

app = Flask(__name__)

# Connect to the RDS database
conn = pymysql.connect(
    host='prod-db.c6orgtvu47no.us-east-1.rds.amazonaws.com,
    port=3306,
    user='admin',
    password='password',
    db='prod-db',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/')
def hello_world():
    # Query the database
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM your-table-name")
        result = cursor.fetchall()
        return str(result)

if __name__ == '__main__':
    app.run()
