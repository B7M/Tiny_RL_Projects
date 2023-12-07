"""
Black rectangles:       Walls       [reward = -100].
Yellow bin circle:      Nirvana     [reward = +10].
All other states:       Path        [reward = -1].
"""

import maze_objects
import numpy as np
import pygame as pg



class AI:
    
    def __init__(self, game):
        self.game = game
        self.current_col=self.game.screen_width//2
        self.current_row=self.game.screen_height
        self.reward_table()
        self.action_index=True

        
    def reward_table(self):
        self.reward=np.full((self.game.screen_height//maze_objects.square_height,self.game.screen_width//maze_objects.square_width),-1)
        self.reward[0][:]=10
        for block in self.game.blocks.blocks:
            self.reward[block.y//maze_objects.square_height][block.x//maze_objects.square_width]=-100
        # print(self.reward)
        return self.reward
        
    
    def terminal_states(self,current_row,current_col):
        if self.reward[current_row//maze_objects.square_height-1,current_col//maze_objects.square_width-1]==10:
            self.game.game_active = False
            return True
        else:
            return False
        
    def next_action(self,current_row,current_col):
        if np.random.random()<self.game.epsilon:
            return np.argmax(self.q_values[:,current_row//maze_objects.square_height-1,current_col//maze_objects.square_width-1])
        else:
            return np.random.randint(0,3)
    
    def next_state(self,current_row,current_col,action_index):
        # action_index: 0:up, 1:down, 2:left, 3:right
        self.game.score -= 1
        if action_index==0 and current_row>maze_objects.square_height:
            return current_row-maze_objects.square_height,current_col
        elif action_index==1 and current_row<self.game.screen_height:#-maze_objects.square_height:
            return current_row+maze_objects.square_height,current_col
        elif action_index==2 and current_col>maze_objects.square_width:
            return current_row,current_col-maze_objects.square_width
        elif action_index==3 and current_col<self.game.screen_width: #-maze_objects.square_width:
            return current_row,current_col+maze_objects.square_width
        else:
            return current_row,current_col
        
        
    def AI_learning(self):
        total_score=[]
        discount_factor=0.9
        learning_rate=0.9
        h=maze_objects.square_height
        w=maze_objects.square_width
        self.q_values=np.zeros((4,self.game.screen_height//maze_objects.square_height,self.game.screen_width//maze_objects.square_width))
        for episodes in range(25):
            sequence_action=[]
            self.current_row,self.current_col=self.game.screen_height,self.game.screen_width//2
            while not self.terminal_states(self.current_row,self.current_col):
                self.action_index=self.next_action(self.current_row,self.current_col)
                # print("action index\n",self.action_index)
                sequence_action.append(self.action_index)
                next_row,next_col=self.next_state(self.current_row,self.current_col,self.action_index)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.game.running = False
                        pg.quit()
                        exit()
                
                self.game.update()
                self.game.draw()
                self.q_values[self.action_index,self.current_row//h-1,self.current_col//w-1]=self.q_values[self.action_index,self.current_row//h-1,self.current_col//w-1]+learning_rate*(self.reward[next_row//h-1, next_col//w-1]+discount_factor*np.max(self.q_values[:,next_row//h-1,next_col//w-1])-self.q_values[self.action_index,self.current_row//h-1,self.current_col//w-1])
                
                pg.image.save(self.game.screen, str(episodes)+"_"+str(self.game.score)+".png")
                
                # print("take look at updated q values\n",self.q_values)
                self.current_row,self.current_col=next_row,next_col
            print("sequence action\n",sequence_action)
            total_score.append(self.game.score)
            self.game.game_active = False
            self.game.update()
            self.game.draw()
            pg.image.save(self.game.screen, str(episodes)+"_win"+".png")
            self.game.game_active = True
        print("Total score in each run\n",total_score)
        self.game.running = False
        pg.quit()
        exit()
