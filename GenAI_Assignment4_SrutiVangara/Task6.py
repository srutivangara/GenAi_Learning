import os
filename = input("Enter the file name: " )
if os.path.exists(filename):
    with open(filename,"r") as f:
        print("File content:\n")
        print(f.read())
else:
    print("File not found. Please check the filename")