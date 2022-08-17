# onlinedot
A dot command line replacement wrapping graphviz.glitch.me online service


It is sometimes difficult or expensive to install graphviz libraries. This small
tool offers a replacement that can be used with python-graphviz to generate
diagrams. All you need to do is to set this file on the system path.

This is based on [graphviz.glitch.me](https://graphviz.glitch.me) by @olragon.

## Command line arguments

```
usage: dot [-h] [-K K] [-T T] [-o OUTPUT] [-O O] [-u] [-V] [instructions ...]

A simplified `dot` comment for directed graphs using `https://graphviz.glitch.me/` online graphviz service

positional arguments:
  instructions   dot script

options:
  -h, --help     show this help message and exit
  -K K           One of the 'dot', 'neato', 'fdp', 'twopi', 'circo' engine.
  -T T           One of the 'svg', 'png', 'jpg' output file format
  -o OUTPUT      Output filename
  -O O           Output filename with automatic extension
  -u, --url      Output online url to graph
  -V, --version  Display version information
```

## example usage

- generate a "Hello World" graph
```shell
echo "digraph G {Hello->World}" | dot.py -Tpng > hello.png
```

- using in python with `python-graphviz`
```python
import graphviz
print(graphviz.backend.version())
```
If this package is used, the latter should return something like
```dot - graphviz version 1.00.0 (graphviz.glitch.me)```
(Note that if you have graphviz installed in your system, it will be used.)
