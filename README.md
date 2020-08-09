# games
some kids games

#install pygame 
#install on Linux
#Debian/Ubuntu/Mint
sudo apt-get install python3-pygame
sudo apt-get install python3-pygame

#Mac
python3 -m pip install -U pygame==2.0.0.dev6 --user
#virtualenv
# create a virtualenv called 'anenv' and use it.
python3 -m virtualenv anenv
. ./anenv/bin/activate
# venvdotapp helps the python be a mac 'app'. So the pygame window can get focus.
python -m pip install venvdotapp
venvdotapp
python -m pip install pygame

# See if pygame works with the oo module, and the aliens example.
python -m pygame.examples.aliens
