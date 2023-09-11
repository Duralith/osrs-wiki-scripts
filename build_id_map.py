import os
import json

cache_name = '2023-08-30-rev216'
cache_path = f'D:\\OSRS Cache\\dump-{cache_name}\\dump'
output_name = f'id_mapping_{cache_name}.json'

item_defs = set(os.listdir(f'{cache_path}\\item_defs'))
object_defs = set(os.listdir(f'{cache_path}\\object_defs'))
npc_defs = set(os.listdir(f'{cache_path}\\npc_defs'))

items = dict()
objects = dict()
npcs = dict()

print(f'Parsing {len(item_defs)} item definitions.')

for _ in item_defs:
    with open(f'{cache_path}\\item_defs\\{_}') as f:
        jdata = json.load(f)
    items[jdata["id"]] = jdata["name"]

print(f'Parsing {len(object_defs)} object definitions.')

for _ in object_defs:
    with open(f'{cache_path}\\object_defs\\{_}') as f:
        jdata = json.load(f)
    objects[jdata["id"]] = jdata["name"]

print(f'Parsing {len(npc_defs)} NPC definitions.')

for _ in npc_defs:
    with open(f'{cache_path}\\npc_defs\\{_}') as f:
        jdata = json.load(f)
    npcs[jdata["id"]] = jdata["name"]

mapping = {
        "cache_version": cache_name,
        "items": items,
        "objects": objects,
        "npcs": npcs
    }

with open(output_name, 'w') as outfile:
    json.dump(mapping, outfile)
