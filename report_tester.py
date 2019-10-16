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
            
----------

def action_rank(self, states, evaluation):

        action_buffer = []
        print("*********************")
        print("*********************")
        print("\n%------------------------")
        print("% STATE @ STEP# "+str(states[0]*states[1]))
        print("%------------------------\n")
        print("Slope: "+str(states[2])+" --- @("+str(states[0])+","+str(states[1])+")")
        
        for _ in range(0,4):

            # here,independent is TRUE because in the normal pipeline you would have to observe after taking an action, but we are simply sampling actions.
            tmp_action = self.agent.act(states=states, independent = True, evaluation = False)
            
            print("\n%------------------------")
            print("% ACTION "+str(_+1))
            print("%------------------------\n")

            print("Camera Angle: "+str(tmp_action[0]))
            print("Speed: "+str(tmp_action[1]))
            print("Height: "+str(tmp_action[2]))            

            action_buffer.append(tmp_action)

        action_choice = int(input("\nPlease select the optimal action (1-4): ")) - 1
        while action_choice>4 or action_choice<0:
            action_choice = int(input("\nPlease select the optimal action (1-4): ")) - 1


        return action_buffer[action_choice]

