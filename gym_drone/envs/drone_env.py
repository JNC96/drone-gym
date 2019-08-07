import gym
import seeding
import math
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
    
    # debug vars
    
    self.__version__ = "0.1.0"
    
    # Hyperparameter definition 
    self.x_min = 0
    self.x_max = 4
    self.y_min = 0
    self.y_max = 4
    
    
    self.visited_entire_grid = False
    
    self.grid_visit_count = 100
    #self.
    
    # Observations are (in this order): current x-pos, current y-pos, terrain angle (from horizontal axis)
    # Let's assume that the map is of grid size 10x10. Position of the drone is represented as (grid x index,
    # grid y index), where (0,0) is the bottom left of the grid ((4,4) is max value)).
    
    # Here, low is the lower limit of observation range, and high is the higher limit.
    low = np.array([self.x_min,  # x-pos
                    self.y_min,  # y-pos
                    0]) # terrain_angle_deg
    high = np.array([self.x_max,  # x-pos
                    self.y_max,  # y-pos
                    90]) # terrain_angle_deg
    self.observation_space = spaces.Box(low, high, dtype=np.float32)

    
  def step(self, action):
    
    """
        The agent (drone) takes a step (flies somewhere) in the environment.
        Parameters
        ----------
        action : (float32,float32) - the coordinates
        Returns
        -------
        ob, reward, episode_over, info : tuple
            ob (object) :
                an environment-specific object representing your observation of
                the environment.
            reward (float) :
                amount of reward achieved by the previous action. The scale
                varies between environments, but the goal is always to increase
                your total reward.
            episode_over (bool) :
                whether it's time to reset the environment again. Most (but not
                all) tasks are divided up into well-defined episodes, and done
                being True indicates the episode has terminated. (For example,
                perhaps the pole tipped too far, or you lost your last life.)
            info (dict) :
                 diagnostic information useful for debugging. It can sometimes
                 be useful for learning (for example, it might contain the raw
                 probabilities behind the environment's last state change).
                 However, official evaluations of your agent are not allowed to
                 use this for learning.
        """
    
    if self.visited_entire_grid:
        raise RuntimeError("Episode is done.") #end execution, and finish run
    self.
    
  def reset(self):
    t3 = 3
  def render(self, mode='human'):
    t4 = 4
  def close(self):
    t5 = 5
