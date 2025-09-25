###########
# Homework 1 (Create Roster Table)
###########
import sqlite3

# Connect to database (creates one if it doesn't exist)
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")
conn.commit()

###########
# Homework 2 (Insert Data)
###########
# Insert data
cursor.executemany("INSERT INTO Roster VALUES (?, ?, ?)", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])
conn.commit()

###########
# Homework 3 (Update Data)
###########
# Update Jadzia Dax to Ezri Dax
cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")
conn.commit()

###########
# Homework 4 (Select Data)
###########
# Select Bajoran names and ages
cursor.execute("""
SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
""")

results = cursor.fetchall()
for row in results:
    print(row)

# Close connection
conn.close()
