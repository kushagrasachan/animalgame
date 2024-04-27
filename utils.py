import curses

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)


def setup_curses() -> None:
    """
    Setup curses to we can correctly use it
    """
    # locale.setlocale(locale.LC_ALL, "")
    curses.curs_set(0)  # don't show cursor
    logger.info(f"set up curses, suppressed cursor")
    curses.noecho()  # don't show what is writen by the user
    curses.cbreak()  # don't wait that the user presses Enter to read what they write

def revert_curses() -> None:
    """
    Reset curses to it's original settings, then quit
    """
    curses.curs_set(1)
    curses.nocbreak()
    curses.echo()
    curses.endwin()