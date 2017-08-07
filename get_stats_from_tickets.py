import os

dir=".\\tickets\\"
files=os.listdir(dir)
print(files)

for curfile in files:
    file=open(dir+curfile,'r')

    print(curfile[:-len('.csv')]+' : '+file.readline()[:-1])