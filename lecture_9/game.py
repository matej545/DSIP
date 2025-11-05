
from start_compiler.import_start import *


try:
    local_vars['secret_number'] = start()
    StartError.lineNumber = 2
    check_events()
    _set('secret_number', local_vars, None)['secret_number'] = _random(number(100)).clone()
    local_vars['guess'] = start()
    local_vars['n'] = start()
    StartError.lineNumber = 7
    check_events()
    _set('n', local_vars, None)['n'] = number(1).clone()
    StartError.lineNumber = 9
    check_events()
    
    while _lt(_get('n', local_vars, None)['n'], number(101)): 
        StartError.lineNumber = 10
        check_events()
        _print_raw(text("Guess the number between 0 and 100:"))
        StartError.lineNumber = 11
        check_events()
        _set('guess', local_vars, None)['guess'] = _input_number().clone()
        StartError.lineNumber = 12
        check_events()
        
        if _lt(_get('guess', local_vars, None)['guess'], _get('secret_number', local_vars, None)['secret_number']): 
            StartError.lineNumber = 13
            check_events()
            _print(text("Too low"))
        else:
            StartError.lineNumber = 15
            check_events()
            
            if _gt(_get('guess', local_vars, None)['guess'], _get('secret_number', local_vars, None)['secret_number']): 
                StartError.lineNumber = 16
                check_events()
                _print(text("Too high"))
            else:
                StartError.lineNumber = 18
                check_events()
                
                break


        StartError.lineNumber = 21
        check_events()
        _set('n', local_vars, None)['n'] = _add(_get('n', local_vars, None)['n'], number(1)).clone()

    StartError.lineNumber = 23
    check_events()
    _print(text("You got it right after"), _get('n', local_vars, None)['n'], text("guesses"))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
