
from start_compiler.import_start import *



class words(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg

def concatenate(*args):
    local_vars = {}
    local_vars['arg1'] = args[0] if len(args) > 0 else start()
    local_vars['arg2'] = args[1] if len(args) > 1 else start()
    local_vars['new'] = start()
    StartError.lineNumber = 25
    check_events()
    _set('new', local_vars, None)['new'] = words().clone()
    local_vars['i'] = start()
    StartError.lineNumber = 27
    check_events()
    _set('i', local_vars, None)['i'] = number(0).clone()
    StartError.lineNumber = 28
    check_events()
    
    while _lt(_get('i', local_vars, None)['i'], _len(_get('arg1', local_vars, None)['arg1'])): 
        StartError.lineNumber = 29
        check_events()
        _set(to_key(_get('i', local_vars, None)['i']), local_vars, _get('new', local_vars, None)['new'])[to_key(_get('i', local_vars, None)['i'])] = _get(to_key(_get('i', local_vars, None)['i']), local_vars, _get('arg1', local_vars, None)['arg1'])[to_key(_get('i', local_vars, None)['i'])].clone()
        StartError.lineNumber = 30
        check_events()
        _set('i', local_vars, None)['i'] = _add(_get('i', local_vars, None)['i'], number(1)).clone()

    StartError.lineNumber = 33
    check_events()
    
    while _lt(_sub(_get('i', local_vars, None)['i'], _len(_get('arg1', local_vars, None)['arg1'])), _len(_get('arg2', local_vars, None)['arg2'])): 
        StartError.lineNumber = 34
        check_events()
        _set(to_key(_get('i', local_vars, None)['i']), local_vars, _get('new', local_vars, None)['new'])[to_key(_get('i', local_vars, None)['i'])] = _get(to_key(_sub(_get('i', local_vars, None)['i'], _len(_get('arg1', local_vars, None)['arg1']))), local_vars, _get('arg2', local_vars, None)['arg2'])[to_key(_sub(_get('i', local_vars, None)['i'], _len(_get('arg1', local_vars, None)['arg1'])))].clone()
        StartError.lineNumber = 35
        check_events()
        _set('i', local_vars, None)['i'] = _add(_get('i', local_vars, None)['i'], number(1)).clone()

    return _get('new', local_vars, None)['new']
try:
    local_vars['text1'] = start()
    StartError.lineNumber = 6
    check_events()
    _set('text1', local_vars, None)['text1'] = words().clone()
    StartError.lineNumber = 7
    check_events()
    _set(to_key(number(0)), local_vars, _get('text1', local_vars, None)['text1'])[to_key(number(0))] = text("This").clone()
    StartError.lineNumber = 8
    check_events()
    _set(to_key(number(1)), local_vars, _get('text1', local_vars, None)['text1'])[to_key(number(1))] = text("is").clone()
    StartError.lineNumber = 9
    check_events()
    _set(to_key(number(2)), local_vars, _get('text1', local_vars, None)['text1'])[to_key(number(2))] = text("a").clone()
    StartError.lineNumber = 10
    check_events()
    _set(to_key(number(3)), local_vars, _get('text1', local_vars, None)['text1'])[to_key(number(3))] = text("sentence").clone()
    local_vars['text2'] = start()
    StartError.lineNumber = 13
    check_events()
    _set('text2', local_vars, None)['text2'] = words().clone()
    StartError.lineNumber = 14
    check_events()
    _set(to_key(number(0)), local_vars, _get('text2', local_vars, None)['text2'])[to_key(number(0))] = text("Here").clone()
    StartError.lineNumber = 15
    check_events()
    _set(to_key(number(1)), local_vars, _get('text2', local_vars, None)['text2'])[to_key(number(1))] = text("is").clone()
    StartError.lineNumber = 16
    check_events()
    _set(to_key(number(2)), local_vars, _get('text2', local_vars, None)['text2'])[to_key(number(2))] = text("another").clone()
    StartError.lineNumber = 17
    check_events()
    _set(to_key(number(3)), local_vars, _get('text2', local_vars, None)['text2'])[to_key(number(3))] = text("sentence").clone()
    StartError.lineNumber = 18
    check_events()
    _set(to_key(number(4)), local_vars, _get('text2', local_vars, None)['text2'])[to_key(number(4))] = text("again").clone()
    StartError.lineNumber = 40
    check_events()
    _print(concatenate(_get('text1', local_vars, None)['text1'], _get('text2', local_vars, None)['text2']))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
