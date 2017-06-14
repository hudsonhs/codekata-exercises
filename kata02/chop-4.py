import unittest
import math

def chop(target, array):
    return chopHelp(target, zipWithIndexes(array))


def chopHelp(target, array):
    if not array:
        return -1
    else:
        mid = len(array) // 2
        if target == array[mid][0]:
            return array[mid][1]
        elif target < array[mid][0]:
            return chopHelp(target, array[0: mid])
        elif target > array[mid][0]:
            return chopHelp(target, array[mid + 1:])

def zipWithIndexes(array):
	i = 0
	returnArray = []
	while i < len(array):
		returnArray.append((array[i], i))
		i += 1
	return returnArray

class TestStringMethods(unittest.TestCase):

	def test_chop_one(self):
		self.assertEqual(-1, chop(3, []))
		self.assertEqual(-1, chop(3, [1]))
		self.assertEqual(0,  chop(1, [1]))

	def test_chop_three(self):
		self.assertEqual(0,  chop(1, [1, 3, 5]))
		self.assertEqual(1,  chop(3, [1, 3, 5]))
		self.assertEqual(2,  chop(5, [1, 3, 5]))
		self.assertEqual(-1, chop(0, [1, 3, 5]))
		self.assertEqual(-1, chop(2, [1, 3, 5]))
		self.assertEqual(-1, chop(4, [1, 3, 5]))
		self.assertEqual(-1, chop(6, [1, 3, 5]))

	def test_chop_four(self):
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

