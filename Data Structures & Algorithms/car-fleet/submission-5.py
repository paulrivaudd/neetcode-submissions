class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dernier_temps=0
        fleet=0
        cars = sorted(zip(position, speed))  
        for pos,vit in reversed(cars):
            time=(target-pos)/vit
            if not dernier_temps or time>dernier_temps:
                dernier_temps=time
                fleet+=1
            
        return fleet
