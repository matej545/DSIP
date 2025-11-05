
from start_compiler.import_start import *


try:
    local_vars['a_value'] = start()
    local_vars['b_value'] = start()
    local_vars['c_value'] = start()
    StartError.lineNumber = 5
    check_events()
    _set('a_value', local_vars, None)['a_value'] = number(1)
    StartError.lineNumber = 6
    check_events()
    _set('b_value', local_vars, None)['b_value'] = number(3)
    StartError.lineNumber = 7
    check_events()
    _set('c_value', local_vars, None)['c_value'] = number(5)
    StartError.lineNumber = 9
    check_events()
    _set('c_value', local_vars, None)['c_value'] = _get('a_value', local_vars, None)['a_value']
    StartError.lineNumber = 10
    check_events()
    _get('a_value', local_vars, None)['a_value'].copy(_set('b_value', local_vars, None)['b_value'])
    StartError.lineNumber = 11
    check_events()
    number(10).copy(_set('a_value', local_vars, None)['a_value'])
    StartError.lineNumber = 12
    check_events()
    _print(_get('a_value', local_vars, None)['a_value'], _get('b_value', local_vars, None)['b_value'], _get('c_value', local_vars, None)['c_value'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
