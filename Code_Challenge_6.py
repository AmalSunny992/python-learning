#Write Python code which Accept the student name and in turn returns their respective Mark.
#Make sure to use dictionaries to store student name and their respective mark.
#The dictionary should include at least 7 elements.

marklist = {"Abin" : 270,"Akhil": 310,"Anand": 175,"Anjana": 480,"Bibitha": 499,"Evelyn": 397,"Gopal": 355,"Hari": 420,"Zeniya": 200 }
print(marklist.keys())
inp = input("Please enter a Student Name from the above list to get the Total Mark : ")
print("Total Marks : ",marklist.get(inp,"Student not found,Kindly Recheck"))