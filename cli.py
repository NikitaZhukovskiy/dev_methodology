import sys

from engine import run_game
from games import gcd

sys.dont_write_bytecode = True  # Магическая строка, отключающая кеш

def main():
    run_game(gcd)

if __name__ == '__main__':
    main()
