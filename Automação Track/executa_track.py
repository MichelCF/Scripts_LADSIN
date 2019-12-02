import os
import subprocess
#Esse script deve estar na pasta principal do algoritimo TRACK
print('Insira o caminho para pasta indat do TRACK')
path_indat = input()
print('Insira o caminho da pasta onde deseja salvar o resultado do TRACK')
path_resultado = input()
arquivos_dat = os.listdir(path_indat)
arquivos_dat = [i for i in arquivos_dat if i.endswith('.dat')]

for arquivo in arquivos_dat:

    subprocess.call(' ./master -c='+arquivo.replace('.dat', '')+' -d=now -e=track.linux -i='+arquivo+ 
                    ' -f=vo1991 -n=1,746,1 -o='+path_resultado+' -r=RUN_AT_ -s=RUNDATIN.VOR -j=RUN_AT.in', shell=True)
    
