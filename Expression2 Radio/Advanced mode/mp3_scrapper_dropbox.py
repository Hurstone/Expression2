import dropbox
import os

# Remplacer 'YOUR_ACCESS_TOKEN' par votre token d'accès Dropbox
ACCESS_TOKEN = ''

def get_dropbox_links(folder_path):
    dbx = dropbox.Dropbox(ACCESS_TOKEN)
    links = []

    try:
        # Initialiser la récupération des fichiers
        result = dbx.files_list_folder(folder_path, recursive=True)
        
        # Fonction pour traiter les entrées et récupérer les liens
        def process_entries(entries):
            for entry in entries:
                if isinstance(entry, dropbox.files.FileMetadata):
                    try:
                        # Essayer de générer un lien temporaire pour chaque fichier
                        shared_link_metadata = dbx.sharing_create_shared_link_with_settings(entry.path_lower)
                        links.append(shared_link_metadata.url)
                    except dropbox.exceptions.ApiError as err:
                        # Si le lien existe déjà, récupérer le lien existant
                        if isinstance(err.error, dropbox.sharing.CreateSharedLinkWithSettingsError):
                            if err.error.is_shared_link_already_exists():
                                try:
                                    shared_links = dbx.sharing_list_shared_links(entry.path_lower, direct_only=True)
                                    if shared_links.links:
                                        links.append(shared_links.links[0].url)
                                except dropbox.exceptions.ApiError as inner_err:
                                    print(f"Erreur API Dropbox lors de la récupération du lien existant pour {entry.path_lower}: {inner_err}")
                        else:
                            print(f"Erreur API Dropbox lors de la création du lien pour {entry.path_lower}: {err}")

        # Traiter la première page de résultats
        process_entries(result.entries)
        
        # Récupérer les pages suivantes si elles existent
        while result.has_more:
            result = dbx.files_list_folder_continue(result.cursor)
            process_entries(result.entries)

    except dropbox.exceptions.ApiError as err:
        print(f'Erreur API Dropbox: {err}')
    return links

def save_links_to_file(links, file_path):
    with open(file_path, 'w') as file:
        for link in links:
            file.write(link + ',')

if __name__ == '__main__':
    folder_path = ''  # Chemin du dossier Dropbox à scanner, par exemple '', '/Musique', etc.
    output_file = 'dropbox_links.txt'

    links = get_dropbox_links(folder_path)
    save_links_to_file(links, output_file)

    print(f'{len(links)} liens ont été sauvegardés dans {os.path.abspath(output_file)}')
