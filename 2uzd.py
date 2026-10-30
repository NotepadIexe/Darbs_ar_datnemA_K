with open("C:/Users/STUDENTS/Downloads/animal_dataset.csv", "r", encoding="utf-8") as file:
    text = file.read()
    #c.	Izveidojiet programmu, kas izvada ierakstu skaitu par dzīvnieku, kuru vārds satur lietotāja ievadīto tekstu.
    dzivnieka_n = str(input("Ievadi dzivnieka vardu: "))
    sar1 = [] #Species
    sar2 = [] #Diet_Type
    sar3 = [] #Intelligence_Level
    sar4 = [] #Nocturnal
    x = 0
    for elem in text.splitlines():
        sar1.append(elem.split(",")[1])
        sar2.append(elem.split(",")[5])
        sar3.append(elem.split(",")[-2])
        sar4.append(elem.split(",")[-4])
    for elem in sar1:
        if elem == dzivnieka_n:
            x += 1
    print(x)
    #d.	Izvadiet visus dzīvniekus, kuri atbilst visiem šiem parametriem (visi parametri attiecas uz vienu ierakstu.
    i = 0
    qsar = []
    for x in range(len(sar1)):
        qsar.append([sar1[i],sar2[i],sar3[i],sar4[i]])
        i += 1
    i = 0
    ksar = []
    for elem in qsar:
        if qsar[i][-3] == "Herbivore": 
            if qsar[i][-2] == "Low" : 
                if qsar[i][-1] == "No":
                    ksar.append(qsar[i][0])
        i += 1
    print(ksar)
    
