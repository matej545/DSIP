
from start_compiler.import_start import *


try:
    StartError.lineNumber = 1
    check_events()
    _print_raw(text("Which number do you want to check ?"))
    local_vars['number_'] = start()
    StartError.lineNumber = 3
    check_events()
    _set('number_', local_vars, None)['number_'] = _input_number().clone()
    StartError.lineNumber = 5
    check_events()
    
    if _lt(_get('number_', local_vars, None)['number_'], number(0)): 
        StartError.lineNumber = 6
        check_events()
        _set('number_', local_vars, None)['number_'] = number(0).clone()
        StartError.lineNumber = 7
        check_events()
        _print(_get('number_', local_vars, None)['number_'])

except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
