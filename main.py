import mysql.connector
from mysql.connector import Error

    

def main():
    
    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Aryu@118',
            database = 'Garhwali_Dict'
        )

        if conn.is_connected():
            print("Connected to mySQL database")
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dictionary")
        rows = cursor.fetchall()
    
        for r in rows:
            print(f"Garhwali: {r[1]}, Hindi: {r[2]}, English: {r[3]}")
    

    except Error as e :
        print(f"Error: {e}")   
        
    finally:
        if cursor:
            cursor.close()
        
        if conn and conn.is_connected():
            conn.close()
             

def addWord():
    num = 0
    
def findEntry():
    n = 0

def removeEntry():
    nu = 0

if __name__ == "__main__":
    main()


