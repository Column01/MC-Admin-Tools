import nbtlib
import glob
from DataTypes.Backpacks import Backpacks
from DataTypes.CellInfo import CellInfo


def set_item_ids(ldat_files, b, c):
    # Loop over all .dat files
    for datfile in ldat_files:
        # If it starts with "level"
        if datfile.startswith("level", 0, 5):
            # Load it and set the drive item IDs
            level_dat = nbtlib.load(datfile)
            set_cell_ids(level_dat, c)
            set_backpack_ids(level_dat, b)


def collect_string_from_ids(arr):
    ret = []
    arr = arr.values()
    for item in arr:
        ret.append(str(item["id"]))
    return ret


# Calculates the drive usage of a drive
def get_drive_usage(item_id, item_count, info, c):
    cell_info = c.get_cell_info()
    for key in info.keys():
        value = info[key]["id"]
        if value == item_id:
            bytes_val = cell_info[key]["byte_val"]
            return item_count * bytes_val


# Sets the bag item IDs in the backpacks dictionary
def set_backpack_ids(ldat, b):
    backpacks = b.get_backpacks()
    for tag in ldat.root["FML"]["ItemData"]:
        for key in backpacks.keys():
            values = backpacks[key]
            if key == tag["K"]:
                b.set_backpack_id(key, tag["V"])


# Sets the drive item IDs in the cell_info dictionary
def set_cell_ids(ldat,c ):
    cell_info = c.get_cell_info()
    for tag in ldat.root["FML"]["ItemData"]:
        for key in cell_info.keys():
            values = cell_info[key]
            if key == tag["K"]:
                c.set_cell_id(key, tag["V"])


# Add an ME cell to
def add_slot(slots, slot, i, is_drive):
    cell_info = c.get_cell_info()
    if is_drive:
        drive_usage = get_drive_usage(slot["id"], slot["tag"]["it"], cell_info, c)
    else:
        drive_usage = 0
    slots[i] = {}
    slots[i]["path"] = "Inventory." + str(slot["Slot"])
    slots[i]["is_drive"] = is_drive
    slots[i]["usage"] = drive_usage


b = Backpacks()
c = CellInfo()
set_item_ids(glob.glob("level/*.dat"), b, c)
cell_info_temp = c.get_cell_info()
backpack_info_temp = b.get_backpacks()
drive_ids = ", ".join(collect_string_from_ids(cell_info_temp))
backpack_ids = ", ".join(collect_string_from_ids(backpack_info_temp))
print(f"Found the following IDs in the level.dat file: "
      f"\nDrive IDs: {drive_ids}"
      f"\nBackpack IDs: {backpack_ids}")

# For all the player data files found
for datfile2 in glob.glob("playerdata/*.dat"):
    player_dat = nbtlib.load(datfile2)
    slots = {}
    # Loop over all slots
    i = 0
    for slot in player_dat.root["Inventory"]:
        # Get each cell item ID and check if it equals the slot's item ID
        cell_info = c.get_cell_info()
        for key in cell_info.keys():
            id_val = cell_info[key]["id"]
            # If the slot's item id is an ME cell.
            if slot['id'] == int(id_val):
                # Get it's usage and append it to the slots list and the usages list
                add_slot(slots, slot, i, True)
                i += 1
        # Get each backpack item ID and check if it equals the slot's item ID
        backpacks = b.get_backpacks()
        for key2 in backpacks:
            value2 = backpacks[key2]["id"]
            if slot['id'] == int(value2):
                add_slot(slots, slot, i, False)
                i +=1
    lenslots = len(slots.keys())
    print(f"Found {lenslots} slots containing ME drives or backpacks in the file: {datfile2}")
