
from start_compiler.import_start import *



class savings(start):
    def __init__(self, *args):
        self.indexLength =- 1
        for i, arg in enumerate(args):
            self.__dict__[str(i)] = arg

class client(start):
    def __init__(self, *args):
        self.name = args[0] if len(args) > 0 else start()
        self.my_savings = args[1] if len(args) > 1 else start()
        self.total_savings = args[2] if len(args) > 2 else start()
try:
    local_vars['my_savings'] = start()
    StartError.lineNumber = 7
    check_events()
    _set('my_savings', local_vars, None)['my_savings'] = savings().clone()
    StartError.lineNumber = 8
    check_events()
    _set(to_key(number(0)), local_vars, _get('my_savings', local_vars, None)['my_savings'])[to_key(number(0))] = number(500).clone()
    StartError.lineNumber = 9
    check_events()
    _set(to_key(number(1)), local_vars, _get('my_savings', local_vars, None)['my_savings'])[to_key(number(1))] = number(1000).clone()
    StartError.lineNumber = 10
    check_events()
    _set(to_key(number(2)), local_vars, _get('my_savings', local_vars, None)['my_savings'])[to_key(number(2))] = number(1500).clone()
    local_vars['total_savings'] = start()
    StartError.lineNumber = 13
    check_events()
    _set('total_savings', local_vars, None)['total_savings'] = _add(_add(_get(to_key(number(0)), local_vars, _get('my_savings', local_vars, None)['my_savings'])[to_key(number(0))], _get(to_key(number(1)), local_vars, _get('my_savings', local_vars, None)['my_savings'])[to_key(number(1))]), _get(to_key(number(2)), local_vars, _get('my_savings', local_vars, None)['my_savings'])[to_key(number(2))]).clone()
    local_vars['bank_account'] = start()
    StartError.lineNumber = 22
    check_events()
    _set('bank_account', local_vars, None)['bank_account'] = client().clone()
    StartError.lineNumber = 23
    check_events()
    _set(to_key(text('name')), local_vars, _get('bank_account', local_vars, None)['bank_account'])[to_key(text('name'))] = text("Matej").clone()
    StartError.lineNumber = 24
    check_events()
    _set(to_key(text('my_savings')), local_vars, _get('bank_account', local_vars, None)['bank_account'])[to_key(text('my_savings'))] = _get('my_savings', local_vars, None)['my_savings'].clone()
    StartError.lineNumber = 25
    check_events()
    _set(to_key(text('total_savings')), local_vars, _get('bank_account', local_vars, None)['bank_account'])[to_key(text('total_savings'))] = _get('total_savings', local_vars, None)['total_savings'].clone()
    StartError.lineNumber = 27
    check_events()
    _print(text("My back account details :"), _get('bank_account', local_vars, None)['bank_account'])
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
