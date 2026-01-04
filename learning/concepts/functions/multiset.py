
class Multiset:
    def __init__(self):
        self.items = []

    def add(self,val):
        self.items.append(val)
    
    def discard(self,val):
        self.items.remove(val)

    def length(self):
        return len(self.items)
    
    def contains(self,val):
        if val in self.items:
            return True
        else:
            return False
    

    @staticmethod
    def sort(decending_order):
        if decending_order == None or False:
            return Multiset.items.sort()
        else:
            return Multiset.items.sort(reverse=True)
    
    def clear(self):
        self.items.clear()
    
    def __str__(self):
        return f"{self.items}"
    

mulset = Multiset()
mulset.add(3)
print(mulset.contains(3))