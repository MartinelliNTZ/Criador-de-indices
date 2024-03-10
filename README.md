# Criador de indíces
 Cria indices a partir de imagens de satelite
 Tanto os poligonos .shp quanto as imagens raster devem estar em WGS84 EPSG:4326 para dar certo
 1- instale essas bibliotecas Python:
import os
import numpy as np
import rasterio
import os
import numpy as np
import rasterio
import shutil
import time
import os
import geopandas as gpd
import rasterio
from rasterio.mask import mask
import os
import geopandas as gpd
import rasterio
from rasterio.mask import mask

2-Coloque seus poligonos no formato .shp dentro da pasta poligonos. Lembrando que para cada arquivo .shp dentro da pasta poligonos sera usado para cortar cada indice em cada data, se vc colorar um multpoligono dentro da pasta e ira recortar somente um aruivo logo vc precisara dividir esse multipoligono para a extensão exata que deseja fazer o recorte, o nome do poligono de recorte sera usado no nome do poligono final.

3-SENTINEL 2-A: para imagens do sentinel 2-a é necessario criar uma subpasta dentro da pasta raiz e e renomeala conforme desejar apenas lembrando que o nome da pasta vai sair no nome final de cada arquivo, normalmente eu coloco apenas a data da imagem no nome da pasta, as imagens baixadas do sentinel devem vir separadas banda a banda se uma banda estiver faltando havera erro no codigo,  os indíces gerados serao: ndvi + moisture + agriculture + ndre + mtli + savi + vari + msavi + evi + reci e tambem uma media com todos eles, caso não queira um desses ou queria adicionar algum calculo basta alterar o script 1, as bandas necessárias são: 
Banda ‘B08’
Banda ‘B04’
Banda ‘B8A’
Banda ‘B11’
Banda ‘B02’
Banda ‘B05’
Banda ‘B03’

Não ´´é necessario renomear as bandas para 'B08' ou 'B04' mas ´´é obrigatorio que em alguma parte do nome contenha o nome da banda. Vc pode pegar varias imagens em datas diferentes basta que cada esteja em uma pasta diferente e o codigo ira gerar os arquivos para cada data, 

4-Por fim execute os scripts em ordem , comece com o script que cria os indices (1) depois oque faz os recortes e por fim oque organiza os arquivos gerados caso queira voce pode parar no passo 2 e seus arquivos estao na pasta recortes dentro da pasta raiz. Se voce tiver 15 .shp e vc tiver 10 pastas com as bandas relativas a 10 datas distintas com alguns minutos o codigo irá gerar 1650 aruivos .tif ja organizados em pastas.
Os arquivos finais serão noemados da seguinte forma (nomeDaSubpasta_nomeDoSHP_nomeDoIndice)Exemplo: 20240310_T38_NDVI, 20230510_TH57_NDRE....
