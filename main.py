from stateMachine import *

while cm_state != state.OFF:
    cm_state = stateMachine(cm_state)
