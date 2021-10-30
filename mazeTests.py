from unittest.loader import defaultTestLoader
from UnionFind import UnionFind
from MinHeap import MinHeap
import unittest
unittest.sortTestMethodsUsing = None

class TestUnionFind(unittest.TestCase):
    union_test_one = UnionFind(10)
    def testSize(self):
        self.assertEqual(self.union_test_one.size, 10, "Should be 10")
    def testIds(self):
        self.assertEqual(self.union_test_one.ids, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "Should be {}".format([i for i in range(10)]))
    def testSize(self):
        self.assertEqual(self.union_test_one.sz, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], "Should be {}".format([1 for i in range(10)]))
    def testNumComponents(self):
        self.assertEqual(self.union_test_one.numComponents, 10, "Should be 10")
    def testFindNoChange(self):
        self.assertEqual(self.union_test_one.find(0), 0, "Should be 0")
    def testUnify(self):
        self.union_test_one.unify(0, 1)
        self.assertEqual(self.union_test_one.ids, [0, 0, 2, 3, 4, 5, 6, 7, 8, 9], "Should be [[0, 0, 2, 3, 4, 5, 6, 7, 8, 9]]")
    def testSizeAfterUnify(self):
        self.union_test_one.unify(0, 1)
        self.assertEqual(self.union_test_one.sz[0], 2, "Should be 2")

if __name__ == '__main__':
    unittest.main()