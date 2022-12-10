from io import StringIO as _Out
from contextlib import contextmanager
import sys
from functools import wraps


@contextmanager
def _stdout_redirected(new_stdout):
    save_stdout = sys.stdout
    sys.stdout = new_stdout
    try:
        yield None
    finally:
        sys.stdout = save_stdout
        
        
class Stdout:
    @staticmethod
    def redirect(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with _Out() as out:
                with _stdout_redirected(out):
                    func(*args, **kwargs)
        return wrapper
