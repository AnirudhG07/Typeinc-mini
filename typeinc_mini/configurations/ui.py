import curses, time

def setup_window(stdscr):
    curses.initscr()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    start_y = 2 
    start_x = 17  
    # Create a new window for the box
    height, width = stdscr.getmaxyx()
    box_width=width//2-2
    box_height=height//2-2
    monitor_l2 = curses.newwin(box_height+1, box_width+2, start_y, start_x-1)
    win = curses.newwin(box_height, box_width, start_y, start_x)

    # Draw a box around the new window
    monitor_l2.box()
    monitor_l2.refresh()
    win.box()
    title = "TERMINAL TYPING SPEED TEST"
    win.addstr(start_y - 2, start_x + box_width // 3 - len(title)//2-3, title, curses.color_pair(5) | curses.A_BOLD)
    win.scrollok(True) # Enable scrolling

    options = curses.newwin(13, 30, 7, box_width+3 + start_x -1) # height, width, y, x
    options.addstr(1, 10, f"OPTIONS", curses.color_pair(4) | curses.A_BOLD)
    options.addstr(2, 1, "="*30, curses.color_pair(1))
    options.addstr(3, 1, "> Press Ctrl C to exit", curses.color_pair(5))
    options.addstr(4, 1, "> Press Ctrl R to restart", curses.color_pair(5))
    options.addstr(5, 1, "> Press Backspace to delete", curses.color_pair(5))
    options.addstr(6, 1, "> Don't mess with arrow keys", curses.color_pair(5))
    options.addstr(7, 1, "'. . .' mean To be Continued", curses.color_pair(5))
    options.addstr(8, 1, "                     ", curses.color_pair(5))
    options.addstr(9, 10, "TIMER", curses.color_pair(4) | curses.A_BOLD)
    options.addstr(10, 1, "="*30, curses.color_pair(1))
    options.addstr(11, 7, f" {0:.2f} second", curses.color_pair(5))
    # Create a new thread for the ticking clock
    
    options.box()
    options.refresh()

    return win, box_width, box_height

