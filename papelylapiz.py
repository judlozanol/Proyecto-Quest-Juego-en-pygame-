from random import randint
lvl=["          ",
    "          ",
    "          ",
    "          ",
    "          ",
    "          "]
bombas=3    
while bombas>0:
    row_c=randint(0, len(lvl)-1)
    column_c=randint(0,len(lvl[row_c])-1)
    for row_index,row in enumerate(lvl):
        if row_index==row_c:
            nueva_linea=""
            for column_index,column in enumerate(row):  
                agregar=column
                if column_index==column_c and column==" ":
                    agregar="B"
                nueva_linea=nueva_linea+agregar
            lvl[row_index]=nueva_linea
            bombas-=1
print(lvl)

