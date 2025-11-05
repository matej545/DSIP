
from start_compiler.import_start import *



def inc(*args):
    local_vars = {}
    local_vars['n'] = args[0] if len(args) > 0 else start()
    StartError.lineNumber = 4
    check_events()
    _add(_get('n', local_vars, None)['n'], number(1)).copy(_set('n', local_vars, None)['n'])
    return _get('n', local_vars, None)['n']
try:
    local_vars['n'] = start()
    StartError.lineNumber = 10
    check_events()
    _set('n', local_vars, None)['n'] = number(1)
    StartError.lineNumber = 11
    check_events()
    inc(_add(_get('n', local_vars, None)['n'], number(1)))
    StartError.lineNumber = 12
    check_events()
    _print(_get('n', local_vars, None)['n'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
