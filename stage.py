from game_data import TFT_CHAMPIONS, ITEM_POOl
from collections import Counter

class Stage1:
    def __init__(self, starting_unit: str) -> None:
        if starting_unit not in TFT_CHAMPIONS:
            raise ValueError("Has to be a unit in the set")
        self.units = [starting_unit]
        self.gold = 0
        self.comp = []
        self.shop_champ_seen = {}
        self.current_stage = 1  

    def round_input(self, orb_drop: list, shop_offered: list = None, units_acquired: list = None) -> None:
        self._process_orb_drop(orb_drop)

        if self.current_stage > 1:
            if shop_offered is None or units_acquired is None:
                raise ValueError("Shop data required for this round")

            self.shop_champ_seen[self.current_stage] = shop_offered

            for unit in units_acquired:
                self.units.append(unit)

        self.current_stage += 1

    def _process_orb_drop(self, orb_drop: list) -> None:
        for drop in orb_drop:
            if drop in ITEM_POOl:
                self.comp.append(drop)
            elif isinstance(drop, int):
                self.gold += drop
            elif drop in TFT_CHAMPIONS:
                self.units.append(drop)
            else:
                raise ValueError("Not correct drops")

    def get_star_level(self) -> dict[str, int]:
        res = {}
        counts = Counter(self.units)
        for unit in counts:
            if counts[unit] >= 9:
                res[unit] = 3
            elif counts[unit] >= 3:
                res[unit] = 2
            else:
                res[unit] = 1
        return res

    