# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap,
# Dustin Wehr, Brian Harrington
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Summer 2017.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
from ConsoleController import ConsoleController
from GUIController import GUIController
from TOAHModel import TOAHModel

import time
NUM_CHEESES = 3

def tour_of_four_stools(model: TOAHModel, delay_btw_moves: float=0.5, 
                        console_animate: bool=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

       model - a TOAHModel with a tower of cheese on the first stool
                and three other empty stools
       console_animate - whether to use ConsoleController to animate the tour       
       delay_btw_moves - time delay between moves in seconds IF 
                         console_animate == True
                         no effect if console_animate == False
    """
    pass

if __name__ == '__main__':
    # DO NOT MODIFY THE CODE BELOW.
    
    four_stools = TOAHModel(4)    
    four_stools.fill_first_stool(number_of_cheeses = 8)
    
    tour_of_four_stools(four_stools, 
                        console_animate=False,                        
                        delay_btw_moves=0.5)
    
    print(four_stools.number_of_moves())
