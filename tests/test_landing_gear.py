from landing_gear import LandingGearController, GearState

def test_initial_state_is_up_locked():
  controller = LandingGearController()
  assert controller.state == GearState.UP_LOCKED

def test_command_gear_down_enters_transition():
  controller = LandingGearController()
  controller.command_gear_down()
  assert controller.state == GearState.TRANSITIONING_DOWN

def test_gear_does_not_lock_down_immediately():
  controller = LandingGearController()
  controller.command_gear_down()
  controller.tick()
  assert controller.state == GearState.TRANSITIONING_DOWN

def test_gear_locks_after_three_ticks():
  controller = LandingGearController()
  controller.command_gear_down()

  controller.tick()
  controller.tick()
  controller.tick()
  
  assert controller.state == GearState.DOWN_LOCKED