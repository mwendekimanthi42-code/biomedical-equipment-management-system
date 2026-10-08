import sqlite3
connection=sqlite3.connect("hospital.db")
connection.execute("PRAGMA foreign_keys = ON")#to protect foreign key
cursor=connection.cursor()
from datetime import datetime
#from dateutil.relativedelta import relativedelta
def valid_date():
    while True:
      date= input("Enter date (YYYY-MM-DD): ")
      try:
        datetime.strptime(date, "%Y-%m-%d")
        print("Valid date")
        return date
      except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS equipment (
        equipment_id INTEGER PRIMARY KEY,
        name TEXT,TEXT,
        department TEXT,
        status TEXT,
        age INTEGER
    )
""")
connection.commit()#savesthe changes made
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
#     WHERE equip(ment_id IN (9, 10, 11, 12)
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
#      name=input("Enter the name: ")
#      status_1=input("Enter the first status to search: ")
#      status_2=input("Enter the second status to search: ")
#      cursor.execute("""SELECT equipment_id,serial_number,name,department,status,age 
#      FROM equipment 
#      WHERE LOWER(name) LIKE LOWER(?)
#      AND(LOWER(status)=LOWER(?)
#      OR LOWER(status)=LOWER(?))""",("%" + name + "%", status_1, status_2))
#      equipment=cursor.fetchall()
#      if equipment:
#        for item in equipment:
#          print("ID:", item[0])
#          print("Serial_number",item[1])
#          print("Name:", item[2])
#          print("Department:", item[3])
#          print("Status:", item[4])
#          print("Age:", item[5])
#          print()
#      else:
#         print("NO equipment found")
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
#search_equipment()
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
#   date=valid_date()
#   type_of_maintenance=input("Type of maintenance: ")
#   engineer=input("Engineer: ")
#   time_taken=input("Time taken: ")
#   description=input("Description: ")
#   try:
#    cursor.execute(""" 
#       INSERT INTO maintenance (equipment_id,date,type_of_maintenance,engineer,time_taken,description)
#       VALUES (?, ?, ?, ?, ?, ?)
#       """,(equipment_id,date,type_of_maintenance,engineer,time_taken,description))
#    connection.commit()
#    print("Maintenance registered successfully.")

