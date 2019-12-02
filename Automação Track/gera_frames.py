import os
import shutil
import subprocess

#Caminhos do track
TRACK_PRINCIPAL = '/home/ladsin/TRACK-1.5.0/'
TRACK_INDAT = '/home/ladsin/TRACK-1.5.0/indat/'
TRACK_OUTDAT = '/home/ladsin/TRACK-1.5.0/outdat/'

#Arquivo de saida de FRAME
MAX_FRAME = '745'
SAIDA_FRAME='specfil.filt_band000'

#Dados de vorticidade
DADOS_VORTICIDADE = '/work/archive/Dados - Vort Rel - 850 - Anne'

#Pega apenas as pastas com os dados
anos = os.listdir(DADOS_VORTICIDADE)
anos = [ ano for ano in anos if len(ano)==4]


for ano in anos:
    meses = os.listdir(DADOS_VORTICIDADE +'/'+ ano)
    for mes in meses:
        shutil.copy2(DADOS_VORTICIDADE + '/' + ano+ '/' + mes,
        TRACK_INDAT + mes)
        print (mes)
        subprocess.call('bin/track.linux -i '+mes+' -f filt < Anne_specfiltT42.in', shell = True)
        os.remove(TRACK_INDAT+mes)
        shutil.move(TRACK_OUTDAT + SAIDA_FRAME, TRACK_INDAT)
        final_frame = mes[0:19].replace('.nc', '.dat')
        os.rename(TRACK_INDAT+SAIDA_FRAME,(TRACK_INDAT+final_frame).replace('.nc', '.dat'))
        
