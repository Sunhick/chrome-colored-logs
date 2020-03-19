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
        # : Dict[str, Callable[[ChromeLogLine], None]]
        self.fmtPicker = {
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
        print("{dateTime} {gc}{level:1.1} {fileName:30} {message}{reset}".format(
            dateTime = logLine.dateTime,
            level = logLine.logLevel,
            fileName = logLine.fileName,
            message = logLine.message,
            gc = fg("green"),
            reset = attr("reset")
        ))

    def error(self, logLine: ChromeLogLine) -> None:
        # print(f'{fg("red")} {logLine} {attr("reset")}')
        print("{dateTime} {rc}{level:1.1} {fileName:30} {message}{reset}".format(
            dateTime = logLine.dateTime,
            level = logLine.logLevel,
            fileName = logLine.fileName,
            message = logLine.message,
            reset = attr("reset"),
            rc = fg("red"),
        ))


    def warning(self, logLine: ChromeLogLine) -> None:
        # print(f'{fg("red")} {logLine} {attr("reset")}')
        print("{dateTime} {yc}{level:1.1} {fileName:30} {message}{reset}".format(
            dateTime = logLine.dateTime,
            level = logLine.logLevel,
            fileName = logLine.fileName,
            message = logLine.message,
            reset = attr("reset"),
            yc = fg("yellow"),
        ))


    def fatal(self, logLine: ChromeLogLine) -> None:
        # print(f'{fg("red")} {logLine} {attr("reset")}')
        print("{dateTime} {rc}{level:1.1} {fileName:30} {message}{reset}".format(
            dateTime = logLine.dateTime,
            level = logLine.logLevel,
            fileName = logLine.fileName,
            message = logLine.message,
            reset = attr("reset"),
            rc = fg("red"),
        ))

    def unknown(self, logLine: ChromeLogLine) -> None:
        # print(f'{fg("blue")} {logLine} {attr("reset")}')
        print("{}{}{}".format(fg("blue"), logLine, attr("reset")))
        print("{dateTime} {bc}{level:1.1} {fileName:30} {message}{reset}".format(
            dateTime = logLine.dateTime,
            level = logLine.logLevel,
            fileName = logLine.fileName,
            message = logLine.message,
            bc = fg("blue"),
            reset = attr("reset")
        ))
