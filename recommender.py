from game_data import TFT_CHAMPIONS
from stage import Stage1
from comp_db import get_all_comps

class EarlyGameRecommender:
    def __init__(self, champion_data: dict[str, dict]) -> None:
        self.champion_data = champion_data

    def slam_for_winstreak(self, session: Stage1) -> dict:
        unit_star_levels = session.get_star_level()
        tanks = 0
        dps = 0

        for unit, star_level in unit_star_levels.items():
            if star_level < 2:
                continue

            role = self.champion_data[unit]["role"]

            if "tank" in role:
                tanks += 1
            else:
                dps += 1

        if tanks >= 2:
            return {
                "should_slam": True,
                "message": "Since you have 2 starred tanks, consider slamming."
            }

        elif tanks >= 1 and dps >= 1:
            return {
                "should_slam": True,
                "message": "Since you have a starred tank and DPS, consider slamming."
            }

        else:
            return {
                "should_slam": False,
                "message": "Board too weak."
            }
        
    def get_available_comps(self):
        return get_all_comps()

    def recommend_comps(self, session: Stage1):
        comps = self.get_available_comps()

        results = []

        play_style = session 

        



    
if __name__ == "__main__":
    recommender = EarlyGameRecommender(TFT_CHAMPIONS)
    print(recommender.get_available_comps())