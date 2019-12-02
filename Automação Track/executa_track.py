import os
import subprocess

arquivos_dat = os.listdir('/home/ladsin/TRACK-1.5.0/indat')
arquivos_dat = [i for i in arquivos_dat if i.endswith('.dat')]
print(arquivos_dat)
for arquivo in arquivos_dat:

    subprocess.call(' ./master -c='+arquivo.replace('.dat', '')+' -d=now -e=track.linux -i='+arquivo+ ' -f=vo1991 -n=1,746,1 -o=/home/ladsin/Documentos -r=RUN_AT_ -s=RUNDATIN.VOR -j=RUN_AT.in', shell=True)
    
