from util import trunc


class Output:

    def __init__(self, main, inbar, infobar, outbar):
        self.main = main
        self.inbar = inbar
        self.infobar = infobar
        self.outbar = outbar

    @staticmethod
    def addstr(win, string):
        """
        Replace the contents of a window with a new string.
          Not for anything where position matters.

        Arguments:
        win: Window on which to display the string.
        string: String to be displayed.
        """
        win.erase()
        win.addstr(trunc(string, win.getmaxyx()[1]))
        win.refresh()

    @staticmethod
    def reset_now_playing():
        try:
            addstr(self.infobar, 'Now playing: None')
        except NameError:
            pass

    @staticmethod
    def show_input_prompt():
        try:
            addstr(self.inbar, '> ')
        except NameError:
            pass

    @staticmethod
    def get_input():
        try:
            s = self.inbar.getstr().decode('utf-8')
            self.inbar.deleteln()
            return s
        except NameError:
            pass

    @staticmethod
    def outbar_msg(msg):
        try:
            addstr(self.outbar, msg)
        except NameError:
            pass

    @staticmethod
    def infobar_msg(msg):
        try:
            addstr(self.infobar, msg)
        except NameError:
            pass

    @staticmethod
    def outbar_erase():
        try:
            self.outbar.erase()
            self.outbar.refresh()
        except NameError:
            pass

    @staticmethod
    def show_help():
        """Display basic self commands."""
        try:
            main.erase()
            main.addstr(
                """
                Commands:
                s/search search-term: Search for search-term
                e/expand 123: Expand item number 123
                p/play: Play current queue
                p/play s: Shuffle and play current queue
                p/play 123: Play item number 123
                q/queue: Show current queue
                q/queue 123:  Add item number 123 to queue
                q/queue 1 2 3:  Add items 1, 2, 3 to queue
                q/queue c:  Clear the current queue
                w/write file-name: Write current queue to file file-name
                r/restore file-name: Replace current queue with playlist from file-name
                h/help: Show this help message
                Ctrl-C: Exit self
                """
            )
            main.refresh()
        except NameError:
            pass

    @staticmethod
    def error_msg(msg):
        """
        Displays an error message.

        Arguments:
        msg: Message to be displayed.
        """
        try:
            addstr(self.outbar,
                   'Error: ' + msg + ' Enter \'h\' or \'help\' for help.')
        except NameError:
            pass

    @staticmethod
    def help_prompt():
        try:
            addstr(self.infobar, 'Enter \'h\' or \'help\' if you need help.')
        except NameError:
            pass

    @staticmethod
    def welcome_msg():
        try:
            main.addstr(5, int(crs.COLS/2) - 9, 'Welcome to self!')
        except NameError:
            pass
