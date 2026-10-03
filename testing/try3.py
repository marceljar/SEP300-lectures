try:
    print("Opening file...")
    f = open("example.txt", "w")
    f.write("Hello, world!")
    print("Write successful")
except IOError:
    print("Could not write to file")
finally:
    print("Closing file...")
    f.close()
