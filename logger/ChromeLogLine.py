#!/usr/bin/env python3

"""
main.py:

Starter file for chrome colored logging

"""

__author__  = "Sunil"

from typing import List
from typing_extensions import Final
from .ChromeConstants import ChromeConstants

kExpectedLogLineChunks: Final = 3
kParsedLogDelimiterLimit: Final = 2
kLogLevel: Final = 1

class ChromeLogLine(object):
    def __init__(self, uncoloredLine: str) -> None:
        parsedLine: List[str] = uncoloredLine.split(ChromeConstants.kLogDelimiter,
                                                    kParsedLogDelimiterLimit)

        # chrome log line doesn't follow
        if (len(parsedLine) != kExpectedLogLineChunks):
            print(uncoloredLine)
            return

        # Colorize the chrome log line
        logLevel: str = parsedLine[kLogLevel]

        self.dateTime = ""
        self.logLevel = ""
        self.fileName = ""
        self.message = ""

    def str(self):
        return f""
