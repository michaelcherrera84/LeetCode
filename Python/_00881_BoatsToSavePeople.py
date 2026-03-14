from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """You are given an array `people` where `people[i]` is the weight of 
        the `ith` person, and an **infinite number of boats** where each boat 
        can carry a maximum weight of `limit`. Each boat carries at most two 
        people at the same time, provided the sum of the weight of those people 
        is at most `limit`.

        Return *the minimum number of boats to carry every given person*.

        Args:
            people (List[int]): list of peoples' weights
            limit (int): weight limit for the boats

        Returns:
            int: fewest possible recue trips
        """

        # Sort people from smallest to largest to see if the largest person
        # has a smaller person he can possibly travel with.
        people.sort()

        smallest = 0
        largest = len(people) - 1
        trips = 0

        # While someone has not been resued...
        while smallest <= largest:
            # If the smallest person and the largest person are at or below the
            # weight limit, they can travel together.
            if people[smallest] + people[largest] <= limit:
                smallest += 1
            
            # Otherwise, the largest person must travel alone.
            largest -= 1
            trips += 1

        return trips