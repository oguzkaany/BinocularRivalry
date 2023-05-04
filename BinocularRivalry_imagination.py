#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Aralık 26, 2022, at 15:10
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
expName = 'BR_St_maintrial_6'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Oğuz Kaan\\OneDrive\\tezson\\kodlar\\BR_St_maintrial_6.py',
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
fixation_n_L = visual.ShapeStim(
    win=win, name='fixation_right', vertices='cross', units = 'deg',
    size=(0.8, 0.8),
    ori=0.0, pos=(-10, 0.0), anchor='center',
    lineWidth=0.001,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[1.0000, 1.0000, 1.0000],
    opacity=None, depth=-1.0, interpolate=True)
fixation_n_R = visual.ShapeStim(
    win=win, name='fixation_right', vertices='cross', units = 'deg',
    size=(0.8, 0.8),
    ori=0.0, pos=(10, 0.0), anchor='center',
    lineWidth=0.001,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[1.0000, 1.0000, 1.0000],
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "trial" ---
red_Gabor = visual.GratingStim(
    win=win, units = 'deg',
    tex=redGrat, mask='gauss', anchor='center',
    ori=90.0, pos=(-10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1 , blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=0.0)
green_Gabor = visual.GratingStim(
    win=win, units = 'deg',
    tex=greenGrat, mask='gauss', anchor='center',
    ori=0, pos=(10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1 , blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=-1.0)
key_resp = keyboard.Keyboard()
red_cue_L = visual.GratingStim(
    win=win, name='red_cue_L', units = 'deg',
    tex='sin', mask='gauss', anchor='center',
    ori=0.0, pos=(-10, 0), size=(5, 5), sf=0.0, phase=0.0,
    color=[1.0000, -1.0000, -1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
green_cue_L = visual.GratingStim(
    win=win, name='green_cue_L', units = 'deg',
    tex='sin', mask='gauss', anchor='center',
    ori=0.0, pos=(-10, 0), size=(5, 5), sf=0.0, phase=0.0,
    color=[-1.0000, 0.0039, -1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
red_cue_R = visual.GratingStim(
    win=win, name='red_cue_R',
    tex='sin', mask='gauss', anchor='center', units = 'deg',
    ori=0.0, pos=(10, 0), size=(5, 5), sf=0.0, phase=0.0,
    color=[1.0000, -1.0000, -1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
green_cue_R = visual.GratingStim(
    win=win, name='green_cue_R', units = 'deg',
    tex='sin', mask='gauss', anchor='center',
    ori=0.0, pos=(10, 0), size=(5, 5), sf=0.0, phase=0.0,
    color=[-1.0000, 0.0039, -1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-6.0)
fixation_L = visual.ShapeStim(
    win=win, name='fixation_right', vertices='cross', units = 'deg',
    size=(0.8, 0.8),
    ori=0.0, pos=(-10, 0.0), anchor='center',
    lineWidth=0.001,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[1.0000, 1.0000, 1.0000],
    opacity=None, depth=-7.0, interpolate=True)
fixation_R = visual.ShapeStim(
    win=win, name='fixation_right', vertices='cross', units = 'deg',
    size=(0.8, 0.8),
    ori=0.0, pos=(10, 0.0), anchor='center',
    lineWidth=0.001,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[1.0000, 1.0000, 1.0000],
    opacity=None, depth=-8.0, interpolate=True)

# --- Initialize components for Routine "mock" ---
key_resp_mock = keyboard.Keyboard()
red_cue_mock_L = visual.GratingStim(
    win=win, name='red_cue_R',
    tex='sin', mask='gauss', anchor='center', units = 'deg',
    ori=0.0, pos=(-10, 0), size=(5, 5), sf=0.0, phase=0.0,
    color=[1.0000, -1.0000, -1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0)
red_cue_mock_R = visual.GratingStim(
    win=win, name='red_cue_R',
    tex='sin', mask='gauss', anchor='center', units = 'deg',
    ori=0.0, pos=(10, 0), size=(5, 5), sf=0.0, phase=0.0,
    color=[1.0000, -1.0000, -1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-2.0)
mock_red_R = visual.GratingStim(
    win=win, units = 'deg',
    tex=redGrat, mask='gauss', anchor='center',
    ori=90.0, pos=(10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=0.0)
mock_red_L = visual.GratingStim(
    win=win, units = 'deg',
    tex=redGrat, mask='gauss', anchor='center',
    ori=90.0, pos=(-10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=0.0)
mock_green_R = visual.GratingStim(
    win=win, units = 'deg',
    tex=greenGrat, mask='gauss', anchor='center',
    ori=0, pos=(10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=0.3, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=-1.0)
mock_green_L = visual.GratingStim(
    win=win, units = 'deg',
    tex=greenGrat, mask='gauss', anchor='center',
    ori=0, pos=(-10, 0), size=(10, 10), sf= 0.67, phase=0.0,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    opacity=0.3, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, maskParams = {'sd': 3}, depth=-1.0)
fixation_mock_L = visual.ShapeStim(
    win=win, name='fixation_mock_L', vertices='cross', units = 'deg',
    size=(0.8, 0.8),
    ori=0.0, pos=(-10, 0.0), anchor='center',
    lineWidth=0.001,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[1.0000, 1.0000, 1.0000],
    opacity=None, depth=-7.0, interpolate=True)
fixation_mock_R = visual.ShapeStim(
    win=win, name='fixation_mock_R', vertices='cross', units = 'deg',
    size=(0.8, 0.8),
    ori=0.0, pos=(10, 0.0), anchor='center',
    lineWidth=0.001,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[1.0000, 1.0000, 1.0000],
    opacity=None, depth=-8.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "null" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
nullComponents = [fixation_n_L, fixation_n_R]
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
    
    # *fixation_n_L* updates
    if fixation_n_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_n_L.frameNStart = frameN  # exact frame index
        fixation_n_L.tStart = t  # local t and not account for scr refresh
        fixation_n_L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_n_L, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fixation_n_L.started')
        fixation_n_L.setAutoDraw(True)
    if fixation_n_L.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_n_L.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            fixation_n_L.tStop = t  # not accounting for scr refresh
            fixation_n_L.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_n_L.stopped')
            fixation_n_L.setAutoDraw(False)
    
    # *fixation_n_R* updates
    if fixation_n_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation_n_R.frameNStart = frameN  # exact frame index
        fixation_n_R.tStart = t  # local t and not account for scr refresh
        fixation_n_R.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation_n_R, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fixation_n_R.started')
        fixation_n_R.setAutoDraw(True)
    if fixation_n_R.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation_n_R.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            fixation_n_R.tStop = t  # not accounting for scr refresh
            fixation_n_R.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_n_R.stopped')
            fixation_n_R.setAutoDraw(False)
    
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
trials_2 = data.TrialHandler(nReps=7.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('BR_main/BR-trials.xlsx'),
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
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        red_cue_L.setOpacity(RedCue)
        green_cue_L.setOpacity(GreenCue)
        red_cue_R.setOpacity(RedCue)
        green_cue_R.setOpacity(GreenCue)
        # keep track of which components have finished
        trialComponents = [red_Gabor, green_Gabor, key_resp, red_cue_L, green_cue_L, red_cue_R, green_cue_R, fixation_L, fixation_R]
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
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *red_Gabor* updates
            if red_Gabor.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
                # keep track of start time/frame for later
                red_Gabor.frameNStart = frameN  # exact frame index
                red_Gabor.tStart = t  # local t and not account for scr refresh
                red_Gabor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_Gabor, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'red_Gabor.started')
                red_Gabor.setAutoDraw(True)
            if red_Gabor.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > red_Gabor.tStartRefresh + 0.75-frameTolerance:
                    # keep track of stop time/frame for later
                    red_Gabor.tStop = t  # not accounting for scr refresh
                    red_Gabor.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'red_Gabor.stopped')
                    red_Gabor.setAutoDraw(False)
            
            # *green_Gabor* updates
            if green_Gabor.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
                # keep track of start time/frame for later
                green_Gabor.frameNStart = frameN  # exact frame index
                green_Gabor.tStart = t  # local t and not account for scr refresh
                green_Gabor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(green_Gabor, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'green_Gabor.started')
                green_Gabor.setAutoDraw(True)
            if green_Gabor.status == STARTED:
                win.getMovieFrame()
                win.saveMovieFrames('C:\\Users\\Oğuz Kaan\\OneDrive\\tezson\\kodlar\\deneme25.png')
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > green_Gabor.tStartRefresh + 0.75-frameTolerance:
                    # keep track of stop time/frame for later
                    green_Gabor.tStop = t  # not accounting for scr refresh
                    green_Gabor.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'green_Gabor.stopped')
                    green_Gabor.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
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
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['left','right','space'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *red_cue_L* updates
            if red_cue_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_cue_L.frameNStart = frameN  # exact frame index
                red_cue_L.tStart = t  # local t and not account for scr refresh
                red_cue_L.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_cue_L, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'red_cue_L.started')
                red_cue_L.setAutoDraw(True)
            if red_cue_L.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > red_cue_L.tStartRefresh + 0.75-frameTolerance:
                    # keep track of stop time/frame for later
                    red_cue_L.tStop = t  # not accounting for scr refresh
                    red_cue_L.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'red_cue_L.stopped')
                    red_cue_L.setAutoDraw(False)
            
            # *green_cue_L* updates
            if green_cue_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                green_cue_L.frameNStart = frameN  # exact frame index
                green_cue_L.tStart = t  # local t and not account for scr refresh
                green_cue_L.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(green_cue_L, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'green_cue_L.started')
                green_cue_L.setAutoDraw(True)
            if green_cue_L.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > green_cue_L.tStartRefresh + 0.75-frameTolerance:
                    # keep track of stop time/frame for later
                    green_cue_L.tStop = t  # not accounting for scr refresh
                    green_cue_L.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'green_cue_L.stopped')
                    green_cue_L.setAutoDraw(False)
            
            # *red_cue_R* updates
            if red_cue_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                red_cue_R.frameNStart = frameN  # exact frame index
                red_cue_R.tStart = t  # local t and not account for scr refresh
                red_cue_R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_cue_R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'red_cue_R.started')
                red_cue_R.setAutoDraw(True)
            if red_cue_R.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > red_cue_R.tStartRefresh + 0.75-frameTolerance:
                    # keep track of stop time/frame for later
                    red_cue_R.tStop = t  # not accounting for scr refresh
                    red_cue_R.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'red_cue_R.stopped')
                    red_cue_R.setAutoDraw(False)
            
            # *green_cue_R* updates
            if green_cue_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                green_cue_R.frameNStart = frameN  # exact frame index
                green_cue_R.tStart = t  # local t and not account for scr refresh
                green_cue_R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(green_cue_R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'green_cue_R.started')
                green_cue_R.setAutoDraw(True)
            if green_cue_R.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > green_cue_R.tStartRefresh + 0.75-frameTolerance:
                    # keep track of stop time/frame for later
                    green_cue_R.tStop = t  # not accounting for scr refresh
                    green_cue_R.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'green_cue_R.stopped')
                    green_cue_R.setAutoDraw(False)
            
            # *fixation_L* updates
            if fixation_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_L.frameNStart = frameN  # exact frame index
                fixation_L.tStart = t  # local t and not account for scr refresh
                fixation_L.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_L, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_L.started')
                fixation_L.setAutoDraw(True)
            if fixation_L.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_L.tStartRefresh + 21.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_L.tStop = t  # not accounting for scr refresh
                    fixation_L.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_L.stopped')
                    fixation_L.setAutoDraw(False)
            
            # *fixation_R* updates
            if fixation_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_R.frameNStart = frameN  # exact frame index
                fixation_R.tStart = t  # local t and not account for scr refresh
                fixation_R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_R.started')
                fixation_R.setAutoDraw(True)
            if fixation_R.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_R.tStartRefresh + 21.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_R.tStop = t  # not accounting for scr refresh
                    fixation_R.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_R.stopped')
                    fixation_R.setAutoDraw(False)
            
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
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
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
    
    # --- Prepare to start Routine "mock" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_mock.keys = []
    key_resp_mock.rt = []
    _key_resp_mock_allKeys = []
    # keep track of which components have finished
    mockComponents = [key_resp_mock, red_cue_mock_L, red_cue_mock_R, mock_red_R, mock_red_L, mock_green_R, mock_green_L, fixation_mock_L, fixation_mock_R]
    for thisComponent in mockComponents:
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
    
    # --- Run Routine "mock" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_mock* updates
        waitOnFlip = False
        if key_resp_mock.status == NOT_STARTED and tThisFlip >= 7.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_mock.frameNStart = frameN  # exact frame index
            key_resp_mock.tStart = t  # local t and not account for scr refresh
            key_resp_mock.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_mock, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_mock.started')
            key_resp_mock.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_mock.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_mock.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_mock.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_mock.getKeys(keyList=['left','right','space'], waitRelease=False)
            _key_resp_mock_allKeys.extend(theseKeys)
            if len(_key_resp_mock_allKeys):
                key_resp_mock.keys = _key_resp_mock_allKeys[-1].name  # just the last key pressed
                key_resp_mock.rt = _key_resp_mock_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *red_cue_mock_L* updates
        if red_cue_mock_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_cue_mock_L.frameNStart = frameN  # exact frame index
            red_cue_mock_L.tStart = t  # local t and not account for scr refresh
            red_cue_mock_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_cue_mock_L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'red_cue_mock_L.started')
            red_cue_mock_L.setAutoDraw(True)
        if red_cue_mock_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > red_cue_mock_L.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                red_cue_mock_L.tStop = t  # not accounting for scr refresh
                red_cue_mock_L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'red_cue_mock_L.stopped')
                red_cue_mock_L.setAutoDraw(False)
        
        # *red_cue_mock_R* updates
        if red_cue_mock_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_cue_mock_R.frameNStart = frameN  # exact frame index
            red_cue_mock_R.tStart = t  # local t and not account for scr refresh
            red_cue_mock_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_cue_mock_R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'red_cue_mock_R.started')
            red_cue_mock_R.setAutoDraw(True)
        if red_cue_mock_R.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > red_cue_mock_R.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                red_cue_mock_R.tStop = t  # not accounting for scr refresh
                red_cue_mock_R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'red_cue_mock_R.stopped')
                red_cue_mock_R.setAutoDraw(False)
        
        # *mock_red_R* updates
        if mock_red_R.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
            # keep track of start time/frame for later
            mock_red_R.frameNStart = frameN  # exact frame index
            mock_red_R.tStart = t  # local t and not account for scr refresh
            mock_red_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mock_red_R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'mock_red_R.started')
            mock_red_R.setAutoDraw(True)
        if mock_red_R.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mock_red_R.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                mock_red_R.tStop = t  # not accounting for scr refresh
                mock_red_R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mock_red_R.stopped')
                mock_red_R.setAutoDraw(False)
        
        # *mock_red_L* updates
        if mock_red_L.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
            # keep track of start time/frame for later
            mock_red_L.frameNStart = frameN  # exact frame index
            mock_red_L.tStart = t  # local t and not account for scr refresh
            mock_red_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mock_red_L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'mock_red_L.started')
            mock_red_L.setAutoDraw(True)
        if mock_red_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mock_red_L.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                mock_red_L.tStop = t  # not accounting for scr refresh
                mock_red_L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mock_red_L.stopped')
                mock_red_L.setAutoDraw(False)
        
        # *mock_green_R* updates
        if mock_green_R.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
            # keep track of start time/frame for later
            mock_green_R.frameNStart = frameN  # exact frame index
            mock_green_R.tStart = t  # local t and not account for scr refresh
            mock_green_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mock_green_R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'mock_green_R.started')
            mock_green_R.setAutoDraw(True)
        if mock_green_R.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mock_green_R.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                mock_green_R.tStop = t  # not accounting for scr refresh
                mock_green_R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mock_green_R.stopped')
                mock_green_R.setAutoDraw(False)
        
        # *mock_green_L* updates
        if mock_green_L.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
            # keep track of start time/frame for later
            mock_green_L.frameNStart = frameN  # exact frame index
            mock_green_L.tStart = t  # local t and not account for scr refresh
            mock_green_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mock_green_L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'mock_green_L.started')
            mock_green_L.setAutoDraw(True)
        if mock_green_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mock_green_L.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                mock_green_L.tStop = t  # not accounting for scr refresh
                mock_green_L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mock_green_L.stopped')
                mock_green_L.setAutoDraw(False)
        
        # *fixation_mock_L* updates
        if fixation_mock_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_mock_L.frameNStart = frameN  # exact frame index
            fixation_mock_L.tStart = t  # local t and not account for scr refresh
            fixation_mock_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_mock_L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_mock_L.started')
            fixation_mock_L.setAutoDraw(True)
        if fixation_mock_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_mock_L.tStartRefresh + 21.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_mock_L.tStop = t  # not accounting for scr refresh
                fixation_mock_L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_mock_L.stopped')
                fixation_mock_L.setAutoDraw(False)
        
        # *fixation_mock_R* updates
        if fixation_mock_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_mock_R.frameNStart = frameN  # exact frame index
            fixation_mock_R.tStart = t  # local t and not account for scr refresh
            fixation_mock_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_mock_R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_mock_R.started')
            fixation_mock_R.setAutoDraw(True)
        if fixation_mock_R.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_mock_R.tStartRefresh + 21.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_mock_R.tStop = t  # not accounting for scr refresh
                fixation_mock_R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_mock_R.stopped')
                fixation_mock_R.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mock" ---
    for thisComponent in mockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_mock.keys in ['', [], None]:  # No response was made
        key_resp_mock.keys = None
    trials_2.addData('key_resp_mock.keys',key_resp_mock.keys)
    if key_resp_mock.keys != None:  # we had a response
        trials_2.addData('key_resp_mock.rt', key_resp_mock.rt)
    # the Routine "mock" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 7.0 repeats of 'trials_2'

# get names of stimulus parameters
if trials_2.trialList in ([], [None], None):
    params = []
else:
    params = trials_2.trialList[0].keys()
# save data for this loop
trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_2.saveAsText(filename + 'trials_2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "mock" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_mock.keys = []
    key_resp_mock.rt = []
    _key_resp_mock_allKeys = []
    # keep track of which components have finished
    mockComponents = [key_resp_mock, red_cue_mock_L, red_cue_mock_R, mock_red_R, mock_red_L, mock_green_R, mock_green_L, fixation_mock_L, fixation_mock_R]
    for thisComponent in mockComponents:
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
    
    # --- Run Routine "mock" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_mock* updates
        waitOnFlip = False
        if key_resp_mock.status == NOT_STARTED and tThisFlip >= 7.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_mock.frameNStart = frameN  # exact frame index
            key_resp_mock.tStart = t  # local t and not account for scr refresh
            key_resp_mock.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_mock, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_mock.started')
            key_resp_mock.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_mock.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_mock.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_mock.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_mock.getKeys(keyList=['left','right','space'], waitRelease=False)
            _key_resp_mock_allKeys.extend(theseKeys)
            if len(_key_resp_mock_allKeys):
                key_resp_mock.keys = _key_resp_mock_allKeys[-1].name  # just the last key pressed
                key_resp_mock.rt = _key_resp_mock_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *red_cue_mock_L* updates
        if red_cue_mock_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_cue_mock_L.frameNStart = frameN  # exact frame index
            red_cue_mock_L.tStart = t  # local t and not account for scr refresh
            red_cue_mock_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_cue_mock_L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'red_cue_mock_L.started')
            red_cue_mock_L.setAutoDraw(True)
        if red_cue_mock_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > red_cue_mock_L.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                red_cue_mock_L.tStop = t  # not accounting for scr refresh
                red_cue_mock_L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'red_cue_mock_L.stopped')
                red_cue_mock_L.setAutoDraw(False)
        
        # *red_cue_mock_R* updates
        if red_cue_mock_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_cue_mock_R.frameNStart = frameN  # exact frame index
            red_cue_mock_R.tStart = t  # local t and not account for scr refresh
            red_cue_mock_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_cue_mock_R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'red_cue_mock_R.started')
            red_cue_mock_R.setAutoDraw(True)
        if red_cue_mock_R.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > red_cue_mock_R.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                red_cue_mock_R.tStop = t  # not accounting for scr refresh
                red_cue_mock_R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'red_cue_mock_R.stopped')
                red_cue_mock_R.setAutoDraw(False)
        
        # *mock_red_R* updates
        if mock_red_R.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
            # keep track of start time/frame for later
            mock_red_R.frameNStart = frameN  # exact frame index
            mock_red_R.tStart = t  # local t and not account for scr refresh
            mock_red_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mock_red_R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'mock_red_R.started')
            mock_red_R.setAutoDraw(True)
        if mock_red_R.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mock_red_R.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                mock_red_R.tStop = t  # not accounting for scr refresh
                mock_red_R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mock_red_R.stopped')
                mock_red_R.setAutoDraw(False)
        
        # *mock_red_L* updates
        if mock_red_L.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
            # keep track of start time/frame for later
            mock_red_L.frameNStart = frameN  # exact frame index
            mock_red_L.tStart = t  # local t and not account for scr refresh
            mock_red_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mock_red_L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'mock_red_L.started')
            mock_red_L.setAutoDraw(True)
        if mock_red_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mock_red_L.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                mock_red_L.tStop = t  # not accounting for scr refresh
                mock_red_L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mock_red_L.stopped')
                mock_red_L.setAutoDraw(False)
        
        # *mock_green_R* updates
        if mock_green_R.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
            # keep track of start time/frame for later
            mock_green_R.frameNStart = frameN  # exact frame index
            mock_green_R.tStart = t  # local t and not account for scr refresh
            mock_green_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mock_green_R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'mock_green_R.started')
            mock_green_R.setAutoDraw(True)
        if mock_green_R.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mock_green_R.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                mock_green_R.tStop = t  # not accounting for scr refresh
                mock_green_R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mock_green_R.stopped')
                mock_green_R.setAutoDraw(False)
        
        # *mock_green_L* updates
        if mock_green_L.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
            # keep track of start time/frame for later
            mock_green_L.frameNStart = frameN  # exact frame index
            mock_green_L.tStart = t  # local t and not account for scr refresh
            mock_green_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mock_green_L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'mock_green_L.started')
            mock_green_L.setAutoDraw(True)
        if mock_green_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mock_green_L.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                mock_green_L.tStop = t  # not accounting for scr refresh
                mock_green_L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mock_green_L.stopped')
                mock_green_L.setAutoDraw(False)
        
        # *fixation_mock_L* updates
        if fixation_mock_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_mock_L.frameNStart = frameN  # exact frame index
            fixation_mock_L.tStart = t  # local t and not account for scr refresh
            fixation_mock_L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_mock_L, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_mock_L.started')
            fixation_mock_L.setAutoDraw(True)
        if fixation_mock_L.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_mock_L.tStartRefresh + 21.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_mock_L.tStop = t  # not accounting for scr refresh
                fixation_mock_L.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_mock_L.stopped')
                fixation_mock_L.setAutoDraw(False)
        
        # *fixation_mock_R* updates
        if fixation_mock_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_mock_R.frameNStart = frameN  # exact frame index
            fixation_mock_R.tStart = t  # local t and not account for scr refresh
            fixation_mock_R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_mock_R, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_mock_R.started')
            fixation_mock_R.setAutoDraw(True)
        if fixation_mock_R.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_mock_R.tStartRefresh + 21.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_mock_R.tStop = t  # not accounting for scr refresh
                fixation_mock_R.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_mock_R.stopped')
                fixation_mock_R.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mock" ---
    for thisComponent in mockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_mock.keys in ['', [], None]:  # No response was made
        key_resp_mock.keys = None
    trials_3.addData('key_resp_mock.keys',key_resp_mock.keys)
    if key_resp_mock.keys != None:  # we had a response
        trials_3.addData('key_resp_mock.rt', key_resp_mock.rt)
    # the Routine "mock" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trials_3'

# get names of stimulus parameters
if trials_3.trialList in ([], [None], None):
    params = []
else:
    params = trials_3.trialList[0].keys()
# save data for this loop
trials_3.saveAsExcel(filename + '.xlsx', sheetName='trials_3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_3.saveAsText(filename + 'trials_3.csv', delim=',',
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
