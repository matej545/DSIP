
from start_compiler.import_start import *



class place(start):
    def __init__(self, *args):
        self.x = args[0] if len(args) > 0 else start()
        self.y = args[1] if len(args) > 1 else start()

def add_four(*args):
    local_vars = {}
    local_vars['value'] = args[0] if len(args) > 0 else start()
    StartError.lineNumber = 15
    check_events()
    _add(_get('value', local_vars, None)['value'], number(4)).copy(_set('value', local_vars, None)['value'])
    return
try:
    local_vars['debug_mode'] = start()
    StartError.lineNumber = 3
    check_events()
    _set('debug_mode', local_vars, None)['debug_mode'] = number(1)
    local_vars['tracking'] = start()
    StartError.lineNumber = 21
    check_events()
    _print_raw(text("what number are we tracking: "))
    StartError.lineNumber = 22
    check_events()
    _set('tracking', local_vars, None)['tracking'] = _input_number().clone()
    StartError.lineNumber = 24
    check_events()
    
    if _get('debug_mode', local_vars, None)['debug_mode']: 
        StartError.lineNumber = 25
        check_events()
        _print(text("Variable tracking is:"), _get('tracking', local_vars, None)['tracking'])

    StartError.lineNumber = 29
    check_events()
    _set('tracking', local_vars, None)['tracking'] = _div(_get('tracking', local_vars, None)['tracking'], number(2))
    StartError.lineNumber = 31
    check_events()
    
    if _get('debug_mode', local_vars, None)['debug_mode']: 
        StartError.lineNumber = 32
        check_events()
        _print(text("Variable tracking is:"), _get('tracking', local_vars, None)['tracking'])

    StartError.lineNumber = 36
    check_events()
    add_four(_get('tracking', local_vars, None)['tracking'])
    StartError.lineNumber = 38
    check_events()
    
    if _get('debug_mode', local_vars, None)['debug_mode']: 
        StartError.lineNumber = 39
        check_events()
        _print(text("Variable tracking is:"), _get('tracking', local_vars, None)['tracking'])

    local_vars['home'] = start()
    StartError.lineNumber = 45
    check_events()
    _set('home', local_vars, None)['home'] = place(_get('tracking', local_vars, None)['tracking'], _get('tracking', local_vars, None)['tracking'])
    StartError.lineNumber = 46
    check_events()
    _add(_get(to_key(text('y')), local_vars, _get('home', local_vars, None)['home'])[to_key(text('y'))], _get(to_key(text('x')), local_vars, _get('home', local_vars, None)['home'])[to_key(text('x'))]).copy(_set(to_key(text('x')), local_vars, _get('home', local_vars, None)['home'])[to_key(text('x'))])
    StartError.lineNumber = 48
    check_events()
    
    if _get('debug_mode', local_vars, None)['debug_mode']: 
        StartError.lineNumber = 49
        check_events()
        _print(text("Variable tracking is:"), _get('tracking', local_vars, None)['tracking'])
        StartError.lineNumber = 50
        check_events()
        _print(text("Variable home is:"), _get('home', local_vars, None)['home'])

    StartError.lineNumber = 54
    check_events()
    _set('tracking', local_vars, None)['tracking'] = _add(_get(to_key(text('x')), local_vars, _get('home', local_vars, None)['home'])[to_key(text('x'))], _get(to_key(text('y')), local_vars, _get('home', local_vars, None)['home'])[to_key(text('y'))]).clone()
    StartError.lineNumber = 56
    check_events()
    
    if _get('debug_mode', local_vars, None)['debug_mode']: 
        StartError.lineNumber = 57
        check_events()
        _print(text("Variable tracking is:"), _get('tracking', local_vars, None)['tracking'])
        StartError.lineNumber = 58
        check_events()
        _print(text("Variable home is:"), _get('home', local_vars, None)['home'])

except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
