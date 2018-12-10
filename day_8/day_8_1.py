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

    def get_all_metadata(self):
        metadata = self.metadata
        for node in self.nodes:
            metadata += node.get_all_metadata()
        return metadata

nodes = list(map(int, stdin.readline().rstrip().split(' ')))
nodes.reverse()
tree = Tree(nodes)
print(sum(tree.get_all_metadata()))

