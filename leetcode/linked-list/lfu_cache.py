class Node:
    def __init__(self, key, val, freq):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None, 0)
        self.tail = Node(None, None, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_node_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def remove_node(self, node):
        
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def is_empty(self):
        return self.head.next == self.tail
    
    def remove_tail_node(self):
        if self.is_empty():
            return None
        tail_node = self.tail.prev
        self.remove_node(tail_node)
        return tail_node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.node_dict = {}
        self.freq_dict = {}
    
    def update_freq_dict(self, node):
        freq = node.freq
        self.freq_dict[freq].remove_node(node)
        if self.min_freq == freq and self.freq_dict[freq].is_empty():
            self.min_freq += 1
        node.freq += 1
        freq = node.freq
        if freq not in self.freq_dict:
            self.freq_dict[freq] = DoublyLinkedList()
        self.freq_dict[freq].add_node_to_head(node)
    
    def get(self, key: int) -> int:
        if key not in self.node_dict:
            return -1
        node = self.node_dict[key]
        self.update_freq_dict(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.node_dict:
            node = self.node_dict[key]
            node.val = value
            self.update_freq_dict(node)
        else:
            if self.size == self.capacity:
                min_freq_list = self.freq_dict[self.min_freq]
                node_to_remove = min_freq_list.remove_tail_node()
                del self.node_dict[node_to_remove.key]
                self.size -= 1
            
            new_node = Node(key, value, 1)
            self.node_dict[key] = new_node
            if 1 not in self.freq_dict:
                self.freq_dict[1] = DoublyLinkedList()
            self.freq_dict[1].add_node_to_head(new_node)
            self.min_freq = 1
            self.size += 1