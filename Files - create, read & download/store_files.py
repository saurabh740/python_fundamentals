import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_dir = os.path.join(BASE_DIR, 'files')

os.makedirs(file_dir, exist_ok=True)

my_file = range(0, 10)

for i in my_file:
    file_path = os.path.join(file_dir, f'{i}.txt')

    if os.path.exists(file_path):
        print(f'{i}.txt skipped')
        continue

    with open(file_path, 'w') as file:
        file.write('hello world')

    
    
