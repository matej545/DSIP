
from start_compiler.import_start import *


try:
    local_vars['name'] = start()
    local_vars['grade'] = start()
    local_vars['course'] = start()
    StartError.lineNumber = 5
    check_events()
    _set('name', local_vars, None)['name'] = text("Matej").clone()
    StartError.lineNumber = 6
    check_events()
    _set('grade', local_vars, None)['grade'] = number(10).clone()
    StartError.lineNumber = 7
    check_events()
    _set('course', local_vars, None)['course'] = text("DSPI").clone()
    StartError.lineNumber = 12
    check_events()
    _print(text("My name is"), _get('name', local_vars, None)['name'], text(" and I want a"), _get('grade', local_vars, None)['grade'], text("for the course "), _get('course', local_vars, None)['course'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
