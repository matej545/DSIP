
from start_compiler.import_start import *


try:
    local_vars['total_viewers'] = start()
    local_vars['country'] = start()
    local_vars['country_viewers'] = start()
    local_vars['percentage'] = start()
    StartError.lineNumber = 12
    check_events()
    _print_raw(text("What is the total number of viewers :"))
    StartError.lineNumber = 13
    check_events()
    _set('total_viewers', local_vars, None)['total_viewers'] = _input_number().clone()
    StartError.lineNumber = 14
    check_events()
    _print_raw(text("Where are the specific viewers from :"))
    StartError.lineNumber = 15
    check_events()
    _set('country', local_vars, None)['country'] = _input_text().clone()
    StartError.lineNumber = 16
    check_events()
    _print_raw(text("What number of viewers is from"), _get('country', local_vars, None)['country'], text(":"))
    StartError.lineNumber = 17
    check_events()
    _set('country_viewers', local_vars, None)['country_viewers'] = _input_number().clone()
    StartError.lineNumber = 19
    check_events()
    _set('percentage', local_vars, None)['percentage'] = _mul(_div(_get('country_viewers', local_vars, None)['country_viewers'], _get('total_viewers', local_vars, None)['total_viewers']), number(100)).clone()
    StartError.lineNumber = 24
    check_events()
    _print_raw(text("The percentage of viewers from"), _get('country', local_vars, None)['country'], text("is: "), _get('percentage', local_vars, None)['percentage'], text("%"))
except Exception as e:
    print(f'Start runtime error in line {StartError.lineNumber}: {e}')
finally:
    listener.stop()
