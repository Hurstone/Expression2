import os

def rename_songs(directory):
    # Vérifier si le chemin est un répertoire
    if not os.path.isdir(directory):
        print(f"{directory} n'est pas un répertoire valide.")
        return

    # Parcourir les fichiers dans le répertoire
    for filename in os.listdir(directory):
        # Obtenir le chemin complet du fichier
        filepath = os.path.join(directory, filename)
        
        # Obtenir le nom de fichier sans extension
        file_name, file_extension = os.path.splitext(filename)
        
        # Séparer le nom de l'artiste du nom de la chanson
        parts = file_name.split('-')
        if len(parts) > 1:
            song_name = parts[1].strip()
        else:
            song_name = parts[0].strip()
        
        # Construire le nouveau chemin de fichier en utilisant uniquement le nom de la chanson
        new_filename = os.path.join(directory, song_name + file_extension)
        
        # Renommer le fichier
        os.rename(filepath, new_filename)
        print(f"Renommage de {filename} à {song_name}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Spécifiez le chemin du répertoire contenant les fichiers audio que vous souhaitez renommer
    directory_path = "F:"
    rename_songs(directory_path)
