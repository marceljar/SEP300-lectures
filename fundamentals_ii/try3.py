try:
    print("Opening file...")
    f = open("example.txt", "w")
    f.write("Hello, world!!!")
except:
    print("Could not write to file")
else: 
    print("File written successfully")
finally:
    print("Closing file...")
    f.close()
