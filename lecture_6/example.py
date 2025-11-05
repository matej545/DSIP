
from start_compiler.import_start import *


try:
    local_vars['name'] = start()
    local_vars['favorite_number'] = start()
    local_vars['result'] = start()
    StartError.lineNumber = 5
    check_events()
    _print_raw(text("What is your name? "))
    StartError.lineNumber = 6
    check_events()
    _set('name', local_vars, None)['name'] = _input_text()
    StartError.lineNumber = 7
    check_events()
    _print_raw(text("Welcome to start "), _get('name', local_vars, None)['name'], text("!\n"))
    StartError.lineNumber = 9
    check_events()
    _print_raw(text("What is your favorite number? "))
    StartError.lineNumber = 10
    check_events()
    _set('favorite_number', local_vars, None)['favorite_number'] = _input_number()
    StartError.lineNumber = 11
    check_events()
    _print(text("Based on your number, I think the following calculation will result in the number 42."))
    StartError.lineNumber = 13
    check_events()
    _print(text("Calculating answer ..."))
    StartError.lineNumber = 14
    check_events()
    _sleep(number(1))
    StartError.lineNumber = 17
    check_events()
    _set('result', local_vars, None)['result'] = _add(_get('favorite_number', local_vars, None)['favorite_number'], number(42))
    StartError.lineNumber = 20
    check_events()
    _set('result', local_vars, None)['result'] = _mul(_get('result', local_vars, None)['result'], number(7))
    StartError.lineNumber = 23
    check_events()
    _set('result', local_vars, None)['result'] = _add(_get('result', local_vars, None)['result'], _pow(number(49), number(0.5)))
    StartError.lineNumber = 26
    check_events()
    _set('result', local_vars, None)['result'] = _sub(_get('result', local_vars, None)['result'], _mul(_add(_get('favorite_number', local_vars, None)['favorite_number'], number(1)), number(7)))
    StartError.lineNumber = 29
    check_events()
    _print(text("The answer is:"), _div(_get('result', local_vars, None)['result'], number(7)))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
