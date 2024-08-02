import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print("Successfully connected to the database.")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")

    def create_tables(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS conversations (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id VARCHAR(255),
                    model VARCHAR(50),
                    mode VARCHAR(50),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    conversation_id INT,
                    role VARCHAR(20),
                    content TEXT,
                    tokens INT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (conversation_id) REFERENCES conversations(id)
                )
            """)

            self.connection.commit()
            print("Tables created successfully.")
        except Error as e:
            print(f"Error creating tables: {e}")

    def insert_conversation(self, user_id, model, mode):
        try:
            query = """
                INSERT INTO conversations (user_id, model, mode)
                VALUES (%s, %s, %s)
            """
            self.cursor.execute(query, (user_id, model, mode))
            self.connection.commit()
            return self.cursor.lastrowid
        except Error as e:
            print(f"Error inserting conversation: {e}")
            return None

    def insert_message(self, conversation_id, role, content, tokens):
        try:
            query = """
                INSERT INTO messages (conversation_id, role, content, tokens)
                VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (conversation_id, role, content, tokens))
            self.connection.commit()
            return self.cursor.lastrowid
        except Error as e:
            print(f"Error inserting message: {e}")
            return None

    def get_conversation_history(self, conversation_id):
        try:
            query = """
                SELECT * FROM messages
                WHERE conversation_id = %s
                ORDER BY created_at
            """
            self.cursor.execute(query, (conversation_id,))
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error retrieving conversation history: {e}")
            return []

# Usage example:
# db = DatabaseManager()
# db.connect()
# db.create_tables()
# conversation_id = db.insert_conversation("user123", "gpt-4", "normal")
# db.insert_message(conversation_id, "user", "Hello, AI!", 5)
# db.insert_message(conversation_id, "assistant", "Hello! How can I help you today?", 10)
# history = db.get_conversation_history(conversation_id)
# print(history)
# db.disconnect()
