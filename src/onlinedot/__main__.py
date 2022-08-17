from .dot import (dot, __version__, add_to_path)


if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description="A simplified `dot` comment for directed graphs using `https://graphviz.glitch.me/` online graphviz service")
    parser.add_argument('instructions', type=str, nargs='*',
                        help='dot script')
    parser.add_argument('-K', dest='K', default="dot",
                        help="One of the 'dot', 'neato', 'fdp', 'twopi', 'circo' engine.")
    parser.add_argument('-T', dest='T', default="svg",
                        help="One of the 'svg', 'png', 'jpg' output file format")
    parser.add_argument('-o', dest='output', default="",
                        help="Output filename")
    parser.add_argument('-O', dest='O', default="",
                        help="Output filename with automatic extension")
    parser.add_argument('-u', '--url', dest='url', action="store_true", default=False,
                        help="Output online url to graph")
    parser.add_argument('-V', '--version', action="store_true", default=False,
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
        if args.T.lower() in ["svg",]:
            mode = "w"
        else:
            mode = "wb"
        with open(args.output, mode) as f:
            f.write(content)

    sys.exit(0)