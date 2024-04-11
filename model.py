import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Execute SQL statements
cursor.execute('''DROP TABLE IF EXISTS poems''')
cursor.execute('''
    CREATE TABLE poems (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        text TEXT
    )
''')

poems_data = [
    ('The Road Not Taken', 'Robert Frost', 'Two roads diverged in a yellow wood, And sorry I could not travel both...'),
    ('Ozymandias', 'Percy Bysshe Shelley', 'I met a traveller from an antique land Who said: Two vast and trunkless legs of stone...'),
    ('Daffodils', 'William Wordsworth', 'I wandered lonely as a cloud That floats on high o''er vales and hills...'),
    ('Sonnet 18', 'William Shakespeare', 'Shall I compare thee to a summer''s day? Thou art more lovely and more temperate...'),
    ('The Raven', 'Edgar Allan Poe', 'Once upon a midnight dreary, while I pondered, weak and weary...')
]

cursor.executemany('''
    INSERT INTO poems (title, author, text)
    VALUES (?, ?, ?)
''', poems_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database 'data.db' has been created and populated with poems.")
