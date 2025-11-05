
from start_compiler.import_start import *



class numbers(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg

class student(start):
    def __init__(self, *args):
        self.names = args[0] if len(args) > 0 else start()
        self.grades = args[1] if len(args) > 1 else start()

    def average(self, *args):
        local_vars = {}
        local_vars['person'] = args[0] if len(args) > 0 else start()
        local_vars['clock'] = start()
        StartError.lineNumber = 14
        check_events()
        _set('clock', local_vars, None)['clock'] = number(0)
        local_vars['total_average'] = start()
        StartError.lineNumber = 16
        check_events()
        _set('total_average', local_vars, None)['total_average'] = number(0).clone()
        StartError.lineNumber = 17
        check_events()
        
        while _lt(_get('clock', local_vars, None)['clock'], _len(_get(to_key(text('grades')), local_vars, _get('person', local_vars, None)['person'])[to_key(text('grades'))])): 
            StartError.lineNumber = 18
            check_events()
            _set('total_average', local_vars, None)['total_average'] = _add(_get('total_average', local_vars, None)['total_average'], _get(to_key(_get('clock', local_vars, None)['clock']), local_vars, _get(to_key(text('grades')), local_vars, _get('person', local_vars, None)['person'])[to_key(text('grades'))])[to_key(_get('clock', local_vars, None)['clock'])])
            StartError.lineNumber = 19
            check_events()
            _set('clock', local_vars, None)['clock'] = _add(_get('clock', local_vars, None)['clock'], number(1))

        StartError.lineNumber = 21
        check_events()
        _set('total_average', local_vars, None)['total_average'] = _div(_get('total_average', local_vars, None)['total_average'], _len(_get(to_key(text('grades')), local_vars, _get('person', local_vars, None)['person'])[to_key(text('grades'))]))
        return _get('total_average', local_vars, None)['total_average']
try:
    local_vars['person'] = start()
    StartError.lineNumber = 30
    check_events()
    _set('person', local_vars, None)['person'] = student(text("Dummy"), numbers(number(5), number(7), number(3), number(8), number(9)))
    StartError.lineNumber = 31
    check_events()
    _print(text(" student :"), _get('person', local_vars, None)['person'], text("has an average grade of"), student.average(None, _get('person', local_vars, None)['person']))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
