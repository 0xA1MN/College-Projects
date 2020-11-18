
# Simple Database Management System

# SOME "DML" Commands 
# INSERT / SELECT

# TODO: Drop All

# Header Start 
print("""
# Simple Database Management System
        With Error handling

  - SOME "DML" Commands : INSERT / SELECT

  * input be like [Identifier] [Data]

  EX: INSERT (Data)       Add Data
      SELECT *            Display all content
      DROP *              Delete all content
      EXIT                End the program

  Hint: App accept lower and upper case identifiers
""")


# libraries
import os
from os import path

# Program Start
while True :
  # Catch Input
  print("Enter Query :")
  query = input()

  # Catch identifier
  identifier =  query.lower().split()[0]
  identifiers = ["insert","select", "drop", "exit"]

  # handle identifier error
  if identifier in identifiers :
    # Catch Data
    wCount = len(query.split()) 
    # check data exist or not
    if wCount > 1 :
      data = query.split(' ', 1)[1]
      
      # Classify identifier
      if identifier == "insert":
        # insert identifier
        table = open("table.txt", "a")
        table.write(data + "\n")
        table.close()
        print(data + " >>> INSERTED Successfully")
        
      elif identifier == "select":
        # select identifier
        if path.exists("guru99.txt") :
          table = open("table.txt", "r")
          content = table.read()
          table.close()
          print(content)
        else :
          print("No Records To Display")

      elif identifier == "drop":
        # drop identifier
        os.remove("table.txt")
        print("All Records Deleted Successfully")
  
    else :
      # data error
      print("""
      Missed Data
      
      [INPUT be Like]
      INSERT (Data)       To Add Data
      SELECT *            To Display All Content
      DROP *              To Delete All Content
      """)
    
    # exit 
    if wCount == 1 :
      identifier = query
      if identifier == "exit" :
        quit()
  
  else :
    # Identifier error
    print("""
    Invalid Identifier

    [INPUT be Like]
    INSERT (Data)       To Add Data
    SELECT *            To Display All Content
    DROP *              To Delete All Content
    """)
