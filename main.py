from js import document

def update_file(*args, **kwargs):
    output = document.getElementById("output")
    

    with open("visitors.txt") as file:
        data = int(file.read())
    with open("visitors.txt", "w") as file:
        file.write(str(data+1))
    output.innerHTML = f"Current Count: {data+1}"