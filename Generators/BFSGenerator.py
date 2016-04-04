from Generators.DFSGenerator import *

class BFSGenerator(DFSGenerator):
    def getNext(self, stack):
        return stack.popleft()