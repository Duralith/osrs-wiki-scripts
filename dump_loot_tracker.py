"""dump_loot_tracker.py
by Duralith, 2023.

Dumps LootTracker.db files from the OSRS mobile app into CSV format.
"""

import sqlite3
import pandas as pd

input_name = 'LootTracker-1.db'     # Location of the LootTracker.db file to dump
loot_output_name = 'loot.csv'       # File name for the loot table dump
source_output_name = 'source.csv'    # File name for the source table dump

dat = sqlite3.connect(input_name)
loot_query = dat.execute("SELECT * FROM loot")
loot_cols = [column[0] for column in loot_query.description]
loot_records = pd.DataFrame.from_records(data=loot_query.fetchall(), columns=loot_cols)

source_query = dat.execute("SELECT * FROM source")
source_cols = [column[0] for column in source_query.description]
source_records = pd.DataFrame.from_records(data=source_query.fetchall(), columns=source_cols)

loot_records.to_csv(loot_output_name, index=False)
source_records.to_csv(source_output_name, index=False)
