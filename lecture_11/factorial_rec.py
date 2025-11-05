
from start_compiler.import_start import *



def facrec(*args):
    local_vars = {}
    local_vars['input'] = args[0] if len(args) > 0 else start()
    local_vars['product'] = start()
    StartError.lineNumber = 9
    check_events()
    
    if _eql_val(_get('input', local_vars, None)['input'], number(0)): 
        StartError.lineNumber = 10
        check_events()
        
        return number(1)

    StartError.lineNumber = 12
    check_events()
    _set('product', local_vars, None)['product'] = _mul(_get('input', local_vars, None)['input'], facrec(_sub(_get('input', local_vars, None)['input'], number(1))))
    return _get('product', local_vars, None)['product']
try:
    local_vars['input'] = start()
    StartError.lineNumber = 2
    check_events()
    _print_raw(text("Input:"))
    StartError.lineNumber = 3
    check_events()
    _set('input', local_vars, None)['input'] = _input_number().clone()
    StartError.lineNumber = 15
    check_events()
    _print(facrec(number(5)))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
