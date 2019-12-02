import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import pandas as pd

#Recebe o numero de um ciclone faz um plot de sua trajetoria
def plot_ciclones(ciclone):
    
    duracao = len(ciclone)
    print(duracao)
    for i in range(duracao-1):
        posicao1 = ciclone.iloc[i]
        posicao2 = ciclone.iloc[i+1]
        print(posicao1,posicao2)
    
        if i == 0:
            frist_lat, frist_lon = posicao1.Latitude, posicao1.Longitude
            second_lat, second_lon = posicao2.Latitude, posicao2.Longitude
            plt.plot([frist_lon, second_lon], [frist_lat, second_lat],
                     color='black',marker='o',linewidth=0.3,
                     transform=ccrs.PlateCarree()
                     )
        else:
            if i == len(ciclone)-2:
                frist_lat, frist_lon = posicao1.Latitude, posicao1.Longitude
                second_lat, second_lon = posicao2.Latitude, posicao2.Longitude
                plt.plot([frist_lon, second_lon], [frist_lat, second_lat],
                     color='green',marker='o',linewidth=0.3,
                     transform=ccrs.PlateCarree()
                     )
            else:
                frist_lat, frist_lon = posicao1.Latitude, posicao1.Longitude
                second_lat, second_lon = posicao2.Latitude, posicao2.Longitude
                plt.plot([frist_lon, second_lon], [frist_lat, second_lat],
                     color='red',linewidth=0.3,
                     transform=ccrs.PlateCarree()
                     )
#Abre a planilha com os ciclones    
print("Insira o caminho para a tabela de ciclones")
data_path = input()
data = pd.read_csv(data_path)


#Inicio das configurações do plot
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()
ax.coastlines()

print('Gostaria de visualizar todos os ciclones?  S ou N')
resposta = input()
if resposta == 'S':
    ciclones = list( dict.fromkeys(data.N_do_Ciclone) )
    for Ciclone in ciclones:
        n_ciclone = data[(data.N_do_Ciclone == Ciclone)].copy()
        plot_ciclones(n_ciclone)
else:
    print("Informe os numeros dos ciclones que vai visualizar")
    print("Os ciclones devem ser separados por virgulas, sem espaço")
    ciclones = list(input().split(","))
    for Ciclone in ciclones:
        n_ciclone = data[(data.N_do_Ciclone == int(Ciclone))].copy()
        print(n_ciclone)
        plot_ciclones(n_ciclone)
    
plt.show()
#plt.imshow(imagem_fundo, interpolation='none', alpha=0.5)
