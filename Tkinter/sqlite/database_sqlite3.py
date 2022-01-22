import sqlite3

# Conect to database
# connect_database = sqlite3.connect(':memory:')  # to run some tests
connect_db = sqlite3.connect('Tkinter\sqlite\customer.db')  # .db stands for 'database'

# Create cursor
cursor_db = connect_db.cursor()

# DATATYPES: 
# NULL: boolean. if doesnt exists, is null, otherwise, is not null.
# INTEGER: int (1, 2, ...)
# REAL: decimal (0.5)
# TEXT: txt
# BLOB: images, audio files

# first_name <DATATYPE> => first_name text

# Create a table
cursor_db.execute("""CREATE TABLE customers(
        first_name text,
        last_name text,
        email text
        )
    """)

# Commit this execution to the database
connect_db.commit()

# Final thing: Close Connection
connect_db.close()