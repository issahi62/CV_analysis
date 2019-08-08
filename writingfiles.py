import csv as cv

conc = []
man =[]
with open("wr.txt", "w+") as file:
    file.seek(0)
    for i in range(1,101):
        conc.append(i)
        man.append(float(1/i))
    for k in man:
        file.write(str(k))
        
        pass
    
    for Y in conc:
        pass 
        file.write('{0}'.format(Y))
        file.write(",\n")
    
    print(conc)
    print(man)
    print(file.read())
    file.close()
