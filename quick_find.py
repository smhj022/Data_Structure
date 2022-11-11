# TODO : DYNAMIC CONNECTIVITY

# PROBLEM STATEMENT --> There is a set of different numbers, in which Numbers can be connected by each
# other. So we have to write the code that can connent numbers and find if they are connected or not.
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


# QUICK FIND

# In quick find approch the initially the id (same as number) is given to every number. When the
# number connects the ids will become same of the connected numbers


class Quickfind():
    def __init__(self, total_num):
        self.number_array = list(range(0, total_num))
        self.ids = self.number_array

    def test(self):
        print(self.ids)

    def union(self, num1, num2):
        # check if the id of num1 and num2 are same or not
        id_1 = self.ids[num1]
        id_2 = self.ids[num2]
        if id_1 == id_2:
            return print(f"{num1} and {num2} are already in union")

        # if the id is not same make them same
        # find all id_1
        i = 0
        for id in self.ids:
            if id == id_1:
                self.ids[i] = id_2
            i += 1
        return self.ids

    def connected(self, num1, num2):
        if self.ids[num1] == self.ids[num2]:
            return True
        return False


dynamic_connect = Quickfind(25)


dynamic_connect.union(2, 6)
dynamic_connect.union(1, 3)
dynamic_connect.union(3, 4)
dynamic_connect.union(6, 1)
dynamic_connect.union(2, 3)

print(dynamic_connect.test())
print(dynamic_connect.connected(7, 4))


# Time complexity of the problem


# N for Initialization method
# N for union method
# 1 for connected method

# As we see both initialization and the union operation involved the for loop that go through
# the entire array. So in particular if we have N union command and n objects they will take
# quadratic time. Quadratic equations are really slower so that they dont scale.

# Union is too expensive in quick find method
