# *.txt  Text storage
# *.dat  Object storage
# MYSQL

#STORE TEXT
file1 = open("mytext.txt","a")

file1.write(input("Write a part of your day: "))
file1.write("\n")
file1.write("Life is beautiful")
file1.write("\n")
file1.close()

file2 = open("mytext.txt","r")

for line in file2:
    a_word = "woke"
    if a_word in line:
        print(line)
file2.close()


