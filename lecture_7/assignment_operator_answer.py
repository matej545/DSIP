
from start_compiler.import_start import *



class grade_list(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg
try:
    local_vars['grades'] = start()
    StartError.lineNumber = 10
    check_events()
    _set('grades', local_vars, None)['grades'] = grade_list().clone()
    StartError.lineNumber = 11
    check_events()
    _set(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))] = number(10).clone()
    StartError.lineNumber = 12
    check_events()
    _set(to_key(number(1)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(1))] = _get(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))]
    StartError.lineNumber = 13
    check_events()
    _set(to_key(number(2)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(2))] = _get(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))]
    StartError.lineNumber = 14
    check_events()
    _set(to_key(number(3)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(3))] = _get(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))]
    StartError.lineNumber = 15
    check_events()
    _set(to_key(number(4)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(4))] = _get(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))]
    StartError.lineNumber = 18
    check_events()
    _print(_get('grades', local_vars, None)['grades'])
    StartError.lineNumber = 19
    check_events()
    number(42).copy(_set(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))])
    StartError.lineNumber = 20
    check_events()
    _print(_get('grades', local_vars, None)['grades'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
