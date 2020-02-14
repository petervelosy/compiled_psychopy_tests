#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.02), February 14, 2020, at 15:48
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Beat Perception Task'  # from the Builder filename that created this script
expInfo = {u'                   uid': u'001', u'            session': u'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.path.sep + expInfo['date']

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1368, 912), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "start"
startClock = core.Clock()
text_start = visual.TextStim(win=win, ori=0, name='text_start',
    text=u'Gold-MSI \xdctemilleszked\xe9s\r\n\xe9szlel\xe9s\xe9t vizsg\xe1l\xf3 teszt\r\n\r\nAmennyiben elolvasta az instrukci\xf3kat, \xe9s nincsen tov\xe1bbi k\xe9rd\xe9se, k\xe9rj\xfck, nyomja meg a SZ\xd3K\xd6Z billenty\u0171t a k\xeds\xe9rlet ind\xedt\xe1s\xe1hoz.\r\n\r\n\r\n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "startpause"
startpauseClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text=None,    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
sound_1 = sound.Sound('A',secs=1)

sound_1 = sound.Sound('A', secs=-1)
sound_1.setVolume(1)
text_sound1 = visual.TextStim(win=win, ori=0, name='text_sound1',
    text=None,    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "dummypause"
dummypauseClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=None,    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "decide"
decideClock = core.Clock()
decide_text = visual.TextStim(win=win, ori=0, name='decide_text',
    text=u'Illeszkedtek a pittyeg\u0151 hangok a zene \xfctem\xe9re, \r\nvagy el voltak cs\xfaszva a zen\xe9hez k\xe9pest?\n0 = El voltak cs\xfaszva, 1 = Illeszedtek',    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=80,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
judgement = visual.RatingScale(win=win, name='judgement', marker='triangle', size=1.0, pos=[0.0, 0.4], choices=[u'0', u'1'], tickHeight=-1, singleClick=True, showAccept=False)
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'\r\nMennyire biztos ebben a v\xe1lasz\xe1ban?\r\n1 = Csak tippeltem. 2 = Azt hiszem, hogy helyes.\n3 = Biztos vagyok benne, hogy helyes.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=80,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
confidence = visual.RatingScale(win=win, name='confidence', marker='triangle', size=1.0, pos=[0.0, -0.4], choices=[u'1', u'2', u'3'], tickHeight=-1, singleClick=True, showAccept=False)

# Initialize components for Routine "end"
endClock = core.Clock()
text_end = visual.TextStim(win=win, ori=0, name='text_end',
    text=u'A k\xeds\xe9rlet befejez\u0151d\xf6tt.\r\n\r\nK\xf6sz\xf6nj\xfck a r\xe9szv\xe9telt!\r\n\r\nK\xe9rj\xfck, nyomja meg a sz\xf3k\xf6z billenty\u0171t a k\xeds\xe9rletb\u0151l val\xf3 kil\xe9p\xe9shez.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "start"-------
t = 0
startClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
start_key = event.BuilderKeyResponse()  # create an object of type KeyResponse
start_key.status = NOT_STARTED
# keep track of which components have finished
startComponents = []
startComponents.append(text_start)
startComponents.append(start_key)
for thisComponent in startComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "start"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = startClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_start* updates
    if t >= 0.0 and text_start.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_start.tStart = t  # underestimates by a little under one frame
        text_start.frameNStart = frameN  # exact frame index
        text_start.setAutoDraw(True)
    
    # *start_key* updates
    if t >= 0.0 and start_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        start_key.tStart = t  # underestimates by a little under one frame
        start_key.frameNStart = frameN  # exact frame index
        start_key.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if start_key.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('BeatPerception_v10.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "startpause"-------
    t = 0
    startpauseClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    startpauseComponents = []
    startpauseComponents.append(text_3)
    for thisComponent in startpauseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "startpause"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = startpauseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        if text_3.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in startpauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "startpause"-------
    for thisComponent in startpauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    
    sound_1.setSound(sound1)
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(sound_1)
    trialComponents.append(text_sound1)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # start/stop sound_1
        if t >= 0.0 and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t  # underestimates by a little under one frame
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        if sound_1.status == STARTED and t >= (0.0 + (sound_1.getDuration()-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_1.stop()  # stop the sound (if longer than duration)
        
        # *text_sound1* updates
        if t >= 0.0 and text_sound1.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_sound1.tStart = t  # underestimates by a little under one frame
            text_sound1.frameNStart = frameN  # exact frame index
            text_sound1.setAutoDraw(True)
        if text_sound1.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_sound1.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    sound_1.stop() #ensure sound has stopped at end of routine
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "dummypause"-------
    t = 0
    dummypauseClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    dummypauseComponents = []
    dummypauseComponents.append(text_2)
    for thisComponent in dummypauseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "dummypause"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = dummypauseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        if text_2.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in dummypauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "dummypause"-------
    for thisComponent in dummypauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "decide"-------
    t = 0
    decideClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    judgement.reset()
    confidence.reset()
    # keep track of which components have finished
    decideComponents = []
    decideComponents.append(decide_text)
    decideComponents.append(judgement)
    decideComponents.append(text)
    decideComponents.append(confidence)
    for thisComponent in decideComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "decide"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = decideClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *decide_text* updates
        if t >= 0.0 and decide_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            decide_text.tStart = t  # underestimates by a little under one frame
            decide_text.frameNStart = frameN  # exact frame index
            decide_text.setAutoDraw(True)
        # *judgement* updates
        if t >= 0.0 and judgement.status == NOT_STARTED:
            # keep track of start time/frame for later
            judgement.tStart = t  # underestimates by a little under one frame
            judgement.frameNStart = frameN  # exact frame index
            judgement.setAutoDraw(True)
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # underestimates by a little under one frame
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        # *confidence* updates
        if t >= 0.0 and confidence.status == NOT_STARTED:
            # keep track of start time/frame for later
            confidence.tStart = t  # underestimates by a little under one frame
            confidence.frameNStart = frameN  # exact frame index
            confidence.setAutoDraw(True)
        continueRoutine &= confidence.noResponse  # a response ends the trial
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in decideComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "decide"-------
    for thisComponent in decideComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('judgement.response', judgement.getRating())
    trials.addData('judgement.rt', judgement.getRT())
    # store data for trials (TrialHandler)
    trials.addData('confidence.response', confidence.getRating())
    trials.addData('confidence.rt', confidence.getRT())
    # the Routine "decide" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
end_key = event.BuilderKeyResponse()  # create an object of type KeyResponse
end_key.status = NOT_STARTED
# keep track of which components have finished
endComponents = []
endComponents.append(text_end)
endComponents.append(end_key)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end* updates
    if t >= 0.0 and text_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_end.tStart = t  # underestimates by a little under one frame
        text_end.frameNStart = frameN  # exact frame index
        text_end.setAutoDraw(True)
    
    # *end_key* updates
    if t >= 0.0 and end_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_key.tStart = t  # underestimates by a little under one frame
        end_key.frameNStart = frameN  # exact frame index
        end_key.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if end_key.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

win.close()
core.quit()
