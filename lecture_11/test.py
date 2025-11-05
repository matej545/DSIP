


from start_compiler.import_start import *



class words(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg

def helper(*args):
    local_vars = {}
    local_vars['list'] = args[0] if len(args) > 0 else start()
    local_vars['clock'] = start()
    local_vars['new_list'] = start()
    StartError.lineNumber = 10
    check_events()
    _set('new_list', local_vars, None)['new_list'] = words().clone()
    StartError.lineNumber = 11
    check_events()
    _set('clock', local_vars, None)['clock'] = number(1).clone()
    StartError.lineNumber = 13
    check_events()
    
    while _lt(_get('clock', local_vars, None)['clock'], _len(_get('list', local_vars, None)['list'])): 
        StartError.lineNumber = 14
        check_events()
        _set(to_key(_sub(_get('clock', local_vars, None)['clock'], number(1))), local_vars, _get('new_list', local_vars, None)['new_list'])[to_key(_sub(_get('clock', local_vars, None)['clock'], number(1)))] = _get(to_key(_get('clock', local_vars, None)['clock']), local_vars, _get('list', local_vars, None)['list'])[to_key(_get('clock', local_vars, None)['clock'])]
        StartError.lineNumber = 15
        check_events()
        _print(_get('clock', local_vars, None)['clock'])
        StartError.lineNumber = 16
        check_events()
        _set('clock', local_vars, None)['clock'] = _add(_get('clock', local_vars, None)['clock'], number(1)).clone()

    return _get('new_list', local_vars, None)['new_list']
try:
    local_vars['sentence'] = start()
    StartError.lineNumber = 23
    check_events()
    _set('sentence', local_vars, None)['sentence'] = words(text("kris"), text("tom"), text("jerry")).clone()
    local_vars['new_sentence'] = start()
    StartError.lineNumber = 26
    check_events()
    _set('new_sentence', local_vars, None)['new_sentence'] = helper(_get('sentence', local_vars, None)['sentence']).clone()
    StartError.lineNumber = 28
    check_events()
    _print(_get('new_sentence', local_vars, None)['new_sentence'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
