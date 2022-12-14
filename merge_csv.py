# Librairies
import os

# Constantes
PATH_CSV = 'csv/'
FILE_MERGED = 'merged.csv'

# Fonctions
def list_all_files():
    files = []
    # Lister les fichiers dans le dossier
    for dir in os.listdir(PATH_CSV):
        # Si c'est un dossier
        current_dir = PATH_CSV + dir
        if os.path.isdir(current_dir):
            # Lister les fichiers dans le dossier
            for f in os.listdir(current_dir):
                # Si c'est un fichier .csv
                if f.endswith('.csv'):
                    files.append(current_dir + '/' + f)
    return files

# Programme principal
# Lister les fichiers dans le dossier
filesname = list_all_files()
filesname.sort()
# Ouvrir le fichier de sortie
with open(FILE_MERGED, 'w') as merged:
    # Entête
    header_written = False
    # Parcourir les fichiers
    for filename in filesname:
        print(filename)
        # Ouvrir le fichier
        with open(filename, 'r') as file:
            # Écrire l'entête une seule fois
            if not header_written:
                # Lire l'entête
                header = file.readline()
                # Le traiter
                header = header.lower()
                header = header.replace(' ', '_')
                # Écrire l'entête
                merged.write(header)
                header_written = True
            else:
                # Lire la 1ère ligne pour supprimer l'entête
                file.readline()
            # Lire le reste du fichier
            lines = file.readlines()
            # Parcourir les lignes
            for line in lines:
                # Isoler l'id
                id = line.split(',')[0]
                # Si l'id n'est pas vide
                if id != '':
                    # Ecrire dans le fichier
                    merged.write(line)
