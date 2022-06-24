import numpy as np


class Environment(object):
    def __init__(self):
        self._env = np.zeros(6, 6)  # in: (0,0) out:(5,5)
        self._env[0, :3] = 1
        self._env[1, 1:2] = 1
        self._env[2, 2] = 1
        self._env[4, :3] = 1
        self._env[
            0, 0
        ] = 2  # 2 represents the _agent that starts at position 0,0 of the _env
        self._pos_agent = (0, 0)  # Tuple to get track of the _agent position7

    def print_env(self):
        pass

    def is_move_allowed(self, state, action):
        pass

    def update_env(self, action):
        pass

    def is_experience_over(self):
        pass

    def get_state(self):
        pass

    def get_reward(
        self, action, state
    ):  # Not sure it should be function of action-only function of state? Easier
        pass
