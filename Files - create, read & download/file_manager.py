import os

this_file_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(this_file_path)

email = os.path.join(BASE_DIR, 'templates', 'email.txt')
content = ""

with open(email, 'r') as file:
    content = file.read()

print(content.format(name='Saurabh'))