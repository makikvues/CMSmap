#!/usr/bin/python3
import signal
import sys

from cmsmap.lib.report import report
from cmsmap.main import main


def exit(signum, frame):
    signal.signal(signal.SIGINT, original_sigint)
    msg = "Interrupt caught. CMSmap exiting."
    report.error(msg)
    msg = "Bye! Quitting.. "
    report.message(msg)
    sys.exit(1)

if __name__ == "__main__":
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit)
    main()
