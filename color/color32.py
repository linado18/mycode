#!/usr/bin/env python3
"""Alta3 Research || Author RZFeeser@alta3.com
Learning how to use functions"""

## Installs the crayons package.
## python3 -m pip install crayons
## import statements ALWAYS go up top
import crayons


def main():
    """run time code. Always indent under function"""

    # print 'red string' in red
    print(crayons.red('red string', bold=True))

    # print 'yellow string' in yellow
    print(crayons.yellow('yellow string', bold=True))

    # print 'magenta string' in magenta
    print(crayons.magenta('magenta string', bold=True))

    # print 'white string' in white
    print(crayons.white('white string', bold=True))

    # print 'black string' in black
    print(crayons.black('black string', bold=True)) 

    # print 'green string' in green
    print(crayons.green('green string', bold=True))

    # print 'cyan string' in cyan
    print(crayons.cyan('cyan string', bold=True))

    # print 'blue string' in blue
    print(crayons.blue('blue string', bold=True))

# this condition is only true if our script is run directly
# it is NOT true if our code is imported into another script
if __name__ == "__main__":
    main()

