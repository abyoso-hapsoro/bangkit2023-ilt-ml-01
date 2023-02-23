import signal
import inspect
import importlib
import glob
from os.path import dirname, basename, join

# get all modules, remove main.py
__all__ = [basename(f)[:-3] for f in glob.glob(join(dirname(__file__), '*.py'))]
__all__.remove('main')

# create global dictionary for evaluating functions
dispatcher = {}
for _module in __all__:
  new_dispatches = dict(
    inspect.getmembers(importlib.import_module(_module), inspect.isfunction)
  )
  dispatcher = {**dispatcher, **new_dispatches}

# create custom error for input timeout
class AlarmException(Exception):
  pass

# setup input timeout
def timeout_handler(signum, frame):
  raise AlarmException('30s idle in input, interrupting execution')
signal.signal(signal.SIGALRM, timeout_handler)

if __name__ == '__main__':
  try:
    print('Job initialized. Please input a function that will be executed.\n\n')
    while True:
      # set 30 second timeout
      signal.alarm(30)

      # await user input
      stdin = input('Input: ')

      # add loop exit methods
      if stdin.lower() in ['break', 'exit', 'quit']:
        print('Exiting job')
        break
      
      # reset timeout for next loop
      signal.alarm(0)

      # evaluate input using global dictionary
      print(f'Output: {eval(stdin, dispatcher)}\n')
  
  except AlarmException as ex:
    print(f'\nTimeout reached: {ex}')
  
  except Exception as ex:
    print(f'Exception: {ex}')
  
  finally:
    print('\n\nJob terminated.')
