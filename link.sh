#! /bin/bash
sudo ln -s $(pwd)/regolith-i3-config /etc/regolith/i3/config -f
ln -s $(pwd)/vimrc $HOME/.vimrc -f
ln -s $(pwd)/bashrc $HOME/.bashrc -f
ln -s $(pwd)/zshrc $HOME/.zshrc -f
