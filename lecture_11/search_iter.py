
from start_compiler.import_start import *



class words(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg

    def search(self, *args):
        local_vars = {}
        local_vars['sentence'] = args[0] if len(args) > 0 else start()
        local_vars['input'] = args[1] if len(args) > 1 else start()
        local_vars['n'] = start()
        StartError.lineNumber = 15
        check_events()
        _set('n', local_vars, None)['n'] = number(0)
        StartError.lineNumber = 16
        check_events()
        
        while _lt(_get('n', local_vars, None)['n'], _len(_get('sentence', local_vars, None)['sentence'])): 
            StartError.lineNumber = 17
            check_events()
            
            if _eql_val(_get(to_key(_get('n', local_vars, None)['n']), local_vars, _get('sentence', local_vars, None)['sentence'])[to_key(_get('n', local_vars, None)['n'])], _get('input', local_vars, None)['input']): 
                StartError.lineNumber = 18
                check_events()
                
                return number(1)
            else:
                StartError.lineNumber = 20
                check_events()
                _set('n', local_vars, None)['n'] = _add(_get('n', local_vars, None)['n'], number(1)).clone()


        return number(0)
try:
    StartError.lineNumber = 1
    check_events()
    _print_raw(text("word to look for?"))
    local_vars['input'] = start()
    StartError.lineNumber = 3
    check_events()
    _set('input', local_vars, None)['input'] = _input_text().clone()
    local_vars['sentence'] = start()
    StartError.lineNumber = 28
    check_events()
    _set('sentence', local_vars, None)['sentence'] = words(text("Let"), text("us"), text("look"), text("for"), text("specific"), text("words"), text("in"), text("a"), text("sentence")).clone()
    StartError.lineNumber = 29
    check_events()
    _print(words.search(None, _get('sentence', local_vars, None)['sentence'], _get('input', local_vars, None)['input']))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
