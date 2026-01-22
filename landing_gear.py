"""
Landing Gear Controller Module Prototype
Description:
    Simulation-driven functional configuration prototype for a landing gear control 
    system. This module models state transitions for landing gear deployment based on 
    commands and time ticks.

Author: Kyle Rothery
Date: 21-01-2026

Requirements:
    FR1: The landing gear shall initialize in the UP_LOCKED state.
    
    FR2: Upon receiving a command to lower the gear, the system shall transition to the 
    TRANSITIONING_DOWN state.
    
    FR3: The gear shall remain in the TRANSITIONING_DOWN state for a predefined number 
    of ticks.
    
    FR4: The system shall ignore additional commands to lower the gear while already in 
    the TRANSITIONING_DOWN state.

Change Log:
- 21-01-2026: Initial prototype implementation
"""

from enum import Enum, auto

# Number of ticks required to deploy the landing gear
DEPLOY_TICKS = 3

class GearState(Enum):
    UP_LOCKED = auto()
    TRANSITIONING_DOWN = auto()
    DOWN_LOCKED = auto()

class LandingGearController:
    def __init__(self):
        self.state = GearState.UP_LOCKED
        self._deploy_ticks_remaining = 0
    
    def log(self, message):
        print(f"[{self.state.name}] {message}")

    def command_gear_down(self):
        self.log("Command received: Gear Down")
        if self.state == GearState.UP_LOCKED:
            self.state = GearState.TRANSITIONING_DOWN
            self._deploy_ticks_remaining = DEPLOY_TICKS
            self.log(f"Gear deploying initiated"
                     f" with {self._deploy_ticks_remaining} ticks remaining"
            )
        elif self.state == GearState.TRANSITIONING_DOWN:
            self.log("Gear is already deploying")
        elif self.state == GearState.DOWN_LOCKED:
            self.log("Gear is already down and locked")
        else:
            self.log("Gear command ignored in current state")

    def tick(self):
        """
        Simulate a time tick for the landing gear controller.

        When the gear is in the TRANSITIONING_DOWN state, the controller
        counts down ticks until the gear reaches the DOWN_LOCKED state.
        """
        if self.state != GearState.TRANSITIONING_DOWN:
            self.log("Tick received but gear is not deploying")
            return
        
        if self._deploy_ticks_remaining > 0:
            self._deploy_ticks_remaining -= 1
            self.log(f"Tick: {self._deploy_ticks_remaining} ticks remaining for gear deployment")

        if self._deploy_ticks_remaining == 0:
            self.state = GearState.DOWN_LOCKED
            self.log("Gear deployment complete: Gear is now down and locked")


if __name__ == "__main__":
    controller = LandingGearController()
    controller.command_gear_down()

    for _ in range(DEPLOY_TICKS):
        import time
        controller.tick()
        time.sleep(1)  # Simulate time delay between ticks