import gym
import seeding
import math
import numpy as np
from gym import error, spaces, utils
from gym.utils 




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
    self.min_cam_angle = 0
    self.max_cam_angle = 90
    self.min_speed = 1
    self.max_speed = 10 #max speed is actually 56 kmh (this is m/s)
    self.min_height = 1 #meter
    self.max_height = 100 #meter
    
    
    # ???
    
    self.visited_entire_grid = False
    self.current_episode = 0
    self.current_timestep = 0
    self.grid_visit_count = (self.x_max+1)*(self.y_max+1)   # 5^2 =25
    #self.
    
    # Observations are (in this order): current x-pos, current y-pos, terrain angle (from horizontal axis)
    # Let's assume that the map is of grid size 10x10. Position of the drone is represented as (grid x index,
    # grid y index), where (0,0) is the bottom left of the grid ((4,4) is max value)).
    
    # Here, low is the lower limit of observation range, and high is the higher limit.
    low_ob = np.array([self.x_min,  # x-pos
                    self.y_min,  # y-pos
                    0]) # terrain_angle_deg
    high_ob = np.array([self.x_max,  # x-pos
                    self.y_max,  # y-pos
                    90]) # terrain_angle_deg
    self.observation_space = spaces.Box(low_ob, high_ob, dtype=np.float32)
    
    # Action space
    low_action = np.array([self.min_cam_angle,  # cam angle in deg
                    self.min_speed,  # flight speed in m/s
                    self.min_height]) # flight height in m
    high_action = np.array([self.max_cam_angle,  # x-pos
                    self.max_speed,  # flight speed in m/s
                    self.max_height]) # flight height in m
    self.action_space = spaces.Box(low_action, high_action, dtype=np.float32)

    
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
    self.grid_visit_count -= 1 # one less grid
    self.current_timestep += 1
    self._take_action(action)
    reward = self._get_reward()
    obs = self._get_state()
    return obs, reward, self.is_banana_sold, {}

    
  def _exec_action(action):
    
    self.action_episode_memory[self.current_episode].append(action)
    
    

    if not grid_visit_count:
        self.visited_entire_grid = True

            
            
  def _get_reward():
    
    
  def _get_state():
    
    
  def get_pred_cov(x):
    # Return the predicted coverage of the environment
    
    
    
  def reset(self):
    t3 = 3
  def render(self, mode='human'):
    t4 = 4
  def close(self):
    t5 = 5
