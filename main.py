import json
import os

foldersinpublic = os.listdir('public')
totallist={}

def getfilesfrommain(folder):
    totallist[f'{folder}']={}
    additionalSlider=os.listdir(f'public/{folder}/additional')
    firstSlider=os.listdir(f'public/{folder}/main')
    firstSliderNew=[]
    additionalSliderNew = []

    for item in firstSlider:
        firstSliderNew.append(f'public/{folder}/main/{item}')
    totallist[f'{folder}']["firstSlider"]=firstSliderNew

    for item in additionalSlider:
        additionalSliderNew.append(f'public/{folder}/additional/{item}')
    totallist[f'{folder}']["additionalSlider"] = additionalSliderNew


for item in foldersinpublic:
    getfilesfrommain(item)


itemstojsonfile={}
itemstojsonfile["kitchensUrls"]=totallist

with open('kitchenPhotos.json', 'w', encoding='utf8') as f:
    json.dump(itemstojsonfile, f, ensure_ascii=False, indent=4)

# with open('kitchenPhotos.json', encoding='utf8') as f:
#     print(f.read())
print("Файл создан!")