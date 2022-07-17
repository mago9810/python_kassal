def run ():
    my_list = [1,"hello", True, 4.5]
    my_dict = {"firsname":"diego","lastname":"Gonzalez"}


    superlist =[
        {"firsname":"diego","lastname":"Gonzalez"}, 
        {"firsname":"Paola","lastname":"Bermudez"},
        {"firsname":"Jeronimo","lastname":"Gonzalez"},
        {"firsname":"Cristobal","lastname":"Gonzalez"},
        {"firsname":"Gilberto","lastname":"Gonzalez"},
        {"firsname":"Ines","lastname":"Diaz"}
    ]
    sueperdict = {
        "natural_nums": [1,9,6,8,5],
        "integer_nums": [-1,-6,0,4,7],
        "floating_nums": [1.2,8.6,51.3,89.66]
    }

    for key , value in sueperdict.items():
        print(key , "-" , value)
        for num in value:
            print(num)
        print()


    for nombre in superlist:
        print(f"""{nombre["firsname"]} {nombre["lastname"]}""")
        if nombre["firsname"] == "diego":
            print("ok")

if __name__ == '__main__':  



    run()


