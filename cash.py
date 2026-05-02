def cache(func):
    cache_storage = {}
    
    def wrapper(*args):
        if args in cache_storage:
            print( {args})
            return cache_storage[args]
        
        print({args})
        result = func(*args)
        
        cache_storage[args] = result
        return result
    
    return wrapper

@cache 
def sum(a,b):
    return a+b
def mult(a,b):
    return a*b

print(mult(15,15))
