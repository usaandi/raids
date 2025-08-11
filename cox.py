from .base_raid import BaseRaid
from cox_loot import get_cox_loot_table
import random
import math

class Cox(BaseRaid):
    
    def __init__(self, cox_total_points, cox_people = 1):
        super().__init__(
            name = "Chambers of Xeric", 
            loot_table = get_cox_loot_table(), 
            purple_chance = None
            )
        self.cox_total_points = cox_total_points
        self.cox_people = cox_people
        self.purple_chance = self.calc_purple_chance()
        """
        Roll loot
        """
    def roll_loot(self, roll_amount):
        
        loot_obtained = {}
        total_value = 0
        purple_chance = self.purple_chance
        random_number = random.random()
        
        
        if random_number < purple_chance:
            uniques = self.loot_table['uniques']
            weights = self.normalize_loot_weights(uniques)
            
            purple_item = random.choices(
                list(uniques.keys()),
                weights = weights
                )[0]
            
            purple_price = uniques[purple_item]["price"]
            
            total_value = purple_price

            result = {
                "purple": (purple_item, purple_price), 
                "normal loot": loot_obtained,
                "total value": total_value,
            }
        else:
            normal_loot = self.loot_table['normal_loot']

            loot_items = list(normal_loot.keys())
            num_loot_items = min(2, len(loot_items))
            loot_randomed = random.sample(loot_items, num_loot_items)
            
            
            for item in loot_randomed:
                loot_item = normal_loot[item]

                cap_points = min(self.cox_total_points, 138111)
                quantity = math.ceil((cap_points / 138111) * loot_item['quantity']) if loot_item['quantity'] > 1 else 1
                total_price = 1 if loot_item.get("tradeable") else quantity * loot_item['price']
                
                loot_obtained[item] = {"quantity": quantity, "total_price": total_price}
                
                total_value += total_price
                    
            result = {
                "purple": None,
                "normal loot": loot_obtained,
                "total value": total_value,
            }
            
        self.update_summary(result)
        
        return result
    
      
    def calc_purple_chance(self):
        """
        Calculate purple chance
        """
        self.purple_chance = min(self.cox_total_points / 570000, 0.657)
        
        return self.purple_chance
    
