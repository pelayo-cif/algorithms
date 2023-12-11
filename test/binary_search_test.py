import unittest
import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parents[1]))

from src.binary_search import BinarySearch

from typing import List

class TestBinarySearch(unittest.TestCase):

    def test_empty(self):
        """Test binary search on empty array 
        """
        binary_search: BinarySearch = BinarySearch()
        self.assertIsNone(binary_search.search(nums = [],n = 1))
    
    def test_length_one_success(self):
        """Test binary search on lenght 1 array, success case
        """
        binary_search: BinarySearch = BinarySearch()
        self.assertEquals(binary_search.search(nums = [1],n = 1),0)
        
    def test_length_one_fail(self):
        """Test binary search on lenght 1 array, fail case
        """
        binary_search: BinarySearch = BinarySearch()
        self.assertIsNone(binary_search.search(nums = [2],n = 1))
        
    def test_length_three_success(self):
        """Test binary search on lenght 3 array, success case
        """
        binary_search: BinarySearch = BinarySearch()
        nums: List[int] = [0,1,2]
        for num in nums:
            self.assertEquals(binary_search.search(nums = nums,n = num),num)
        
    def test_length_three_fail(self):
        """Test binary search on lenght 3 array, fail case
        """
        binary_search: BinarySearch = BinarySearch()
        self.assertIsNone(binary_search.search(nums = [0,1,2],n = 10))
        
    def test_length_ten_success(self):
        """Test binary search on lenght 10 array, success case
        """
        binary_search: BinarySearch = BinarySearch()
        nums: List[int] = [0,1,2,3,4,5,6,7,8,9]
        for num in nums:
            self.assertEquals(binary_search.search(nums = nums,n = num),num)
        
    def test_length_ten_fail(self):
        """Test binary search on lenght 10 array, fail case
        """
        binary_search: BinarySearch = BinarySearch()
        self.assertIsNone(binary_search.search(nums = [0,1,2,3,4,5,6,7,8,9],n = 10))

if __name__ == '__main__':
    unittest.main()