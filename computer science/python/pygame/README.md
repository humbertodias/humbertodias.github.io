# PyGame

Learn Python by running Scripts



[https://www.pygame.org/docs/](https://www.pygame.org/docs/)


## Interpreter

<pre>

$ python
Python 3.2.3 (v3.2.3:3d0686d90f55, Apr 10 2012, 11:09:56) 
[GCC 4.0.1 (Apple Inc. build 5493)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
</pre>


## How to install

First install the Mercurial version control system:

<pre>brew install mercurial</pre>

Note: It didn't work for me at first. To test if it works for you, type:
hg
and press enter. If you don't get an error but a text that starts with Mercurial Distributed SCM, you have no problem. If you do get an error, type again
brew install mercurial
and press enter. Hopefully it will work.
Then do the same for the git version control system, which is needed by a 
dependency package:
<pre>
brew install git
</pre>
Now install all the dependencies of Pygame:
<pre>
brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
</pre>
And now, finally:

<pre>pip3 install hg+http://bitbucket.org/pygame/pygame</pre>

## How to import 

<pre>
>>> import pygame
</pre>

## Version

<pre>
>>> pygame.__version__
'1.9.2a0'
</pre>
