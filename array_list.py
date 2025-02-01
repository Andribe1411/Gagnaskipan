class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        """Initialise the instance of ArrayList"""
        self.capacity = 4
        self.size = 0
        self.arr = [0]*self.capacity
        self.ordered = True

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        """"Return the string"""
        return_string = "<"
        for i in range(self.size):
            return_string += str(self.arr[i])+", "
        if self.size > 0:
            return_string = return_string[:-2]+">"
        else:
            return_string = return_string+">"
        return return_string + " ,Ordered : " + str(self.ordered)

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        """ insert value at beginning of array """
        last = 0
        temp = 0
        if value > self.arr[0]:
            self.ordered = False

        if self.size == self.capacity:
            self.resize()

        self.size +=1
        for x in range(self.size):
            if x == 0:
                last = self.arr[x]
                self.arr[x] = value
            else:
                temp = self.arr[x]
                self.arr[x] = last
                last = temp
                




    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        """ insert value at specific index of array """
        last = 0
        temp = 0
        if self.arr[index] == self.arr[self.size]:
            if value > self.arr[index]:
                self.ordered = False
        if index == 0:
            if value > self.arr[index]:
                self.ordered = False

        if value > self.arr[index]:
                self.ordered = False



        if self.size == self.capacity:
            self.resize()
        self.size +=1
        for x in range(index,self.size):
            if x == index:
                #if value > self.arr[x]:
                #    self.ordered = False
                last = self.arr[x]
                self.arr[x] = value
            else:
                temp = self.arr[x]
                self.arr[x] = last
                last = temp


    #Time complexity: O(1) - constant time
    def append(self, value):
        """ insert value at the end of array """
        #print(value,self.arr[self.size-1],self.size)
        if value < self.arr[self.size-1] and self.size != 0:
            self.ordered = False
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = value
        self.size += 1
        
 
    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        """ set value at specific index of array """
        self.arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        """ get first value form the array """ 
        return self.arr[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        """ get value from specific index """
        return self.arr[index]

    #Time complexity: O(1) - constant time
    def get_last(self):
        """ get last value from the array """
        return self.arr[self.size]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        """ allocate more space by increasing array's capacity """
        self.capacity *= 2
        new_arr = [0]*self.capacity
        for x in range(self.size):
            new_arr[x] = self.arr[x]
        self.arr = new_arr

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        """ remove value at specific index of the array """
        for x in range(index,self.size):
            if x != self.size - 1:
                self.arr[x] = self.arr[x+1]
            else:
                self.arr[x] = 0
        self.size -=1


    #Time complexity: O(1) - constant time
    def clear(self):
        """ removes all values from the array """
        self.arr = [0]*self.capacity
        self.size = 0

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        """ insert a value so that the array retains ordering """
        if self.ordered:
            middle = self.size//2
            
        else:
            raise NotOrdered()

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    # arr_lis.append(1)
    # arr_lis.append(2)
    #arr_lis.append(3)
    # arr_lis.append(4)
    # arr_lis.append(5)
    arr_lis.append(2)
    arr_lis.append(4)
    arr_lis.append(6)
    # print(str(arr_lis))
    arr_lis.insert(5,3)
    # arr_lis.clear()
    # print(str(arr_lis))
    print(arr_lis)
    arr_lis.prepend(1)
    print(arr_lis)
    # print(arr_lis.ordered)
    #arr_lis.remove_at(3)
    #arr_lis.prepend(10)
