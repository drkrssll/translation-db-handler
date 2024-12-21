import sqlite3

conn = sqlite3.connect('translations.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS word_pairs')
