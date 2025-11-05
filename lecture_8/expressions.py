
from start_compiler.import_start import *



class numbers(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg
try:
    local_vars['npassing'] = start()
    local_vars['nfailing'] = start()
    local_vars['pass'] = start()
    StartError.lineNumber = 5
    check_events()
    _set('pass', local_vars, None)['pass'] = number(6).clone()
    local_vars['grades'] = start()
    StartError.lineNumber = 12
    check_events()
    _set('grades', local_vars, None)['grades'] = numbers().clone()
    StartError.lineNumber = 13
    check_events()
    _set(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))] = number(4).clone()
    StartError.lineNumber = 14
    check_events()
    _set(to_key(number(1)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(1))] = number(8.5).clone()
    StartError.lineNumber = 15
    check_events()
    _set(to_key(number(2)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(2))] = number(6).clone()
    StartError.lineNumber = 16
    check_events()
    _set(to_key(number(3)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(3))] = number(7).clone()
    StartError.lineNumber = 17
    check_events()
    _set(to_key(number(4)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(4))] = number(5.5).clone()
    StartError.lineNumber = 20
    check_events()
    _set('npassing', local_vars, None)['npassing'] = _gte(_get(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))], _get('pass', local_vars, None)['pass']).clone()
    StartError.lineNumber = 21
    check_events()
    _set('nfailing', local_vars, None)['nfailing'] = _lt(_get(to_key(number(0)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(0))], _get('pass', local_vars, None)['pass']).clone()
    StartError.lineNumber = 22
    check_events()
    _set('npassing', local_vars, None)['npassing'] = _add(_gte(_get(to_key(number(1)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(1))], _get('pass', local_vars, None)['pass']), _get('npassing', local_vars, None)['npassing']).clone()
    StartError.lineNumber = 23
    check_events()
    _set('nfailing', local_vars, None)['nfailing'] = _add(_lt(_get(to_key(number(1)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(1))], _get('pass', local_vars, None)['pass']), _get('nfailing', local_vars, None)['nfailing']).clone()
    StartError.lineNumber = 24
    check_events()
    _set('npassing', local_vars, None)['npassing'] = _add(_gte(_get(to_key(number(2)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(2))], _get('pass', local_vars, None)['pass']), _get('npassing', local_vars, None)['npassing']).clone()
    StartError.lineNumber = 25
    check_events()
    _set('nfailing', local_vars, None)['nfailing'] = _add(_lt(_get(to_key(number(2)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(2))], _get('pass', local_vars, None)['pass']), _get('nfailing', local_vars, None)['nfailing']).clone()
    StartError.lineNumber = 26
    check_events()
    _set('npassing', local_vars, None)['npassing'] = _add(_gte(_get(to_key(number(3)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(3))], _get('pass', local_vars, None)['pass']), _get('npassing', local_vars, None)['npassing']).clone()
    StartError.lineNumber = 27
    check_events()
    _set('nfailing', local_vars, None)['nfailing'] = _add(_lt(_get(to_key(number(3)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(3))], _get('pass', local_vars, None)['pass']), _get('nfailing', local_vars, None)['nfailing']).clone()
    StartError.lineNumber = 28
    check_events()
    _set('npassing', local_vars, None)['npassing'] = _add(_gte(_get(to_key(number(4)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(4))], _get('pass', local_vars, None)['pass']), _get('npassing', local_vars, None)['npassing']).clone()
    StartError.lineNumber = 29
    check_events()
    _set('nfailing', local_vars, None)['nfailing'] = _add(_lt(_get(to_key(number(4)), local_vars, _get('grades', local_vars, None)['grades'])[to_key(number(4))], _get('pass', local_vars, None)['pass']), _get('nfailing', local_vars, None)['nfailing']).clone()
    StartError.lineNumber = 31
    check_events()
    _print(text("Given the grades"), _get('grades', local_vars, None)['grades'])
    StartError.lineNumber = 32
    check_events()
    _print(_get('npassing', local_vars, None)['npassing'], text("passing grade ( s ) ; a pass is 6 or higher ."))
    StartError.lineNumber = 33
    check_events()
    _print(_get('nfailing', local_vars, None)['nfailing'], text(" failing grade ( s ) ; a fail is lower then 6"))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
