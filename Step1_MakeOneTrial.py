#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 1
Use this template script to present one trial with your desired structure
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height')

instr = visual.TextStim(win, color = 'black', height=.05, text="""Rachel Forbes PS5 
Step 1: Make one trial

Hope you like cute pets! In this experiment you will be rating different pets on cuteness.

To make a rating click somewhere on the line. To accept your rating, either press 'enter' or click the glowing button.

Press any key to begin (or escape to quit).""")

event.clearEvents()
instr.draw()
win.flip()
if 'escape' in event.waitKeys():
    core.quit()

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
#trialClock = core.Clock()

#%% up to you!
# this is where you build a trial that you might actually use one day!
# just try to make one trial ordering your lines of code according to the 
# sequence of events that happen on one trial
# if you're stuck you can use the responseExercise.py answer as a starting point 

# maybe start by making stimulus objects (e.g. myPic = visual.ImageStim(...))  
ratingScale = visual.RatingScale(win, textColor = 'black', lineColor = 'black', choices=['cute', 'very cute', 'cutest'], pos=(0, -.45))
text = visual.TextStim(win, text='How cute is this picture?', color = 'black', pos=(0,-.4), height=.05)
x, y = ratingScale.win.size
image1 = visual.ImageStim(win=win, image='Pics/Gizmo.jpg', units='pix',pos=[0, y//15])

# then draw all stimuli and flip window
while ratingScale.noResponse:
    text.draw()
    ratingScale.draw()
    image1.draw()
    win.flip()
    if event.getKeys(['escape']):
        core.quit()

core.wait(0.2)

# then record your responses
data= [ratingScale.getRating(), ratingScale.getRT()]

close = visual.TextStim(win, color = 'black', height=.05, text="""Rachel Forbes PS5
Step 1: Make one trial

You have rated one pet!
Press escape to quit. """)

close.draw()
win.flip()
if 'escape' in event.waitKeys():
    core.quit()
#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

win.close()