#   except sqlite3.IntegrityError:#to handle foreign key constraint errors
#     connection.rollback()
#     print("Equipment ID does not exist.")
# def view_maintenance():
#   cursor.execute("""
#   SELECT equipment.serial_number,equipment.name,maintenance.date,maintenance.type_of_maintenance,maintenance.engineer,maintenance.time_taken,maintenance.description
#   FROM maintenance
#   JOIN equipment
#   ON maintenance.equipment_id=equipment.equipment_id""")
#   results= cursor.fetchall()
#   for item in results:
#    print("serial_number:",item[0])
#    print("name:",item[1])
#    print("date:",item[2])
#    print("type_of_maintenance:",item[3])
#    print("engineer:",item[4])
#    print("time_taken:",item[5])
#    print("description:",item[6])
#    print()
#register_maintenance()
#  view_maintenance()
# def search_maintenance():
#     serial_number=input("Enter serial number: ")
#     cursor.execute("""
#     SELECT equipment.serial_number,equipment.name,maintenance.date,maintenance.type_of_maintenance,maintenance.engineer,maintenance.time_taken,maintenance.description
#     FROM maintenance
#     JOIN equipment
#     ON maintenance.equipment_id=equipment.equipment_id
#     WHERE equipment.serial_number= ?""",(serial_number,))
#     results=cursor.fetchall()
#     if results:
#      for item in results:
#         print("serial number:",item[0])
#         print("Name:",item[1])
#         print("Date:",item[2])
#         print("Type of maintenance:",item[3])
#         print("Engineer:",item[4])
#         print("Time taken:",item[5])
#         print("Description",item[6])
#         print()
#     else:
#         print("Equipment with this serial number does not exixst")
# search_maintenance()
# def update_maintenance():
#   description=input("What is the updated description ")
#   maintenance_id=input("What is the maintenance id ")
#   cursor.execute("""
#   UPDATE maintenance
#   SET description= ? 
#   WHERE maintenance_id= ?""",(description,maintenance_id))
#   connection.commit()
#   if cursor.rowcount==1:
#     print("Maintenance updated successfully.")
#   else:
#     print("Maintenance record not found")
# update_maintenance()
# def delete_maintenance():
#   maintenance_id=input("What is the maintenance id ")
#   cursor.execute("""
#   DELETE FROM maintenance
#   WHERE maintenance_id= ?""",(maintenance_id,))
#   connection.commit()
#   if cursor.rowcount==1:
#     print("Maintenance deleted successfully.")
#   else:
#     print("Maintenance record not found")
# delete_maintenance()
# cursor.execute("""
# UPDATE maintenance
# SET date=?
# WHERE date=?
# """,("2026-01-03","2026-1-3"))
# connection.commit()
# def maintenance_history():
#     cursor.execute( """
#     SELECT equipment.serial_number,equipment.name,maintenance.date,maintenance.type_of_maintenance,maintenance.engineer,maintenance.time_taken,maintenance.description
#     FROM maintenance
#     JOIN equipment
#     ON maintenance.equipment_id=equipment.equipment_id
#     ORDER BY maintenance.date DESC
#     """)
#     results=cursor.fetchall()
#     for item in results:
#         print("Equipment serial number:",item[0])
#         print("Equipment name:",item[1])
#         print("Date:",item[2])
#         print("Type of maintenance:",item[3])
#         print("Engineer:",item[4])
#         print("Time taken:",item[5])
#         print("Description:",item[6])
#         print( )
# maintenance_history()
# def search_maintenance_date():
#     maintenance_date=valid_date()
#     cursor.execute("""
#     SELECT equipment.serial_number,equipment.name,maintenance.date,maintenance.type_of_maintenance,maintenance.engineer,maintenance.time_taken,maintenance.description
#     FROM maintenance
#     JOIN equipment
#     ON maintenance.equipment_id=equipment.equipment_id
#     WHERE maintenance.date=?
# """,(maintenance_date,))
#     results=cursor.fetchall()
#     if results:
#       for item in results:
#         print("Equipment serial number:",item[0])
#         print("Equipment name:",item[1])
#         print("Date:",item[2])
#         print("Type of maintenance:",item[3])
#         print("Engineer:",item[4])
#         print("Time taken:",item[5])
#         print("Description:",item[6])
#         print( ) 
#     else:
#         print("NO maintenace record available for this date")
# search_maintenance_date()
# def search_maintenance_type():
#     type=input("Enter maintenance type: ")
#     cursor.execute("""
#     SELECT equipment.serial_number,equipment.name,maintenance.date,maintenance.type_of_maintenance,maintenance.engineer,maintenance.time_taken,maintenance.description
#     FROM maintenance
#     JOIN equipment
#     ON maintenance.equipment_id=equipment.equipment_id
#     WHERE maintenance.type_of_maintenance=?""",(type,))
#     results=cursor.fetchall()
#     if results:
#       for item in results:
#         print("Equipment serial number:",item[0])
#         print("Equipment name:",item[1])
#         print("Date:",item[2])
#         print("Type of maintenance:",item[3])
#         print("Engineer:",item[4])
#         print("Time taken:",item[5])
#         print("Description:",item[6])
#         print( ) 
#     else:
#         print("NO maintenace record available for this type")
# search_maintenance_type()        
# def search_maintenance_engineer():
#     engineer=input("Name of engineer:")
#     cursor.execute("""
#     SELECT equipment.serial_number,equipment.name,maintenance.date,maintenance.type_of_maintenance,maintenance.engineer,maintenance.time_taken,maintenance.description
#     FROM maintenance
#     JOIN equipment
#     ON maintenance.equipment_id=equipment.equipment_id
#     WHERE LOWER(maintenance.engineer)=LOWER(?)""",(engineer,))
#     results=cursor.fetchall()
#     if results:
#       for item in results:
#         print("Equipment serial number:",item[0])
#         print("Equipment name:",item[1])
#         print("Date:",item[2])
#         print("Type of maintenance:",item[3])
#         print("Engineer:",item[4])
#         print("Time taken:",item[5])
#         print("Description:",item[6])
#         print( ) 
#     else:
#         print("NO maintenace record available for this engineer")
# search_maintenance_engineer()        
# def maintenance_report():
#    cursor.execute("""SELECT LOWER(engineer),COUNT(*)
#    FROM maintenance
#    GROUP BY LOWER(engineer)
#    ORDER BY COUNT(*) DESC
#    """)
#    results=cursor.fetchall()
#    for item in results:
#     print(item[0],":" ,item[1])
# maintenance_report()
# def maintenance_type_report():
#    cursor.execute("""SELECT LOWER(type_of_maintenance),COUNT(*)
#    FROM maintenance
#    GROUP BY LOWER(type_of_maintenance)
#    ORDER BY COUNT(*) DESC
#    """)
#    results=cursor.fetchall()
#    for item in results:
#     print(item[0],":" ,item[1])
# maintenance_type_report()
# def maintenance_report():
#    cursor.execute("""SELECT equipment.name,equipment.serial_number,COUNT(*)
#    FROM maintenance
#    JOIN equipment
#    ON maintenance.equipment_id=equipment.equipment_id
#    GROUP BY maintenance.equipment_id
#    ORDER BY COUNT(*) DESC
#    """)
#    results=cursor.fetchall()
#    for item in results:
#     print("name:",item[0],"serial number:",item[1],":",item[2],"maintenance records")
# maintenance_report()
# def latest_maintenance_report():
#     cursor.execute("""SELECT equipment.name,equipment.serial_number,maintenance.date,maintenance.type_of_maintenance
#     FROM maintenance
#     JOIN equipment
#     ON maintenance.equipment_id=equipment.equipment_id
#     WHERE type_of_maintenance=?
#     GROUP BY maintenance.equipment_id
#     ORDER BY MAX(maintenance.date)
#     """,("preventive",))
#     results=cursor.fetchall()
#     for item in results:
#       print("name: ",item[0])
#       print("serial number: ",item[1])
#       print("Last preventive maintenance: ",item[2])
# latest_maintenance_report()
# def next_maintenance_date():
#     cursor.execute("""
#     SELECT MAX(maintenance.date)
#     FROM maintenance
#     WHERE type_of_maintenance='preventive'
#     """)
#     result=cursor.fetchone()
#     last_date=datetime.strptime(result[0],"%Y-%m-%d")
#     month = last_date.month + 6
#     year = last_date.year

