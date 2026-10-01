import sqlite3
connection=sqlite3.connect("hospital.db")
cursor=connection.cursor()
#print("Database created")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS equipment (
        equipment_id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        status TEXT,
        age INTEGER
    )
""")
connection.commit()#savesthe changes I just made
cursor.execute("""
    CREATE UNIQUE INDEX IF NOT EXISTS idx_equipment_serial_number
    ON equipment(serial_number)
""")

connection.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS maintenance(
maintenance_id INTEGER PRIMARY KEY,
equipment_id INTEGER,
date TEXT,
type_of_maintenance TEXT,
engineer TEXT,
time_taken INTEGER,
description TEXT,
FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id))
""")
connection.commit()
# print("Unique serial-number rule created")
# cursor.execute("""
#     SELECT serial_number, COUNT(*)
#     FROM equipment
#     WHERE serial_number IS NOT NULL
#     GROUP BY serial_number
#     HAVING COUNT(*) > 1
# """)
# duplicates = cursor.fetchall()
# print("Duplicate serial numbers:")
# for item in duplicates:
#     print(item)
# cursor.execute("""
#     SELECT equipment_id, serial_number, name, department, status, age
#     FROM equipment
#     WHERE serial_number IN ('00074', '6570394', '657813mz')
#     ORDER BY serial_number, equipment_id
# """)

# duplicates = cursor.fetchall()

# for item in duplicates:
#     print("ID:", item[0])
#     print("Serial:", item[1])
#     print("Name:", item[2])
#     print("Department:", item[3])
#     print("Status:", item[4])
#     print("Age:", item[5])
#     print()
# cursor.execute("""
#     DELETE FROM equipment
#     WHERE equipment_id IN (9, 10, 11, 12)
# """)

# connection.commit()

# print("Test duplicate records removed")
# cursor.execute("ALTER TABLE equipment ADD COLUMN serial_number TEXT")
# connection.commit()
#print("Equipment table created!")
# def register_equipment():
#   name = input("Enter equipment name: ")
#   serial_number=input("Enter equipment serial number: ")
#   department = input("Enter department: ")
#   status = input("Enter equipment status: ")
#   age = int(input("Enter equipment age: "))
#   try:
#     cursor.execute("""
#       INSERT INTO equipment (name,serial_number, department, status, age)
#       VALUES (?, ?, ?, ?, ?)
#       """,(name,serial_number,department,status,age))
#     connection.commit()
#     print("Equipment registered")
#   except sqlite3.IntegrityError:
#     print("Serial number already exists")
# def search_equipment():
#      name=input("Enter the name of the equipment to search: ")
#      cursor.execute("SELECT equipment_id,serial_number,name,department,status,age FROM equipment WHERE LOWER(name)=LOWER(?)",(name,))
#      equipment=cursor.fetchall()
#      for item in equipment:
#        print("ID:", item[0])
#        print("Serial_number",item[1])
#        print("Name:", item[2])
#        print("Department:", item[3])
#        print("Status:", item[4])
#        print("Age:", item[5])
#        print()
#status=input("Enter status to search: ")
# def update_equipment():
#  number = int(input("How many equipment serial numbers do you want to update? "))
#  for i in range(number): 
#    equipment_id = int(input("Enter equipment ID: "))
#    serial_number = input("Enter new serial number: ")
#    cursor.execute("""
#         UPDATE equipment
#         SET serial_number = ?
#         WHERE equipment_id = ?
#     """, (serial_number, equipment_id))
#    if cursor.rowcount == 1:
#             print("Serial number updated successfully!")
#    else:
#             print("Equipment ID not found.")

