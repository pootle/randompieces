#!/usr/bin/env python

"""
skeleton module to separate out the low level guiding from PiAGM
"""

def closeagent():
    pass
    #finished with guiding

def poll():
    pass
    #check to see if there is anything else to do once each time round piag's loop

def stop(ver=False, hor=False):
    pass
    #stop activity on specified axes

def guidenudge(nudgedir):
    pass
    # nudge needed
    
def move(mdir):
    pass
    # move in given direction

def setAutoGuide(enabled):
    pass
    # start guiding

def corrections(vertcorr, horcorr):
    pass
    # apply specified corrections
