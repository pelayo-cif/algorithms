from typing import Optional

class BinarySearch():
    
    def search(self, nums: list[int], n:int) -> int | None:
        """ Searchs an element n insede the array nums. 
        Array must be sorted in order to successfully find the number.

        Args:
            nums (list[int]): Sorted array where the search is going to be done.
            n (int): Element to find.

        Returns:
            int | None: Pos of n inside the array or None if not found
        """
        # Empty array
        if len(nums) == 0:
            return None
        # Last option
        if len(nums) == 1:
            return 0 if nums[0] == n else None
        # Get element in the middle
        pos: int = len(nums) // 2
        # Evaluate next call
        if nums[pos] == n:
            return pos
        elif n < nums[pos]:
            return self.search(nums[0:pos],n)
        else:
            res: int | None = self.search(nums[pos:len(nums)],n)
            return res + len(nums[0:pos]) if res is not None else None 
    
    
binary_search = BinarySearch()
res = binary_search.search(nums = [0,1,2,3,4,5,6,7,8,9,10],n = 20)
print(res)