
def update_file():

    with open("visitors.txt") as file:
        data = int(file.read())
    with open("visitors.txt", "w") as file:
        file.write(str(data+1))