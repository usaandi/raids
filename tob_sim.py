import random
from tob_loot import get_tob_loot_table

loot_table = get_tob_loot_table()

tob_uniques = loot_table['uniques']
tob_normal = loot_table['normal_loot']

# ToB Loot Rates fix prices to be dynamic
# tob_unqiues = {
#   "Scythe of vitur (uncharged)": {
#         "quantity": 1,
#         "price": prices.get("Scythe of vitur (uncharged)"),
#         "rate": 1/19
#     },
#     "Sanguinesti staff (uncharged)": {
#         "quantity": 1,
#         "price": 65_000_000,
#         "rate": 2/19
#     },
#     "Ghrazi rapier": {
#         "quantity": 1,
#         "price": 34_000_000,
#         "rate": 2/19
#     },
#     "Avernic defender hilt": {
#         "quantity": 1,
#         "price": 40_000_000,
#         "rate": 8/19
#     },
#     "Justiciar faceguard": {
#         "quantity": 1,
#         "price": 12_000_000,
#         "rate": 2/19
#     },
#      "Justiciar chestguard": {
#         "quantity": 1,
#         "price": 13_000_000,
#         "rate": 2/19
#     },
#      "Justiciar legguards": {
#         "quantity": 1,
#         "price": 12_000_000,
#         "rate": 2/19
#     },
# }

# normal_loot = {
#     "Vial of blood": {
#         "quantity": random.randint(45, 60),
#         "price": 14_300,
#         "rate": 1/15  # Special rate
#     },
#     "Death rune": {
#         "quantity": random.randint(500, 600),
#         "price": 170,
#         "rate": 1/30
#     },
#     "Blood rune": {
#         "quantity": random.randint(500, 600),
#         "price": 299,
#         "rate": 1/30
#     },
#     "Swamp tar": {
#         "quantity": random.randint(500, 600),
#         "price": 3,
#         "rate": 1/30
#     },
#     "Coal": {
#         "quantity": random.randint(500, 600),
#         "price": 167,
#         "rate": 1/30
#     },
#     "Gold ore": {
#         "quantity": random.randint(300, 360),
#         "price": 154,
#         "rate": 1/30
#     },
#     "Molten glass": {
#         "quantity": random.randint(200, 240),
#         "price": 94,
#         "rate": 1/30
#     },
#     "Adamantite ore": {
#         "quantity": random.randint(130, 156),
#         "price": 995,
#         "rate": 1/30
#     },
#     "Runite ore": {
#         "quantity": random.randint(60, 72),
#         "price": 10_941,
#         "rate": 1/30
#     },
#     "Wine of zamorak": {
#         "quantity": random.randint(50, 60),
#         "price": 950,
#         "rate": 1/30
#     },
#     "Potato cactus": {
#         "quantity": random.randint(50, 60),
#         "price": 53,
#         "rate": 1/30
#     },
#     "Grimy cadantine": {
#         "quantity": random.randint(50, 60),
#         "price": 3_190,
#         "rate": 1/30
#     },
#     "Grimy avantoe": {
#         "quantity": random.randint(40, 48),
#         "price": 2_496,
#         "rate": 1/30
#     },
#     "Grimy toadflax": {
#         "quantity": random.randint(37, 44),
#         "price": 2_865,
#         "rate": 1/30
#     },
#     "Grimy ranarr weed": {
#         "quantity": random.randint(30, 36),
#         "price": 5_873,
#         "rate": 1/30
#     },
#     "Grimy kwuarm": {
#         "quantity": random.randint(36, 43),
#         "price": 2_987,
#         "rate": 1/30
#     },  
#     "Grimy irit leaf": {
#         "quantity": random.randint(34, 40),
#         "price": 1_175,
#         "rate": 1/30
#     },
#     "Grimy snapdragon": {
#         "quantity": random.randint(27, 32),
#         "price": 7_917,
#         "rate": 1/30
#     },
#     "Grimy lantadyme": {
#         "quantity": random.randint(26, 31),
#         "price": 1_701,
#         "rate": 1/30
#     },
#     "Grimy dwarf weed": {
#         "quantity": random.randint(24, 28),
#         "price": 1_885,
#         "rate": 1/30
#     },
#     "Grimy torstol": {
#         "quantity": random.randint(20, 24),
#         "price": 3_445,
#         "rate": 1/30
#     },
#     "Battlestaff": {
#         "quantity": random.randint(15, 18),
#         "price": 8_178,
#         "rate": 1/30
#     },
#     "Rune battleaxe": {
#         "quantity": 4,
#         "price": 24_227,
#         "rate": 1/30
#     },
#     "Rune platebody": {
#         "quantity": 4,
#         "price": 38_378,
#         "rate": 1/30
#     },
#     "Rune chainbody": {
#         "quantity": 4,
#         "price": 29_410,
#         "rate": 1/30
#     },
#     "Palm tree seed": {
#         "quantity": 3,
#         "price": 17_842,
#         "rate": 1/30
#     },
#     "Yew seed": {
#         "quantity": 3,
#         "price": 27_846,
#         "rate": 1/30
#     },
#     "Magic seed": {
#         "quantity": 3,
#         "price": 105_649,
#         "rate": 1/30
#     },
#     "Mahogany seed": {
#         "quantity": random.randint(10, 12),
#         "price": 803,
#         "rate": 1/30
#     }
# }

