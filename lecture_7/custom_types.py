
from start_compiler.import_start import *



class savings(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg
try:
    local_vars['my_savings'] = start()
    StartError.lineNumber = 6
    check_events()
    _set('my_savings', local_vars, None)['my_savings'] = savings().clone()
    StartError.lineNumber = 7
    check_events()
    _set(to_key(number(0)), local_vars, _get('my_savings', local_vars, None)['my_savings'])[to_key(number(0))] = number(500).clone()
    StartError.lineNumber = 8
    check_events()
    _set(to_key(number(1)), local_vars, _get('my_savings', local_vars, None)['my_savings'])[to_key(number(1))] = number(1000).clone()
    StartError.lineNumber = 9
    check_events()
    _set(to_key(number(2)), local_vars, _get('my_savings', local_vars, None)['my_savings'])[to_key(number(2))] = number(1500).clone()
    local_vars['total_savings'] = start()
    StartError.lineNumber = 15
    check_events()
    _set('total_savings', local_vars, None)['total_savings'] = _add(_add(_get(to_key(number(0)), local_vars, _get('my_savings', local_vars, None)['my_savings'])[to_key(number(0))], _get(to_key(number(1)), local_vars, _get('my_savings', local_vars, None)['my_savings'])[to_key(number(1))]), _get(to_key(number(2)), local_vars, _get('my_savings', local_vars, None)['my_savings'])[to_key(number(2))]).clone()
    StartError.lineNumber = 17
    check_events()
    _print(text("My savings accounts have the following amounts :"), _get('my_savings', local_vars, None)['my_savings'])
    StartError.lineNumber = 18
    check_events()
    _print(text(" which total :"), _get('total_savings', local_vars, None)['total_savings'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
