import mysql.connector
from mysql.connector import Error


def main():
    
    connection = create_connection()
    choice = int(input("Enter your input.\n1. Find\n2. Add word\n3. Remove\n"))
    
    if choice == 1:
        word = input("Enter English word ")
        findEntry(connection, word)
    elif choice == 2:   
        addWord(connection, word)
    elif choice == 3:
        removeEntry(connection)
    else:
        print("Error. You entered a wrong choice")    
    

def addWord(connection):
    cursor = connection.cursor()
    
def findEntry(connection, word):
    cursor = connection.cursor()
    
    
    query = "SELECT * FROM dictionary WHERE English_word = %s"
    cursor.execute(query, (word,))
    
    output = cursor.fetchall()
    
    for row in output:
        print(f"Hindi_word: {row[2]}, Garhwali_word: {row[1]}")

def removeEntry(connection):
    cursor = connection.cursor()
 
#Establishes the connection to SQL database    
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Aryu@118',
            database = 'Garhwali_Dict'
        )
        print("Connection to database successful")
    except Error as e:
        print(f"The Error '{e}' occurred")
     
    return connection

if __name__ == "__main__":
    main()

