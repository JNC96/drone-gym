if self.agent.episodes == 0 and self.interactive:
                print(self.interactive)
                print(self.agent.episodes)
                user_action = self.action_rank(states=states, evaluation=evaluation)
            else:
                user_action = 0
            # run with selected action
            if self.agent.episodes > 0:
                self.interactive = False
            actions = self.agent.act(states=states, evaluation=evaluation, int_bool = self.interactive, int_act = user_action)
