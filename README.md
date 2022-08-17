# online-dot
A dot command line replacement wrapping graphviz.glitch.me online service


It is sometimes difficult or expensive to install graphviz libraries. This small
tool offers a replacement that can be used with python-graphviz to generate
diagrams. All you need to do is to set this file on the system path.

This is based on [graphviz.glitch.me](https://graphviz.glitch.me) by @olragon.

## example usage

- generate the snakemake graph of the current directory
```shell
echo "digraph G {Hello->World}" | dot.py -Tpng > hello.png
```

- set path to use with python-graphviz (use first argument to replace local dot command)
```python
from onlinedot import add_to_path
add_to_path(first=False)
import graphviz
print(graphviz.backend.version())
```
The latter should return something like
```dot - graphviz version 1.00.0 (graphviz.glitch.me)```
