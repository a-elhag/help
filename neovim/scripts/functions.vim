function! BS() abort
	normal! ggyG
	normal! Gkk
	execute 'vsplit'
	let @/=""
endfunction
