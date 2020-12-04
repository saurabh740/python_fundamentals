import os
from download_util import download_file, download_file_slower

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR = os.path.join(BASE_DIR, 'downloads')
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Classic_view_of_a_cloudfree_Peyto_Lake%2C_Banff_National_Park%2C_Alberta%2C_Canada_%284110933448%29.jpg/240px-Classic_view_of_a_cloudfree_Peyto_Lake%2C_Banff_National_Park%2C_Alberta%2C_Canada_%284110933448%29.jpg'

file_name = download_file(url=url, directory=DOWNLOAD_DIR, fname='downlaod1.jpg')
print(f'{file_name} saved' )

file_name = download_file_slower(url=url, directory=DOWNLOAD_DIR, fname='download2.jpg')
print(file_name)