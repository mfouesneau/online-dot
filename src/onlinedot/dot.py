#!/usr/bin/env python3
"""Wrapper to graphviz.glitch.me as a dot command line replacement.

It is sometimes difficult or expensive to install graphviz libraries. This small
tool offers a replacement that can be used with python-graphviz to generate
diagrams. All you need to do is to set this file on the system path.

example usage

- generate the snakemake graph of the current directory
shell> snakemake --dag 2> /dev/null | ./dot.py -Tsvg -O test

- set path to use with python-graphviz (use first argument to replace local dot command)
python> import dot; add_to_path(first=False);
python> import graphviz; print(graphviz.backend.version())
"""
import sys
import requests

__version__ = "dot - graphviz version 1.00.0 (graphviz.glitch.me)"


def add_to_path(first: bool = False):
    """ Add the location of this file to the environment PATH.

    Parameters
    ----------
    first: bool
        add first to the path otherwise at the end.
    """
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if first:
        os.environ["PATH"] = dir_path + os.pathsep + os.environ["PATH"]
        print(f'path updated as PATH={dir_path}{os.pathsep}${{PATH}}')
    else:
        os.environ["PATH"] += os.pathsep + dir_path
        print(f'path updated as PATH=${{PATH}}{os.pathsep}{dir_path}')


def dot(graph: str,
        K: str = 'dot',
        T: str = 'svg',
        url_only: bool = False,
        **kwargs):
    """ A wrapper to graphviz.glitch.me
        as a simplified replacement to graphviz dot local command

        Parameters
        ----------
        K: str
        Engine in
            dot — filter for drawing directed graphs
            neato — filter for drawing undirected graphs
            twopi — filter for radial layouts of graphs
            circo — filter for circular layout of graphs
            fdp — filter for drawing undirected graphs
            patchwork — filter for squarified tree maps
            osage — filter for array-based layouts
        url_only: bool
            return the online editor url only

        Returns
        -------
        graph output rendering
    """
    engines = ['dot', 'neato', 'fdp', 'twopi', 'circo']
    if K not in engines:
        raise ValueError(f"the engine (K) needs to be in {engines}")

    encoded = requests.utils.quote(''.join(graph))
    base_url = f'https://graphviz.glitch.me/graphviz?layout={K:s}&format={T:s}&mode=download&graph='
    final_url = (base_url + encoded)
    if url_only:
        return final_url
    content = requests.get(final_url).content
    try:
        return content.decode()
    except UnicodeDecodeError:
        return content


def main():
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description=
        "A simplified `dot` comment for directed graphs using `https://graphviz.glitch.me/` online graphviz service"
    )
    parser.add_argument('instructions', type=str, nargs='*', help='dot script')
    parser.add_argument(
        '-K',
        dest='K',
        default="dot",
        help="One of the 'dot', 'neato', 'fdp', 'twopi', 'circo' engine.")
    parser.add_argument(
        '-T',
        dest='T',
        default="svg",
        help="One of the 'svg', 'png', 'jpg' output file format")
    parser.add_argument('-o',
                        dest='output',
                        default="",
                        help="Output filename")
    parser.add_argument('-O',
                        dest='O',
                        default="",
                        help="Output filename with automatic extension")
    parser.add_argument('-u',
                        '--url',
                        dest='url',
                        action="store_true",
                        default=False,
                        help="Output online url to graph")
    parser.add_argument('-V',
                        '--version',
                        action="store_true",
                        default=False,
                        help="Display version information")

    args = parser.parse_args()

    if args.version:
        print(__version__)
        sys.exit(0)

    txt = ' '.join(args.instructions).encode('utf8')
    if not txt:
        txt = sys.stdin.read()

    content = dot(txt, K=args.K, T=args.T, url_only=args.url)

    if args.O:
        args.output = args.O + "." + args.T

    if args.output in [None, ""] or args.url:
        print(content)
    else:
        if args.T.lower() in [
                "svg",
        ]:
            mode = "w"
        else:
            mode = "wb"
        with open(args.output, mode) as f:
            f.write(content)

    sys.exit(0)


if __name__ == "__main__":
    main()