#  connection.commit()
#  print("Serial number updated successfully!")
# def view_equipment():
#   cursor.execute("SELECT equipment_id,serial_number,name,department,status,age FROM equipment")
#   equipment = cursor.fetchall()
#   for item in equipment:
#        print("ID:", item[0])
#        print("Serial_number",item[1])
#        print("Name:", item[2])
#        print("Department:", item[3])
#        print("Status:", item[4])
#        print("Age:", item[5])
#        print()
# update_equipment()
# #delete_equipment()
#register_equipment()
# view_equipment()
# search_equipment()
# def search_serial_number():
#     serial_number=input("Enter the serial_number of the equipment to search: ")
#     cursor.execute("SELECT equipment_id,serial_number,name,department,status,age FROM equipment WHERE LOWER(serial_number)=LOWER(?)",(serial_number,))
#     equipment=cursor.fetchall()
#     if equipment:#=='True':
#       print("Serial number exists")
#       for item in equipment:
#        print("ID:", item[0])
#        print("Serial_number",item[1])
#        print("Name:", item[2])
#        print("Department:", item[3])
#        print("Status:", item[4])
#        print("Age:", item[5])
#        print()
#     else:
#         print("Serial number is not registered")
# search_serial_number()
# def search_menu():
#  print("Search Equipment")
#  print("1. Search by name")
#  print("2. Search by serial number")
#  print("3. Search by department")
#  print("4. Search by status")
#  print("5. Exit")
#  while True:
#   choice=input("Choose an option: ")
#   if choice=="1":
#    name=input("Enter the name of the equipment to search: ")
#    cursor.execute("SELECT equipment_id,serial_number,name,department,status,age FROM equipment WHERE LOWER(name)=LOWER(?)",(name,))
#    equipment=cursor.fetchall()
#    if equipment:
#       for item in equipment:
#        print("ID:", item[0])
#        print("Serial_number",item[1])
#        print("Name:", item[2])
#        print("Department:", item[3])
#        print("Status:", item[4])
#        print("Age:", item[5])
#        print()   
#    else:
#       print("Machine not found")  
#   elif choice=="2":
#     serial_number=input("Enter the serial_number of the equipment to search: ")
#     cursor.execute("SELECT equipment_id,serial_number,name,department,status,age FROM equipment WHERE LOWER(serial_number)=LOWER(?)",(serial_number,))
#     equipment=cursor.fetchall()
#     if equipment:
#       for item in equipment:
#        print("ID:", item[0])
#        print("Serial_number",item[1])
#        print("Name:", item[2])
#        print("Department:", item[3])
#        print("Status:", item[4])
#        print("Age:", item[5])
#        print()
#     else:
#        print("Machine not found")  
#   elif choice=="3":
#     department=input("Enter the department to search: ")
#     cursor.execute("SELECT equipment_id,serial_number,name,department,status,age FROM equipment WHERE LOWER(department)=LOWER(?)",(department,))
#     equipment=cursor.fetchall()
#     if equipment:
#       for item in equipment:
#        print("ID:", item[0])
#        print("Serial_number",item[1])
#        print("Name:", item[2])
#        print("Department:", item[3])
#        print("Status:", item[4])
#        print("Age:", item[5])
#        print()
#     else:
#       print("Machine not found")  
#   elif choice=="4":
#     status=input("Enter the status of the equipment to search: ")
#     cursor.execute("SELECT equipment_id,serial_number,name,department,status,age FROM equipment WHERE LOWER(status)=LOWER(?)",(status,))
#     equipment=cursor.fetchall()
#     if equipment:
#       for item in equipment:
#        print("ID:", item[0])
#        print("Serial_number",item[1])
#        print("Name:", item[2])
#        print("Department:", item[3])
#        print("Status:", item[4])
#        print("Age:", item[5])
#        print()
#     else:
#       print("Machine not found")  
#   elif choice=="5":
#     print("Exiting search...")
#     break
#   else:
#         print("Choice not valid")
# search_menu()
# def equipment_report():
#   cursor.execute("SELECT COUNT(*) FROM equipment")
#   total=cursor.fetchone()
#   print("Total equipments:",total[0])
# #def equipment_status_report():
#   cursor.execute("""SELECT LOWER(department),LOWER(status),COUNT(*)
#    FROM equipment
#    GROUP BY LOWER(department),LOWER(status)
#    ORDER BY COUNT(*) DESC
#    """)
#   results=cursor.fetchall()
#   for item in results:
#     print(item[0],":" ,item[1],":",item[2])

# equipment_report()
# def register_maintenance():
#   equipment_id=input("Equipment_id: ")
#   date=input("Date: ")
#   type_of_maintenance=input("Type of maintenance: ")
#   engineer=input("Engineer: ")
#   time_taken=input("Time taken: ")
#   description=input("Description: ")
#   cursor.execute(""" 
#       INSERT INTO maintenance (equipment_id,date,type_of_maintenance,engineer,time_taken,description)
#       VALUES (?, ?, ?, ?, ?, ?)
#       """,(equipment_id,date,type_of_maintenance,engineer,time_taken,description))
#   connection.commit()
# def view_maintenance():
#    cursor.execute("SELECT maintenance_id,equipment_id,date,type_of_maintenance,engineer,time_taken,description FROM maintenance")
#    maintenance = cursor.fetchall()
#    for item in maintenance:
#         print("maintenance id:", item[0])
#         print("equipment id:",item[1])
#         print("date:", item[2])
#         print("type_of_maintenance:", item[3])
#         print("engineer:", item[4])
#         print("time_taken:", item[5])
#         print("description:",item[6])
#         print() 
cursor.execute("""
SELECT maintenance.equipment_id,maintenance.date,maintenance.type_of_maintenance,maintenance.engineer,maintenance.time_taken,maintenance.description,equipment.serial_number,equipment.name
 FROM maintenance
JOIN equipment
ON maintenance.equipment_id=equipment.equipment_id""")
results= cursor.fetchall()
for item in results:
 print("equipment_id",item[0])
 print("date",item[1])
 print("type_of_maintenance",item[2])
 print("engineer",item[3])
 print("time_taken",item[4])
 print("description",item[5])
 print("serial_number",item[6])
 print("name",item[7])
 print()
# register_maintenance()
# view_maintenance()