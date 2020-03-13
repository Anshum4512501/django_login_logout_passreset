import psycopg2 

try:
    connection = psycopg2.connect("dbname=testdb user=testuser password=testuser host=localhost" )
    print("Connected")
    with connection.cursor() as cursor:
        print("cursor",cursor)
        # cursor.execute("UPDATE user_user SET username = anshu WHERE username = %s", ["anshum45"])
        
        cursor.execute("SELECT * FROM user_user WHERE username= %s",['anshum45'])
        row = cursor.fetchall()
        print("Row",row)
        connection.close()
except:
    ConnectionError
    print("can not be connected")
    connection.close()