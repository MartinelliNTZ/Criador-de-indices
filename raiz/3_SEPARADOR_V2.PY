import os
import shutil

# Diretório da pasta raiz e da pasta 'poligonos'
dir_raiz = os.getcwd()
dir_poligonos = os.path.join(dir_raiz, 'poligonos')

# Lista todos os shapefiles na pasta 'poligonos' e remove a extensão '.shp' para criar a lista de strings
strings = [os.path.splitext(f)[0] for f in os.listdir(dir_poligonos) if f.endswith('.shp')]

# Vetor com as strings que serão usadas na separação.
indices = ['AGRICULTURE', 'MOISTURE', 'MTLI', 'NDRE', 'NDVI', 'MSAVI', 'VARI', 'SAVI', 'MEDIA','EVI','RECI','EVI','RECI']

dir_recortes = os.path.join(dir_raiz, 'recortes')

# Itera sobre cada string na lista de talhões
for nome_pasta in strings:
    # Cria a nova pasta se ela não existir
    dir_novo = os.path.join(dir_recortes, nome_pasta)
    os.makedirs(dir_novo, exist_ok=True)

    # Lista todos os arquivos no diretório 'recortes'
    itens = os.listdir(dir_recortes)

    # Itera sobre cada item
    for item in itens:
        # Verifica se o item é um arquivo (não uma pasta)
        if os.path.isfile(os.path.join(dir_recortes, item)):
            # Verifica se a string está no nome do item
            if nome_pasta in item:
                # Move o arquivo para a nova pasta
                shutil.move(os.path.join(dir_recortes, item), os.path.join(dir_novo, item))

    print(f"Arquivos movidos para a pasta '{nome_pasta}' com sucesso!")

print("Talhoes Separados")

# Itera sobre cada subpasta na pasta 'recortes'
for subpasta in os.listdir(dir_recortes):
    dir_atual = os.path.join(dir_recortes, subpasta)
    if os.path.isdir(dir_atual):
        # Itera sobre cada string na lista de índices
        for nome_pasta in indices:
            # Cria a nova pasta se ela não existir
            dir_novo = os.path.join(dir_atual, nome_pasta)
            os.makedirs(dir_novo, exist_ok=True)

            # Lista todos os arquivos no diretório atual
            itens = os.listdir(dir_atual)

            # Itera sobre cada item
            for item in itens:
                # Verifica se o item é um arquivo (não uma pasta)
                if os.path.isfile(os.path.join(dir_atual, item)):
                    # Verifica se a string está no nome do item
                    if nome_pasta in item:
                        # Move o arquivo para a nova pasta
                        shutil.move(os.path.join(dir_atual, item), os.path.join(dir_novo, item))

            print(f"Arquivos movidos para a pasta '{nome_pasta}' com sucesso!")

print("Script finalizado.")
