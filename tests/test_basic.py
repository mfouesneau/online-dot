""" Adding basic tests """


def test_basic_run():
    """
    Basic hello world diagram to stdout
    """
    from onlinedot import dot
    r = dot("digraph G {Hello->World}", T='svg')
    assert r not in [None, '']
