# Criador de Índices
https://youtu.be/MdF2Xvwqzmw?si=HrzwSXjpGxDXzN3F

Este script cria índices a partir de imagens de satélite. Tanto os polígonos .shp quanto as imagens raster devem estar em WGS84 EPSG:4326 para funcionar corretamente.

## Instruções

1. **Instale as seguintes bibliotecas Python**:
    - os
    - numpy
    - rasterio
    - shutil
    - time
    - geopandas
    - rasterio.mask

2. **Coloque seus polígonos no formato .shp dentro da pasta 'poligonos'**. Para cada arquivo .shp dentro da pasta 'poligonos', será usado para cortar cada índice em cada data. Se você colocar um multipolígono dentro da pasta, ele irá recortar somente um arquivo. Portanto, você precisará dividir esse multipolígono para a extensão exata que deseja fazer o recorte. O nome do polígono de recorte será usado no nome do polígono final.

3. **Para imagens do Sentinel 2-A**: é necessário criar uma subpasta dentro da pasta raiz e renomeá-la conforme desejar. Lembre-se de que o nome da pasta aparecerá no nome final de cada arquivo. Normalmente, eu coloco apenas a data da imagem no nome da pasta. As imagens baixadas do Sentinel devem vir separadas banda a banda. Se uma banda estiver faltando, haverá erro no código. Os índices gerados serão: NDVI, Moisture, Agriculture, NDRE, MTLI, SAVI, VARI, MSAVI, EVI, RECI e também uma média com todos eles. Caso não queira um desses ou queira adicionar algum cálculo, basta alterar o script 1. As bandas necessárias são: 
    - Banda 'B08'
    - Banda 'B04'
    - Banda 'B8A'
    - Banda 'B11'
    - Banda 'B02'
    - Banda 'B05'
    - Banda 'B03'

    Não é necessário renomear as bandas para 'B08' ou 'B04', mas é obrigatório que em alguma parte do nome contenha o nome da banda. Você pode pegar várias imagens em datas diferentes, desde que cada uma esteja em uma pasta diferente, e o código irá gerar os arquivos para cada data.

4. **Por fim, execute os scripts em ordem**. Comece com o script que cria os índices (1), depois o que faz os recortes e, por fim, o que organiza os arquivos gerados. Caso queira, você pode parar no passo 2 e seus arquivos estarão na pasta 'recortes' dentro da pasta raiz. Se você tiver 15 .shp e tiver 10 pastas com as bandas relativas a 10 datas distintas, em alguns minutos o código irá gerar 1650 arquivos .tif já organizados em pastas. Os arquivos finais serão nomeados da seguinte forma (nomeDaSubpasta_nomeDoSHP_nomeDoIndice). Exemplo: 20240310_T38_NDVI, 20230510_TH57_NDRE...

# Index Creator

This script creates indices from satellite images. Both .shp polygons and raster images must be in WGS84 EPSG:4326 to work correctly.


## Instructions

1. **Install the following Python libraries**:
    - os
    - numpy
    - rasterio
    - shutil
    - time
    - geopandas
    - rasterio.mask

2. **Place your polygons in .shp format inside the 'polygons' folder**. For each .shp file inside the 'polygons' folder, it will be used to cut each index on each date. If you put a multipolygon inside the folder, it will only cut one file. Therefore, you will need to split this multipolygon to the exact extent you want to make the cut. The name of the cutting polygon will be used in the final polygon name.

3. **For Sentinel 2-A images**: it is necessary to create a subfolder within the root folder and rename it as you wish. Remember that the name of the folder will appear in the final name of each file. Usually, I just put the date of the image in the folder name. The images downloaded from Sentinel must come separated band by band. If a band is missing, there will be an error in the code. The generated indices will be: NDVI, Moisture, Agriculture, NDRE, MTLI, SAVI, VARI, MSAVI, EVI, RECI and also an average with all of them. If you don't want one of these or want to add some calculation, just change script 1. The necessary bands are: 
    - Band 'B08'
    - Band 'B04'
    - Band 'B8A'
    - Band 'B11'
    - Band 'B02'
    - Band 'B05'
    - Band 'B03'

    It is not necessary to rename the bands to 'B08' or 'B04', but it is mandatory that some part of the name contains the name of the band. You can get several images on different dates, as long as each one is in a different folder, and the code will generate the files for each date.

4. **Finally, run the scripts in order**. Start with the script that creates the indices (1), then the one that makes the cuts and finally the one that organizes the generated files. If you want, you can stop at step 2 and your files will be in the 'cuts' folder within the root folder. If you have 15 .shp and have 10 folders with the bands relative to 10 different dates, in a few minutes the code will generate 1650 .tif files already organized in folders. The final files will be named in the following way (nameOfSubfolder_nameOfSHP_nameOfIndex). Example: 20240310_T38_NDVI, 20230510_TH57_NDRE...


# Creador de Índices

Este script crea índices a partir de imágenes de satélite. Tanto los polígonos .shp como las imágenes raster deben estar en WGS84 EPSG:4326 para funcionar correctamente.

## Instrucciones

1. **Instale las siguientes bibliotecas de Python**:
    - os
    - numpy
    - rasterio
    - shutil
    - time
    - geopandas
    - rasterio.mask

2. **Coloque sus polígonos en formato .shp dentro de la carpeta 'poligonos'**. Para cada archivo .shp dentro de la carpeta 'poligonos', se utilizará para cortar cada índice en cada fecha. Si pone un multipolígono dentro de la carpeta, sólo cortará un archivo. Por lo tanto, necesitará dividir este multipolígono hasta la extensión exacta que desea hacer el corte. El nombre del polígono de corte se utilizará en el nombre del polígono final.

3. **Para imágenes del Sentinel 2-A**: es necesario crear una subcarpeta dentro de la carpeta raíz y renombrarla como desee. Recuerde que el nombre de la carpeta aparecerá en el nombre final de cada archivo. Normalmente, sólo pongo la fecha de la imagen en el nombre de la carpeta. Las imágenes descargadas del Sentinel deben venir separadas banda por banda. Si falta una banda, habrá un error en el código. Los índices generados serán: NDVI, Moisture, Agriculture, NDRE, MTLI, SAVI, VARI, MSAVI, EVI, RECI y también un promedio con todos ellos. Si no quiere uno de estos o quiere añadir algún cálculo, sólo tiene que cambiar el script 1. Las bandas necesarias son: 
    - Banda 'B08'
    - Banda 'B04'
    - Banda 'B8A'
    - Banda 'B11'
    - Banda 'B02'
    - Banda 'B05'
    - Banda 'B03'

    No es necesario renombrar las bandas a 'B08' o 'B04', pero es obligatorio que alguna parte del nombre contenga el nombre de la banda. Puede obtener varias imágenes en diferentes fechas, siempre y cuando cada una esté en una carpeta diferente, y el código generará los archivos para cada fecha.

4. **Finalmente, ejecute los scripts en orden**. Comience con el script que crea los índices (1), luego el que hace los cortes y finalmente el que organiza los archivos generados. Si lo desea, puede detenerse en el paso 2 y sus archivos estarán en la carpeta 'recortes' dentro de la carpeta raíz. Si tiene 15 .shp y tiene 10 carpetas con las bandas rel
