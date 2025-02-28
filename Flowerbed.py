You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Add empty plots at the start and at the end of the flowerbed to simplify edge case handling
        flowerbed = [0] + flowerbed + [0]
      
        # Iterate over each plot in the flowerbed starting from the first actual plot to the last
        for i in range(1, len(flowerbed) - 1):
            # Check if the current plot and its adjacent plots are empty
            if sum(flowerbed[i - 1: i + 2]) == 0:
                # Plant a flower in the current plot
                flowerbed[i] = 1
                # Decrement the count of flowers we need to plant
                n -= 1
                # If we have planted all required flowers, we can end early
                if n == 0:
                    return True
      
        # After checking all plots, decide if we were able to plant all flowers
        return n <= 0
