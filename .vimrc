syntax on 
set smartindent
set tabstop=4
set expandtab
set shiftwidth=4

highlight Pmenu ctermfg=15 ctermbg=0 guifg=#ffffff guibg=#000000

set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'Valloric/YouCompleteMe'

Plugin 'VundleVim/Vundle.vim'

Plugin 'tpope/vim-fugitive'

Plugin 'git://git.wincent.com/command-t.git'

Plugin 'rstacruz/sparkup', {'rtp' : 'vim/'}

call vundle#end()
filetype plugin indent on

let g:ycm_extra_conf_globlist = ['~/.vim/*', ]

let g:ycm_python_binary_path = 'python'

let g:ycm_filetype_whitelist={'*':1}



