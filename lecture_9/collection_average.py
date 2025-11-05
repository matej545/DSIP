
from start_compiler.import_start import *



class numbers(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg
try:
    local_vars['grades'] = start()
    StartError.lineNumber = 6
    check_events()
    _set('grades', local_vars, None)['grades'] = numbers().clone()
    local_vars['fillclock'] = start()
    StartError.lineNumber = 8
    check_events()
    _set('fillclock', local_vars, None)['fillclock'] = number(0).clone()
    StartError.lineNumber = 9
    check_events()
    
    while _lt(_get('fillclock', local_vars, None)['fillclock'], number(4)): 
        StartError.lineNumber = 10
        check_events()
        _set(to_key(_get('fillclock', local_vars, None)['fillclock']), local_vars, _get('grades', local_vars, None)['grades'])[to_key(_get('fillclock', local_vars, None)['fillclock'])] = _random(number(10)).clone()
        StartError.lineNumber = 11
        check_events()
        _set('fillclock', local_vars, None)['fillclock'] = _add(_get('fillclock', local_vars, None)['fillclock'], number(1)).clone()

    local_vars['clock'] = start()
    StartError.lineNumber = 16
    check_events()
    _set('clock', local_vars, None)['clock'] = number(0).clone()
    local_vars['sum'] = start()
    StartError.lineNumber = 19
    check_events()
    _set('sum', local_vars, None)['sum'] = number(0).clone()
    StartError.lineNumber = 21
    check_events()
    
    while _lt(_get('clock', local_vars, None)['clock'], _len(_get('grades', local_vars, None)['grades'])): 
        StartError.lineNumber = 22
        check_events()
        _set('sum', local_vars, None)['sum'] = _add(_get('sum', local_vars, None)['sum'], _get(to_key(_get('clock', local_vars, None)['clock']), local_vars, _get('grades', local_vars, None)['grades'])[to_key(_get('clock', local_vars, None)['clock'])]).clone()
        StartError.lineNumber = 23
        check_events()
        _set('clock', local_vars, None)['clock'] = _add(_get('clock', local_vars, None)['clock'], number(1)).clone()

    StartError.lineNumber = 26
    check_events()
    _print(_div(_get('sum', local_vars, None)['sum'], _len(_get('grades', local_vars, None)['grades'])))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
