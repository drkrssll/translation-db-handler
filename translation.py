import sqlite3
import sys

conn = sqlite3.connect('translations.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS word_pairs (
        id INTEGER PRIMARY KEY,
        source_word TEXT NOT NULL,
        target_word TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS phrases (
        id INTEGER PRIMARY KEY,
        source_phrase TEXT NOT NULL,
        target_phrase TEXT NOT NULL
    );
''')

def add_phrase(source, target):
    cursor.execute('INSERT INTO phrases (source_phrase, target_phrase) VALUES (?, ?)', (source, target))
    conn.commit()

def add_pair(source, target):
    cursor.execute('INSERT INTO word_pairs (source_word, target_word) VALUES (?, ?)', (source, target))
    conn.commit()

def get_phrases():
    cursor.execute('SELECT * FROM phrases')
    return cursor.fetchall()

def get_pairs():
    cursor.execute('SELECT * FROM word_pairs')
    return cursor.fetchall()

def get_target(source):
    source = (source,)
    cursor.execute('SELECT target_word FROM word_pairs WHERE source_word = ?', source)
    return cursor.fetchone()

# while True:
#     table = input('Enter table name: ')
#     source = input('Enter source word: ')
#     target = input('Enter target word: ')
# 
#     if table == 'phrases':
#         add_phrase(source, target)
#         print(get_phrases())
#     elif table == 'word_pairs':
#         add_pair(source, target)
#         print(get_pairs())

source_arg = sys.argv[1]

print(get_target(source_arg))
