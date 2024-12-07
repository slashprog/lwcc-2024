import shelve

d = shelve.open("user_info")

name = input("Enter your name: ")
place = input("Where do you stay ? ")
d["name"] = name
d["place"] = place
d.close()
print("Stored details")
