#!/usr/bin/env python3

"""
main.py:

Starter file for chrome colored logging

"""

__author__  = "Sunil"

import sys
import signal

from typing import List
from typing_extensions import Final

from logger import *

def quit(signum, frame) -> None:
    # TODO: might need threading.
    sys.exit(0)

def installSigTermHandler() -> None:
    signal.signal(signal.SIGTERM, quit)

def main(args: List[str]) -> None:
    installSigTermHandler()
    colorize: ChromeColoredLogger = ChromeColoredLogger()

    for rawLine in sys.stdin:
        uncoloredLine: str = rawLine.strip()
        chromeLogLine: ChromeLogLine = ChromeLogLine(uncoloredLine)
        print(uncoloredLine)

if __name__ == "__main__":
    main(sys.argv[1:])
