from sys import stdin

class Tree:
    def __init__(self, nodes):
        n, m = nodes.pop(), nodes.pop()
        self.nodes = []
        self.metadata = []
        for i in range(n):
            self.nodes.append(Tree(nodes))
        for i in range(m):
            self.metadata.append(nodes.pop())

    def value(self):
        if not self.nodes:
            return sum(self.metadata)
        value = 0
        for x in self.metadata:
            if x <= len(self.nodes):
                value += self.nodes[x - 1].value()
        return value

nodes = list(map(int, stdin.readline().rstrip().split(' ')))
nodes.reverse()
tree = Tree(nodes)
print(tree.value())

