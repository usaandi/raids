from .base_raid import BaseRaid
from tob_loot import get_tob_loot_table
import random


class Tob(BaseRaid):
    
    def __init__(self):
        super().__init__(
            name = "Theatre of Blood", 
            loot_table = get_tob_loot_table(), 
            purple_chance = 1 / 27
        )
        self.since_purple = 0
        
        
    def roll_loot(self, roll_nr):
        loot_obtained = {}
        total_value = 0
        
        random_roll = random.random()
        if random_roll < self.purple_chance:
            if self.since_purple > self.dry_streak:
                self.dry_streak = self.since_purple
                self.since_purple = 0
                
            uniques = self.loot_table['uniques']
            weights = self.normalize_loot_weights(uniques)
            
            purple_item = random.choices(
                list(uniques.keys()),
                weights = weights
                )[0]
            
            purple_price = uniques[purple_item]["price"]
            print(f"ROLLNR: {roll_nr}, PURPLE: {purple_item}")
            
        
            total_value = purple_price
        
            result = {
                "purple": (purple_item, purple_price), 
                "normal loot": loot_obtained,
                "total value": total_value,
            }
        else:
            self.since_purple += 1
            normal_loot = self.loot_table['normal_loot']
            weights = self.normalize_loot_weights(normal_loot)
            
            normal_drops = random.choices(
                list(normal_loot.keys()), 
                weights = weights, 
                k = 3)
            
            for item in normal_drops:
                loot_entry = normal_loot[item]
                if isinstance(loot_entry["quantity"], tuple):
                    quantity =random.randint(*loot_entry["quantity"])
                else:
                    quantity = loot_entry["quantity"]
                
                price_per_item = loot_entry["price"]
                total_price = quantity * price_per_item
                
                loot_obtained[item] = {"quantity": quantity, "total_price": total_price}
            
                total_value += total_price
                    
            result = {
            "purple": None,
            "normal loot": loot_obtained,
            "total value": total_value,
            }
        self.update_summary(result)
        
        return result
        
   