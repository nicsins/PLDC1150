print("\033[30m orange")
def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))

prGreen("Hello world")
prCyan("Im Cyan who are you")

from clint.textui import colored
print (colored.red('some warning message'))
print (colored.green('nicely done!'))

from sty import fg, bg, ef, rs, Rule

foo = fg.red + 'This is red text!' + fg.rs
bar = bg.blue + 'This has a blue background!' + bg.rs
baz = ef.italic + 'This is italic text' + rs.italic
qux = fg(201) + 'This is pink text using 8bit colors' + fg.rs
qui = fg(255, 10, 10) + 'This is red text using 24bit colors.' + fg.rs

# Add new colors:

fg.orange = Rule('rgb_fg', 255, 150, 50)

buf = fg.orange + 'Yay, Im orange.' + fg.rs


print(foo, bar, baz, qux, qui, buf, sep='\n')

from colorama import Fore, Style
import sys

class Highlight:
  def __init__(self, clazz, color):
    self.color = color
    self.clazz = clazz
  def __enter__(self):
    print(self.color, end="")
  def __exit__(self, type, value, traceback):
    if self.clazz == Fore:
      print(Fore.RESET, end="")
    else:
      assert self.clazz == Style
      print(Style.RESET_ALL, end="")
    sys.stdout.flush()

with Highlight(Fore, Fore.GREEN):
  print("this is highlighted")
print("this is not")

# Pure Python 3.x demo, 256 colors
# Works with bash under Linux

fg = lambda text, color: "\33[38;5;" + str(color) + "m" + text + "\33[0m"
bg = lambda text, color: "\33[48;5;" + str(color) + "m" + text + "\33[0m"

def print_six(row, format):
    for col in range(6):
        color = row*6 + col + 4
        if color>=0:
            text = "{:3d}".format(color)
            print (format(text,color), end=" ")
        else:
            print("   ", end=" ")

for row in range(-1,42):
    print_six(row, fg)
    print("",end=" ")
    print_six(row, bg)
    print()