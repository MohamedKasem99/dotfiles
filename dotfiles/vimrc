"set spell
" set relativenumber
set number
set showmatch
set wrap
set ttyfast
set backspace=indent,eol,start
set laststatus=2
set showmode
set showcmd
set matchpairs+=<:>
set autoindent	
set smartindent
syntax on
set confirm
set hlsearch
set smartcase
set tabstop=4
set shiftwidth=4
set expandtab
set mouse=a

colo monokai
imap <C-c> <ESC>


set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'tell-k/vim-autopep8'
Plugin 'psf/black'
" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
Plugin 'tpope/vim-fugitive'
Plugin 'Valloric/YouCompleteMe'
Plugin 'preservim/nerdtree'
Plugin 'itchyny/lightline.vim'
Plugin 'haya14busa/is.vim'
Plugin 'BurntSushi/ripgrep'
Plugin 'junegunn/fzf'
Plugin 'junegunn/fzf.vim'
" plugin from http://vim-scripts.org/vim/scripts.html
" Plugin 'L9'
" Git plugin not hosted on GitHub
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
" Plugin 'ascenator/L9', {'name': 'newL9'}

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

" NERDTree Configurations
" autocmd vimenter * NERDTree
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists("s:std_in") | exe 'NERDTree' argv()[0] | wincmd p | ene | exe 'cd '.argv()[0] | endif
map <C-n> :NERDTreeToggle<CR>
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" BLACK Formatter Plugin configs 
autocmd BufWritePre *.py execute ':Black'

set statusline=%{FugitiveStatusline()}%F%m%r%h%w\ \ [TYPE=%Y]\ [POS=%l,%v]


" Adding git to lightline (statusline)
let gilightline = {
      \ 'colorscheme': 'wombat',
      \ 'active': {
      \   'left': [ [ 'mode', 'paste' ],
      \             [ 'gitbranch', 'readonly', 'filename', 'modified' ] ]
      \ },
      \ 'component_function': {
      \   'gitbranch': 'FugitiveHead'
      \ },
      \ }




" My keymappings 
nnoremap <Leader>r :%s///gc<LEFT><LEFT><LEFT>
xnoremap <Leader>r :%s///gc<LEFT><LEFT><LEFT>
xnoremap * y/<C-f>p<CR>
nnoremap <C-p> :Files<CR>
nnoremap <C-f> :Rg<CR>
nnoremap <C-d> :YcmCompleter GoToDefinition<CR>
nnoremap <C-e> :norm O__import__("ipdb").set_trace()<ESC>
