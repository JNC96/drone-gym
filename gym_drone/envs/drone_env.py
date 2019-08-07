import gym
import seeding
import numpy as np
from gym import error, spaces, utils
from gym.utils 

def get_pred_cov(x):
    # Return the predicted coverage of the environment
    e = math.exp(1)
    return (1.0 + e) / (1. + math.exp(x + 1))


class DroneEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    
    self.__version__ = "0.1.0"
    #self.
    
    # Observations are (in this order): current x-pos, current y-pos, terrain angle (from horizontal axis)
    # Let's assume that the map is of grid size 10x10. Position of the drone is represented as (grid x index,
    # grid y index), where (0,0) is the bottom left of the grid ((9,9) is max value)).
    
    # Here, low is the lower limit of observation range, and high is the higher limit.
    low = np.array([0,  # x-pos
                    0,  # y-pos
                    0]) # terrain_angle_deg
    high = np.array([9,  # x-pos
                    9,  # y-pos
                    90]) # terrain_angle_deg
    self.observation_space = spaces.Box(low, high, dtype=np.float32)

    
  def step(self, action):
    t1 = 2
  def reset(self):
    t3 = 3
  def render(self, mode='human'):
    t4 = 4
  def close(self):
    t5 = 5
