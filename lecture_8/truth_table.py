
from start_compiler.import_start import *


try:
    local_vars['p'] = start()
    local_vars['q'] = start()
    local_vars['and'] = start()
    local_vars['or'] = start()
    StartError.lineNumber = 6
    check_events()
    _print(text("p | q | p and q | p or q"))
    StartError.lineNumber = 7
    check_events()
    _print(text(" ------------------------"))
    StartError.lineNumber = 8
    check_events()
    _set('p', local_vars, None)['p'] = number(1).clone()
    StartError.lineNumber = 9
    check_events()
    _set('q', local_vars, None)['q'] = number(1).clone()
    StartError.lineNumber = 10
    check_events()
    _set('and', local_vars, None)['and'] = _and(_get('p', local_vars, None)['p'], _get('q', local_vars, None)['q']).clone()
    StartError.lineNumber = 11
    check_events()
    _set('or', local_vars, None)['or'] = _or(_get('p', local_vars, None)['p'], _get('q', local_vars, None)['q']).clone()
    StartError.lineNumber = 12
    check_events()
    _print(_get('p', local_vars, None)['p'], text("|"), _get('q', local_vars, None)['q'], text("| "), _get('and', local_vars, None)['and'], text(" | "), _get('or', local_vars, None)['or'])
    StartError.lineNumber = 13
    check_events()
    _set('p', local_vars, None)['p'] = number(1).clone()
    StartError.lineNumber = 14
    check_events()
    _set('q', local_vars, None)['q'] = number(0).clone()
    StartError.lineNumber = 15
    check_events()
    _set('and', local_vars, None)['and'] = _and(_get('p', local_vars, None)['p'], _get('q', local_vars, None)['q']).clone()
    StartError.lineNumber = 16
    check_events()
    _set('or', local_vars, None)['or'] = _or(_get('p', local_vars, None)['p'], _get('q', local_vars, None)['q']).clone()
    StartError.lineNumber = 17
    check_events()
    _print(_get('p', local_vars, None)['p'], text("|"), _get('q', local_vars, None)['q'], text("| "), _get('and', local_vars, None)['and'], text(" | "), _get('or', local_vars, None)['or'])
    StartError.lineNumber = 18
    check_events()
    _set('p', local_vars, None)['p'] = number(0).clone()
    StartError.lineNumber = 19
    check_events()
    _set('q', local_vars, None)['q'] = number(1).clone()
    StartError.lineNumber = 20
    check_events()
    _set('and', local_vars, None)['and'] = _and(_get('p', local_vars, None)['p'], _get('q', local_vars, None)['q']).clone()
    StartError.lineNumber = 21
    check_events()
    _set('or', local_vars, None)['or'] = _or(_get('p', local_vars, None)['p'], _get('q', local_vars, None)['q']).clone()
    StartError.lineNumber = 22
    check_events()
    _print(_get('p', local_vars, None)['p'], text("|"), _get('q', local_vars, None)['q'], text("| "), _get('and', local_vars, None)['and'], text(" | "), _get('or', local_vars, None)['or'])
    StartError.lineNumber = 23
    check_events()
    _set('p', local_vars, None)['p'] = number(0).clone()
    StartError.lineNumber = 24
    check_events()
    _set('q', local_vars, None)['q'] = number(0).clone()
    StartError.lineNumber = 25
    check_events()
    _set('and', local_vars, None)['and'] = _and(_get('p', local_vars, None)['p'], _get('q', local_vars, None)['q']).clone()
    StartError.lineNumber = 26
    check_events()
    _set('or', local_vars, None)['or'] = _or(_get('p', local_vars, None)['p'], _get('q', local_vars, None)['q']).clone()
    StartError.lineNumber = 27
    check_events()
    _print(_get('p', local_vars, None)['p'], text("|"), _get('q', local_vars, None)['q'], text("| "), _get('and', local_vars, None)['and'], text(" | "), _get('or', local_vars, None)['or'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
