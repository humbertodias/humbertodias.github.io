# Swift Trainning

Learn Swift by running Scripts

## Interpreter

<pre>

$ swift
Welcome to Apple Swift version 2.0 (700.0.59 700.0.72). Type :help for assistance.
 1> print(“Hello World”)
Hello World
 2>
 
</pre>


## Hello World

<pre>
echo 'print("Hello World!")' > hello.swift
</pre>

## How to run

<pre>
$ swift hello.swift
Hello World!
</pre>

## How to run as script

<pre>
echo '#!/usr/bin/env swift

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
$ swiftc hello.swift -o hello
$ ./hello
Hello World!!
</pre>