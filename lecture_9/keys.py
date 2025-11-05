
from start_compiler.import_start import *

def event0():
    if _key(text("w")): 
        StartError.lineNumber = 6
        _sleep(number(0.08))
        StartError.lineNumber = 7
        _set('counter', local_vars, None)['counter'] = _add(_get('counter', local_vars, None)['counter'], number(1)).clone()
        StartError.lineNumber = 8
        _print(text("current counter is :"), _get('counter', local_vars, None)['counter'])

def event1():
    if _key(text("s")): 
        StartError.lineNumber = 11
        _sleep(number(0.08))
        StartError.lineNumber = 12
        _set('counter', local_vars, None)['counter'] = _sub(_get('counter', local_vars, None)['counter'], number(1)).clone()
        StartError.lineNumber = 13
        _print(text("current counter is :"), _get('counter', local_vars, None)['counter'])

def event2():
    if _key(text("q")): 
        StartError.lineNumber = 16
        
        listener.stop()
        exit(0)


try:
    local_vars['counter'] = start()
    StartError.lineNumber = 2
    check_events()
    _set('counter', local_vars, None)['counter'] = number(0).clone()
    StartError.lineNumber = 4
    check_events()
    
    while number(1): 
        StartError.lineNumber = 5
        check_events()
        
        start_events["""_key(text("w"))"""] = event0
        StartError.lineNumber = 10
        check_events()
        
        start_events["""_key(text("s"))"""] = event1
        StartError.lineNumber = 15
        check_events()
        
        start_events["""_key(text("q"))"""] = event2

except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
