
class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    my_dict = {}


    def add(self, number):
        # write your code here
        if number not in self.my_dict:
            self.my_dict[number] = 1
        else:
            self.my_dict[number] += 1


    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for d_key, d_value in self.my_dict.items():
            if value - d_key in self.my_dict:
                if d_key == value / 2 and self.my_dict[d_key] < 2:
                    continue
                else:
                    return True
        return False


sol = TwoSum()

sol.add(2)
sol.add(3)

print(sol.find(4))
print(sol.find(5))
print(sol.find(6))
sol.add(3)
sol.add(-1)

print(sol.find(6))