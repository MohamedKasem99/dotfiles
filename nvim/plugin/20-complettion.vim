set shortmess+=c
autocmd BufEnter * call ncm2#enable_for_buffer()
set completeopt=noinsert,menuone,noselect
" Use <TAB> to select the popup menu:
inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"
let g:jedi#completions_enabled = 0
let g:jedi#documentation_command = ""
let g:jedi#goto_command = "<c-d>"
let g:jedi#usages_command = "gu"
let g:float_preview#docked = 1
let g:float_preview#auto_close = 1

inoremap <silent> <expr> <CR> ncm2_ultisnips#expand_or("\<CR>", 'n')
" c-j c-k for moving in snippet
let g:UltiSnipsExpandTrigger		= "<Plug>(ultisnips_expand)"
let g:UltiSnipsJumpForwardTrigger	= "<c-j>"
let g:UltiSnipsJumpBackwardTrigger	= "<c-k>"
let g:UltiSnipsRemoveSelectModeMappings = 0
let g:ale_fixers = {
\   'python': ['black'],
\}

let g:LanguageClient_serverCommands = {
    \ 'go': ['gopls'],
    \ }

nnoremap <leader>lm :call LanguageClient_contextMenu()<CR>
nnoremap <leader>lh :call LanguageClient#textDocument_hover()<CR>
" Or map each action separately
nnoremap <silent>gd :call LanguageClient#textDocument_definition()<CR>
nnoremap <leader>r :call LanguageClient#textDocument_rename()<CR>
