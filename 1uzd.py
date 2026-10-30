with open("animal_info.txt", "r", encoding="utf-8") as file:
    #b.	Saskaitiet par cik dzīvniekiem ir doti dati failā un izvadiet rezultātu 
    text = file.read()
    z = 0
    for x in text.splitlines():
        z += 1
    """print(z)"""
    #c.	Izvadiet dzīvnieku nosaukumus dilstošā alfabētiskā secībā 
    sar = []
    x = 0
    for elem in text.splitlines():
        sar.append(elem.split(" -", 1)[0])
    sar.sort()
    """print(sar)"""
    #d.	Izvadiet dzīvniekus ar visgarāko latīnisko nosaukumu 
    lenght = 0
    for elem in sar:
        if len(elem) > int(lenght):
            lenght = len(elem)
            dziv = elem
    print(lenght, dziv)
