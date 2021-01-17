#! /usr/bin/python3
import os
import sys

HOME = os.environ.get("HOME")
if not HOME:
    print("HOME env variable is not set. Exitting")
    sys.exit(1)

FILE_GUIDE = {
    "vimrc": "{}/.vimrc".format(HOME),
    "bashrc": "{}/.bashrc".format(HOME),
    "zshrc": "{}/.zshrc".format(HOME),
    "regolith-i3-config": "{}/.config/regolith/i3/config".format(HOME),
}


def check_target_path(target):
    parent_dir = os.path.dirname(target)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    if os.path.exists(target) or os.path.islink(target):
        os.remove(target)


def main():
    for src, dest in FILE_GUIDE.items():
        src_path = f"{HOME}/dotfiles/dotfiles/{src}"
        if os.path.exists(src_path):
            check_target_path(dest)
            os.symlink(src_path, dest)
            print("[+] Created symlink {} -> {}".format(src, dest))
        else:
            print("[!] Couldn't find file: {}".format(src))


if __name__ == "__main__":
    main()
