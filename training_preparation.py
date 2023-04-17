import os

# # 1. клонировать репозиторий и сменить ветку
# print("=== Cloning repo ===")
# os.system("git clone https://github.com/datapaf/sit_asg.git; cd sit_asg; git checkout -b emb_cpu; git pull origin emb_cpu")

# 2. скачать датасет токенов data.zip из гугл драйва(для гитхаба слишком много весит), разархивировать и положить папку sit_asg
print("=== Downloading data.zip ===")
os.system("pip install gdown")
import gdown
url = 'https://drive.google.com/uc?id=1iVR0WsEs3v9NLKEjBmQnaLuqccK2pyl5'
output = 'data.zip'
gdown.download(url, output, quiet=False)
os.system("unzip data.zip -d sit_asg/")

# 3. скачать все файлы частично обученной модели и положить в папку SiTASGModels, соседствующую с sit_asg
print("=== Downloading SiTASGModels ===")
url = 'https://drive.google.com/uc?id=1nP8evjcN4kE0OXO6-g2BxRuWp0CCt283'
output = 'SiTASGModels.zip'
gdown.download(url, output, quiet=False)
os.system("unzip SiTASGModels.zip -d sit_asg/")

# 4. разархивировать lines.zip и adjacency.zip в sit_asg
print("=== Unzipping lines.zip and adjacency.zip ===")
os.system("unzip sit_asg/adjacency.zip -d sit_asg/")
os.system("unzip sit_asg/lines.zip -d sit_asg/")
