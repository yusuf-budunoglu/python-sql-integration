import sqlite3

print("Database integration starting...\n")
print("-" * 40)

connection = sqlite3.connect("company_data.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees (
    Employee_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Department TEXT NOT NULL,
    Salary INTEGER
)
""")
print("[SUCCESS] 'Employees' table is ready in the database.")

cursor.execute("DELETE FROM Employees") 

employees_data = [
    ("Yusuf Budunoglu", "Data Science", 6000),
    ("Anna Kowalska", "AI Research", 8500),
    ("John Doe", "Engineering", 7000)
]

cursor.executemany("INSERT INTO Employees (Name, Department, Salary) VALUES (?, ?, ?)", employees_data)
print(f"[SUCCESS] {cursor.rowcount} employee records inserted securely.")

connection.commit()
connection.close()

print("-" * 40)
print("[COMPLETED] Database connection closed safely.")