import nbtlib

class RFToolsTablet():
    
    def __init__(self, slot):
        self.tablet = slot

    def unstuff_rftools_tablet(self):
        for i in range(len(self.tablet["tag"]["Items"])):
            try:
                print(self.tablet["tag"]["Items"][i]["id"], f"I = {i}")
                # Do unstuff of RF tools tablet
            except KeyError:
                # empty slot
                continue
        return