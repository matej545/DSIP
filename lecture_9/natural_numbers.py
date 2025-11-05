
from start_compiler.import_start import *


try:
    StartError.lineNumber = 1
    check_events()
    _print_raw(text("Enter the last natural number to sum :"))
    local_vars['n'] = start()
    StartError.lineNumber = 3
    check_events()
    _set('n', local_vars, None)['n'] = _input_number().clone()
    local_vars['c'] = start()
    StartError.lineNumber = 5
    check_events()
    _set('c', local_vars, None)['c'] = number(0).clone()
    local_vars['sum'] = start()
    StartError.lineNumber = 7
    check_events()
    _set('sum', local_vars, None)['sum'] = number(0).clone()
    StartError.lineNumber = 8
    check_events()
    
    while _lt(_get('c', local_vars, None)['c'], _get('n', local_vars, None)['n']): 
        StartError.lineNumber = 9
        check_events()
        _set('c', local_vars, None)['c'] = _add(_get('c', local_vars, None)['c'], number(1)).clone()
        StartError.lineNumber = 10
        check_events()
        _set('sum', local_vars, None)['sum'] = _add(_get('sum', local_vars, None)['sum'], _get('c', local_vars, None)['c']).clone()

    StartError.lineNumber = 12
    check_events()
    _print(_get('sum', local_vars, None)['sum'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
