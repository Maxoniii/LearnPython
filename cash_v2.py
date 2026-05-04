import json
import os
from functools import wraps

def cache(file_path='cache.json', key_type='all'):
    def decorator(func):
        cache_data = {}
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    cache_data = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                cache_data = {}
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            if key_type == 'num':
                key = str(args)
            elif key_type == 'name':
                key = str(tuple(sorted(kwargs.items())))
            else:
                key = (args, tuple(sorted(kwargs.items())))
                key = str(key)
            
            if key in cache_data:
                print(key)
                return cache_data[key]
            
            print( key)
            result = func(*args, **kwargs)
            
            cache_data[key] = result
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, ensure_ascii=False, indent=2)
            
            return result
        
        return wrapper
    return decorator



@cache(file_path = 'dif_type_cache.json', key_type = 'all')
def calculate(x,y, znak = "add"):
    if znak == "add":
        return x+y
    elif znak == "multiply":
        return x*y
    else:
        return x-y

print(calculate(9,6,znak = "add"))
print(calculate(9,6,znak = "multiply"))
print(calculate(9,6,znak = "musor"))