#     if month > 12:
#       month -= 12
#       year += 1
#     next_date = last_date.replace(year=year, month=month)
#     print("Last preventive maintenance: ",last_date.strftime("%Y-%m-%d"))
#     print("Next prreventive maintenance: ",next_date.strftime("%Y-%m-%d"))
# next_maintenance_date()

# cursor.execute("""
# DELETE FROM equipment
# WHERE age is NULL""")
# connection.commit()

# cursor.execute("""
# SELECT *
# FROM equipment
# WHERE age is NULL
# """)
# results=cursor.fetchall()
# for item in results:
#   print(item)
# def youngest_equipment():
#   cursor.execute("""
#   SELECT MIN(equipment.age) FROM equipment
#   """)
#   result=cursor.fetchone()
#   print("Youngest equipment age: ",result[0],"years")
# youngest_equipment()
# def oldest_equipment():
#   cursor.execute("""
#   SELECT MAX(equipment.age)
#   FROM equipment """)
#   result=cursor.fetchone()
#   print("Oldest equipment age: ",result[0],"years")
# oldest_equipment()
# def avg_equipment_age():
#   cursor.execute("""
#   SELECT AVG(age)
#   FROM equipment""")
#   result=cursor.fetchone()
#   print("Average age: ",result[0],"years")
# avg_equipment_age()
# def total_equipment_age():
#   cursor.execute("""
#   SELECT SUM(age)
#   FROM equipment""")
#   result=cursor.fetchone()
#   print("Total equipment age: ",result[0],"years")
# total_equipment_age()
# def total_equipment():
#   cursor.execute("""
#   SELECT COUNT(*)
#   FROM equipment""")
#   result=cursor.fetchone()
#   print("Total number of equipment: ",result[0])
# total_equipment
# def equipment_by_department():
#   cursor.execute("""
#   SELECT department, COUNT(*)
#   FROM equipment
#   GROUP BY department
#   ORDER BY COUNT(*) DESC""")
#   result=cursor.fetchall()
#   for item in result:
#     print(item[0],":", item[1])
# equipment_by_department()
# def equipment_by_department_status():
#   cursor.execute("""
#   SELECT department,status,COUNT(*)
#   FROM equipment
#   GROUP BY department,status
#   ORDER BY COUNT(*) DESC""")
#   result=cursor.fetchall()
#   for item in result:
#     print(item[0], ":", item[1], ":", item[2])
# equipment_by_department_status()

# def maintenance_engineer():
#   cursor.execute("""
#   SELECT LOWER(engineer), COUNT(*)
#   FROM maintenance
#   GROUP BY LOWER(engineer)
#   ORDER BY COUNT(*) DESC
#   """)
#   result=cursor.fetchall()
#   for item in result:
#     print(item[0], ":" ,item[1])
# maintenance_engineer()
 
# def maintenance_type_records():
#   cursor.execute("""
#   SELECT type_of_maintenance, COUNT(*)
#   FROM maintenance
#   GROUP BY type_of_maintenance
#   ORDER BY COUNT(*) DESC""")
#   result=cursor.fetchall()
#   for item in result:
#     print(item[0], ":" ,item[1])
# maintenance_type_records()

def equipment_maintenance_records():
  cursor.execute("""
  SELECT equipment.name,equipment.serial_number, COUNT(*)
  FROM maintenance
  JOIN equipment
  ON maintenance.equipment_id=equipment.equipment_id
  GROUP BY equipment.name
  ORDER BY COUNT(*) DESC
  """)
  result=cursor.fetchall()
  for item in result:
    print(item[0], ":" ,item[1], ":" ,item[2])
equipment_maintenance_records()