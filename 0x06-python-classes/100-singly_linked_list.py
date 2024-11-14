#!/usr/bin/python3
"""
Singly linked list implementation using OOP
"""


class Node:
    """Represents a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialization"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''"data" attribute getter'''
        return self.__data

    @data.setter
    def data(self, data):
        '''"data" attribute setter'''
        if type(data) is not int:
            raise TypeError('data must be an integer')
        self.__data = data

    @property
    def next_node(self):
        '''"next_node" attribute getter'''
        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        '''"next_node" attribute setter'''
        if type(node) is not Node and node is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = node


class SinglyLinkedList:
    """Represents singly linked lists"""

    def __init__(self):
        """Initialization"""
        self.__head = None

    def sorted_insert(self, value):
        """Stores a new node in a sorted order"""
        if not self.__head:
            self.__head = Node(value)
            return
        new_node = Node(value)
        if new_node.data < self.__head.data:
            biggest_node = self.__head
            self.__head = new_node
            self.__head.next_node = biggest_node
        else:
            temp_node = self.__head
            while temp_node.next_node:
                if temp_node.next_node.data > new_node.data:
                    new_node.next_node = temp_node.next_node
                    temp_node.next_node = new_node
                    return
                temp_node = temp_node.next_node
            temp_node.next_node = new_node

    def __str__(self):
        """Customized string representation"""
        temp_node = self.__head
        string = ""
        while temp_node:
            string += str(temp_node.data) + "\n"
            temp_node = temp_node.next_node
        return string[:-1]