def roll_tob(team_size, deaths):

    #teamscore and deaths, weights
    base_team_score = 32 + (team_size - 1) * 18
    final_team_score = max(0, base_team_score - (deaths * 4))
    loot_multiplier = final_team_score / base_team_score if base_team_score > 0 else 0
    
    purple_chance = (1/9.1) * loot_multiplier
    unique_weights = [item["rate"] for item in tob_uniques.values()]
    total_unique_weight = sum(unique_weights)

    #purples
    if random.random() < purple_chance:
        weights = [w / total_unique_weight for w in unique_weights]
        purple_item = random.choices(
            list(tob_uniques.keys()),
            weights
            )[0]
        purple_price = tob_uniques[purple_item]["price"]
        return {"purple": (purple_item, purple_price), "normal loot": {}, "total value": purple_price}
    

    normal_drops = random.sample(list(tob_normal.keys()), 3)
    loot_obtained = {}
    total_value = 0

    for item in normal_drops:
        quantity = tob_normal[item]["quantity"]
        price_per_item = tob_normal[item]["price"]

        #scale loot
        adjusted_qty = max(1, int(quantity * loot_multiplier))
        total_price = adjusted_qty * price_per_item

        loot_obtained[item] = (quantity, total_price)
        total_value += total_price
    
    return {"purple": None, "normal loot": loot_obtained, "total value": total_value}

def simulate_tob_chests(n, team_size, deaths):
    """
    Simulates 'n' number of ToB chests and tracks total loot.
    """
    total_purples = 0
    total_normal_loot = {}
    total_gp_value = 0
    purple_drops = {}

    for _ in range(n):
        chest = roll_tob(team_size, deaths)
        total_gp_value += chest["total value"]

        if chest["purple"]:
            total_purples += 1
            item, value = chest["purple"]
            purple_drops[item] = purple_drops.get(item, 0) + 1
        elif chest["normal loot"]:
            for item, (qty, value) in chest["normal loot"].items():
                if item in total_normal_loot:
                    total_normal_loot[item][0] += qty
                    total_normal_loot[item][1] += value
                else:
                    total_normal_loot[item] = [qty, value]

    # Print summary
    print(f"📦 Simulated {n} ToB Chests")
    print(f"🎭 Total Purple Drops: {total_purples} ({(total_purples / n) * 100:.2f}%)")
    print(f"💰 Total Value: {total_gp_value:,} gp")
    print("\n🔮 Purple Drop Breakdown:")
    for item, count in purple_drops.items():
        print(f"   {item}: {count} times. price:")

    print("\n📜 Normal Loot Breakdown (Sorted by Value):")
    sorted_loot = sorted(total_normal_loot.items(), key=lambda x: x[1][1], reverse=True)  # Sort by total GP value
    for item, (qty, value) in sorted_loot:
        print(f"   {item}: {qty} units = {value:,} gp")
        
#user inputs
n = int(input("Enter the number of tob completions to simulate: "))
team_size = int(input("Enter team size (1-5 players): "))
deaths = int(input("Enter number of total deaths: "))

simulate_tob_chests(n, team_size, deaths)
