class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times=[]
        fleet=0
        cars = sorted(zip(position, speed))  
        for pos,vit in reversed(cars):
            time=(target-pos)/vit
            if not times or time>times[-1]:
                times.append(time)
                fleet+=1
            
        return fleet
