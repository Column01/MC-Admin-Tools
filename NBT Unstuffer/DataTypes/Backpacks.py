class Backpacks:
    def __init__(self):
        self.backpacks = {
            "ExtraUtilities:golden_bag": {
                "id": 0
            },
            "rftools:storageModuleTabletItem": {
                "id": 1
            }
        }   
        super().__init__()
    

    def set_backpack_id(self, key, item_id):
        self.backpacks[key]["id"] = item_id


    def get_backpacks(self):
        return self.backpacks