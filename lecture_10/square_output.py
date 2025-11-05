
from start_compiler.import_start import *



class numbers(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg

def square(*args):
    local_vars = {}
    local_vars['number_'] = args[0] if len(args) > 0 else start()
    local_vars['clock'] = start()
    StartError.lineNumber = 22
    check_events()
    _set('clock', local_vars, None)['clock'] = number(0).clone()
    local_vars['number__'] = start()
    StartError.lineNumber = 24
    check_events()
    _set('number__', local_vars, None)['number__'] = numbers().clone()
    StartError.lineNumber = 26
    check_events()
    
    while _lt(_get('clock', local_vars, None)['clock'], _len(_get('number_', local_vars, None)['number_'])): 
        StartError.lineNumber = 27
        check_events()
        _set(to_key(_get('clock', local_vars, None)['clock']), local_vars, _get('number__', local_vars, None)['number__'])[to_key(_get('clock', local_vars, None)['clock'])] = _mul(_get(to_key(_get('clock', local_vars, None)['clock']), local_vars, _get('number_', local_vars, None)['number_'])[to_key(_get('clock', local_vars, None)['clock'])], _get(to_key(_get('clock', local_vars, None)['clock']), local_vars, _get('number_', local_vars, None)['number_'])[to_key(_get('clock', local_vars, None)['clock'])]).clone()
        StartError.lineNumber = 28
        check_events()
        _set('clock', local_vars, None)['clock'] = _add(_get('clock', local_vars, None)['clock'], number(1)).clone()

    return _get('number__', local_vars, None)['number__']
try:
    local_vars['number_'] = start()
    StartError.lineNumber = 5
    check_events()
    _set('number_', local_vars, None)['number_'] = numbers().clone()
    StartError.lineNumber = 6
    check_events()
    _set(to_key(number(0)), local_vars, _get('number_', local_vars, None)['number_'])[to_key(number(0))] = number(1).clone()
    StartError.lineNumber = 7
    check_events()
    _set(to_key(number(1)), local_vars, _get('number_', local_vars, None)['number_'])[to_key(number(1))] = number(2).clone()
    StartError.lineNumber = 8
    check_events()
    _set(to_key(number(2)), local_vars, _get('number_', local_vars, None)['number_'])[to_key(number(2))] = number(3).clone()
    StartError.lineNumber = 9
    check_events()
    _set(to_key(number(3)), local_vars, _get('number_', local_vars, None)['number_'])[to_key(number(3))] = number(4).clone()
    StartError.lineNumber = 10
    check_events()
    _set(to_key(number(4)), local_vars, _get('number_', local_vars, None)['number_'])[to_key(number(4))] = number(5).clone()
    StartError.lineNumber = 11
    check_events()
    _set(to_key(number(5)), local_vars, _get('number_', local_vars, None)['number_'])[to_key(number(5))] = number(6).clone()
    StartError.lineNumber = 12
    check_events()
    _set(to_key(number(6)), local_vars, _get('number_', local_vars, None)['number_'])[to_key(number(6))] = number(7).clone()
    StartError.lineNumber = 13
    check_events()
    _set(to_key(number(7)), local_vars, _get('number_', local_vars, None)['number_'])[to_key(number(7))] = number(8).clone()
    StartError.lineNumber = 14
    check_events()
    _set(to_key(number(8)), local_vars, _get('number_', local_vars, None)['number_'])[to_key(number(8))] = number(9).clone()
    StartError.lineNumber = 15
    check_events()
    _set(to_key(number(9)), local_vars, _get('number_', local_vars, None)['number_'])[to_key(number(9))] = number(10).clone()
    StartError.lineNumber = 35
    check_events()
    _print(text("The squares of"), _get('number_', local_vars, None)['number_'], text("are"), square(_get('number_', local_vars, None)['number_']))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
