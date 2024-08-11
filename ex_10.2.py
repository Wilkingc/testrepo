fname = input("Enter file:")
if len(fname) < 1: fname = "mbox-short.txt"
fhand = open(fname)

count = dict()

for line in fhand:
    if line.startswith("From "):
        word = line.split()
        time = word[5]
        hour = time[:2]
        count[hour] = count.get(hour, 0) + 1
        
        
        #print(word)
for key, val in sorted(count.items()):
    print(key,val)
       
        
  
