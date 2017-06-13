import unittest

def chop(target, array):
	return chopHelp(target, array, 0, len(array) - 1)

def chopHelp(target, array, min, max):
    i = int(min + ((max-min) / 2))
    if min > max:
        return -1
    else:
    	if target == array[i]:
        	return i
    	elif target < array[i]:
        	return chopHelp(target, array, min, i-1)
    	else:
        	return chopHelp(target, array, i + 1, max)

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

