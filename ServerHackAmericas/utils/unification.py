import os
import json


rootdir = 'C:/Users/Dell/Downloads/DatosTaxisBogotaY4PT/DatosTaxisBogotaY4PT/'
unificados=[]
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print(rootdir+str(file))
        with open(rootdir+str(file), 'r') as f:
            rutas = json.load(f)
        for ruta in rutas:
            if ruta.get('interrumpircarrera') is None and not ruta.get('fincarrera') is None:
                unificado={}
                unificado['destino']=ruta['destino']
                unificado['origen']=ruta['origen']
                unificado['fecha_calculo']=ruta['fecha_calculo']['$date']
                unificados.append(unificado)
with open('unificados.json', 'w') as fp:
    json.dump(unificados, fp)    
        
                
       

