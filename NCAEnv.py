import numpy as np
import gymnasium as gym
from gymnasium import spaces

class NCAEnv(gym.Env):
    def __init__(self):
        super(NCAEnv, self).__init__()
        
        # action and observation space (3x3 grid, two colors)
        # 3 x 3 x 2 = 18 (we probably want to give these values to the constructor, later)
        self.action_space = spaces.Discrete(18) # (row, column, color to use)
        self.observation_space = spaces.Box(low=0, high=1, shape=(9,), dtype=np.int32)
        
        # target color (red = 1)
        self.target_color = 1

    def reset(self, seed=None, options=None):
        # initialize grid with random colors
        self.grid = np.random.choice([0, 1], size=(3, 3))
        # TODO the {} represents the info
        return self.grid.flatten(), {}

    def step(self, action):
        # apply action 
        row, col, color = self._decode_action(action)
        self.grid = self.grid.reshape(3, 3)
        self.grid[row, col] = color

        # calculate reward (sum of correct colors)
        reward = -(self.grid != self.target_color).sum()

        # all cells are the target color
        terminated = (self.grid == self.target_color).all()

        return self.grid.flatten(), reward, terminated, False, {}
    
    def _decode_action(self, action):
        # Decode action into row, column, and color
        row = action // 6
        col = (action // 2) % 3
        color = action % 2
        return row, col, color

    def render(self, mode='human'):
        # simple text rendering of the grid
        print(self.grid.reshape(3, 3))
