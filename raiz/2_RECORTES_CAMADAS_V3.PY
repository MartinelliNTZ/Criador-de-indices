import os
import geopandas as gpd
import rasterio
from rasterio.mask import mask

# Diretórios das pastas
dir_raiz = os.getcwd()
dir_poligonos = os.path.join(dir_raiz, 'poligonos')
dir_recortes = os.path.join(dir_raiz, 'recortes')
print("Pastas Lidas")
# Cria a pasta 'recortes' se ela não existir
os.makedirs(dir_recortes, exist_ok=True)

# Lista todos os shapefiles
shapefiles = [f for f in os.listdir(dir_poligonos) if f.endswith('.shp')]
print("Shapefiles Listados")
c =1
# Percorre todas as subpastas no diretório raiz
for subpasta in os.listdir(dir_raiz):
    print("iniciado {c}° pasta")
    c = c+1
    # Ignora o diretório raiz, a pasta 'poligonos' e arquivos .py
    if subpasta in [os.path.basename(dir_raiz), 'poligonos'] or subpasta.endswith('.py'):
        continue

    # Define o diretório da subpasta e a pasta 'indices' dentro da subpasta
    dir_subpasta = os.path.join(dir_raiz, subpasta)
    dir_indices = os.path.join(dir_subpasta, 'indices')

    # Verifica se o diretório 'indices' existe antes de tentar listar seus arquivos
    if os.path.isdir(dir_indices):
        rasters = [f for f in os.listdir(dir_indices) if f.endswith('.tif')]
    else:
        print(f"O diretório {dir_indices} não existe")
        continue

    # Itera sobre cada combinação de shapefile e raster
    for shapefile in shapefiles:
        for raster in rasters:
            try:
                # Carrega o shapefile como um geodataframe
                gdf = gpd.read_file(os.path.join(dir_poligonos, shapefile))

                # Converte o geodataframe em um formato que rasterio pode usar
                geoms = gdf.geometry.values.tolist()

                # Abre o arquivo raster
                with rasterio.open(os.path.join(dir_indices, raster)) as src:
                    out_image, out_transform = mask(src, geoms, crop=True)
                    out_meta = src.meta.copy()

                # Atualiza as metainformações com as novas dimensões, transformações e (se necessário) sistema de coordenadas
                out_meta.update({"driver": "GTiff",
                                 "height": out_image.shape[1],
                                 "width": out_image.shape[2],
                                 "transform": out_transform})

                # Define o nome do novo raster recortado
                nome_recorte = os.path.join(dir_recortes, f'{subpasta}_{os.path.splitext(shapefile)[0]}_{os.path.splitext(raster)[0]}.tif')

                # Verifica se o arquivo já existe e, em caso afirmativo, adiciona um sufixo
                if os.path.exists(nome_recorte):
                    base, ext = os.path.splitext(nome_recorte)
                    i = 1
                    while os.path.exists(f"{base}_{i}{ext}"):
                        i += 1
                    nome_recorte = f"{base}_{i}{ext}"

                # Salva o novo raster recortado
                with rasterio.open(nome_recorte, 'w', **out_meta) as dest:
                    dest.write(out_image)
            except Exception as e:
                print(f"Erro ao processar o raster {raster} com o shapefile {shapefile}: {str(e)}")

print("SCRIPT FINALIZADO 100%")
