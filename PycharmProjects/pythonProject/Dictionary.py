user = {
    "name": "Grace",
    "age" : 21,
    "height" : 5.1,
}
print(user)
print("Name is", user.get("name"))
print("Height is", user.get('height', 53))
print("Age is", user["age"])


user = [
    { "name": "grace",
      "age" : 21,
      "height" : 5.4,
      "hobbies" : ("eating"),
    },
    {"name": "aj",
     "age": 40,
     "height": 5.3,
     "hobbies": "sleeping",
     },
    {"name": "americana",
     "age": 55,
     "height": 5.2,
     "hobbies": "singing",
     }
]

# print(user[0]["gender"] = ["female"])
print(user[0]["name"],"\n", user[0]["age"], "\n", user[0]["height"], "\n", user[0]["hobbies"])


book = {
    "title": "The tortoise and the snail.",
    "author": "Tomide",
    "ISBN": 121212221,
    "price": 500
}

book.update({"title": "Ashley", "color": "black"})

book2 = book.copy()
book.clear()
print(book)
print(book2)

for key, value in book.items():
    for value in book.keys():
        print(key,value)
        print(key)

    #print("title" in book.keys())
    # print("Tomide" in book.values())