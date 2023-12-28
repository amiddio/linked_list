from typing import Any
from collections import defaultdict


class Node:
    """Node of linked list"""

    def __init__(self, data, nxt=None) -> None:
        self.data = data
        self.next = nxt

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    """Linked list class"""

    def __init__(self, seq=None) -> None:
        self.length = 0
        self.head = None
        if seq:
            for data in seq:
                self.append(data)

    def __len__(self) -> int:
        return self.length

    def __contains__(self, data: Any) -> bool:
        pvt = self.head
        while pvt:
            if pvt.data == data:
                return True
            pvt = pvt.next
        return False

    def __str__(self) -> str:
        lst = []
        pvt = self.head
        while pvt:
            lst.append(str(pvt))
            pvt = pvt.next
        return f"[{' -> '.join(lst)}]"

    def get_list(self) -> list[Any]:
        """Converted linked list to list and return it"""
        return self.__convert_to_list()

    def append(self, data: Any) -> None:
        """Added item to the end of linked list"""
        node = Node(data)
        if self.head:
            pvt = self.head
            while pvt and pvt.next:
                pvt = pvt.next
            pvt.next = node
        else:
            self.head = node
        self.length += 1

    def append_left(self, data: Any) -> None:
        """Added item to the start of linked list"""
        node = Node(data)
        if self.head:
            nxt = self.head
            self.head = node
            self.head.next = nxt
            self.length += 1
        else:
            self.append(data)

    def insert(self, pos: int, data: Any) -> None:
        """
        Added item to some position into linked list.
        Parameter pos: positive number or zero.
        """
        if pos == 0:
            self.append_left(data)
        elif pos > len(self) - 1:
            self.append(data)
        else:
            pvt = self.head
            inx = 0
            while inx < pos - 1:
                pvt = pvt.next
                inx += 1
            nxt = pvt.next
            pvt.next = Node(data)
            pvt.next.next = nxt
            self.length += 1

    def counter(self) -> dict:
        """
        Return a collection where elements are stored as dictionary keys,
        and their counts are stored as dictionary values.
        """
        dct = defaultdict(int)
        pvt = self.head
        while pvt:
            dct[pvt.data] += 1
            pvt = pvt.next
        return dct

    def pop(self, pos: int = None) -> Node | None:
        """
        Deleted and return item from linked list.
        Parameter pos: positive number, zero or None.
        """
        if not self.head:
            return
        inx, res, pvt = 0, None, self.head
        if pos is None:
            while pvt and inx < len(self) - 1:
                pvt = pvt.next
                inx += 1
            res = pvt
            pvt.next = None
        elif pos == 0:
            res = pvt
            self.head = self.head.next
        else:
            while pvt and inx < pos - 1:
                pvt = pvt.next
                inx += 1
            res = pvt.next
            if pvt.next:
                pvt.next = pvt.next.next
        self.length -= 1
        return res

    def delete(self, data: Any) -> None:
        """Deleted node from linked list by content"""
        if not self.head:
            return
        prev = ptv = self.head
        inx = 0
        while ptv:
            if ptv.data == data:
                if prev == ptv:
                    self.pop(0)
                    prev = ptv = self.head
                    continue
                else:
                    self.pop(inx)
                    prev.next = ptv.next
                    inx -= 1
            prev = ptv
            ptv = ptv.next
            inx += 1

    def is_palindrome(self) -> bool:
        """Checked if linked list is palindrome"""
        if self.length in [0, 1]:
            return True
        stack = self.__convert_to_list()
        current = self.head
        while current:
            if current.data != stack.pop():
                return False
            current = current.next
        return True

    def reverse(self) -> None:
        """Reversed linked list"""
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def __convert_to_list(self) -> list:
        """Converted linked list to list"""
        lst = [None] * self.length
        inx = 0
        current = self.head
        while current:
            lst[inx] = current.data
            inx += 1
            current = current.next
        return lst
