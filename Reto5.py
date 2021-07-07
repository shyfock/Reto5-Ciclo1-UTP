from numpy import average
import pandas as pd

def contaminantes(ruta_archivo, anio, codRes):
    try:
        df = pd.read_csv(ruta_archivo, sep = ';')
    except:
        return 'Error con la url del archivo de datos'
    if codRes == 1:
        return Codigo1(anio, df)
    elif codRes == 2:
        return Codigo2(anio, df)
    elif codRes == 3:
        return Codigo3(anio, df)

def Codigo1(Anio, CSV_File):
    listCont1 = []
    listCont2 = []
    listCont3 = []
    for i in range(len(list(CSV_File['codAnio']))):
        if list(CSV_File['codAnio'])[i] == Anio:
            listCont1.append(CSV_File['Cont1'][i])
            listCont2.append(CSV_File['Cont2'][i])
            listCont3.append(CSV_File['Cont3'][i])
        suma = [sum(listCont1), sum(listCont2), sum(listCont3)]
    return suma

def Codigo2(Anio, CSV_File):
    listCont1 = []
    listCont2 = []
    listCont3 = []
    for i in range(len(list(CSV_File['codAnio']))):
        if list(CSV_File['codAnio'])[i] == Anio:
            listCont1.append(CSV_File['Cont1'][i])
            listCont2.append(CSV_File['Cont2'][i])
            listCont3.append(CSV_File['Cont3'][i])
        prom = [round(average(listCont1),1), round(average(listCont2),1), round(average(listCont3),1)]
    return prom

def Codigo3(Anio, CSV_File):
    
    listCodCiud = []
    listCont1 = []
    listCont2 = []
    listCont3 = []
    for i in range(len(list(CSV_File['codAnio']))):
        if list(CSV_File['codAnio'])[i] == Anio:
            listCodCiud.append(CSV_File['CodCiud'][i])
            listCont1.append(CSV_File['Cont1'][i])
            listCont2.append(CSV_File['Cont2'][i])
            listCont3.append(CSV_File['Cont3'][i])
    codCiud = [listCodCiud[listCont1.index(max(listCont1))], listCodCiud[listCont2.index(max(listCont2))], listCodCiud[listCont3.index(max(listCont3))]]
    return codCiud

print(contaminantes('otro.csv',2019,1))
