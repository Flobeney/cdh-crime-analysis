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
    # Parcourir les fichiers
    for filename in filesname:
        print(filename)
        # Ouvrir le fichier
        with open(filename, 'r') as file:
            # Lire la 1ère ligne pour supprimer l'entête
            file.readline()
            # Lire le reste du fichier
            content = file.read()
            # Ecrire dans le fichier
            merged.write(content)
