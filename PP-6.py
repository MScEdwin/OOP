table=int(input("Enter the multiplication table:"))
n= table*11
multi=-1
for i in range(0,n,table):
   multi=multi+1
   print(table, "*", multi, "=", i)