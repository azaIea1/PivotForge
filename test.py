from stage import Stage1
from game_data import TFT_CHAMPIONS
from recommender import EarlyGameRecommender

# --- slam_for_winstreak: tank + dps case ---
slam_session = Stage1(starting_unit="Ornn")  # Ornn: magic tank
slam_session.round_input(orb_drop=["Ornn", "Ornn"])  # 3 total copies -> 2 star
slam_session.round_input(
    orb_drop=["Xayah", "Xayah", "Xayah"],  # 3 copies -> 2 star (attack marksman/dps)
    shop_offered=["Karma"],
    units_acquired=[]
)

recommender = EarlyGameRecommender(TFT_CHAMPIONS)
result = recommender.slam_for_winstreak(slam_session)

assert result["should_slam"] is True, f"expected True, got {result}"
assert "tank" in result["message"].lower() or "dps" in result["message"].lower(), f"unexpected message: {result['message']}"
print("slam_for_winstreak (tank + dps) test passed")

# --- slam_for_winstreak: 2 starred tanks case ---
tanks_session = Stage1(starting_unit="Ornn")
tanks_session.round_input(orb_drop=["Ornn", "Ornn"])  # Ornn to 2 star
tanks_session.round_input(
    orb_drop=["Leona", "Leona", "Leona"],  # Leona: magic tank, to 2 star
    shop_offered=["Karma"],
    units_acquired=[]
)

result = recommender.slam_for_winstreak(tanks_session)
assert result["should_slam"] is True, f"expected True, got {result}"
assert "2 starred tanks" in result["message"], f"unexpected message: {result['message']}"
print("slam_for_winstreak (2 tanks) test passed")

# --- slam_for_winstreak: board too weak (no 2-star units at all) ---
weak_session = Stage1(starting_unit="Ornn")
weak_session.round_input(orb_drop=["sword"])  # Ornn stays 1 star, no other units

result = recommender.slam_for_winstreak(weak_session)
assert result["should_slam"] is False, f"expected False, got {result}"
assert result["message"] == "Board too weak.", f"unexpected message: {result['message']}"
print("slam_for_winstreak (too weak) test passed")