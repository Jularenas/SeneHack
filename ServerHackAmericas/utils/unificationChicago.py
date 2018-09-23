import os
import json
import csv


rootdir = 'C:/Users/Dell/Downloads/DatosTaxisBogotaY4PT/DatosTaxisBogotaY4PT/'
unificados=[]
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print(rootdir+str(file))
        with open(file, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are ',row[20],row[21],row[17],row{18},row[2])
                    line_count += 1
                else:
                    line_count += 1
                    if (line_count==20):
                        break
                    unificado={}
                    unificado['destino']={}
                    unificado['destino']['latitud']=row[20]
                    unificado['destino']['longitud']=row[21]
                    unificado['origen']={}
                    unificado['origen']['latitud']=row[17]
                    unificado['origen']['longitud']=row[18]
                    unificado['fecha_calculo']=row[2]
                    unificados.append(unificado)

with open('unificadosChicago.json', 'w') as fp:
    json.dump(unificados, fp)    
        
                
       

