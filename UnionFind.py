class UnionFind:
    def __init__(self, size):
        self.size = size
        self.ids = [i for i in range(size)]
        self.sz = [1 for i in range(size)]
        self.numComponents = size

    def find(self, p):
        root = p

        while (root != self.ids[root]):
            root = self.ids[root]

        while (p != root):
            next = self.ids[p]
            self.ids[p] = root
            p = next

        return root

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def componentSize(self, p):
        return self.sz[self.find(p)]

    def size(self):
        return self.size

    def components(self):
        return self.numComponents

    def unify(self, p, q):

        # if connected, then do not need to unify!
        if self.connected(p, q):
            return

        pRoot = self.find(p)
        qRoot = self.find(q)

        # merge smaller component/set into the larger one
        if (self.sz[pRoot] < self.sz[qRoot]):
            self.sz[qRoot] += self.sz[pRoot]
            self.ids[pRoot] = qRoot
            self.sz[pRoot] = 0
        else:
            self.sz[pRoot] += self.sz[qRoot]
            self.ids[qRoot] = pRoot
            self.sz[qRoot] = 0

        self.numComponents -= 1

        
