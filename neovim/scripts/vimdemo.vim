"The function gets the current line to a variable, prompts the user to enter a name,
"then appends the entered name to the current line.
"This is only a simple demonstration, and is not intended to do anything useful.

function! Demo()
  let curline = getline('.')
  call inputsave()
  let name = input('Enter name: ')
  call inputrestore()
  call setline('.', curline . ' ' . name)
endfunction

" To run, type
" :so vimdemo.vim
" :call Demo()

