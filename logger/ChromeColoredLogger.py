#!/usr/bin/env python3

"""
ChromeColoredLogger.py

Colorize chrome logs for the terminal

"""

from collections import defaultdict

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
        self.fmtPicker = defaultdict(lambda: self.unknown)
        self.fmtPicker["INFO"] = self.info
        self.fmtPicker["WARNING"] = self.warning
        self.fmtPicker["ERROR"] = self.error
        self.fmtPicker["FATAL"] = self.fatal
        self.msgFmt = "{dtc}{pid} {tid} {dateTime} {lc}{level:1.1} {fileName:30} {message}{reset}"

    def log(self, chromeLogLine: ChromeLogLine) -> None:
        self.fmtPicker[chromeLogLine.logLevel](chromeLogLine)

    def info(self, logLine: ChromeLogLine) -> None:
        print(self.msgFmt.format(
            pid = logLine.pid,
            tid = logLine.tid,
            dateTime = logLine.dateTime,
            level = logLine.logLevel,
            fileName = logLine.fileName,
            message = logLine.message,
            lc = fg("green"),
            reset = attr("reset"),
            dtc = fg("dark_gray"),
        ))

    def error(self, logLine: ChromeLogLine) -> None:
        print(self.msgFmt.format(
            pid = logLine.pid,
            tid = logLine.tid,
            dateTime = logLine.dateTime,
            level = logLine.logLevel,
            fileName = logLine.fileName,
            message = logLine.message,
            reset = attr("reset"),
            lc = fg("red"),
            dtc = fg("dark_gray"),
        ))


    def warning(self, logLine: ChromeLogLine) -> None:
        print(self.msgFmt.format(
            pid = logLine.pid,
            tid = logLine.tid,
            dateTime = logLine.dateTime,
            level = logLine.logLevel,
            fileName = logLine.fileName,
            message = logLine.message,
            reset = attr("reset"),
            lc = fg("yellow"),
            dtc = fg("dark_gray"),
        ))


    def fatal(self, logLine: ChromeLogLine) -> None:
        print(self.msgFmt.format(
            pid = logLine.pid,
            tid = logLine.tid,
            dateTime = logLine.dateTime,
            level = logLine.logLevel,
            fileName = logLine.fileName,
            message = logLine.message,
            reset = attr("reset"),
            lc = fg("red"),
            dtc = fg("dark_gray"),
        ))

    def unknown(self, logLine: ChromeLogLine) -> None:
        print(self.msgFmt.format(
            pid = logLine.pid,
            tid = logLine.tid,
            dateTime = logLine.dateTime,
            level = logLine.logLevel,
            fileName = logLine.fileName,
            message = logLine.message,
            lc = fg("blue"),
            reset = attr("reset"),
            dtc = fg("dark_gray"),
        ))
