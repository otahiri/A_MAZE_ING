import curses


def main(stdscr):
    stdscr.clear()
    stdscr.addstr(5, 10, "hello please")
    stdscr.refresh()
    stdscr.getkey()


curses.wrapper(main)
