from gym.envs.registration import register

register(
    id='drone-v0',
    entry_point='gym_drone.envs:DroneEnv',
)
