import os

def listar_pdfs(pasta):
    pdfs_dir = []

    for item in os.listdir(pasta):
        item_dir = os.path.join(pasta, item)

        if os.path.isfile(item_dir) and item_dir.lower().endswith(".pdf"):
            pdfs_dir.append(item_dir)
    
    return pdfs_dir