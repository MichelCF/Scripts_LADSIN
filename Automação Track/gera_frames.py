import os
import shutil
import subprocess

#Caminhos do track
print('Insira o caminho para a pasta principal do TRACK')
TRACK_PRINCIPAL = input()
print('Insira o caminho para a pasta indat do TRACK')
TRACK_INDAT = input()
print('Insira o caminho para a pasta outdat do TRACK')
TRACK_OUTDAT = input()

#Arquivo de saida de FRAME

SAIDA_FRAME='specfil.filt_band000'

#Dados de vorticidade
print('Informe o caminho para a pasta com seus dados de vorticidade')
DADOS_VORTICIDADE = input()

#Pega apenas as pastas com os dados
anos = os.listdir(DADOS_VORTICIDADE)
anos = [ ano for ano in anos if len(ano)==4] #pensar em uma solução melhor

#Pega o nome do arquivo specfiltT42
print('informe o nome do seu arquivo de filtragem')
specfiltT42 = input()


for ano in anos:
    meses = os.listdir(DADOS_VORTICIDADE +'/'+ ano)
    for mes in meses:
        shutil.copy2(DADOS_VORTICIDADE + '/' + ano+ '/' + mes,
        TRACK_INDAT + mes)
        print (mes)
        subprocess.call('bin/track.linux -i '+mes+' -f filt < '+specfiltT42, shell = True)
        os.remove(TRACK_INDAT+mes)
        shutil.move(TRACK_OUTDAT + SAIDA_FRAME, TRACK_INDAT)
        final_frame = mes[0:19].replace('.nc', '.dat')#pensar em uma solução melhor
        os.rename(TRACK_INDAT+SAIDA_FRAME,(TRACK_INDAT+final_frame).replace('.nc', '.dat'))
        
