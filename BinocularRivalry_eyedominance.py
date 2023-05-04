#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Aralık 16, 2022, at 10:58
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'BR_St_eyedominance_2'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data' + os.sep + u'psychopy_data_' + data.getDateStr()

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Oğuz Kaan\\OneDrive\\tezson\\kodlar\\BR_St_eyedominance_2.py',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

redGrat = np.zeros([256,256,3],'f')#the f indicates we want floats 
redGrat[:,:,0] = visual.filters.makeGrating(256,gratType='sin')
redGrat[:,:,1] = -1.0 
redGrat[:,:,2] = -1.0

greenGrat = np.zeros([256,256,3],'f')#the f indicates we want floats 
greenGrat[:,:,0] = -1.0
greenGrat[:,:,1] =  visual.filters.makeGrating(256,gratType='sin')
greenGrat[:,:,2] = -1.0


# --- Initialize components for Routine "null" ---
fixation_left = visual.ShapeStim(
    win=win, name='fixation_left', vertices='cross', units = 'deg', 
    size=(0.8, 0.8),
    ori=0.0, pos=(-10, 0.0), anchor='center',
    lineWidth=0.001,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[1.0000, 1.0000, 1.0000],
    opacity=None, depth=0.0, interpolate=True)
fixation_right = visual.ShapeStim(
    win=win, name='fixation_right', vertices='cross', units = 'deg',
    size=(0.8, 0.8),
    ori=0.0, pos=(10, 0.0), anchor='center',
    lineWidth=0.001,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[1.0000, 1.0000, 1.0000],
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "eye_dominance" ---
rivalry1_gabor_R = visual.GratingStim(
    win=win, units = 'deg',
    tex=redGrat, mask='gauss', anchor='center',
    ori=90.0, pos=(-10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=-1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0, maskParams = {'sd': 3})
rivalry1_gabor_G = visual.GratingStim(
    win=win, units = 'deg',
    tex=greenGrat, mask='gauss', anchor='center',
    ori=0, pos=(10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0, maskParams = {'sd': 3})
interv_gabor_R = visual.GratingStim(
    win=win, units = 'deg',
    tex=redGrat, mask='gauss', anchor='center',
    ori=90.0, pos=(-10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0, maskParams = {'sd': 3})
interv_gabor_G = visual.GratingStim(
    win=win, units = 'deg',
    tex=greenGrat, mask='gauss', anchor='center',
    ori=0, pos=(10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0, maskParams = {'sd': 3})
rivalry2_gabor_R = visual.GratingStim(
    win=win, units = 'deg',
    tex=redGrat, mask='gauss', anchor='center',
    ori=90.0, pos=(-10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0, maskParams = {'sd': 3})
rivalry2_gabor_G = visual.GratingStim(
    win=win, units = 'deg',
    tex=greenGrat, mask='gauss', anchor='center',
    ori=0, pos=(10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0, maskParams = {'sd': 3})
R_fixation_rivalry = visual.ShapeStim(
    win=win, name='R_fixation_rivalry', vertices='cross', units = 'deg',
    size=(0.8, 0.8),
    ori=0.0, pos=(10, 0.0), anchor='center',
    lineWidth=0.001,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[1.0000, 1.0000, 1.0000],
    opacity=None, depth=-6.0, interpolate=True)
L_fixation_rivalry = visual.ShapeStim(
    win=win, name='L_fixation_rivalry', vertices='cross', units = 'deg',
    size=(0.8, 0.8),
    ori=0.0, pos=(-10, 0.0), anchor='center',
    lineWidth=0.001,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[1.0000, 1.0000, 1.0000],
    opacity=None, depth=-7.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "null" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
nullComponents = [fixation_left, fixation_right]
for thisComponent in nullComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "null" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_left* updates
    if fixation_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_left.frameNStart = frameN  # exact frame index
        fixation_left.tStart = t  # local t and not account for scr refresh
        fixation_left.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_left, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fixation_left.started')
        fixation_left.setAutoDraw(True)
    if fixation_left.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_left.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            fixation_left.tStop = t  # not accounting for scr refresh
            fixation_left.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_left.stopped')
            fixation_left.setAutoDraw(False)
    
    # *fixation_right* updates
    if fixation_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_right.frameNStart = frameN  # exact frame index
        fixation_right.tStart = t  # local t and not account for scr refresh
        fixation_right.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_right, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fixation_right.started')
        fixation_right.setAutoDraw(True)
    if fixation_right.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_right.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            fixation_right.tStop = t  # not accounting for scr refresh
            fixation_right.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_right.stopped')
            fixation_right.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in nullComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "null" ---
for thisComponent in nullComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# set up handler to look after randomisation of conditions etc
eye_dominance_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BR_eyedominance/conditions_BREDGD.xlsx'),
    seed=None, name='eye_dominance_loop')
thisExp.addLoop(eye_dominance_loop)  # add the loop to the experiment
thisEye_dominance_loop = eye_dominance_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEye_dominance_loop.rgb)
if thisEye_dominance_loop != None:
    for paramName in thisEye_dominance_loop:
        exec('{} = thisEye_dominance_loop[paramName]'.format(paramName))

for thisEye_dominance_loop in eye_dominance_loop:
    currentLoop = eye_dominance_loop
    # abbreviate parameter names if possible (e.g. rgb = thisEye_dominance_loop.rgb)
    if thisEye_dominance_loop != None:
        for paramName in thisEye_dominance_loop:
            exec('{} = thisEye_dominance_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "eye_dominance" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    rivalry1_gabor_R.setContrast(ContrastRed)
    rivalry1_gabor_G.setContrast(ContrastGreen)
    rivalry2_gabor_R.setContrast(ContrastRed)
    rivalry2_gabor_G.setContrast(ContrastGreen)
    # keep track of which components have finished
    eye_dominanceComponents = [rivalry1_gabor_R, rivalry1_gabor_G, interv_gabor_R, interv_gabor_G, rivalry2_gabor_R, rivalry2_gabor_G, R_fixation_rivalry, L_fixation_rivalry]
    for thisComponent in eye_dominanceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "eye_dominance" ---
    while continueRoutine and routineTimer.getTime() < 21.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rivalry1_gabor_R* updates
        if rivalry1_gabor_R.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            rivalry1_gabor_R.frameNStart = frameN  # exact frame index
            rivalry1_gabor_R.tStart = t  # local t and not account for scr refresh
            rivalry1_gabor_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rivalry1_gabor_R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rivalry1_gabor_R.started')
            rivalry1_gabor_R.setAutoDraw(True)
        if rivalry1_gabor_R.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rivalry1_gabor_R.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                rivalry1_gabor_R.tStop = t  # not accounting for scr refresh
                rivalry1_gabor_R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rivalry1_gabor_R.stopped')
                rivalry1_gabor_R.setAutoDraw(False)
        
        # *rivalry1_gabor_G* updates
        if rivalry1_gabor_G.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            rivalry1_gabor_G.frameNStart = frameN  # exact frame index
            rivalry1_gabor_G.tStart = t  # local t and not account for scr refresh
            rivalry1_gabor_G.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rivalry1_gabor_G, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rivalry1_gabor_G.started')
            rivalry1_gabor_G.setAutoDraw(True)
        if rivalry1_gabor_G.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rivalry1_gabor_G.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                rivalry1_gabor_G.tStop = t  # not accounting for scr refresh
                rivalry1_gabor_G.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rivalry1_gabor_G.stopped')
                rivalry1_gabor_G.setAutoDraw(False)
        
        # *interv_gabor_R* updates
        if interv_gabor_R.status == NOT_STARTED and tThisFlip >= 3.75-frameTolerance:
            # keep track of start time/frame for later
            interv_gabor_R.frameNStart = frameN  # exact frame index
            interv_gabor_R.tStart = t  # local t and not account for scr refresh
            interv_gabor_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(interv_gabor_R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'interv_gabor_R.started')
            interv_gabor_R.setAutoDraw(True)
        if interv_gabor_R.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > interv_gabor_R.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                interv_gabor_R.tStop = t  # not accounting for scr refresh
                interv_gabor_R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'interv_gabor_R.stopped')
                interv_gabor_R.setAutoDraw(False)
        
        # *interv_gabor_G* updates
        if interv_gabor_G.status == NOT_STARTED and tThisFlip >= 14.5-frameTolerance:
            # keep track of start time/frame for later
            interv_gabor_G.frameNStart = frameN  # exact frame index
            interv_gabor_G.tStart = t  # local t and not account for scr refresh
            interv_gabor_G.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(interv_gabor_G, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'interv_gabor_G.started')
            interv_gabor_G.setAutoDraw(True)
        if interv_gabor_G.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > interv_gabor_G.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                interv_gabor_G.tStop = t  # not accounting for scr refresh
                interv_gabor_G.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'interv_gabor_G.stopped')
                interv_gabor_G.setAutoDraw(False)
        
        # *rivalry2_gabor_R* updates
        if rivalry2_gabor_R.status == NOT_STARTED and tThisFlip >= 10.75-frameTolerance:
            # keep track of start time/frame for later
            rivalry2_gabor_R.frameNStart = frameN  # exact frame index
            rivalry2_gabor_R.tStart = t  # local t and not account for scr refresh
            rivalry2_gabor_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rivalry2_gabor_R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rivalry2_gabor_R.started')
            rivalry2_gabor_R.setAutoDraw(True)
        if rivalry2_gabor_R.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rivalry2_gabor_R.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                rivalry2_gabor_R.tStop = t  # not accounting for scr refresh
                rivalry2_gabor_R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rivalry2_gabor_R.stopped')
                rivalry2_gabor_R.setAutoDraw(False)
        
        # *rivalry2_gabor_G* updates
        if rivalry2_gabor_G.status == NOT_STARTED and tThisFlip >= 10.75-frameTolerance:
            # keep track of start time/frame for later
            rivalry2_gabor_G.frameNStart = frameN  # exact frame index
            rivalry2_gabor_G.tStart = t  # local t and not account for scr refresh
            rivalry2_gabor_G.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rivalry2_gabor_G, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rivalry2_gabor_G.started')
            rivalry2_gabor_G.setAutoDraw(True)
        if rivalry2_gabor_G.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rivalry2_gabor_G.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                rivalry2_gabor_G.tStop = t  # not accounting for scr refresh
                rivalry2_gabor_G.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rivalry2_gabor_G.stopped')
                rivalry2_gabor_G.setAutoDraw(False)
        
        # *R_fixation_rivalry* updates
        if R_fixation_rivalry.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R_fixation_rivalry.frameNStart = frameN  # exact frame index
            R_fixation_rivalry.tStart = t  # local t and not account for scr refresh
            R_fixation_rivalry.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R_fixation_rivalry, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R_fixation_rivalry.started')
            R_fixation_rivalry.setAutoDraw(True)
        if R_fixation_rivalry.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > R_fixation_rivalry.tStartRefresh + 21.5-frameTolerance:
                # keep track of stop time/frame for later
                R_fixation_rivalry.tStop = t  # not accounting for scr refresh
                R_fixation_rivalry.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'R_fixation_rivalry.stopped')
                R_fixation_rivalry.setAutoDraw(False)
        
        # *L_fixation_rivalry* updates
        if L_fixation_rivalry.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            L_fixation_rivalry.frameNStart = frameN  # exact frame index
            L_fixation_rivalry.tStart = t  # local t and not account for scr refresh
            L_fixation_rivalry.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_fixation_rivalry, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'L_fixation_rivalry.started')
            L_fixation_rivalry.setAutoDraw(True)
        if L_fixation_rivalry.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > L_fixation_rivalry.tStartRefresh + 21.5-frameTolerance:
                # keep track of stop time/frame for later
                L_fixation_rivalry.tStop = t  # not accounting for scr refresh
                L_fixation_rivalry.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'L_fixation_rivalry.stopped')
                L_fixation_rivalry.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eye_dominanceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "eye_dominance" ---
    for thisComponent in eye_dominanceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-21.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'eye_dominance_loop'

# get names of stimulus parameters
if eye_dominance_loop.trialList in ([], [None], None):
    params = []
else:
    params = eye_dominance_loop.trialList[0].keys()
# save data for this loop
eye_dominance_loop.saveAsExcel(filename + '.xlsx', sheetName='eye_dominance_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
eye_dominance_loop.saveAsText(filename + 'eye_dominance_loop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
