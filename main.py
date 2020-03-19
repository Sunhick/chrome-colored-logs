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

# : ChromeColoredLogger
coloredLog = ChromeColoredLogger()

def quit(signum, frame) -> None:
    # TODO: might need threading.
    sys.exit(0)

def installSigTermHandler() -> None:
    signal.signal(signal.SIGTERM, quit)

def processLine(uncoloredLine: str) -> None:
    try:
        # : ChromeLogLine
        chromeLogLine = ChromeLogLine(uncoloredLine)
        coloredLog.log(chromeLogLine)
    except Exception as e:
        # log line doesn't follow standard chrome convention
        # dump it as it is to the console "unformatted"
        print(str(e))

def main(args: List[str]) -> None:
    installSigTermHandler()

    for rawLine in sys.stdin:
        processLine(rawLine.rstrip())

if __name__ == "__main__":
    main(sys.argv[1:])
