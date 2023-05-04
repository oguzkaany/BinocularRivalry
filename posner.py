#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Şubat 24, 2023, at 17:32
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
expName = 'posner_3'  # from the Builder filename that created this script
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
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Oğuz Kaan\\OneDrive\\tezson\\kodlar\\posner_3.py',
    savePickle=True, saveWideText=True,
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

# --- Initialize components for Routine "null" ---
null_fixation = visual.ShapeStim(
    win=win, name='null_fixation', vertices='cross',units='deg', 
    size=(1, 1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "cued_trials" ---
right_frame = visual.Rect(
    win=win, name='right_frame',units='deg', 
    width=(5, 5)[0], height=(5, 5)[1],
    ori=0.0, pos=(5, 0), anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
left_frame = visual.Rect(
    win=win, name='left_frame',units='deg', 
    width=(5, 5)[0], height=(5, 5)[1],
    ori=0.0, pos=(-5, 0), anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=-1.0, interpolate=True)
right_cue = visual.Rect(
    win=win, name='right_cue',units='deg', 
    width=(5, 5)[0], height=(5, 5)[1],
    ori=0.0, pos=(5, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=1.0, depth=-2.0, interpolate=True)
left_cue = visual.Rect(
    win=win, name='left_cue',units='deg', 
    width=(5, 5)[0], height=(5, 5)[1],
    ori=0.0, pos=(-5, 0), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor=[1.0000, 1.0000, 1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=1.0, depth=-3.0, interpolate=True)
target_SOA200 = visual.ShapeStim(
    win=win, name='target_SOA200', vertices='star7',units='deg', 
    size=(3, 3),
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-4.0, interpolate=True)
target_SOA400 = visual.ShapeStim(
    win=win, name='target_SOA400', vertices='star7',units='deg', 
    size=(3, 3),
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-5.0, interpolate=True)
target_SOA800 = visual.ShapeStim(
    win=win, name='target_SOA800', vertices='star7',units='deg', 
    size=(3, 3),
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-6.0, interpolate=True)
key_resp = keyboard.Keyboard()
target_SOA600 = visual.ShapeStim(
    win=win, name='target_SOA600', vertices='star7',units='deg', 
    size=(3, 3),
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-8.0, interpolate=True)
target1100 = visual.ShapeStim(
    win=win, name='target1100', vertices='star7',units='deg', 
    size=(3, 3),
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-9.0, interpolate=True)
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',units='deg', 
    size=(1, 1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-10.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "null" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
nullComponents = [null_fixation]
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
    
    # *null_fixation* updates
    if null_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        null_fixation.frameNStart = frameN  # exact frame index
        null_fixation.tStart = t  # local t and not account for scr refresh
        null_fixation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(null_fixation, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'null_fixation.started')
        null_fixation.setAutoDraw(True)
    if null_fixation.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > null_fixation.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            null_fixation.tStop = t  # not accounting for scr refresh
            null_fixation.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'null_fixation.stopped')
            null_fixation.setAutoDraw(False)
    
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
excercise_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('posner/conditions_3.xlsx'),
    seed=None, name='excercise_trials')
thisExp.addLoop(excercise_trials)  # add the loop to the experiment
thisExcercise_trial = excercise_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExcercise_trial.rgb)
if thisExcercise_trial != None:
    for paramName in thisExcercise_trial:
        exec('{} = thisExcercise_trial[paramName]'.format(paramName))

for thisExcercise_trial in excercise_trials:
    currentLoop = excercise_trials
    # abbreviate parameter names if possible (e.g. rgb = thisExcercise_trial.rgb)
    if thisExcercise_trial != None:
        for paramName in thisExcercise_trial:
            exec('{} = thisExcercise_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "cued_trials" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    right_cue.setOpacity(right_cue_presence)
    left_cue.setOpacity(left_cue_presence)
    target_SOA200.setOpacity(target_SOA200_presence)
    target_SOA200.setPos([targetX, 0])
    target_SOA400.setOpacity(target_SOA400_presence)
    target_SOA400.setPos([targetX, 0])
    target_SOA800.setOpacity(target_SOA800_presence)
    target_SOA800.setPos([targetX, 0])
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    target_SOA600.setOpacity(target_SOA600_presence)
    target_SOA600.setPos([targetX, 0])
    target1100.setOpacity(target_1100_presence)
    target1100.setPos([targetX, 0])
    # keep track of which components have finished
    cued_trialsComponents = [right_frame, left_frame, right_cue, left_cue, target_SOA200, target_SOA400, target_SOA800, key_resp, target_SOA600, target1100, fixation]
    for thisComponent in cued_trialsComponents:
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
    
    # --- Run Routine "cued_trials" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *right_frame* updates
        if right_frame.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_frame.frameNStart = frameN  # exact frame index
            right_frame.tStart = t  # local t and not account for scr refresh
            right_frame.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_frame, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'right_frame.started')
            right_frame.setAutoDraw(True)
        if right_frame.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > right_frame.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                right_frame.tStop = t  # not accounting for scr refresh
                right_frame.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'right_frame.stopped')
                right_frame.setAutoDraw(False)
        
        # *left_frame* updates
        if left_frame.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_frame.frameNStart = frameN  # exact frame index
            left_frame.tStart = t  # local t and not account for scr refresh
            left_frame.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_frame, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'left_frame.started')
            left_frame.setAutoDraw(True)
        if left_frame.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > left_frame.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                left_frame.tStop = t  # not accounting for scr refresh
                left_frame.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'left_frame.stopped')
                left_frame.setAutoDraw(False)
        
        # *right_cue* updates
        if right_cue.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            right_cue.frameNStart = frameN  # exact frame index
            right_cue.tStart = t  # local t and not account for scr refresh
            right_cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_cue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'right_cue.started')
            right_cue.setAutoDraw(True)
        if right_cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > right_cue.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                right_cue.tStop = t  # not accounting for scr refresh
                right_cue.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'right_cue.stopped')
                right_cue.setAutoDraw(False)
        
        # *left_cue* updates
        if left_cue.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            left_cue.frameNStart = frameN  # exact frame index
            left_cue.tStart = t  # local t and not account for scr refresh
            left_cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_cue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'left_cue.started')
            left_cue.setAutoDraw(True)
        if left_cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > left_cue.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                left_cue.tStop = t  # not accounting for scr refresh
                left_cue.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'left_cue.stopped')
                left_cue.setAutoDraw(False)
        
        # *target_SOA200* updates
        if target_SOA200.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
            # keep track of start time/frame for later
            target_SOA200.frameNStart = frameN  # exact frame index
            target_SOA200.tStart = t  # local t and not account for scr refresh
            target_SOA200.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_SOA200, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_SOA200.started')
            target_SOA200.setAutoDraw(True)
        if target_SOA200.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target_SOA200.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                target_SOA200.tStop = t  # not accounting for scr refresh
                target_SOA200.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_SOA200.stopped')
                target_SOA200.setAutoDraw(False)
        
        # *target_SOA400* updates
        if target_SOA400.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
            # keep track of start time/frame for later
            target_SOA400.frameNStart = frameN  # exact frame index
            target_SOA400.tStart = t  # local t and not account for scr refresh
            target_SOA400.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_SOA400, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_SOA400.started')
            target_SOA400.setAutoDraw(True)
        if target_SOA400.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target_SOA400.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                target_SOA400.tStop = t  # not accounting for scr refresh
                target_SOA400.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_SOA400.stopped')
                target_SOA400.setAutoDraw(False)
        
        # *target_SOA800* updates
        if target_SOA800.status == NOT_STARTED and tThisFlip >= 1.8-frameTolerance:
            # keep track of start time/frame for later
            target_SOA800.frameNStart = frameN  # exact frame index
            target_SOA800.tStart = t  # local t and not account for scr refresh
            target_SOA800.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_SOA800, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_SOA800.started')
            target_SOA800.setAutoDraw(True)
        if target_SOA800.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target_SOA800.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                target_SOA800.tStop = t  # not accounting for scr refresh
                target_SOA800.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_SOA800.stopped')
                target_SOA800.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
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
            if tThisFlipGlobal > key_resp.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.stopped')
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *target_SOA600* updates
        if target_SOA600.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            target_SOA600.frameNStart = frameN  # exact frame index
            target_SOA600.tStart = t  # local t and not account for scr refresh
            target_SOA600.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_SOA600, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_SOA600.started')
            target_SOA600.setAutoDraw(True)
        if target_SOA600.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target_SOA600.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                target_SOA600.tStop = t  # not accounting for scr refresh
                target_SOA600.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_SOA600.stopped')
                target_SOA600.setAutoDraw(False)
        
        # *target1100* updates
        if target1100.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
            # keep track of start time/frame for later
            target1100.frameNStart = frameN  # exact frame index
            target1100.tStart = t  # local t and not account for scr refresh
            target1100.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target1100, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target1100.started')
            target1100.setAutoDraw(True)
        if target1100.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target1100.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                target1100.tStop = t  # not accounting for scr refresh
                target1100.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target1100.stopped')
                target1100.setAutoDraw(False)
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation.started')
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.stopped')
                fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cued_trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "cued_trials" ---
    for thisComponent in cued_trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    excercise_trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        excercise_trials.addData('key_resp.rt', key_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'excercise_trials'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
