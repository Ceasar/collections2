from nose.tools import raises
 
from queue import Queue2 as queue
 
 
def test_top():
    q = queue(10)
    q.push(1)
    assert q.top == 1
 
 
def test_empty():
    q = queue(10)
    assert q.empty
 
 
def test_not_empty():
    q = queue(10)
    q.push(1)
    assert not q.empty
 
 
def test_push():
    q = queue(10)
    size = len(q)
    q.push(1)
    assert len(q) == size + 1
    assert 1 in q
 
 
def test_pop():
    q = queue(10)
    q.push(1)
    size = len(q)
    assert q.pop() == 1
    assert len(q) == size - 1
    assert 1 not in q
 
 
def test_len():
    q = queue(10)
    q.push(1)
    q.push(2)
    q.push(3)
    assert len(q) == 3
 
 
def test_keep_order():
    q = queue(10)
    q.push(1)
    q.push(2)
    q.push(3)
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.pop() == 3
 
 
@raises(ValueError)
def test_doesnt_exceed_size():
    q = queue(2)
    q.push(1)
    q.push(2)
    q.push(3)
 
 
@raises(IndexError)
def test_cant_pop_from_empty_queue():
    q = queue(2)
    q.pop()
