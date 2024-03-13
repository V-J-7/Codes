import csv
fh=open("Anime.csv","w")
aniwriter=csv.writer(fh)
aniwriter.writerow(["Name","Rating out of 10"])
for x in range(5):
    print("Show number:-",(x+1))
    name=input("Enter the name:-")
    rating=float(input("Enter the rating out of 10"))
    anirec=[name,rating]
    aniwriter.writerow(anirec)
fh.close()
