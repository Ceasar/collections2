import nose.tools
 
from linkedlist import DoubleLinkedList
 
 
def test_dll_empty():
    dll = DoubleLinkedList()
    assert dll.empty
 
 
def test_dll_not_empty():
    dll = DoubleLinkedList(range(10))
    assert not dll.empty
 
 
def test_dll_append():
    dll = DoubleLinkedList()
    dll.append(1)
    assert dll.right == 1
 
 
def test_dll_append_twice():
    dll = DoubleLinkedList()
    dll.append(1)
    dll.append(2)
    assert dll.right == 2
 
 
def test_dll_append_four_right():
    dll = DoubleLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    assert dll.right == 4
 
 
def test_dll_append_four_left():
    dll = DoubleLinkedList(range(4))
    assert dll.left == 0
 
 
def test_dll_append_singleton():
    dll = DoubleLinkedList()
    dll.append(1)
    assert dll.left == dll.right == 1
 
 
def test_dll_appendleft():
    dll = DoubleLinkedList()
    dll.appendleft(1)
    assert dll.left == 1
 
 
def test_dll_appendleft_singleton():
    dll = DoubleLinkedList()
    dll.appendleft(1)
    assert dll.left == dll.right == 1
 
 
def test_dll_appendleft_twice():
    dll = DoubleLinkedList()
    dll.appendleft(1)
    dll.appendleft(2)
    assert dll.left == 2
 
 
def test_pop():
    dll = DoubleLinkedList()
    dll.append(1)
    assert dll.pop() == 1
 
 
def test_popleft():
    dll = DoubleLinkedList()
    dll.append(1)
    assert dll.popleft() == 1
 
 
def test_append_twice_pop_once():
    dll = DoubleLinkedList()
    dll.append(1)
    dll.append(2)
    assert dll.pop() == 2
 
 
def test_append_twice_pop_twice():
    dll = DoubleLinkedList()
    dll.append(1)
    dll.append(2)
    dll.pop()
    assert dll.pop() == 1
 
 
def test_appendleft_full():
    dll = DoubleLinkedList(range(3))
    dll.appendleft(5)
    nose.tools.assert_equal(dll.pop(), 2)
 
 
def test_appendleft_many():
    dll = DoubleLinkedList()
    dll.appendleft(1)
    dll.appendleft(2)
    dll.appendleft(3)
    dll.appendleft(4)
    nose.tools.assert_equal(dll.pop(), 1)
