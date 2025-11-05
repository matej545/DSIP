
from start_compiler.import_start import *


try:
    local_vars['x'] = start()
    StartError.lineNumber = 2
    check_events()
    number(3).copy(_set('x', local_vars, None)['x'])
    StartError.lineNumber = 3
    check_events()
    _print(_get('x', local_vars, None)['x'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
