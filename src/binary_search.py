from typing import Optional

class BinarySearch():
    
    def search(self, nums: list[int], n:int) -> Optional[int]:
        """ Searchs an element n insede the array nums. 
        Array must be sorted in order to successfully find the number.

        Args:
            nums (list[int]): Sorted array where the search is going to be done.
            n (int): Element to find.

        Returns:
            Optional[int]: Pos or n inside the array
        """
        # Empty array
        if len(nums) == 0:
            return None
        # Last option
        if len(nums) == 1:
            return 0 if nums[0] == n else None
        # Filter
        pos: int = (len(nums) // 2) + 1
        return pos        