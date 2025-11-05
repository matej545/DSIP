
from start_compiler.import_start import *



class words(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg

    def helper(self, *args):
        local_vars = {}
        local_vars['list'] = args[0] if len(args) > 0 else start()
        local_vars['clock'] = start()
        local_vars['new_list'] = start()
        StartError.lineNumber = 14
        check_events()
        _set('new_list', local_vars, None)['new_list'] = words().clone()
        StartError.lineNumber = 15
        check_events()
        _set('clock', local_vars, None)['clock'] = number(1).clone()
        StartError.lineNumber = 16
        check_events()
        
        while _lt(_get('clock', local_vars, None)['clock'], _len(_get('list', local_vars, None)['list'])): 
            StartError.lineNumber = 17
            check_events()
            _set(to_key(_sub(_get('clock', local_vars, None)['clock'], number(1))), local_vars, _get('new_list', local_vars, None)['new_list'])[to_key(_sub(_get('clock', local_vars, None)['clock'], number(1)))] = _get(to_key(_get('clock', local_vars, None)['clock']), local_vars, _get('list', local_vars, None)['list'])[to_key(_get('clock', local_vars, None)['clock'])].clone()
            StartError.lineNumber = 18
            check_events()
            _set('clock', local_vars, None)['clock'] = _add(_get('clock', local_vars, None)['clock'], number(1)).clone()

        return _get('new_list', local_vars, None)['new_list']

    def search(self, *args):
        local_vars = {}
        local_vars['sentence'] = args[0] if len(args) > 0 else start()
        local_vars['input'] = args[1] if len(args) > 1 else start()
        StartError.lineNumber = 27
        check_events()
        
        if _eql_val(_len(_get('sentence', local_vars, None)['sentence']), number(0)): 
            StartError.lineNumber = 28
            check_events()
            
            return number(0)
        else:
            StartError.lineNumber = 30
            check_events()
            
            if _eql_val(_get(to_key(number(0)), local_vars, _get('sentence', local_vars, None)['sentence'])[to_key(number(0))], _get('input', local_vars, None)['input']): 
                StartError.lineNumber = 31
                check_events()
                
                return number(1)


        return words.search(None, words.helper(None, _get('sentence', local_vars, None)['sentence']), _get('input', local_vars, None)['input'])
try:
    StartError.lineNumber = 1
    check_events()
    _print_raw(text("word to look for?"))
    local_vars['input'] = start()
    StartError.lineNumber = 3
    check_events()
    _set('input', local_vars, None)['input'] = _input_text().clone()
    local_vars['sentence'] = start()
    StartError.lineNumber = 44
    check_events()
    _set('sentence', local_vars, None)['sentence'] = words(text("Let"), text("us"), text("look"), text("for"), text("specific"), text("words"), text("in"), text("a"), text("sentence")).clone()
    StartError.lineNumber = 45
    check_events()
    _print(words.search(None, _get('sentence', local_vars, None)['sentence'], _get('input', local_vars, None)['input']))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
