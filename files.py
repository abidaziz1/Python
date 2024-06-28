f = open("F:\USER\Documents\file1.txt","a")
f.write("Now the file has more content!")
f.close()

f = open("F:\USER\Documents\file1.txt","r")
print(f.read())

