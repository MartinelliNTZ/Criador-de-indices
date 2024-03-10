import os
import numpy as np
import rasterio
import shutil
import time
import os
import geopandas as gpd
import rasterio
from rasterio.mask import mask

# Códigos e pastas a serem ignoradas
codigos = ["B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08", "B8A", "B09", "B11", "B12"]
ignore = ["scripts","recortes","poligonos"]

# Caminho relativo para o diretório com os arquivos
diretorio_raiz = os.path.dirname(os.path.realpath(__file__))

# Percorre todos os subdiretórios no diretório raiz
CONT = 0
for diretorio, subdiretorios, arquivos in os.walk(diretorio_raiz):
    CONT=CONT+1
    print("Analisando pasta {CONT}")
    # Ignora o diretório raiz e as pastas listadas em 'ignore'
    if diretorio == diretorio_raiz or any(ignorado in diretorio for ignorado in ignore):
        continue

    # Cria as pastas 'bandas' e 'indices' dentro de cada subdiretório
    pasta_bandas = os.path.join(diretorio, 'bandas')
    pasta_saida = os.path.join(diretorio, 'indices')
    os.makedirs(pasta_bandas, exist_ok=True)
    os.makedirs(pasta_saida, exist_ok=True)

    # Percorre todos os arquivos no subdiretório atual
    for nome_arquivo in arquivos:
        # Verifica se o arquivo contém algum dos códigos
        for codigo in codigos:
            if codigo in nome_arquivo:
                # Separa o nome do arquivo e a extensão
                nome_base, extensao = os.path.splitext(nome_arquivo)
                # Renomeia o arquivo para o código encontrado, mantendo a extensão original
                novo_nome_arquivo = codigo + extensao
                if not os.path.exists(os.path.join(diretorio, novo_nome_arquivo)):
                    os.rename(os.path.join(diretorio, nome_arquivo), os.path.join(diretorio, novo_nome_arquivo))

    print("Arquivos renomeados com sucesso!")

    # Abra as bandas como datasets separados
    bandas = {}
    meta = None

    # Percorra todos os arquivos no diretório atual
    for nome_arquivo in os.listdir(diretorio):
        # Verifique se o arquivo contém algum dos códigos
        for codigo in codigos:
            if codigo in nome_arquivo:
                # Abra o arquivo como um dataset rasterio
                with rasterio.open(os.path.join(diretorio, nome_arquivo)) as src:
                    # Salve os dados da banda e os metadados
                    bandas[codigo] = src.read(1)
                    if meta is None:
                        meta = src.meta

    # Gere os índices    
    ndvi = (bandas['B08'].astype(float) - bandas['B04'].astype(float)) / (bandas['B08'] + bandas['B04'])
    moisture = (bandas['B8A'] - bandas['B11']) / (bandas['B8A'] + bandas['B11'])
    agriculture = bandas['B11'] + bandas['B8A'] + bandas['B02']
    ndre = (bandas['B08'] - bandas['B05']) / (bandas['B08'] + bandas['B05'])
    mtli = (bandas['B05'] - bandas['B04']) / (bandas['B05'] + bandas['B04'])
    savi = 1.5 * (bandas['B08'] - bandas['B04']) / (bandas['B08'] + bandas['B04'] + 0.5)
    vari = (bandas['B03'] - bandas['B04']) / (bandas['B03'] + bandas['B04'] - bandas['B02'])
    msavi = (2 * bandas['B04'] + 1 - np.sqrt((2 * bandas['B04'] + 1)**2 - 8 * (bandas['B04'] - bandas['B03']))) / 2
    evi = 2.5 * ((bandas['B08'] - bandas['B04']) / (bandas['B08'] + 6 * bandas['B04'] - 7.5 * bandas['B02'] + 1))
    reci = (bandas['B08']-bandas['B04'])- 1
    media =(ndvi + moisture + agriculture + ndre + mtli + savi + vari + msavi + evi + reci) /10
    indices = {'NDVI': ndvi, 'MOISTURE': moisture, 'AGRICULTURE': agriculture, 'NDRE': ndre, 'MTLI': mtli, 'SAVI': savi, 'VARI': vari, 'MSAVI': msavi, 'EVI':evi,'RECI':reci}

    for indice_nome, indice_valores in indices.items():
        # Atualize a metainformação do conjunto de dados de destino
        meta.update(driver='GTiff', dtype=rasterio.float32, height=indice_valores.shape[0], width=indice_valores.shape[1])

        # Cria o nome do arquivo de saída usando a data, o nome e o nome do índice fornecidos pelo usuário
        nome_arquivo_saida = os.path.join(pasta_saida, f"{indice_nome}.tif")

        with rasterio.open(nome_arquivo_saida, 'w', **meta) as dest:
            dest.write(indice_valores.astype(rasterio.float32), 1)

        print(f"Arquivo {indice_nome} salvo como {nome_arquivo_saida}!")
print('SCRIPT FINALIZADO 100%')