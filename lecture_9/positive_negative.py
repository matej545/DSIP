
from start_compiler.import_start import *


try:
    StartError.lineNumber = 1
    check_events()
    _print_raw(text("Enter the number you want to check : positive , negative , or zero ?"))
    local_vars['n'] = start()
    StartError.lineNumber = 3
    check_events()
    _set('n', local_vars, None)['n'] = _input_number().clone()
    StartError.lineNumber = 4
    check_events()
    
    if _gt(_get('n', local_vars, None)['n'], number(0)): 
        StartError.lineNumber = 5
        check_events()
        _print(text("The number"), _get('n', local_vars, None)['n'], text("is positive"))
    else:
        StartError.lineNumber = 7
        check_events()
        
        if _lt(_get('n', local_vars, None)['n'], number(0)): 
            StartError.lineNumber = 8
            check_events()
            _print(text("The number"), _get('n', local_vars, None)['n'], text("is negative"))
        else:
            StartError.lineNumber = 10
            check_events()
            _print(text("The number"), _get('n', local_vars, None)['n'], text("is 0"))


except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
