
from start_compiler.import_start import *

def event0():
    if _lt(_get('counter', local_vars, None)['counter'], number(0)): 
        StartError.lineNumber = 9
        
        listener.stop()
        exit(0)


try:
    local_vars['counter'] = start()
    StartError.lineNumber = 5
    check_events()
    _print_raw(text(" start counter : "))
    StartError.lineNumber = 6
    check_events()
    _set('counter', local_vars, None)['counter'] = _input_number()
    StartError.lineNumber = 8
    check_events()
    
    start_events["""_lt(_get('counter', local_vars, None)['counter'], number(0))"""] = event0
    StartError.lineNumber = 12
    check_events()
    
    while number(1): 
        StartError.lineNumber = 13
        check_events()
        _print(text(" current counter is:"), _get('counter', local_vars, None)['counter'])
        StartError.lineNumber = 14
        check_events()
        _sub(_get('counter', local_vars, None)['counter'], number(1)).copy(_set('counter', local_vars, None)['counter'])

except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
