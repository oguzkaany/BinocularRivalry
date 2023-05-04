#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Ocak 06, 2023, at 11:05
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
expName = 'BR_St_switch_11'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Oğuz Kaan\\OneDrive\\tezson\\kodlar\\BR_St_switch_11.py',
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

# --- Initialize components for Routine "fixation" ---
fixation_null_L = visual.ShapeStim(
    win=win, name='fixation_right', vertices='cross', units = 'deg',
    size=(0.8, 0.8),
    ori=0.0, pos=(-10, 0.0), anchor='center',
    lineWidth=0.001,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[1.0000, 1.0000, 1.0000],
    opacity=None, depth=0.0, interpolate=True)
fixation_null_R =  visual.ShapeStim(
    win=win, name='fixation_right', vertices='cross', units = 'deg',
    size=(0.8, 0.8),
    ori=0.0, pos=(10, 0.0), anchor='center',
    lineWidth=0.001,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[1.0000, 1.0000, 1.0000],
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "trial" ---
Gabor_R2 = visual.GratingStim(
    win=win, units = 'deg', name = 'Gabor_R2',
    tex=redGrat, mask='gauss', anchor='center',
    ori=90.0, pos=(-10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=0.0)
Gabor_G2 = visual.GratingStim(
    win=win, units = 'deg', name = 'Gabor_G2',
    tex=greenGrat, mask='gauss', anchor='center',
    ori=0, pos=(10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=-1.0)
Gabor_R3 = visual.GratingStim(
    win=win, units = 'deg', name = 'Gabor_R3',
    tex=redGrat, mask='gauss', anchor='center',
    ori=90.0, pos=(-10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=-2.0)
Gabor_mock_RR1 = visual.GratingStim(
    win=win, units = 'deg', name = 'Gabor_mock_RR_1',
    tex=redGrat, mask='gauss', anchor='center',
    ori=90.0, pos=(10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=0.0)
Gabor_Mock_RL_1 = visual.GratingStim(
    win=win, units = 'deg', name ='Gabor_mock_RL_1',
    tex=redGrat, mask='gauss', anchor='center',
    ori=90.0, pos=(-10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=0.0)
Gabor_Mock_GR_1 = visual.GratingStim(
    win=win, units = 'deg', name ='Gabor_mock_GR_1',
    tex=greenGrat, mask='gauss', anchor='center',
    ori=0, pos=(10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=0.0)
Gabor_Mock_GL_1 = visual.GratingStim(
    win=win, units = 'deg', name ='Gabor_mock_GL_1',
    tex=greenGrat, mask='gauss', anchor='center',
    ori=0, pos=(-10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=0.0)
Gabor_G3 = visual.GratingStim(
    win=win, units = 'deg', name ='Gabor_G3',
    tex=greenGrat, mask='gauss', anchor='center',
    ori=0, pos=(10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=-7.0)
Gabor_Mock_RR2 = visual.GratingStim(
    win=win, units = 'deg', name ='Gabor_mock_RR2',
    tex=redGrat, mask='gauss', anchor='center',
    ori=90.0, pos=(10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=0.0)
Gabor_Mock_RL2 = visual.GratingStim(
    win=win, units = 'deg', name ='Gabor_mock_RL2',
    tex=redGrat, mask='gauss', anchor='center',
    ori=90.0, pos=(-10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=0.0)
Gabor_Mock_GR2 = visual.GratingStim(
    win=win, units = 'deg', name ='Gabor_mock_GR2',
    tex=greenGrat, mask='gauss', anchor='center',
    ori=0, pos=(10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=0.0)
Gabor_Mock_GL2 = visual.GratingStim(
    win=win, units = 'deg', name ='Gabor_mock_GL2',
    tex=greenGrat, mask='gauss', anchor='center',
    ori=0, pos=(-10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=0.0)
Gabor_R1 = visual.GratingStim(
    win=win, units = 'deg', name ='Gabor_R1',
    tex=redGrat, mask='gauss', anchor='center',
    ori=90.0, pos=(-10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=-12.0)
Gabor_G1 = visual.GratingStim(
    win=win, units = 'deg', name ='Gabor_G1',
    tex=greenGrat, mask='gauss', anchor='center',
    ori=0, pos=(10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=-13.0)
key_resp = keyboard.Keyboard()
fixation_trial_L = visual.ShapeStim(
    win=win, name='fixation_right', vertices='cross', units = 'deg',
    size=(0.8, 0.8),
    ori=0.0, pos=(-10, 0.0), anchor='center',
    lineWidth=0.001,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[1.0000, 1.0000, 1.0000],
    opacity=None, depth=-15.0, interpolate=True)
fixation_trial_R =  visual.ShapeStim(
    win=win, name='fixation_right', vertices='cross', units = 'deg',
    size=(0.8, 0.8),
    ori=0.0, pos=(10, 0.0), anchor='center',
    lineWidth=0.001,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[1.0000, 1.0000, 1.0000],
    opacity=None, depth=-16.0, interpolate=True)
    
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "fixation" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
fixationComponents = [fixation_null_L, fixation_null_R]
for thisComponent in fixationComponents:
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

# --- Run Routine "fixation" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation_null_L* updates
    if fixation_null_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_null_L.frameNStart = frameN  # exact frame index
        fixation_null_L.tStart = t  # local t and not account for scr refresh
        fixation_null_L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_null_L, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fixation_null_L.started')
        fixation_null_L.setAutoDraw(True)
    if fixation_null_L.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_null_L.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            fixation_null_L.tStop = t  # not accounting for scr refresh
            fixation_null_L.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_null_L.stopped')
            fixation_null_L.setAutoDraw(False)
    
    # *fixation_null_R* updates
    if fixation_null_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_null_R.frameNStart = frameN  # exact frame index
        fixation_null_R.tStart = t  # local t and not account for scr refresh
        fixation_null_R.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_null_R, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fixation_null_R.started')
        fixation_null_R.setAutoDraw(True)
    if fixation_null_R.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_null_R.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            fixation_null_R.tStop = t  # not accounting for scr refresh
            fixation_null_R.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_null_R.stopped')
            fixation_null_R.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "fixation" ---
for thisComponent in fixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BR_main/BR-switch.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Gabor_R2.setContrast(RedContrast)
    Gabor_G2.setContrast(GreenContrast)
    Gabor_R3.setContrast(RedContrast)
    Gabor_mock_RR1.setContrast(RedContrast)
    Gabor_Mock_RL_1.setContrast(RedContrast)
    Gabor_Mock_GR_1.setContrast(GreenContrast)
    Gabor_Mock_GL_1.setContrast(GreenContrast)
    Gabor_G3.setContrast(GreenContrast)
    Gabor_Mock_RR2.setContrast(RedContrast)
    Gabor_Mock_RL2.setContrast(RedContrast)
    Gabor_Mock_GR2.setContrast(GreenContrast)
    Gabor_Mock_GL2.setContrast(GreenContrast)
    Gabor_R1.setContrast(RedContrast)
    Gabor_G1.setContrast(GreenContrast)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [Gabor_R2, Gabor_G2, Gabor_R3, Gabor_mock_RR1, Gabor_Mock_RL_1, Gabor_Mock_GR_1, Gabor_Mock_GL_1, Gabor_G3, Gabor_Mock_RR2, Gabor_Mock_RL2, Gabor_Mock_GR2, Gabor_Mock_GL2, Gabor_R1, Gabor_G1, key_resp, fixation_trial_L, fixation_trial_R]
    for thisComponent in trialComponents:
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
    
    # --- Run Routine "trial" ---
    while continueRoutine and routineTimer.getTime() < 120.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Gabor_R2* updates
        if Gabor_R2.status == NOT_STARTED and tThisFlip >= 45-frameTolerance:
            # keep track of start time/frame for later
            Gabor_R2.frameNStart = frameN  # exact frame index
            Gabor_R2.tStart = t  # local t and not account for scr refresh
            Gabor_R2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Gabor_R2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Gabor_R2.started')
            Gabor_R2.setAutoDraw(True)
        if Gabor_R2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Gabor_R2.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                Gabor_R2.tStop = t  # not accounting for scr refresh
                Gabor_R2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Gabor_R2.stopped')
                Gabor_R2.setAutoDraw(False)
        
        # *Gabor_G2* updates
        if Gabor_G2.status == NOT_STARTED and tThisFlip >= 45-frameTolerance:
            # keep track of start time/frame for later
            Gabor_G2.frameNStart = frameN  # exact frame index
            Gabor_G2.tStart = t  # local t and not account for scr refresh
            Gabor_G2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Gabor_G2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Gabor_G2.started')
            Gabor_G2.setAutoDraw(True)
        if Gabor_G2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Gabor_G2.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                Gabor_G2.tStop = t  # not accounting for scr refresh
                Gabor_G2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Gabor_G2.stopped')
                Gabor_G2.setAutoDraw(False)
        
        # *Gabor_R3* updates
        if Gabor_R3.status == NOT_STARTED and tThisFlip >= 90-frameTolerance:
            # keep track of start time/frame for later
            Gabor_R3.frameNStart = frameN  # exact frame index
            Gabor_R3.tStart = t  # local t and not account for scr refresh
            Gabor_R3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Gabor_R3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Gabor_R3.started')
            Gabor_R3.setAutoDraw(True)
        if Gabor_R3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Gabor_R3.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                Gabor_R3.tStop = t  # not accounting for scr refresh
                Gabor_R3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Gabor_R3.stopped')
                Gabor_R3.setAutoDraw(False)
        
        # *Gabor_mock_RR1* updates
        if Gabor_mock_RR1.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
            # keep track of start time/frame for later
            Gabor_mock_RR1.frameNStart = frameN  # exact frame index
            Gabor_mock_RR1.tStart = t  # local t and not account for scr refresh
            Gabor_mock_RR1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Gabor_mock_RR1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Gabor_mock_RR1.started')
            Gabor_mock_RR1.setAutoDraw(True)
        if Gabor_mock_RR1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Gabor_mock_RR1.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                Gabor_mock_RR1.tStop = t  # not accounting for scr refresh
                Gabor_mock_RR1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Gabor_mock_RR1.stopped')
                Gabor_mock_RR1.setAutoDraw(False)
        
        # *Gabor_Mock_RL_1* updates
        if Gabor_Mock_RL_1.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
            # keep track of start time/frame for later
            Gabor_Mock_RL_1.frameNStart = frameN  # exact frame index
            Gabor_Mock_RL_1.tStart = t  # local t and not account for scr refresh
            Gabor_Mock_RL_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Gabor_Mock_RL_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Gabor_Mock_RL_1.started')
            Gabor_Mock_RL_1.setAutoDraw(True)
        if Gabor_Mock_RL_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Gabor_Mock_RL_1.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                Gabor_Mock_RL_1.tStop = t  # not accounting for scr refresh
                Gabor_Mock_RL_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Gabor_Mock_RL_1.stopped')
                Gabor_Mock_RL_1.setAutoDraw(False)
        
        # *Gabor_Mock_GR_1* updates
        if Gabor_Mock_GR_1.status == NOT_STARTED and tThisFlip >= 34-frameTolerance:
            # keep track of start time/frame for later
            Gabor_Mock_GR_1.frameNStart = frameN  # exact frame index
            Gabor_Mock_GR_1.tStart = t  # local t and not account for scr refresh
            Gabor_Mock_GR_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Gabor_Mock_GR_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Gabor_Mock_GR_1.started')
            Gabor_Mock_GR_1.setAutoDraw(True)
        if Gabor_Mock_GR_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Gabor_Mock_GR_1.tStartRefresh + 11-frameTolerance:
                # keep track of stop time/frame for later
                Gabor_Mock_GR_1.tStop = t  # not accounting for scr refresh
                Gabor_Mock_GR_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Gabor_Mock_GR_1.stopped')
                Gabor_Mock_GR_1.setAutoDraw(False)
        
        # *Gabor_Mock_GL_1* updates
        if Gabor_Mock_GL_1.status == NOT_STARTED and tThisFlip >= 34-frameTolerance:
            # keep track of start time/frame for later
            Gabor_Mock_GL_1.frameNStart = frameN  # exact frame index
            Gabor_Mock_GL_1.tStart = t  # local t and not account for scr refresh
            Gabor_Mock_GL_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Gabor_Mock_GL_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Gabor_Mock_GL_1.started')
            Gabor_Mock_GL_1.setAutoDraw(True)
        if Gabor_Mock_GL_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Gabor_Mock_GL_1.tStartRefresh + 11-frameTolerance:
                # keep track of stop time/frame for later
                Gabor_Mock_GL_1.tStop = t  # not accounting for scr refresh
                Gabor_Mock_GL_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Gabor_Mock_GL_1.stopped')
                Gabor_Mock_GL_1.setAutoDraw(False)
        
        # *Gabor_G3* updates
        if Gabor_G3.status == NOT_STARTED and tThisFlip >= 90-frameTolerance:
            # keep track of start time/frame for later
            Gabor_G3.frameNStart = frameN  # exact frame index
            Gabor_G3.tStart = t  # local t and not account for scr refresh
            Gabor_G3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Gabor_G3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Gabor_G3.started')
            Gabor_G3.setAutoDraw(True)
        if Gabor_G3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Gabor_G3.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                Gabor_G3.tStop = t  # not accounting for scr refresh
                Gabor_G3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Gabor_G3.stopped')
                Gabor_G3.setAutoDraw(False)
        
        # *Gabor_Mock_RR2* updates
        if Gabor_Mock_RR2.status == NOT_STARTED and tThisFlip >= 84-frameTolerance:
            # keep track of start time/frame for later
            Gabor_Mock_RR2.frameNStart = frameN  # exact frame index
            Gabor_Mock_RR2.tStart = t  # local t and not account for scr refresh
            Gabor_Mock_RR2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Gabor_Mock_RR2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Gabor_Mock_RR2.started')
            Gabor_Mock_RR2.setAutoDraw(True)
        if Gabor_Mock_RR2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Gabor_Mock_RR2.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                Gabor_Mock_RR2.tStop = t  # not accounting for scr refresh
                Gabor_Mock_RR2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Gabor_Mock_RR2.stopped')
                Gabor_Mock_RR2.setAutoDraw(False)
        
        # *Gabor_Mock_RL2* updates
        if Gabor_Mock_RL2.status == NOT_STARTED and tThisFlip >= 84-frameTolerance:
            # keep track of start time/frame for later
            Gabor_Mock_RL2.frameNStart = frameN  # exact frame index
            Gabor_Mock_RL2.tStart = t  # local t and not account for scr refresh
            Gabor_Mock_RL2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Gabor_Mock_RL2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Gabor_Mock_RL2.started')
            Gabor_Mock_RL2.setAutoDraw(True)
        if Gabor_Mock_RL2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Gabor_Mock_RL2.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                Gabor_Mock_RL2.tStop = t  # not accounting for scr refresh
                Gabor_Mock_RL2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Gabor_Mock_RL2.stopped')
                Gabor_Mock_RL2.setAutoDraw(False)
        
        # *Gabor_Mock_GR2* updates
        if Gabor_Mock_GR2.status == NOT_STARTED and tThisFlip >= 75-frameTolerance:
            # keep track of start time/frame for later
            Gabor_Mock_GR2.frameNStart = frameN  # exact frame index
            Gabor_Mock_GR2.tStart = t  # local t and not account for scr refresh
            Gabor_Mock_GR2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Gabor_Mock_GR2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Gabor_Mock_GR2.started')
            Gabor_Mock_GR2.setAutoDraw(True)
        if Gabor_Mock_GR2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Gabor_Mock_GR2.tStartRefresh + 9-frameTolerance:
                # keep track of stop time/frame for later
                Gabor_Mock_GR2.tStop = t  # not accounting for scr refresh
                Gabor_Mock_GR2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Gabor_Mock_GR2.stopped')
                Gabor_Mock_GR2.setAutoDraw(False)
        
        # *Gabor_Mock_GL2* updates
        if Gabor_Mock_GL2.status == NOT_STARTED and tThisFlip >= 75-frameTolerance:
            # keep track of start time/frame for later
            Gabor_Mock_GL2.frameNStart = frameN  # exact frame index
            Gabor_Mock_GL2.tStart = t  # local t and not account for scr refresh
            Gabor_Mock_GL2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Gabor_Mock_GL2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Gabor_Mock_GL2.started')
            Gabor_Mock_GL2.setAutoDraw(True)
        if Gabor_Mock_GL2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Gabor_Mock_GL2.tStartRefresh + 9-frameTolerance:
                # keep track of stop time/frame for later
                Gabor_Mock_GL2.tStop = t  # not accounting for scr refresh
                Gabor_Mock_GL2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Gabor_Mock_GL2.stopped')
                Gabor_Mock_GL2.setAutoDraw(False)
        
        # *Gabor_R1* updates
        if Gabor_R1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Gabor_R1.frameNStart = frameN  # exact frame index
            Gabor_R1.tStart = t  # local t and not account for scr refresh
            Gabor_R1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Gabor_R1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Gabor_R1.started')
            Gabor_R1.setAutoDraw(True)
        if Gabor_R1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Gabor_R1.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                Gabor_R1.tStop = t  # not accounting for scr refresh
                Gabor_R1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Gabor_R1.stopped')
                Gabor_R1.setAutoDraw(False)
        
        # *Gabor_G1* updates
        if Gabor_G1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Gabor_G1.frameNStart = frameN  # exact frame index
            Gabor_G1.tStart = t  # local t and not account for scr refresh
            Gabor_G1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Gabor_G1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Gabor_G1.started')
            Gabor_G1.setAutoDraw(True)
        if Gabor_G1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Gabor_G1.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                Gabor_G1.tStop = t  # not accounting for scr refresh
                Gabor_G1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Gabor_G1.stopped')
                Gabor_G1.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 120-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.stopped')
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
        
        # *fixation_trial_L* updates
        if fixation_trial_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_trial_L.frameNStart = frameN  # exact frame index
            fixation_trial_L.tStart = t  # local t and not account for scr refresh
            fixation_trial_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_trial_L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_trial_L.started')
            fixation_trial_L.setAutoDraw(True)
        if fixation_trial_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_trial_L.tStartRefresh + 120-frameTolerance:
                # keep track of stop time/frame for later
                fixation_trial_L.tStop = t  # not accounting for scr refresh
                fixation_trial_L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_trial_L.stopped')
                fixation_trial_L.setAutoDraw(False)
        
        # *fixation_trial_R* updates
        if fixation_trial_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_trial_R.frameNStart = frameN  # exact frame index
            fixation_trial_R.tStart = t  # local t and not account for scr refresh
            fixation_trial_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_trial_R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_trial_R.started')
            fixation_trial_R.setAutoDraw(True)
        if fixation_trial_R.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_trial_R.tStartRefresh + 120-frameTolerance:
                # keep track of stop time/frame for later
                fixation_trial_R.tStop = t  # not accounting for scr refresh
                fixation_trial_R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_trial_R.stopped')
                fixation_trial_R.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-120.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
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
