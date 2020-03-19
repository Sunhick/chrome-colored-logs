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
        print("{dtc}{dateTime} {gc}{level:1.1} {fileName:30} {message}{reset}".format(
            dateTime = logLine.dateTime,
            level = logLine.logLevel,
            fileName = logLine.fileName,
            message = logLine.message,
            gc = fg("green"),
            reset = attr("reset"),
            dtc = fg("dark_gray"),
        ))

    def error(self, logLine: ChromeLogLine) -> None:
        # print(f'{fg("red")} {logLine} {attr("reset")}')
        print("{dtc}{dateTime} {rc}{level:1.1} {fileName:30} {message}{reset}".format(
            dateTime = logLine.dateTime,
            level = logLine.logLevel,
            fileName = logLine.fileName,
            message = logLine.message,
            reset = attr("reset"),
            rc = fg("red"),
            dtc = fg("dark_gray"),
        ))


    def warning(self, logLine: ChromeLogLine) -> None:
        # print(f'{fg("red")} {logLine} {attr("reset")}')
        print("{dtc}{dateTime} {yc}{level:1.1} {fileName:30} {message}{reset}".format(
            dateTime = logLine.dateTime,
            level = logLine.logLevel,
            fileName = logLine.fileName,
            message = logLine.message,
            reset = attr("reset"),
            yc = fg("yellow"),
            dtc = fg("dark_gray"),
        ))


    def fatal(self, logLine: ChromeLogLine) -> None:
        # print(f'{fg("red")} {logLine} {attr("reset")}')
        print("{dtc}{dateTime} {rc}{level:1.1} {fileName:30} {message}{reset}".format(
            dateTime = logLine.dateTime,
            level = logLine.logLevel,
            fileName = logLine.fileName,
            message = logLine.message,
            reset = attr("reset"),
            rc = fg("red"),
            dtc = fg("dark_gray"),
        ))

    def unknown(self, logLine: ChromeLogLine) -> None:
        # print(f'{fg("blue")} {logLine} {attr("reset")}')
        print("{dtc}{dateTime} {bc}{level:1.1} {fileName:30} {message}{reset}".format(
            dateTime = logLine.dateTime,
            level = logLine.logLevel,
            fileName = logLine.fileName,
            message = logLine.message,
            bc = fg("blue"),
            reset = attr("reset"),
            dtc = fg("dark_gray"),
        ))
