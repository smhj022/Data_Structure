# DYNAMIC CONNECTIVITY WITH QUICK UNION

# PROBLEM STATEMENT --> There is a set of different numbers, in which Numbers can be connected by each
# other. So we have to write the code that can connect numbers and find if they are connected or not.
#  For Example :

#         1----2    3----4    5
#         |    |              |
#         6    7----8    9----0

# In the above example following numbers are connected
#    (1,2,6,7,8)
#    (3,4)
#    (5,0,9)

# connected function

# connected(1,8) --> return True
# connected(6,8) --> return True
# connected(1,9) --> return False

# union function .
# will have to connect the numbers if it is not connected

# union(4,9)

#         1----2    3----4    5
#         |    |         |    |
#         6    7----8    9----0

# Quick Union

# in quick union approach
print([0] * 10)


class WeightedQuickUnion():
    def __init__(self, total_num):
        self.ids = list(range(0, total_num))
        self.size = [1] * total_num

    def find_root(self, num):
        """function to find roots of the number for example

            1    2      5    7    8
                        |\        |
                        4 3       6
                        |
                        9

        So in the example above the root of 9, 4, 3 is 5 and root of 6 is 8"""
        while num != self.ids[num]:
            # ONLY THIS LINE IS ADDED TO MAKE TREE ALMOST FLAT
            self.ids[num] = self.ids[self.ids[num]]
            num = self.ids[num]
        return num

    def union(self, num1, num2):
        # find root of both number
        root1 = self.find_root(num1)
        root2 = self.find_root(num2)

        size_1 = self.size[root1]
        size_2 = self.size[root2]
        # only one change in is required
        if size_1 >= size_2:
            self.ids[root2] = root1
            self.size[root1] += self.size[root2]
        else:
            self.ids[root1] = root2
            self.size[root2] += self.size[root1]
        return self.ids

    # def connected(self, num1, num2):
    #     return self.root(num1) == self.root(num2)


quick_union_obj = WeightedQuickUnion(10)

quick_union_obj.union(4, 3)

print(quick_union_obj.ids)
# print(quick_union_obj.roots_count)


quick_union_obj.union(3, 8)

print(quick_union_obj.ids)
# print(quick_union_obj.roots_count)

quick_union_obj.union(6, 5)

print(quick_union_obj.ids)
# print(quick_union_obj.roots_count)

quick_union_obj.union(9, 4)

print(quick_union_obj.ids)
# print(quick_union_obj.roots_count)

quick_union_obj.union(2, 1)

print(quick_union_obj.ids)
# print(quick_union_obj.roots_count)

# print(quick_union_obj.connected(8, 9))

# print(quick_union_obj.connected(5, 4))

quick_union_obj.union(5, 0)

print(quick_union_obj.ids)
# print(quick_union_obj.roots_count)

quick_union_obj.union(7, 2)

print(quick_union_obj.ids)
# print(quick_union_obj.roots_count)

quick_union_obj.union(6, 1)

print(quick_union_obj.ids)
# print(quick_union_obj.roots_count)

quick_union_obj.union(7, 3)

print(quick_union_obj.ids)
print(quick_union_obj.size)


# Time complexity
