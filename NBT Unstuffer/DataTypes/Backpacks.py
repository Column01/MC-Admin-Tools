class Backpacks:
    def __init__(self):
        self.backpacks = {
            "ExtraUtilities:golden_bag": {
                "id": 0,
                "name": "eugoldenbag"
            },
            "rftools:storageModuleTabletItem": {
                "id": 1,
                "name": "rftoolstablet"
            }
        }   
    

    def set_backpack_id(self, key, item_id):
        self.backpacks[key]["id"] = item_id


    def get_backpacks(self):
        return self.backpacks