import unittest
import math

def chop(target, array):
	i = len(array) // 2
	while i < len(array):
		if (i == 0 or i == len(array) - 1) and array[i] != target:
			return -1
		elif array[i] == target:
			return i
		elif target > array[i]:
			i = i + (len(array[i + 1:]) // 2) + 1
		elif target < array[i]:
			i = i - math.ceil(len(array[0: i]) / 2)
	return -1

class TestStringMethods(unittest.TestCase):
	def test_chop(self):
		self.assertEqual(-1, chop(3, []))
		self.assertEqual(-1, chop(3, [1]))
		self.assertEqual(0,  chop(1, [1]))
		#
		self.assertEqual(0,  chop(1, [1, 3, 5]))
		self.assertEqual(1,  chop(3, [1, 3, 5]))
		self.assertEqual(2,  chop(5, [1, 3, 5]))
		self.assertEqual(-1, chop(0, [1, 3, 5]))
		self.assertEqual(-1, chop(2, [1, 3, 5]))
		self.assertEqual(-1, chop(4, [1, 3, 5]))
		self.assertEqual(-1, chop(6, [1, 3, 5]))
		#
		self.assertEqual(0,  chop(1, [1, 3, 5, 7]))
		self.assertEqual(1,  chop(3, [1, 3, 5, 7]))
		self.assertEqual(2,  chop(5, [1, 3, 5, 7]))
		self.assertEqual(3,  chop(7, [1, 3, 5, 7]))
		self.assertEqual(-1, chop(0, [1, 3, 5, 7]))
		self.assertEqual(-1, chop(2, [1, 3, 5, 7]))
		self.assertEqual(-1, chop(4, [1, 3, 5, 7]))
		self.assertEqual(-1, chop(6, [1, 3, 5, 7]))
		self.assertEqual(-1, chop(8, [1, 3, 5, 7]))

if __name__ == '__main__':
    unittest.main()
    
