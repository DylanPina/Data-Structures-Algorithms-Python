from sortedcontainers import SortedSet  # for better time complexity
from typing import List
from collections import defaultdict


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisineMap = defaultdict(SortedSet)
        self.foodMap = defaultdict(list)
        for x, y, z in zip(foods, cuisines, ratings):
            self.cuisineMap[y].add((-z, x))
            self.foodMap[x].append((y, z))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.foodMap[food][0]
        self.cuisineMap[cuisine].remove((-rating, food))
        self.cuisineMap[cuisine].add((-newRating, food))
        self.foodMap[food][0] = (cuisine, newRating)

    def highestRated(self, cuisine: str) -> str:
        return self.cuisineMap[cuisine][0][1]
