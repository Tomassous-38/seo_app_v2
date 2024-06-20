import sqlite3

def init_db():
    conn = sqlite3.connect('conversations.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS conversations
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    c.execute('''CREATE TABLE IF NOT EXISTS messages
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, conversation_id INTEGER, role TEXT, content TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                 FOREIGN KEY (conversation_id) REFERENCES conversations (id))''')
    conn.commit()
    conn.close()

def save_new_conversation(title):
    conn = sqlite3.connect('conversations.db')
    c = conn.cursor()
    c.execute("INSERT INTO conversations (title) VALUES (?)", (title,))
    conn.commit()
    conversation_id = c.lastrowid
    conn.close()
    print(f"New conversation saved with ID: {conversation_id}")
    return conversation_id

def save_message(conversation_id, role, content):
    conn = sqlite3.connect('conversations.db')
    c = conn.cursor()
    c.execute("INSERT INTO messages (conversation_id, role, content) VALUES (?, ?, ?)", (conversation_id, role, content))
    conn.commit()
    conn.close()
    print(f"Message saved in conversation ID: {conversation_id}")

def get_messages(conversation_id):
    conn = sqlite3.connect('conversations.db')
    c = conn.cursor()
    c.execute("SELECT role, content, timestamp FROM messages WHERE conversation_id = ? ORDER BY timestamp", (conversation_id,))
    messages = c.fetchall()
    conn.close()
    return messages

def delete_conversation(conversation_id):
    conn = sqlite3.connect('conversations.db')
    c = conn.cursor()
    c.execute("DELETE FROM messages WHERE conversation_id = ?", (conversation_id,))
    c.execute("DELETE FROM conversations WHERE id = ?", (conversation_id,))
    conn.commit()
    conn.close()
    print(f"Conversation {conversation_id} deleted")

def get_saved_conversations():
    conn = sqlite3.connect('conversations.db')
    c = conn.cursor()
    c.execute("SELECT id, title, timestamp FROM conversations ORDER BY timestamp DESC")
    conversations = c.fetchall()
    conn.close()
    return conversations

# Initialize the database at the start
init_db()