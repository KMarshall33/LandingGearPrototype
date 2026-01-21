from landing_gear import LandingGearController, GearState

def test_initial_state_is_up_locked():
  controller = LandingGearController()
  assert controller.state == GearState.UP_LOCKED

def test_command_gear_down():
  controller = LandingGearController()
  controller.command_gear_down()
  assert controller.state == GearState.DOWN_LOCKED