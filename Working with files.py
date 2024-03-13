f=open("created using python.txt","r+")
#a=input("Enter whatever you want:")
#a=a[::2]
#f.write(a)
f.seek(0)
b=f.read()
print(b)
f.close()

