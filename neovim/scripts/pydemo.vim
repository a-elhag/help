
function! DefPython()
python3 << PYEND
import vim
def python_input(message = 'input'):
  vim.command('call inputsave()')
  vim.command("let user_input = input('" + message + ": ')")
  vim.command('call inputrestore()')
  return vim.eval('user_input')

def demo():
  curline = vim.current.line
  name = python_input('Enter name')
  vim.current.line = curline + ' ' + name
PYEND
endfunction
call DefPython()


" Same as the other one,
" :so pydemo.vim
" :py3 demo()
