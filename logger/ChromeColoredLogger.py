#!/usr/bin/env python3

"""
ChromeColoredLogger.py

Colorize chrome logs for the terminal

"""

from .ChromeLogLine import ChromeLogLine

from typing import (Callable,
                    Dict,
                    DefaultDict)

from colored import (fg,
                     bg,
                     attr)

class ChromeColoredLogger(object):
    def __init__(self) -> None:
        self.fmtPicker # : Dict[str, Callable[[ChromeLogLine], None]] =
        {
            "INFO": self.info,
            "WARNING": self.warning,
            "ERROR": self.error,
            "FATAL": self.fatal,
        }

    def log(self, chromeLogLine: ChromeLogLine) -> None:
        if (chromeLogLine.logLevel in self.fmtPicker):
            self.fmtPicker[chromeLogLine.logLevel](chromeLogLine)
        else:
            self.unknown(chromeLogLine)

    def info(self, logLine: ChromeLogLine) -> None:
        # print(f'{fg("green")} {logLine} {attr("reset")}')
        print("{}{}{}".format(fg("green"), logLine, attr("reset")))

    def error(self, logLine: ChromeLogLine) -> None:
        # print(f'{fg("red")} {logLine} {attr("reset")}')
        print("{}{}{}".format(fg("red"), logLine, attr("reset")))

    def fatal(self, logLine: ChromeLogLine) -> None:
        # print(f'{fg("red")} {logLine} {attr("reset")}')
        print("{}{}{}".format(fg("red"), logLine, attr("reset")))

    def unknown(self, logLine: ChromeLogLine) -> None:
        # print(f'{fg("blue")} {logLine} {attr("reset")}')
        print("{}{}{}".format(fg("blue"), logLine, attr("reset")))
