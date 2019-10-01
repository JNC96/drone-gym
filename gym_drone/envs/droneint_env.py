import gym
import logging
import math
import numpy as np
from gym import error, spaces, utils
from gym.utils import seeding


class DroneIntEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    
    # debug vars
    
    self.__version__ = "1.0.0"
    
    # Hyperparameter definition 
    self.x_min = int(0)
    self.x_max = int(4)
    self.y_min = int(0)
    self.y_max = int(4)
    self.min_cam_angle = int(1)
    self.max_cam_angle = int(3)
    self.min_terr_angle = int(1)
    self.max_terr_angle = int(3) #terrain angle - something that is observed
    self.min_speed = int(1)
    self.max_speed = int(3) #max speed is actually 56 kmh (this is m/s)
    self.min_height = int(1) #meter
    self.max_height = int(3) #meter
    
    
    # ???
    self.state = None #initiate state holder
    self.episode_over = False
    self.current_episode = -1 
    self.current_timestep = 0 # -1 because timestep increments before action
    self.current_pos = [0,0]
    self.action_episode_memory = []
    self.grid_step_max = (self.x_max+1)*(self.y_max+1) - 1 # number of grid squares
    self.max_timestep = 2*self.grid_step_max   # Visits all grid squares twice.
    #self.
    
    # Observations are (in this order): current x-pos, current y-pos, terrain angle (from horizontal axis)
    # Let's assume that the map is of grid size 5x5. Position of the drone is represented as (grid x index,
    # grid y index), where (0,0) is the top left of the grid ((4,4) is max value)).
    
    # Here, low is the lower limit of observation range, and high is the higher limit.
    low_ob = np.array([self.x_min,  # x-pos
                    self.y_min,  # y-pos
                    self.min_cam_angle]) # terrain_angle_deg
    high_ob = np.array([self.x_max,  # x-pos
                    self.y_max,  # y-pos
                    self.max_cam_angle]) # terrain_angle_deg
    self.observation_space = spaces.Box(low_ob, high_ob, dtype=np.float32)
    
    # Action space
    low_action = np.array([self.min_cam_angle,  # cam angle in deg
                    self.min_speed,  # flight speed in m/s
                    self.min_height]) # flight height in m
    high_action = np.array([self.max_cam_angle,  # cam angle in deg
                    self.max_speed,  # flight speed in m/s
                    self.max_height]) # flight height in m
    self.action_space = spaces.MultiDiscrete([self.max_cam_angle,  self.max_speed, self.max_height])
    
    # generate random terrain gradients/create them here
    # import random
    # list  = [111,222,333,444,555]
    # print("random.choice() to select random item from list - ", random.choice(list))

    
    self.terr_angle_grid = [0,0,0,0,0,
                            0,0,0,0,0,
                            1,1,1,1,1,
                            0,0,0,0,0,
                            0,0,0,0,0
                           ]

  def step(self, action):
    
    """
        The agent (drone) takes a step (flies somewhere) in the environment.
        Parameters
        ----------
 action : (int,int) - the coordinates, (int) - the terrain gradient
        Returns: (int) - terrain angle (observation), (float32) reward, (bool) episode_over, (int,int) - coords
        -------
        ob, reward, episode_over, info : tuple
            ob (object) :
                an environment-specific object representing your observation of
                the environment.
            reward (float) :
                amount of reward achieved by the previous action. The scale
                varies between environments, but the goal is always to increase
                your total reward. (This reward per step is normalised to 1.)
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
    
    if self.episode_over:
        raise RuntimeError("Episode is done. You're running step() despite this fact. Or reset the env by calling reset().") #end execution, and finish run

    # Return the reward for action taken given state. Save action to action memory buffer.
    self.action_episode_memory[self.current_episode].append(action)
    

    # Take a step, and observe environment.
    self.current_timestep += 1
    self.current_pos = self.index2coord(self.current_timestep)
    self.current_pos.append(self.terr_angle_grid[self.current_timestep%self.grid_step_max])
    self.state = list.copy(self.current_pos)

    reward = self.get_user_reward(action,self.state)                         
    
    if self.current_timestep>=self.max_timestep:
      self.episode_over = True
      
    return self.state, reward, self.episode_over, {}

  #def print_action(self,action):
            
  def index2coord(self, index):
    
    # converts an index value to x-y coords
    # see order of the grid above in __init__
    
    if (index<=self.x_max):
      return [0, index]
    else:        
      return [(index%(self.grid_step_max+1))//(self.x_max+1), index%(self.x_max+1)]
          
      # grid step max is n*m (grid dimensions) -1

  def _get_state(self):
    
    return self.terr_angle_grid[self.current_timestep%self.grid_step_max]
  
  def _get_info(self):
    
    return self.index2coord(self.current_timestep)
  
  def _get_reward(self,action):

     # reward factors
    
    gradient_delta_rf = 0.3
    speed_rf = 0.35
    height_rf = 0.35
    
    #logging.warning("the current timestep.  ="+str(self.current_timestep))
    #logging.warning("self.current_timestep%self.grid_step_max  =  "+ str(self.current_timestep%self.grid_step_max))

    gradient_delta = abs(self.terr_angle_grid[(self.current_timestep%self.grid_step_max)] - action[0]) # action [1] is the camera angle

    gradient_delta_norm = 1 - gradient_delta/self.max_cam_angle # this will give us a normalised value that rewards less difference
    
    speed_norm = 1 - action[1]/self.max_speed # speed normalised, and reward less speed
    
    height_norm = action[2]/self.max_height # height normalised, and more height is better (FOR NOW)
    
    tmp_reward = gradient_delta_norm*gradient_delta_rf + speed_norm*speed_rf + height_norm*height_rf
    
    return tmp_reward
  
  def get_user_reward(self, action, state):

    #init variables.
    uinput_reward = None
    
    print("Given that the:\n\n")
    print("Slope is"+str(state[2])+".\n")
    print("@("+str(state[0])+","+str(state[1])+")\n\n")

    print("Agent takes actions:\n\n")
    print("Camera Angle: "+str(action[0])+"\n")
    print("Speed: "+str(action[1])+"\n")
    print("Height: "+str(action[2])+"\n\n")

    print("This returns a predicted coverage of:")
    tmp = _get_reward(action)
    print("\n\n")
                         
    uinput_reward = input("How would you rate the most recent action?")
    return uinput_reward
    
  def reset(self):
    # reset should always run at the end of an episode and before the first run.
    self.current_timestep = 0
    self.current_episode += 1
    self.action_episode_memory.append([])
    self.episode_over = False
    
    self.current_pos = self.index2coord(self.current_timestep)
    self.current_pos.append(self.terr_angle_grid[self.current_timestep%self.grid_step_max])
    self.state = list.copy(self.current_pos)
    
    return self.state
    
  def _render(self, mode='human', close=False):
    return 0
  def close(self):
    return 0
