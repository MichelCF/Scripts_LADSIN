'''@author: Michel Vieira Caiafa'''

import os
import shutil
import subprocess
import gzip


#Deve ser colocado na pasta Documentos

#Onde estão as pastas com os arquivos parar gerar as tabelas
Inicial ='/home/ladsin/Documentos'

#Onde as tabelas vão ser salvas
Final='/home/ladsin/Área de Trabalho/Anne/JIC/Tabelas/'

#Onde estão os programas que geram as tabelas
Caminho_gera_Tabela = '/home/ladsin/TRACK-1.5.0/utils/bin'


mes = os.listdir(Inicial)
mes = [i for i in mes if i.startswith('_level_ano')]
contador = 0
for i in mes:
    arquivo = os.listdir(Inicial +'/'+i)
    arquivo = [tr for tr in arquivo if tr.startswith('tr')]
    #print(mes[0][10:])
    with gzip.open(i+'/'+arquivo[0], 'rb') as entrada:
       with open(Caminho_gera_Tabela+'/tr_trs', 'wb') as saida:
            shutil.copyfileobj(entrada, saida)
            subprocess.call('./count tr_trs 0 0 5 4 0 '+mes[contador][10:]+ '0100 1', cwd =Caminho_gera_Tabela+'/', shell=True)
            os.rename(Caminho_gera_Tabela+'/tr_trs.new',Caminho_gera_Tabela+'/tr_trs')
            subprocess.call('tr2csv tr_trs', cwd=Caminho_gera_Tabela+'/', shell=True)
            os.remove(Caminho_gera_Tabela+'/tr_trs')
            shutil.move(Caminho_gera_Tabela+'/alltr.csv', Final+mes[contador][10:]+'.csv')
            contador = contador +1
            
    
    

