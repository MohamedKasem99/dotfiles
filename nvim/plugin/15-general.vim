let mapleader = ","

au BufNewFile,BufRead *.wiki set filetype=confluencewiki
au BufNewFile,BufRead *.go setlocal noet ts=4 sw=4 sts=4

autocmd BufWritePost .vimrc source $MYVIMRC
autocmd BufWritePost .vimrc filetype plugin indent on

set t_Co=256
set background=dark
filetype plugin on

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
let python_highlight_all=1
syntax on
set confirm
set hlsearch
set smartcase
set tabstop=4
set shiftwidth=4
set expandtab
set mouse=a
set guifont=Monospace\ 8
set fdm=indent
set foldlevel=30
set cursorline
set ignorecase
set wildmenu

if (has("nvim"))
    "For Neovim 0.1.3 and 0.1.4 < https://github.com/neovim/neovim/pull/2198 >
    let $NVIM_TUI_ENABLE_TRUE_COLOR=1
endif
"For Neovim > 0.1.5 and Vim > patch 7.4.1799 < https://github.com/vim/vim/commit/61be73bb0f965a895bfb064ea3e55476ac175162 >
"Based on Vim patch 7.4.1770 (`guicolors` option) < https://github.com/vim/vim/commit/8a633e3427b47286869aa4b96f2bfc1fe65b25cd >
" < https://github.com/neovim/neovim/wiki/Following-HEAD#20160511 >
if (has("termguicolors"))
    set termguicolors
endif

if has('gui_running')
    colorscheme onedark
else
    colorscheme onedark
endif
