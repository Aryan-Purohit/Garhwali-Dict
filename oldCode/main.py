import mysql.connector
from mysql.connector import Error


def main():
    
    connection = create_connection()
    if connection:
        choice = int(input("Enter your input.\n1. Find\n2. Add word\n3. Remove\n4. Show all entries\n"))
    
        if choice == 1:
            word = input("Enter English word ")
            findEntry(connection, word)
        elif choice == 2:
            Gword = input("Enter Garhwali Word")
            Hword = input("Enter Hindi Word")
            Eword = input("Enter English Word")   
            addWord(connection, Gword, Hword, Eword)
        elif choice == 3:
            Rword = input("Enter Entry to be removed")
            removeEntry(connection, Rword)
        elif choice == 4:
            showAllEntries(connection)
        else:
            print("Error. You entered a wrong choice")    
    

def addWord(connection, Gword, Hword, Eword):
    cursor = connection.cursor()
    
    query = "INSERT INTO dictionary(Garhwali_Word, Hindi_Word, English_Word) VALUES (%s, %s, %s)"
    
    cursor.execute(query, (Gword, Hword, Eword))
    
    connection.commit()
    print("Word added successfully")
    
    cursor.close()
    
def findEntry(connection, word):
    cursor = connection.cursor()
     
    query = "SELECT * FROM dictionary WHERE English_word = %s"
    cursor.execute(query, (word,))
    
    output = cursor.fetchall()
    
    for row in output:
        print(f"Hindi_word: {row[2]}, Garhwali_word: {row[1]}")
    
    cursor.close()

def removeEntry(connection, Rword):
    cursor = connection.cursor()
    
    query = "DELETE FROM dictionary WHERE English_word = %s"
    
    cursor.execute(query, (Rword,))
    
    connection.commit()
    
    print("Entry removed successfully")
    
def showAllEntries(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM dictionary"
    cursor.execute(query)
    output = cursor.fetchall()
    print("\nAll Dictionary Entries:")
    for row in output:
        print(f"Garhwali: {row[1]}, Hindi: {row[2]}, English: {row[3]}")
    cursor.close()
 
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

