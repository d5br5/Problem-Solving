class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        high = max(candies)
        def mapFn(elem):
            return elem + extraCandies >= high
        return map(mapFn, candies)
            