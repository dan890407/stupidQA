with open ("tw.txt","r",encoding="UTF-8") as f:
    with open ("tw.dict.txt","w",encoding="UTF-8") as p:
        i=0
        for line in f.readlines():
            word=line.split(" ")
            k=word[0]+" "+word[1]+" "+word[2].lower()
            p.write(k)
            i+=1
