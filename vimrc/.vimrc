set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

Plugin 'tpope/vim-fugitive'

Plugin 'ctrlpvim/ctrlp.vim'

Plugin 'bling/vim-airline'

Plugin 'Raimondi/delimitMate'

"Plugin 'octol/vim-cpp-enhanced-highlight'

Plugin 'Valloric/YouCompleteMe'

Plugin 'easymotion/vim-easymotion'

Plugin 'altercation/vim-colors-solarized'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

set laststatus=2 " status bar enabled at startup

let g:ycm_auto_trigger = 1  " change this for autocompletion

highlight YcmErrorSection guibg=#3f0000    " error highlighting off
highlight YcmWarningSection guibg=#3f0000  " error highlighting off

set tabstop=2 " two spaces when pressing tab
set shiftwidth=2 
set expandtab " spaces as tabs
set ai " auto indent

:set incsearch

syntax enable

if has('gui_running')
  " GUI is running or is about to start.
  set lines=999 columns=999
  set guifont=Monospace\ 12 
  set background=dark
  colorscheme solarized
else
  set t_Co=256
  "let g:solarized_termcolors=256
  set background=dark
  let g:solarized_termtrans = 1
  colorscheme solarized
endif

let g:ctrlp_working_path_mode = 0  " ctrl-p stays in its directory

set splitright
set splitbelow

nnoremap <silent> <C-Right> <c-w>l
nnoremap <silent> <C-Left> <c-w>h
nnoremap <silent> <C-Up> <c-w>k
nnoremap <silent> <C-Down> <c-w>j

let g:ycm_autoclose_preview_window_after_insertion = 1 " close scratch/preview_window in ycm
let g:ycm_autoclose_preview_window_after_completion = 1
