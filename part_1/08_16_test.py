import test_mod                           # 1
from test_mod import magic                # 2
from test_mod import magicians as mag     # 3
import test_mod as m                      # 4
from test_mod import *                    # 5
                                          # |
names = ['Добрыня', 'Петя', 'Вася']       # |
                                          # |
test_mod.magicians(names)                 # 1
magic(names)                              # 2
mag(names)                                # 3
m.magicians(names)                        # 4
magicians(names)                          # 5
