"""Command line entry point for subzero-benchmark."""

import argparse
import sys

from .benchmark import command


def build_parser():
    parser = argparse.ArgumentParser(
        prog="subzero-benchmark",
        description="Benchmark subtitle translation models with JSON and Markdown reports",
    )
    parser.add_argument("--config", required=True, help="Path to benchmark JSON configuration")
    parser.add_argument("--output", required=True, help="Path to output JSON report (Markdown is written alongside)")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    return command(args)


if __name__ == "__main__":
    sys.exit(main())
