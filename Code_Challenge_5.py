#Code Challenge 5
#1. Write Python code to open a file named Fileprogram.txt and write some random data into it.
file = open("Fileprogram.txt", 'w')
file.write("what are you? ")
file.close()
#2. Open the file, read the contents and display them as output.
file = open("Fileprogram.txt", 'r')
content = file.read()
print (content)
file.close()
#3. Write python code to add additional text to the existing file on a new line without deleting the previous contents
file = open("Fileprogram.txt", 'a')
file.write("why are you here when you have other places to be.")
file.close()
file = open("Fileprogram.txt", 'r')
content = file.read()
print (content)
file.close()