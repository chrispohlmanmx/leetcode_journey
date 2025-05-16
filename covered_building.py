def countCoveredBuildings(n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        #n is the max value a building can be located to the right or above a building
        #so if a building has an x or y value == to n then it can't be covered
        
        #My solution works but is too slow
        #solutions I'm seeing online involve precomputing some values and comparing to those
        """
        step0: if len(buildings) is less than 5 return 0
        step1: for each building determine if it has the potential to be covered
        step2: if it does check rest of buildings to see if 1 is above, below, right, and left
        step3: if yes then increment count by 1
        step4: move to the next potential building and repeat 2 and 3
        """
        
        covered_count = 0
        potential_buildings = []
        if len(buildings) < 5:
            return covered_count
        
        for building in buildings:
            if building[0] != n and building[1] != n:
                potential_buildings.append(building)
        print(f'potential_building list = {potential_buildings}') 
        covered_buildings = []
        for potential_building in potential_buildings:
            above = 0
            below = 0
            right = 0
            left = 0
            pot_y, pot_x = potential_building[1], potential_building[0]
            for building in buildings:
                 
                #print(f'current potential building {potential_building}')
                #print(f'current building being checked {building}')
                building_y, building_x = building[1], building[0]
                #above
                if building_y < pot_y and building_x == pot_x:
                    above += 1
                #below
                elif building_y > pot_y and building_x == pot_x:
                    below += 1
                #right
                elif building_y == pot_y and building_x > pot_x:
                    right += 1
                #left
                elif building_y == pot_y and building_x < pot_x:
                    left += 1
            
            if right > 0 and left > 0 and above > 0 and below > 0:
                covered_count += 1
                print(f'currently on potential_building {potential_building} and building being checked {building} and adding building to covered list')
                covered_buildings.append(potential_building) 
        print(f"covered building list = {covered_buildings}")
        return covered_count


def main():
    test_data = [[1,2],[2,1],[3,1],[1,1],[2,3],[3,3],[2,2],[3,2],[1,3]]
    test_n = 3

    result = countCoveredBuildings(test_n, test_data)
    print(result)

if __name__ == "__main__":
    main()
