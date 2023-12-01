from datetime import datetime

import os
import sys

session = os.environ["AOC_COOKIE"]


if len(sys.argv) > 1:
    day = sys.argv[1]
else:
    day = datetime.now().day


os.system(
    f'curl --cookie "session={session}" https://adventofcode.com/2023/day/{day}/input > day_{day}.txt'
)
