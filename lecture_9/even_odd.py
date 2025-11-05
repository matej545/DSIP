
from start_compiler.import_start import *


try:
    StartError.lineNumber = 1
    check_events()
    _print_raw(text("Enter the number you want to check : even or odd ? "))
    local_vars['nmb'] = start()
    StartError.lineNumber = 3
    check_events()
    _set('nmb', local_vars, None)['nmb'] = _input_number().clone()
    StartError.lineNumber = 4
    check_events()
    
    if _mod(_get('nmb', local_vars, None)['nmb'], number(2)): 
        StartError.lineNumber = 5
        check_events()
        _print(text("The number"), _get('nmb', local_vars, None)['nmb'], text("is even"))
    else:
        StartError.lineNumber = 7
        check_events()
        _print(text("The number"), _get('nmb', local_vars, None)['nmb'], text("is odd"))

except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
