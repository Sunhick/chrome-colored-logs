#!/usr/bin/env python3

"""
main.py:

Starter file for chrome colored logging

"""

__author__  = "Sunil"

from typing import List
from typing_extensions import Final
from .ChromeConstants import ChromeConstants

# : Final
kExpectedLogLineChunks = 5
# : Final
kParsedLogDelimiterLimit = 4

# : Final
kDateTime = 0
# : Final
kLogLevel = 1

class ChromeLogLine(object):
    def __init__(self, uncoloredLine: str) -> None:
        # : List[str]
        # expectedLogLevels = ["INFO", "ERROR", "WARNING", "FATAL"]
        # : List[str]
        parsedLine = uncoloredLine.split(ChromeConstants.kLogDelimiter,
                                                    kParsedLogDelimiterLimit)

        # [28474:775:0318/214434.970195:INFO:content_main_runner_impl.cc(974)] Chrome is running in full browser mode.
        # chrome log line doesn't follow
        if (len(parsedLine) != kExpectedLogLineChunks):
            raise Exception(uncoloredLine)

        pid, tid, rawDateTime, level, rest = parsedLine

        # if (level not in expectedLogLevels):
        #     raise Exception(uncoloredLine)

        _, self.pid = pid.split('[', maxsplit=1)
        self.tid = tid

        # Colorize the chrome log line
        # : str
        self.logLevel = level
        # : str
        self.dateTime = rawDateTime[1:]

        if (len(rest.split(']',  maxsplit=1)) != 2):
            raise Exception(uncoloredLine)

        # extract filename and message
        fileName, msg = rest.split(']', maxsplit=1)

        # : str
        self.fileName = fileName
        #: str
        self.message = msg

    def __str__(self) -> str:
        # return f"{self.dateTime} {self.logLevel} {self.fileName} {self.message}"
        return "{} {:1.1} {:30} {}".format(self.dateTime, self.logLevel, self.fileName, self.message)
