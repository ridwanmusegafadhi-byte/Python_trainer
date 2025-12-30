squares = []

for i in range(10):
    squares.append(i * i)
    print(squares)

print("------------")

squares = [i*i for i in range (10)]
print(squares)
print("-------------")

fruits =[" apple", "banana", "mango", 'coffe']
print(fruits[3])
fruits.append('orange')
print(fruits)
print("_-------------")


coordinates = (10,20)
print(coordinates[0])


print("-----------")

unique_numbers = {1,2,3,2}
print(unique_numbers)
print("---------------")

person ={"name": "alice", "age": 25, "phone": "+2527896578"}
print(person["name"])
person["city"]= "Hargiesa"
print(person["city"])
person["date_of_birt"] = "1960"
print(person)

greating = "big hello"
name = "mr. muse"
print(greating)
print(name)
print(greating + " " + name)
print("---------")

message = f"{greating} {name}"
print(message)
print("----------")
print(message.upper())
print(message.lower())
print(message.split())
print("---------------")

class RemoteControl:

    def change_channel(self, channel):
        return f"Change channel to {channel}"


if __name__ == "__main__":
    remote = RemoteControl()
    print(remote.change_channel("Tv 4"))










