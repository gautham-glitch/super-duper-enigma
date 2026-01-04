class circle:
    def __init__(self,radius):
        self._radius = radius
    @property
    def radius(self):
        return f"{self._radius:.1f} cm"

    @radius.setter
    def radius(self,new_radius):
        if abs(new_radius) > 0:
            self._radius = abs(new_radius)
        else:
            print("width not possible")

    @radius.deleter
    def radius(self):
        del self._radius
        print("old radius deleted")
