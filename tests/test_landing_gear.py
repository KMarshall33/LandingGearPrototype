from landing_gear import LandingGearController, GearState, DEPLOY_TICKS

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

def test_command_gear_down_is_rejected_when_hydraulic_pressure_not_ok():
  controller = LandingGearController()
  controller.hydraulic_pressure_ok = False
  controller.command_gear_down()
  assert controller.state == GearState.UP_LOCKED

def test_command_gear_down_is_accepted_when_hydraulic_pressure_ok():
  controller = LandingGearController()
  controller.hydraulic_pressure_ok = True
  controller.command_gear_down()
  assert controller.state == GearState.TRANSITIONING_DOWN

def test_tick_does_nothing_when_not_transitioning():
  controller = LandingGearController()
  controller.tick()
  assert controller.state == GearState.UP_LOCKED

def test_command_gear_down_when_already_down_locked():
  controller = LandingGearController()
  controller.command_gear_down()
  for _ in range(DEPLOY_TICKS):
    controller.tick()
  assert controller.state == GearState.DOWN_LOCKED

  controller.command_gear_down()
  assert controller.state == GearState.DOWN_LOCKED

def test_duplicate_command_gear_down_during_transition():
  controller = LandingGearController()
  controller.command_gear_down()

  controller.tick()
  assert controller.state == GearState.TRANSITIONING_DOWN

  controller.command_gear_down()

  for _ in range(DEPLOY_TICKS - 1):
    controller.tick()

  assert controller.state == GearState.DOWN_LOCKED

def test_rejected_command_does_not_transition_or_tick():
  controller = LandingGearController()
  controller.hydraulic_pressure_ok = False

  controller.command_gear_down()
  assert controller.state == GearState.UP_LOCKED

  for _ in range(DEPLOY_TICKS + 1):
    controller.tick()

  assert controller.state == GearState.UP_LOCKED