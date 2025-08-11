from abc import ABC, abstractmethod

class BaseRaid(ABC):
    def __init__(self, name, loot_table, purple_chance):
        self.name = name
        self.loot_table = loot_table
        self.purple_chance = purple_chance
        
        # Tracking loot
        self.dry_streak = 0
        self.total_loot = {}
        self.total_purples = 0
        self.total_normal_loot = {}
        self.total_gp_value = 0
        self.purple_drops = {}
        self.num_rolls = 0
        
    @abstractmethod
    def roll_loot(self):
        """Method to simulate loot drops, implemented in child classes"""
        pass
    
    def roll_multiple_times(self, num_rolls):
        """Simulate multiple loot rolls"""
        self.num_rolls = num_rolls
        return [self.roll_loot(_) for _ in range(num_rolls)]
    
    def normalize_loot_weights(self, loot_dict):
        """
        Normalizes loot drop rates to sum to 1.
        :param loot_dict: Dictionary with item names as keys and {"rate": X} as values.
        :return: List of normalized weights.
        """
        total_weight = sum([item["rate"] for item in loot_dict.values()])
        return [(item["rate"] / total_weight) for item in loot_dict.values()] if total_weight > 0 else []
    
    def get_loot_summary(self):
        return {
            "Raid": self.name,
            "Total purples": self.total_purples,
            "Total normal loot": self.total_normal_loot,
            "Total GP value": self.total_gp_value,
            "Purple drops": self.purple_drops
        }
        
    def update_summary(self, roll_result):
        if roll_result["purple"]:
            purple_item, purple_price = roll_result["purple"]
            self.total_purples += 1
            self.purple_drops[purple_item] = self.purple_drops.get(purple_item, 0) + 1
        
        for item, loot_entry in roll_result["normal loot"].items():
            
            self.total_normal_loot[item] = self.total_normal_loot.get(item, 0 ) + loot_entry['quantity']
            
        self.total_gp_value += roll_result["total value"]
        
    def print_summary(self):
        total_purple_value = 0
        total_normal_loot_value = 0
        print(f"Rolled {self.num_rolls} times")
        print("\n📜 **LOOT SUMMARY** 📜\n")
        sorted_normal_loot = sorted(
            self.total_normal_loot.items(),
            key=lambda item: self.loot_table['normal_loot'][item[0]]['price'] * item[1],
            reverse = True
        )

        
        for item, quantity in sorted_normal_loot:
            price = self.loot_table['normal_loot'][item]['price']
            total_price = quantity * price
            total_normal_loot_value += total_price
            print(f"- {item}: {quantity}x ({total_price:,} gp)")

        print("\n🎭 **Total Purple Drops:**")
        
        sorted_unqiues_loot = sorted(
            self.purple_drops.items(),
            key =lambda item: self.loot_table['uniques'][item[0]]['price'] * item[1],
            reverse = True
        )
        for item, count in sorted_unqiues_loot:
    
            price = self.loot_table['uniques'][item]['price']
            total_price = count * price
            total_purple_value += total_price
            print(f"- {item}: {count}x ({total_price:,} gp)")
        #print(f"🎭 Total Purple Drops: {self.total_purples} ({(self.total_purples / self.num_rolls) * 100:.2f}%)")
        print(f"\n💎 **Total Purples:** {self.total_purples}")
        print(f"\n💎 **Biggest Purples dry streak:** {self.dry_streak}")
        print(f"💰 **Total Purple Loot Value:** {total_purple_value:,} gp")
        print(f"\n💰 **Total Normal Loot Value:** {total_normal_loot_value:,} gp") 
        print(f"💰 **Total GP Value:** {total_normal_loot_value + total_purple_value:,} gp\n")
            