class MinHeap:
    def __init__(self):
        self.array = [None]
        self.count = 0

    def __repr__(self):
        return str(self.array)

    def parent_index(self, index):
        return index // 2
    def left_child_index(self, index):
        return 2 * index
    def right_child_index(self, index):
        return 2 * index + 1
        
    def insert(self, value):
        self.count += 1
        self.array.append(value)

        child_index = self.count
        parent_index = self.parent_index(child_index)

        while parent_index > 0:
            child = self.array[child_index]
            parent = self.array[parent_index]

            if child < parent:
                self.array[parent_index] = child
                self.array[child_index] = parent
            else:
                return

            child_index = parent_index
            parent_index = self.parent_index(parent_index)

    def retrieve(self):
        if self.count == 0:
            return None
        root = self.array[1]
    
        child = self.array.pop()
        self.count -= 1

        if self.count == 0:
            return child
        
        self.array[1] = child
        
        cur_index = 1
        
        while self.left_child_index(cur_index) <= self.count:
            left_child_index = self.left_child_index(cur_index)
            right_child_index = self.right_child_index(cur_index)

            change_index = cur_index

            
            if self.array[left_child_index] < self.array[change_index]:
                change_index = left_child_index
                
            if right_child_index <= self.count:
                #print("parent: {} - left: {} - right: {}".format(self.array[cur_index], self.array[left_child_index], self.array[right_child_index]))
        
                if self.array[right_child_index] < self.array[change_index]:
                    change_index = right_child_index

            if cur_index == change_index:
                break

            #swap
            temp = self.array[cur_index]
            self.array[cur_index] = self.array[change_index]
            self.array[change_index] = temp
            
            cur_index = change_index
            print(self.array)

        return root
