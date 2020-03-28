#!/usr/bin/env python3

"""
main.py:

Starter file for chrome colored logging

"""

__author__  = "Sunil"

import sys

from typing import List
from typing_extensions import Final

from logger import *

# : ChromeColoredLogger
coloredLog = ChromeColoredLogger()

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
    for rawLine in sys.stdin:
        processLine(rawLine.rstrip('\n'))

if __name__ == "__main__":
    main(sys.argv[1:])
