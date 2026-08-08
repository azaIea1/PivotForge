from stage import Stage1
from game_data import TFT_CHAMPIONS, ITEM_POOl

#Happy path: construct with a valid starting unit
stage = Stage1(starting_unit="Ornn")
assert stage.units == ["Ornn"], f"expected ['Ornn'], got {stage.units}"
assert stage.gold == 0, f"expected 0, got {stage.gold}"
assert stage.comp == [], f"expected [], got {stage.comp}"
assert stage.current_stage == 1, f"expected 1, got {stage.current_stage}"
print("Constructor test passed")

#Stage 1-2: no shop, just orb drop (items + gold, no champions this time)
stage.round_input(orb_drop=["sword", "rod", 3])
assert stage.comp == ["sword", "rod"], f"expected ['sword', 'rod'], got {stage.comp}"
assert stage.gold == 3, f"expected 3, got {stage.gold}"
assert stage.units == ["Ornn"], f"units shouldn't change on no-shop round, got {stage.units}"
assert stage.current_stage == 2, f"expected 2, got {stage.current_stage}"
print("Stage 1-2 (no shop) test passed")

#Stage 1-3: orb drop + shop
stage.round_input(
    orb_drop=["belt"],
    shop_offered=["Ahri", "Karma", "Veigar", "Rakan", "Camille"],
    units_acquired=["Karma"]
)
assert stage.comp == ["sword", "rod", "belt"], f"got {stage.comp}"
assert stage.units == ["Ornn", "Karma"], f"got {stage.units}"
assert stage.shop_champ_seen == {2: ["Ahri", "Karma", "Veigar", "Rakan", "Camille"]}, f"got {stage.shop_champ_seen}"
assert stage.current_stage == 3, f"expected 3, got {stage.current_stage}"
print("Stage 1-3 (shop) test passed")

#Stage 1-4: orb drop + shop, another purchase
stage.round_input(
    orb_drop=["tear", 2],
    shop_offered=["Leona", "Yorick", "Ornn", "Xayah", "Rek'Sai"],
    units_acquired=["Xayah", "Yorick"]
)
assert stage.gold == 5, f"expected 5, got {stage.gold}"
assert stage.units == ["Ornn", "Karma", "Xayah", "Yorick"], f"got {stage.units}"
assert 3 in stage.shop_champ_seen, f"missing stage 3 key, got {stage.shop_champ_seen.keys()}"
assert stage.current_stage == 4, f"expected 4, got {stage.current_stage}"
print("Stage 1-4 (shop) test passed")

#Error case: invalid starting unit
try:
    Stage1(starting_unit="NotARealChamp")
    assert False, "expected ValueError for invalid starting unit"
except ValueError as e:
    print(f"Correctly raised on invalid starting unit: {e}")

#Error case: invalid orb drop content
stage2 = Stage1(starting_unit="Leona")
try:
    stage2.round_input(orb_drop=["not_a_real_item_or_champ"])
    assert False, "expected ValueError for invalid drop"
except ValueError as e:
    print(f"Correctly raised on invalid drop: {e}")

#Error case: shop round missing shop data
try:
    stage2.round_input(orb_drop=["sword"])  #current_stage is now 2, needs shop data
    assert False, "expected ValueError for missing shop data on shop round"
except ValueError as e:
    print(f"Correctly raised on missing shop data: {e}")

print("\nAll tests passed!")


stage3 = Stage1(starting_unit="Leona")
stage3.round_input(orb_drop=["sword"])  # valid no-shop round, current_stage goes 1 -> 2

try:
    stage3.round_input(orb_drop=["belt"])  # now current_stage is 2, should require shop data
    assert False, "expected ValueError for missing shop data on shop round"
except ValueError as e:
    print(f"Correctly raised on missing shop data: {e}")