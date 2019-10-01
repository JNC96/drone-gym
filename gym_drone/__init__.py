from gym.envs.registration import register

register(
    id='drone-v0',
    entry_point='gym_drone.envs:DroneEnv',
    max_episode_steps=50,
    reward_threshold = 0.95,
    nondeterministic = False
)

register(
    id='droneInt-v0',
    entry_point='gym_drone.envs:DroneIntEnv',
    max_episode_steps=50,
    reward_threshold=0.95,
    nondeterministic = False,
)

