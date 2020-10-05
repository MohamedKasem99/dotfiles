#! /usr/bin/python3
import os
from sys import exit

HOME = os.environ.get("HOME", "/home")

os.chdir("dotfiles")

file_guide = {
    "vimrc": "{}/.vimrc".format(HOME),
    "bashrc": "{}/.bashrc".format(HOME),
    "zshrc": "{}/.zshrc".format(HOME),
    "regolith-i3-config": "{}/.config/regolith/i3/config".format(HOME),
}


def display_warnings():
    files_not_included = filter(lambda x: x not in file_guide.keys(), os.listdir())
    for not_included in files_not_included:
        print(
            "[!!!] File: {} is in the repo but has no specified destination".format(
                not_included
            )
        )


def check_target_path(target):
    parent_dir = os.path.dirname(target)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    if os.path.exists(target):
        os.remove(target)


display_warnings()
for src, dest in file_guide.items():
    if os.path.exists(src):
        check_target_path(dest)
        os.symlink(os.path.join(os.getcwd(), src), dest)
        print("[+] Created symlink {} -> {}".format(src, dest))
    else:
        print("[!] Couldn't find file: {}".format(src))
