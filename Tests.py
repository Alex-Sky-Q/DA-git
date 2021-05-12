import sqlite3 as sq3
import random as rd
import time

# Speed diff test between file and db writing
# start_time = time.time()
# connection = sq3.connect('original.db')
# cursor = connection.cursor()
# cursor.execute('CREATE TABLE IF NOT EXISTS Pressure (reading REAL)')
#
# query = 'INSERT into Pressure (reading) VALUES (?)'
# for i in range(100001):
#     num = rd.randrange(10, 26)
#     cursor.execute(query, [num])
#
# connection.commit()
# cursor.close()
# connection.close()
# print(f'DB - {(time.time() - start_time)} sec')
#
# start_time = time.time()
# with open('original.txt', 'w') as orig_file:
#     for i in range(100001):
#         num = rd.randrange(10, 26)
#         orig_file.write(f'{num}\n')
#
# print(f'File - {(time.time() - start_time)} sec')
# DB size = 876 kb, File size = 391 kb
# DB - 0.36696958541870117 sec, File - 0.17054152488708496 sec


# Speed diff test between SQL and Python filters. Do not use 1st run - its creation tables run
start_time = time.time()
connection = sq3.connect('original.db')
cursor = connection.cursor()
orig_data = cursor.execute('SELECT * FROM Pressure WHERE reading > 20').fetchall()
cursor.close()
connection.close()

connection = sq3.connect('backupSQL.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Pressure (reading REAL)')

query = 'INSERT into Pressure (reading) VALUES (?)'
for i in orig_data:
    cursor.execute(query, [i[0]])
connection.commit()
cursor.close()
connection.close()
print(f'SQL Filter - {(time.time() - start_time)} sec')

start_time = time.time()
connection = sq3.connect('original.db')
cursor = connection.cursor()
orig_data = cursor.execute('SELECT * FROM Pressure').fetchall()
cursor.close()
connection.close()

connection = sq3.connect('backupPY.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Pressure (reading REAL)')

query = 'INSERT into Pressure (reading) VALUES (?)'
for i in orig_data:
    if i[0] > 20:
        cursor.execute(query, [i[0]])
connection.commit()
cursor.close()
connection.close()
print(f'Python filter - {(time.time() - start_time)} sec')
# SQL Filter - 0.11562585830688477 sec, Python filter - 0.1586904525756836 sec


# Size diff test between lists and tuples
# import sys
# max_num = 10 ** 7
# nums_1 = [num for num in range(1, max_num + 1)]
# print(f'{sum(nums_1)} - {sys.getsizeof(nums_1)}')
# nums_2 = (num for num in range(1, max_num + 1))
# print(f'{sum(nums_2)} - {sys.getsizeof(nums_2)}')


# Some other tests
# txt = ''
# for prod in basket:
#     txt += prod
#     txt += ', '
# print(txt.strip(', '))

# if [] or {} or 0:
#     txt = 'Name'
#     print(txt[:-2])
# print([] or [] or [])
