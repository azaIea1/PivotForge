class Stage1:
    def __init__(self) -> None:
        self.gold = 0
        self.units = []
        self.shop_rolls = []
        self.comp = []
        self.level = 0 

    def stage1_2_input(self, orb_drop: list) -> None:
        self.level += 1
        item_pool = ['sword', 'glove', 'cloak', 'rod', 'tear', 'belt', 'bow', 'vest', 'dupe']
        unit_pool = []
        for drop in orb_drop:
            if drop in item_pool:
                self.comp.append(drop)
            elif drop is type(int):
                self.gold += drop
            elif drop in unit_pool:
                self.units.append(drop)
            else:
                raise ValueError("Not correct drops")
            
    def stage1_3_input(self, orb_drop: list, shop_units: list) -> None:
        self.level += 1
        item_pool = ['sword', 'glove', 'cloak', 'rod', 'tear', 'belt', 'bow', 'vest', 'dupe']
        unit_pool = []
        
    
        for drop in orb_drop:
            if drop in item_pool:
                self.comp.append(drop)
            elif drop is type(int):
                self.gold += drop
            elif drop in unit_pool:
                self.units.append(drop)
            else:
                raise ValueError("Not correct drops")
        for units in shop_units:
            self.shop_rolls.append(units)
        
    def stage1_4_input(self, orb_drop, shop_units) -> None:
        self.level += 1
        item_pool = ['sword', 'glove', 'cloak', 'rod', 'tear', 'belt', 'bow', 'vest', 'dupe']
        unit_pool = []
        for drop in orb_drop:
            if drop in item_pool:
                self.comp.append(drop)
            elif drop is isinstance(int):
                self.gold += drop
            elif drop in unit_pool:
                self.units.append(drop)
            else:
                raise ValueError("Not correct drops")

        for units in shop_units:
            self.shop_rolls.append(units)