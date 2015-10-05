# Python Trainning

Learn Python by running Scripts

## Interpreter

<pre>

$ python
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World")
Hello World
>>> 

 
</pre>


## Hello World

<pre>
echo 'print("Hello World!")' > hello.py
</pre>

## How to run

<pre>
$ python hello.py
Hello World!
</pre>

## How to run as script

<pre>
echo '#!/usr/bin/env python

print("hello world!!")' > hello.sh
</pre>

and

<pre>
$ chmod +x hello.sh
$ ./hello.sh
Hello World!!
</pre>

## How to compile

<pre>
$ python -m py_compile hello.py
$ python hello.pyc
Hello World
</pre>