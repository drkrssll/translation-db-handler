import sqlite3

conn = sqlite3.connect('translations.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS word_pairs (
        id INTEGER PRIMARY KEY,
        source_word TEXT NOT NULL,
        target_word TEXT NOT NULL
    )
''')

def add_pair(source, target):
    cursor.execute('INSERT INTO word_pairs (source_word, target_word) VALUES (?, ?)', (source, target))
    conn.commit()


def get_pairs():
    cursor.execute('SELECT * FROM word_pairs')
    return cursor.fetchall()

# take input from user and add pairs to database
while True:
    source = input('Enter source word: ')
    target = input('Enter target word: ')

    add_pair(source, target)

    print(get_pairs())
