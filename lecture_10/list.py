
from start_compiler.import_start import *



class list(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg

    def append(self, *args):
        local_vars = {}
        local_vars['start_list'] = args[0] if len(args) > 0 else start()
        local_vars['add'] = args[1] if len(args) > 1 else start()
        local_vars['clock'] = start()
        StartError.lineNumber = 9
        check_events()
        _set('clock', local_vars, None)['clock'] = number(0).clone()
        local_vars['new_list'] = start()
        StartError.lineNumber = 11
        check_events()
        _set('new_list', local_vars, None)['new_list'] = list().clone()
        StartError.lineNumber = 12
        check_events()
        
        while _lt(_get('clock', local_vars, None)['clock'], _len(_get('start_list', local_vars, None)['start_list'])): 
            StartError.lineNumber = 13
            check_events()
            _set(to_key(_get('clock', local_vars, None)['clock']), local_vars, _get('new_list', local_vars, None)['new_list'])[to_key(_get('clock', local_vars, None)['clock'])] = _get(to_key(_get('clock', local_vars, None)['clock']), local_vars, _get('start_list', local_vars, None)['start_list'])[to_key(_get('clock', local_vars, None)['clock'])]
            StartError.lineNumber = 14
            check_events()
            _set('clock', local_vars, None)['clock'] = _add(_get('clock', local_vars, None)['clock'], number(1)).clone()

        StartError.lineNumber = 16
        check_events()
        _set(to_key(_get('clock', local_vars, None)['clock']), local_vars, _get('new_list', local_vars, None)['new_list'])[to_key(_get('clock', local_vars, None)['clock'])] = _get('add', local_vars, None)['add']
        StartError.lineNumber = 17
        check_events()
        _get('new_list', local_vars, None)['new_list'].copy(_set('start_list', local_vars, None)['start_list'])
        return

    def remove(self, *args):
        local_vars = {}
        local_vars['start_list'] = args[0] if len(args) > 0 else start()
        local_vars['remove'] = args[1] if len(args) > 1 else start()
        local_vars['clock'] = start()
        StartError.lineNumber = 26
        check_events()
        _set('clock', local_vars, None)['clock'] = number(0).clone()
        local_vars['clockfixer'] = start()
        StartError.lineNumber = 28
        check_events()
        _set('clockfixer', local_vars, None)['clockfixer'] = number(0).clone()
        local_vars['new_list'] = start()
        StartError.lineNumber = 30
        check_events()
        _set('new_list', local_vars, None)['new_list'] = list().clone()
        StartError.lineNumber = 31
        check_events()
        
        while _lt(_get('clock', local_vars, None)['clock'], _len(_get('start_list', local_vars, None)['start_list'])): 
            StartError.lineNumber = 32
            check_events()
            
            if _eql_val(_get(to_key(_get('clock', local_vars, None)['clock']), local_vars, _get('start_list', local_vars, None)['start_list'])[to_key(_get('clock', local_vars, None)['clock'])], _get('remove', local_vars, None)['remove']): 
                StartError.lineNumber = 33
                check_events()
                _set('clock', local_vars, None)['clock'] = _add(_get('clock', local_vars, None)['clock'], number(1)).clone()
                StartError.lineNumber = 34
                check_events()
                _set('clockfixer', local_vars, None)['clockfixer'] = _add(_get('clockfixer', local_vars, None)['clockfixer'], number(1)).clone()
            else:
                StartError.lineNumber = 36
                check_events()
                _set(to_key(_add(_get('clock', local_vars, None)['clock'], _get('clockfixer', local_vars, None)['clockfixer'])), local_vars, _get('new_list', local_vars, None)['new_list'])[to_key(_add(_get('clock', local_vars, None)['clock'], _get('clockfixer', local_vars, None)['clockfixer']))] = _get(to_key(_get('clock', local_vars, None)['clock']), local_vars, _get('start_list', local_vars, None)['start_list'])[to_key(_get('clock', local_vars, None)['clock'])]
                StartError.lineNumber = 37
                check_events()
                _set('clock', local_vars, None)['clock'] = _add(_get('clock', local_vars, None)['clock'], number(1)).clone()


        StartError.lineNumber = 40
        check_events()
        _get('new_list', local_vars, None)['new_list'].copy(_set('start_list', local_vars, None)['start_list'])
        return
try:
    local_vars['start_list'] = start()
    StartError.lineNumber = 46
    check_events()
    _set('start_list', local_vars, None)['start_list'] = list(number(4), number(5), number(2), number(10), number(9), number(5)).clone()
    StartError.lineNumber = 47
    check_events()
    list.append(None, _get('start_list', local_vars, None)['start_list'], number(8))
    StartError.lineNumber = 48
    check_events()
    list.remove(None, _get('start_list', local_vars, None)['start_list'], number(5))
    StartError.lineNumber = 49
    check_events()
    _print(_get('start_list', local_vars, None)['start_list'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
