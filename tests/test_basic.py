import pytest
from onlinedot import dot

def check_basic_run():
    """
    Basic hello world diagram
    """
    r = dot("digraph G {Hello->World}", T='svg')
    assert r not in [None, '']

