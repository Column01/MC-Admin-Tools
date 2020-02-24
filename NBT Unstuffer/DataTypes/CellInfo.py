class CellInfo:
    def __init__(self):
        self.cell_info = {
            "appliedenergistics2:item.ItemBasicStorageCell.1k": {
                "byte_val": 8,
                "id": 0
            },
            "appliedenergistics2:item.ItemBasicStorageCell.4k": {
                "byte_val": 32, 
                "id": 1
            },
            "appliedenergistics2:item.ItemBasicStorageCell.16k": {
                "byte_val": 128, 
                "id": 2
            },
            "appliedenergistics2:item.ItemBasicStorageCell.64k": {
                "byte_val": 512, 
                "id": 3
            }
        }
        super().__init__()
    

    def set_cell_id(self, key, item_id):
        self.cell_info[key]["id"] = item_id


    def get_cell_info(self):
        return self.cell_info