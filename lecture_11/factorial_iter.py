
from start_compiler.import_start import *


try:
    local_vars['input'] = start()
    StartError.lineNumber = 2
    check_events()
    _print_raw(text("Input:"))
    StartError.lineNumber = 3
    check_events()
    _set('input', local_vars, None)['input'] = _input_number().clone()
    local_vars['product'] = start()
    local_vars['n'] = start()
    StartError.lineNumber = 7
    check_events()
    _set('n', local_vars, None)['n'] = number(1)
    StartError.lineNumber = 8
    check_events()
    _set('product', local_vars, None)['product'] = number(1)
    StartError.lineNumber = 9
    check_events()
    
    while _lt(_get('n', local_vars, None)['n'], _get('input', local_vars, None)['input']): 
        StartError.lineNumber = 10
        check_events()
        _set('product', local_vars, None)['product'] = _mul(_get('product', local_vars, None)['product'], _get('n', local_vars, None)['n'])
        StartError.lineNumber = 11
        check_events()
        _set('n', local_vars, None)['n'] = _add(_get('n', local_vars, None)['n'], number(1))

    StartError.lineNumber = 13
    check_events()
    _print(_get('product', local_vars, None)['product'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
