message = "Babak Khorramdin"

print(message[0])
print(message[6])
splited=message.split(" ")
print(splited)
print(message[0:12:2])

counter=1
for elm in message:
    if elm == message[counter] and counter < len(message):
        print(f"repeated {elm}")
        counter+=1
    counter+=1
    if elm == "m":
        print("True")
        break