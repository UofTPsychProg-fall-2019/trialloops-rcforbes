#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
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
Step 2: Build a trial loop

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


#%% your loop here
# start by copying your one trial here, then identify what needs to be
# changed on every trial.  Likely your stimuli, but you might want to change a few things
ratingScale = visual.RatingScale(win, textColor = 'black', lineColor = 'black', choices=['cute', 'very cute', 'cutest'], pos=(0, -.45))
text = visual.TextStim(win, text='How cute is this picture?', color = 'black', pos=(0,-.4), height=.05)

# make a list or a pd.DataFrame that contains trial-specific info (stimulus, etc)
# e.g. stim = ['1.jpg','2.jpg','3.jpg']
imageList = ['Pics/Gizmo.jpg', 'Pics/Minnie.jpg', 'Pics/Artemis.jpg']
data = []

# make your loop
for image in imageList:
    x, y = ratingScale.win.size
    text = visual.SimpleImageStim(win=win, image=image, units='pix', pos=[0, y//7])
    ratingScale.reset()
    event.clearEvents()
    while ratingScale.noResponse:
         text.draw()
         ratingScale.draw()
         win.flip()
         if event.getKeys(['escape']):
             core.quit()
    data.append([image, ratingScale.getRating(), ratingScale.getRT()])


    
    # include your trial code in your loop but replace anything that should 
    # change on each trial with a variable that uses your iterater
    # e.g. thisStimName = stim[t]
    #      thisStim = visual.ImageStim(win, image=thisStimName ...)
    
    # if you're recording responses, be sure to store your responses in a list
    # or DataFrame which also uses your iterater!

close = visual.TextStim(win, color = 'black', height=.05, text="""Rachel Forbes PS5
Step 2: Build a trial loop

You have rated all my pets! 
Press escape to quit. """)

event.clearEvents()
close.draw()
win.flip()
if 'escape' in event.waitKeys():
    core.quit()

#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly
win.close()
