
from re import X


with open ("database.config") as file:
    ip = file.read()
    ip.strip()
    x = "a"
    for char in ip:
        if char != "\n":
            x = x + char 

    y = x.replace("a", "")
    y.strip()
   
name = f"mongodb://{y}:27017"
