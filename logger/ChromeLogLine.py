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
kParsedLogDelimiterLimit = kExpectedLogLineChunks - 1 # Always one less than expected chunks

class ChromeLogLine(object):
    def __init__(self, uncoloredLine: str) -> None:
        # quick and fast way to eliminate if this log line doesn't need formatting.
        if (len(uncoloredLine) == 0 or uncoloredLine[0] != '['):
            raise Exception(uncoloredLine)

        # : List[str]
        parsedLine = uncoloredLine.split(ChromeConstants.kLogDelimiter,
                                                    kParsedLogDelimiterLimit)

        # Chrome log line format: [process_id:thread_id:time_stamp:log_level:file_name(line_number)] message
        # For instance:
        # [28474:775:0318/214434.970195:INFO:content_main_runner_impl.cc(974)] Chrome is running in full browser mode.

        # Parsed more? Probably log line doesn't adhere to expected format.
        if (len(parsedLine) != kExpectedLogLineChunks):
            raise Exception(uncoloredLine)

        pid, tid, rawDateTime, level, rest = parsedLine

        _, self.pid = pid.split('[', maxsplit=1)
        self.tid = tid

        # Colorize the chrome log line
        # : str
        self.logLevel = level
        # : str
        self.dateTime = rawDateTime[1:]

        fileNameMsg = rest.split(']',  maxsplit=1)
        if (len(fileNameMsg) != 2):
            raise Exception(uncoloredLine)

        # extract filename and message
        self.fileName, self.message = fileNameMsg


    def __str__(self) -> str:
        # return f"{self.dateTime} {self.logLevel} {self.fileName} {self.message}"
        return "{} {:1.1} {:30} {}".format(self.dateTime, self.logLevel, self.fileName, self.message)
