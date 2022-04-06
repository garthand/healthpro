#!/bin/bash

# Clone pyenv to allow us to install multiple versions of Python
# Note this command is for Debian-based Linux distributions
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
# Install the build dependencies so pyenv can build other versions of python
sudo apt install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev -y
# Set up environment for pyenv
# the sed invocation inserts the lines at the start of the file
# after any initial comment lines
sed -Ei -e '/^([^#]|$)/ {a \
export PYENV_ROOT="$HOME/.pyenv"
a \
export PATH="$PYENV_ROOT/bin:$PATH"
a \
' -e ':a' -e '$!{n;ba};}' ~/.profile
echo 'eval "$(pyenv init --path)"' >>~/.profile

echo 'eval "$(pyenv init -)"' >> ~/.bashrc
# Reload shell
exec $SHELL
# Use pyenv to install Python 3.7.11
pyenv install 3.7.11
# Make Python 3.7.11 the default option when invoking python3
pyenv global 3.7.11
# Creation a virtual environment to install kivy dependencies
python3 -m venv kivy_env
# Activate the kivy venv
source kivy_env/bin/activate
# Install kivy's dependencies. Not matplotlib needs to be version 3.1.3,
# the latest release has a bug that causes it to have issues with matplotlib
pip3 install kivy kivymd kivy-garden matplotlib==3.1.3
# I needed this when running a few test kivy apps, it may be a common dependency
sudo apt install xclip -y
# I couldn't execute the garden exectuable by default, I needed to change its permissions
chmod 744 kivy_env/bin/garden
# Use garden to install graph and matplotlib (again)
garden install graph
garden install matplotlib
# For kivy apps, the .py file can be any name
# However, the .kv file should be reprodexample3.kv in the StackExchange example.
# The name is drawn from the class that starts the app per https://kivy.org/doc/stable/tutorials/firstwidget.html
