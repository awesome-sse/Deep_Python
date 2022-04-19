"""Custom list implementaion"""


class CustomList(list):
    """Class CustomList"""

    def sum(self):
        """Sum elements in CustomList"""
        ans = 0
        for elem in enumerate(self):
            ans += elem[1]

        return ans

    def __eq__(self, other):
        return self.sum() == other.sum()

    def __ne__(self, other):
        return self.sum() != other.sum()

    def __lt__(self, other):
        return self.sum() < other.sum()

    def __le__(self, other):
        return self.sum() <= other.sum()

    def __gt__(self, other):
        return self.sum() > other.sum()

    def __ge__(self, other):
        return self.sum() >= other.sum()

    def __str__(self):
        return super().__str__() + " " + str(self.sum())

    def __add__(self, other):
        if max(len(self), len(other)) == len(self):
            add_result = CustomList(self)
            for i, elem in enumerate(other):
                add_result[i] += elem

        else:
            add_result = CustomList(other)
            for i, elem in enumerate(self):
                add_result[i] += elem

        return add_result

    def __sub__(self, other):
        if max(len(self), len(other)) == len(self):
            sub_result = CustomList(self)
            for i, elem in enumerate(other):
                sub_result[i] -= elem

        else:
            sub_result = CustomList(other)
            for i, elem in enumerate(self):
                sub_result[i] -= elem

            for i in range(len(other)):
                sub_result[i] *= -1

        return sub_result

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return CustomList(map(lambda x: x * -1, self.__sub__(other)))
