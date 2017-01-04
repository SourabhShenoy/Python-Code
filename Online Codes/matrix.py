#!/usr/bin/env python

import fcntl, termios, struct, os
import random
import time, sys

def ioctl_GWINSZ(fd):
    ''' Get terminal size, by giving the proper file descriptor '''
    try:
        cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
    except:
        return None
    return cr
        
def get_terminal_size():
    ''' Get terminal size, or assume one '''
    
    # Either stdin (0), stdout (1), stderr (2)
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    
    # If not available in either of these
    # obtain the proper file descriptor
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass

    # If still not available
    # get the information from the environment, or assume a size
    if not cr:
        try:
            cr = (env['LINES'], env['COLUMNS'])
        except:
            cr = (25, 80)

    return int(cr[1]), int(cr[0])

def get_rand_num():
    ''' Get 0, 1, or 2 randomly for the matrix '''
    return random.randint(0, 2)

def get_line():
    '''
    Return a line with numbers
    that is as long as the width of the current terminal
    '''
    n = 0
    line = ''

    width, height = get_terminal_size()

    while n < width:
        width, height = get_terminal_size()
        line += str(get_rand_num())
        n += 1
    return line

def matrix():
    '''
    Create a pseudo-matrix of binary numbers scrolling in one horizontal line.
    It is inspired in how the code looks like in the movie The Matrix
    '''
    n = 0
    t = 0.50  # Seconds after which the line refreshes

    width, height = get_terminal_size()

    # Refresh the line until a keyboard interrupt
    while n < height:
        try:
            # Only '0' and '1', with random spaces in between
            binary_line = get_line().replace('2', ' ')
            
            # Write to the terminal,
            # returning the cursor to the beginning of the line
            sys.stdout.write('\033[1m\033[32m' + binary_line + '\033[0m' + '\r')
            sys.stdout.flush()
            time.sleep(t)
        except KeyboardInterrupt, EOFError:
            # Ctrl+C, Ctrl+D
            sys.stdout.write('\n' + '=== END ===' + '\n')
            sys.stdout.flush()
            time.sleep(1.0)
            break

matrix()