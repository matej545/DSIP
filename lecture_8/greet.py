
from start_compiler.import_start import *



def beer(*args):
    local_vars = {}
    local_vars['student'] = args[0] if len(args) > 0 else start()
    local_vars['age'] = args[1] if len(args) > 1 else start()
    StartError.lineNumber = 5
    check_events()
    _print(text("Hello"), _get('student', local_vars, None)['student'])
    StartError.lineNumber = 6
    check_events()
    _print(text("Welcome to the DSPI course !"))
    return _gte(_get('age', local_vars, None)['age'], number(18))
try:
    StartError.lineNumber = 9
    check_events()
    _print(text("Drink Beer:"), beer(text("Matej"), number(18)))
    StartError.lineNumber = 10
    check_events()
    _print(text("Drink Beer:"), beer(text("Matko"), number(17)))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
