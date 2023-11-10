#gauranteed to get half odd, have even integers
#return order does not matter, as long as it satisfies criteria
#based on example, it appears we want to do it with odd, even order  

#basically what we want to do is
#set two pointers -> run until r has gone across the full array
    #run the first one until it hits an out of place number
    #run the second one until it finds an out of place complement
    #swap them
#increment them both by one
#repeat


#brute force
#filter the odds
#filter the evens

#zipper merge them

#return the merged array
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odds = [num for num in nums if num % 2 == 1]
        evens = [num for num in nums if num % 2 == 0]

        out = []
        i = 0

        while odds or evens:
            if i % 2 == 0:
                out.append(evens.pop())
            if i % 2 == 1:
                out.append(odds.pop())
            i += 1

        return out