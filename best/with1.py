print("Opening file...")
with open("example.txt", "w") as f:
    try:
        f.write("Hello, world!")
        print("Write successful")
    except IOError:
        print("Could not write to file")
print("File is now closed")
