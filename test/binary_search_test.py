import unittest
import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parents[1]))

from src.binary_search import BinarySearch


class TestBinarySearch(unittest.TestCase):

    def test_empty(self):
        """Test binary search on empty array 
        """
        binary_search = BinarySearch()
        self.assertIsNone(binary_search.search(nums = [],n = 1))
    
    def test_length_one_success(self):
        """Test binary search on lenght 1 array, success case
        """
        binary_search = BinarySearch()
        self.assertEquals(binary_search.search(nums = [1],n = 1),0)
        
    def test_length_one_fail(self):
        """Test binary search on lenght 1 array, fail case
        """
        binary_search = BinarySearch()
        self.assertIsNone(binary_search.search(nums = [2],n = 1))


if __name__ == '__main__':
    unittest.main()