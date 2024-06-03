##Python - Code Challenge 1
##1. Make a list of your favourite Movies, the list should have minimum 8 elements.
##Answer
fav_movz = ["Dark Knight","Inception","Prestige","Memento","Dunkirk","Tenet","Oppenheimer","Interstellar"]
##2. Print a specified list after removing the 5th element.
##Answer
fav_movz.pop(4)
print(fav_movz)
##3. Insert your favourite movie director name at the 4th index position of the list and print out the list elements.
##Answer
fav_movz.insert(3,"Christopher Nolan")
print(fav_movz)
##4. List out the 4th element in the list.
print(fav_movz[3])
##5. Add additional item to the current list and display the list.
new_movie = input("Enter a movie name : ")
fav_movz.append(new_movie)
print(fav_movz)