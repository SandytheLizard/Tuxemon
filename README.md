![build-status](https://travis-ci.org/Tuxemon/Tuxemon.svg?branch=master)

Tuxemon
=========

Tuxemon is a free, open source monster-fighting RPG.

![screenshot](http://www.tuxemon.org/images/featurette-01.png)


Version
----

0.2


Requirements
-----------

Tuxemon uses a number of open source projects to work properly:

* *python* - version 2.7+
* *python-pygame* - python game library
* *python-pytmx* - python library to read Tiled Map Editor's TMX maps.


Installation
--------------

Ubuntu

```sh

sudo apt-get install python python-pygame python-pip python-imaging python-yapsy git
sudo pip install pytmx
git clone https://github.com/Tuxemon/Tuxemon.git
cd Tuxemon/tuxemon
./tuxemon.py

```

Mac OS X (Yosemite)

```sh
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew tap Homebrew/python
brew update
brew install python
brew install sdl sdl_image sdl_mixer sdl_ttf portmidi hg git
pip install pytmx
pip install pillow
pip install Yapsy
pip install hg+http://bitbucket.org/pygame/pygame
git clone https://github.com/Tuxemon/Tuxemon.git
cd Tuxemon/tuxemon
ulimit -n 10000; python tuxemon.py

```


Controls
--------------

##### Tuxemon
* *Arrow Keys* - Movement
* *Enter* - Select/activate
* *ESC* - Menu/Cancel


##### Map Editor

Use *Tiled* map editor: http://www.mapeditor.org/


License
----

GNU v3

Copyright (C) 2015 William Edwards <shadowapex@gmail.com>, Benjamin Bean <superman2k5@gmail.com>

This software is distributed under the GNU General Public Licence as published
by the Free Software Foundation.  See the file LICENCE for the conditions
under which this software is made available.  Tuxemon also contains code from
other sources.

