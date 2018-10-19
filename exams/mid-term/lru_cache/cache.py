######################### lru_cache ########################
# Implements a LRU cache using a doubly linked list. You   #
# must use the below Node() class in order to get credits. #
# Any changes to Node() class will result 0-credit penalty.#
############################################################
import functools
import time

"""DO NOT CHANGE this Node() class"""
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return "{}->{}".format(self.key, self.value)


class LRUCache():
    """DO NOT CHANGE this __init__() function"""
    def __init__(self, capacity=3):
        self.capacity = capacity
        self.map = {} # map holds {key} -> node relationship.
        self.head = Node(0, 0) # dummy head node
        self.tail = Node(0, 0) # dummy tail node
        self.head.next = self.tail # head being oldest
        self.tail.prev = self.head # tail being most recent

    def put(self, key, value):
        # TODO
        pass
        

    def get(self, key):
        # TODO
        return None



"""DO NOT CHANGE this lru_cache decorator function"""
def lru_cache(size=3):
    c = LRUCache(size)

    def decorator(func):
        @functools.wraps(func)
        def cache(*args, **kwargs):
            name = func.__name__
            arg_list = []
            if args:
                arg_list.append(', '.join(repr(arg) for arg in args))
            if kwargs:
                pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_str = ', '.join(arg_list)
            
            cache_key = name + '-' + arg_str
            cache_result = c.get(cache_key)
            
            if cache_result:
                print('[cache-hit] %s(%s) -> %r ' % (name, arg_str, cache_result))
                return cache_result

            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start_time
            c.put(cache_key, result)
            print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
            return result
        return cache

    return decorator

