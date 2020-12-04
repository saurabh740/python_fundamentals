import os
import requests
import shutil

def download_file(url, directory, fname=None):
    if fname == None:
        fname = os.path.basename(url)
    
    dl_path = os.path.join(directory, fname)

    with requests.get(url, stream=True) as r:
        r.raise_for_status()

        with open(dl_path, 'wb') as file:
            shutil.copyfileobj(r.raw, file)
    
    return dl_path

def download_file_slower(url, directory, fname=None):
    if fname == None:
        fname = url.split('/')[-1]
    
    dl_path = os.path.join(directory, fname)

    with requests.get(url=url, stream=True) as r:
        r.raise_for_status()
        with open(dl_path, 'wb') as file:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
            
    return dl_path

