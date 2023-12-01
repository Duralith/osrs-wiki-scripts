"""bulk_moid_downloader.py
by Duralith, 2023.

Script to save images in bulk from the Old School RuneScape Wiki's
Minimal OSRS item DB (moid).
(https://chisel.weirdgloop.org/moid/)

Using this script:
Edit the following values below (Marked with TODOs to find easily since one had to be buried in a loop) as
appropriate:

input_file_name: Should be a CSV file with columns ("id,"filename"), where id is the item/object/NPC id and filename
    is the desired file name to use locally, sans extension.

file_path: Desired location for downloads

url_type: Used to set the specific image type retrieved. Refer to the commented-out table above the declaration
    for formats.

"""

import os
import requests
import pandas as pd

# TODO set input file here
input_file_name = 'files_to_fetch.csv'

# TODO set download location here
file_path = f'.\\moid_downloads'


def download(url, filename):
    with open(filename, 'wb') as file:
        response = requests.get(url)
        file.write(response.content)

base_url = 'https://chisel.weirdgloop.org/static/img/'

with open(input_file_name, 'r', encoding='utf-8-sig') as infile:
    df = pd.read_csv(infile)

if not os.path.exists(file_path):
    os.makedirs(file_path)

for i in range(len(df.index)):
    file_id = df.at[i, "id"]
    file_name = f'{file_path}\\{df.at[i, "filename"]}.png'

    # Moid URL types:
    # NPC: /osrs-npc/
    #   <id>_128.png
    #   <id>_288.png
    #   <id>_1664.png
    # NPC chathead: /osrs-chathead/<id>.png
    # item sprite: /osrs-sprite/<id>.png
    # item DII:    /osrs-dii/<id>.png
    # object: /osrs-object/
    #   <id>_orient0.png
    #   <id>_orient1.png
    #   <id>_orient2.png
    #   <id>_orient3.png
    # TODO set URL type here, referring to above
    url_type = f'/osrs-dii/{file_id}.png'

    file_url = f'{base_url}/{url_type}'
    print(f'Downloading file {file_name} with ID {file_id} from URL {file_url}\n')
    try:
        download(file_url, file_name)
    except Exception as e:
        print(f'File {file_name} with ID {file_id} encountered an error while fetching from URL {file_url}:\n'
              f'{e}')
        continue