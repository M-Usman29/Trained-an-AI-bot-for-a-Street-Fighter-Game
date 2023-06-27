from command import Command
import numpy as np
import pandas as pd
from buttons import Buttons
import csv
import pickle
import time

data_list = []

class Bot:

    def __init__(self):
        # < - v + < - v - v + > - > + Y
        self.fire_code = ["<", "!<", "v+<", "!v+!<",
                          "v", "!v", "v+>", "!v+!>", ">+Y", "!>+!Y"]
        self.exe_code = 0
        self.start_fire = True
        self.remaining_code = []
        self.my_command = Command()
        self.buttn = Buttons()
        

    def fight(self, current_game_state, player):
        # python Videos\gamebot-competition-master\PythonAPI\controller.py 1
        if player == "1":
            # print("1")
            # v - < + v - < + B spinning
            if (self.exe_code != 0):
                self.run_command([], current_game_state.player1)
                 

            
            # diff = current_game_state.player2.x_coord - current_game_state.player1.x_coord
            # if (diff > 20):
            #     toss = np.random.randint(3)
            #     if (toss == 0):
            #         self.run_command([">+^+Y",">+^+Y",">+^+Y","!>+!^+!Y"],current_game_state.player1)
            #         #self.run_command([">", "-", "!>", "v+>", "-", "!v+!>", "v", "-", "!v",
            #          #                "v+<", "-", "!v+!<", "<+Y", "-", "!<+!Y"], current_game_state.player1)
            #     elif (toss == 1):
            #         self.run_command(
            #             [">+^+B", ">+^+B", "!>+!^+!B"], current_game_state.player1)
            #     else:  # fire
            #         self.run_command(["<", "-", "!<", "v+<", "-", "!v+!<", "v", "-", "!v",
            #                          "v+>", "-", "!v+!>", ">+Y", "-", "!>+!Y"], current_game_state.player1)
            # elif (diff < -20):
            #     toss = np.random.randint(3)
            #     if (toss == 0):  # spinning
            #         self.run_command(["<+^+Y","<+^+Y","<+^+Y","!<+!^+!Y"],current_game_state.player1)
            #         #self.run_command(["<", "-", "!<", "v+<", "-", "!v+!<", "v", "-", "!v",
            #           #               "v+>", "-", "!v+!>", ">+Y", "-", "!>+!Y"], current_game_state.player1)
            #     elif (toss == 1):
            #         self.run_command(
            #             ["<+^+B", "<+^+B", "!<+!^+!B"], current_game_state.player1)
            #     else:  # fire
            #         self.run_command([">", "-", "!>", "v+>", "-", "!v+!>", "v", "-", "!v",
            #                          "v+<", "-", "!v+!<", "<+Y", "-", "!<+!Y"], current_game_state.player1)
            # else:
            #     # anyFightActionIsTrue(current_game_state.player2.player_buttons)
            #     toss = np.random.randint(2)
            #     if (toss >= 1):
            #         if (diff > 0):
            #             self.run_command(["<", "<", "!<"],
            #                              current_game_state.player1)
            #         else:
            #             self.run_command([">", ">", "!>"],
            #                              current_game_state.player1)
            #     else:
            #         self.run_command(
            #             ["v+R", "v+R", "v+R", "!v+!R"], current_game_state.player1)
 
            with open('./my_code/model1.pkl', 'rb') as f:
                model1 = pickle.load(f)
            
            data = [[
                current_game_state.player1.health,
                current_game_state.player1.x_coord,
                current_game_state.player1.y_coord,
                current_game_state.player1.is_jumping,
                current_game_state.player1.is_crouching,
                current_game_state.player1.player_buttons.up,
                current_game_state.player1.player_buttons.down,
                current_game_state.player1.player_buttons.right,
                current_game_state.player1.player_buttons.left,
                current_game_state.player1.player_buttons.Y,
                current_game_state.player1.player_buttons.B,
                current_game_state.player1.player_buttons.A,
                current_game_state.player1.player_buttons.X,
                current_game_state.player1.player_buttons.L,
                current_game_state.player1.player_buttons.R,
                current_game_state.player2.health,
                current_game_state.player2.x_coord,
                current_game_state.player2.y_coord,
                current_game_state.player2.is_jumping,
                current_game_state.player2.is_crouching,
                current_game_state.player2.player_buttons.up,
                current_game_state.player2.player_buttons.down,
                current_game_state.player2.player_buttons.right,
                current_game_state.player2.player_buttons.left,
                current_game_state.player2.player_buttons.Y,
                current_game_state.player2.player_buttons.B,
                current_game_state.player2.player_buttons.A,
                current_game_state.player2.player_buttons.X,
                current_game_state.player2.player_buttons.L,
                current_game_state.player2.player_buttons.R
                
            ]]
            
            df = pd.DataFrame(data, columns=[
                                  'player1_health',
                                  'player1_x_coord',
                                  'player1_y_coord',
                                  'player1_is_jumping',
                                  'player1_is_crouching',
                                  'player1_button_up',
                                  'player1_button_down',
                                  'player1_button_right',
                                  'player1_button_left',
                                  'player1_button_Y',
                                  'player1_button_B',
                                  'player1_button_A',
                                  'player1_button_X',
                                  'player1_button_L',
                                  'player1_button_R',
                                  'player2_health',
                                  'player2_x_coord',
                                  'player2_y_coord',
                                  'player2_is_jumping',
                                  'player2_is_crouching',
                                  'player2_button_up',
                                  'player2_button_down',
                                  'player2_button_right',
                                  'player2_button_left',
                                  'player2_button_Y',
                                  'player2_button_B',
                                  'player2_button_A',
                                  'player2_button_X',
                                  'player2_button_L',
                                  'player2_button_R'])
            
            df = df.replace(True, 1)
            df = df.replace(False, 0)
            
            pred = model1.predict(df)
            y_pred_rounded1 = np.round(pred)
            y_pred_rounded1[y_pred_rounded1 > 0] = True
            y_pred_rounded1[y_pred_rounded1 <= 0] = False
            y_pred_rounded1 = y_pred_rounded1.astype(int)
            #print(y_pred_rounded1)
            
            if(y_pred_rounded1[0][0] == 0):
                self.buttn.up = False
            else:
                self.buttn.up = True
                
            if(y_pred_rounded1[0][1] == 0):
                self.buttn.down = False
            else:
                self.buttn.down = True
                
            if(y_pred_rounded1[0][2] == 0):
                self.buttn.right = False
            else:
                self.buttn.right = True
                
            if(y_pred_rounded1[0][3] == 0):
                self.buttn.left = False
            else:
                self.buttn.left = True
                
            if(y_pred_rounded1[0][4] == 0):
                self.buttn.Y = False
            else:
                self.buttn.Y = True
                
            if(y_pred_rounded1[0][5] == 0):
                self.buttn.B = False
            else:
                self.buttn.B = True
                
            if(y_pred_rounded1[0][6] == 0):
                self.buttn.A = False
            else:
                self.buttn.A = True
                
            if(y_pred_rounded1[0][7] == 0):
                self.buttn.X = False
            else:
                self.buttn.X = True
                
            if(y_pred_rounded1[0][8] == 0):
                self.buttn.L = False
            else:
                self.buttn.L = True
                
            if(y_pred_rounded1[0][9] == 0):
                self.buttn.R = False
            else:
                self.buttn.R = True
                
            # if (self.buttn.down and self.buttn.right and self.buttn.A):
            #     self.buttn.A = False
            #     # delay for a short amount of time before pressing the next button
            #     time.sleep(0.2)
            #     self.buttn.down = False
            #     self.buttn.right = False
            #     self.buttn.A = True                
                            

            
            self.my_command.player_buttons = self.buttn

        elif player == "2":

            if (self.exe_code != 0):
                self.run_command([], current_game_state.player2)
            # diff = current_game_state.player1.x_coord - current_game_state.player2.x_coord
            # if (diff > 20):
            #     toss = np.random.randint(3)
            #     if (toss == 0):
            #         self.run_command([">+^+Y",">+^+Y",">+^+Y","!>+!^+!Y"],current_game_state.player2)
            #         #self.run_command([">", "-", "!>", "v+>", "-", "!v+!>", "v", "-", "!v",
            #          #                "v+<", "-", "!v+!<", "<+Y", "-", "!<+!Y"], current_game_state.player2)
            #     elif (toss == 1):
            #         self.run_command(
            #             [">+^+B", ">+^+B", "!>+!^+!B"], current_game_state.player2)
            #     else:
            #         self.run_command(["<", "-", "!<", "v+<", "-", "!v+!<", "v", "-", "!v",
            #                          "v+>", "-", "!v+!>", ">+Y", "-", "!>+!Y"], current_game_state.player2)
            # elif (diff < -20):
            #     toss = np.random.randint(3)
            #     if (toss == 0):
            #         self.run_command(["<+^+Y","<+^+Y","<+^+Y","!<+!^+!Y"],current_game_state.player2)
            #         #self.run_command(["<", "-", "!<", "v+<", "-", "!v+!<", "v", "-", "!v",
            #            #              "v+>", "-", "!v+!>", ">+Y", "-", "!>+!Y"], current_game_state.player2)
            #     elif (toss == 1):
            #         self.run_command(
            #             ["<+^+B", "<+^+B", "!<+!^+!B"], current_game_state.player2)
            #     else:
            #         self.run_command([">", "-", "!>", "v+>", "-", "!v+!>", "v", "-", "!v",
            #                          "v+<", "-", "!v+!<", "<+Y", "-", "!<+!Y"], current_game_state.player2)
            # else:
            #     # anyFightActionIsTrue(current_game_state.player2.player_buttons)
            #     toss = np.random.randint(2)
            #     if (toss >= 1):
            #         if (diff < 0):
            #             self.run_command(["<", "<", "!<"],
            #                              current_game_state.player2)
            #         else:
            #             self.run_command([">", ">", "!>"],
            #                              current_game_state.player2)
            #     else:
            #         self.run_command(
            #             ["v+R", "v+R", "v+R", "!v+!R"], current_game_state.player2)
            with open('./my_code/model2.pkl', 'rb') as f:
                model2 = pickle.load(f)
            
            data1 = [[
                current_game_state.player1.health,
                current_game_state.player1.x_coord,
                current_game_state.player1.y_coord,
                current_game_state.player1.is_jumping,
                current_game_state.player1.is_crouching,
                current_game_state.player1.player_buttons.up,
                current_game_state.player1.player_buttons.down,
                current_game_state.player1.player_buttons.right,
                current_game_state.player1.player_buttons.left,
                current_game_state.player1.player_buttons.Y,
                current_game_state.player1.player_buttons.B,
                current_game_state.player1.player_buttons.A,
                current_game_state.player1.player_buttons.X,
                current_game_state.player1.player_buttons.L,
                current_game_state.player1.player_buttons.R,
                current_game_state.player2.health,
                current_game_state.player2.x_coord,
                current_game_state.player2.y_coord,
                current_game_state.player2.is_jumping,
                current_game_state.player2.is_crouching,
                current_game_state.player2.player_buttons.up,
                current_game_state.player2.player_buttons.down,
                current_game_state.player2.player_buttons.right,
                current_game_state.player2.player_buttons.left,
                current_game_state.player2.player_buttons.Y,
                current_game_state.player2.player_buttons.B,
                current_game_state.player2.player_buttons.A,
                current_game_state.player2.player_buttons.X,
                current_game_state.player2.player_buttons.L,
                current_game_state.player2.player_buttons.R
                
            ]]
            
            df1 = pd.DataFrame(data1, columns=[
                                  'player1_health',
                                  'player1_x_coord',
                                  'player1_y_coord',
                                  'player1_is_jumping',
                                  'player1_is_crouching',
                                  'player1_button_up',
                                  'player1_button_down',
                                  'player1_button_right',
                                  'player1_button_left',
                                  'player1_button_Y',
                                  'player1_button_B',
                                  'player1_button_A',
                                  'player1_button_X',
                                  'player1_button_L',
                                  'player1_button_R',
                                  'player2_health',
                                  'player2_x_coord',
                                  'player2_y_coord',
                                  'player2_is_jumping',
                                  'player2_is_crouching',
                                  'player2_button_up',
                                  'player2_button_down',
                                  'player2_button_right',
                                  'player2_button_left',
                                  'player2_button_Y',
                                  'player2_button_B',
                                  'player2_button_A',
                                  'player2_button_X',
                                  'player2_button_L',
                                  'player2_button_R'])
            
            df1 = df1.replace(True, 1)
            df1 = df1.replace(False, 0)
            
            pred1 = model2.predict(df1)
            y_pred_rounded11 = np.round(pred1)
            y_pred_rounded11[y_pred_rounded11 > 0] = True
            y_pred_rounded11[y_pred_rounded11 <= 0] = False
            y_pred_rounded11 = y_pred_rounded11.astype(int)
            #print(y_pred_rounded11)
            
            if(y_pred_rounded11[0][0] == 0):
                self.buttn.up = False
            else:
                self.buttn.up = True
                
            if(y_pred_rounded11[0][1] == 0):
                self.buttn.down = False
            else:
                self.buttn.down = True
                
            if(y_pred_rounded11[0][2] == 0):
                self.buttn.right = False
            else:
                self.buttn.right = True
                
            if(y_pred_rounded11[0][3] == 0):
                self.buttn.left = False
            else:
                self.buttn.left = True
                
            if(y_pred_rounded11[0][4] == 0):
                self.buttn.Y = False
            else:
                self.buttn.Y = True
                
            if(y_pred_rounded11[0][5] == 0):
                self.buttn.B = False
            else:
                self.buttn.B = True
                
            if(y_pred_rounded11[0][6] == 0):
                self.buttn.A = False
            else:
                self.buttn.A = True
                
            if(y_pred_rounded11[0][7] == 0):
                self.buttn.X = False
            else:
                self.buttn.X = True
                
            if(y_pred_rounded11[0][8] == 0):
                self.buttn.L = False
            else:
                self.buttn.L = True
                
            if(y_pred_rounded11[0][9] == 0):
                self.buttn.R = False
            else:
                self.buttn.R = True
                
            self.my_command.player2_buttons = self.buttn
            
        # data_list.append([
        #     current_game_state.timer,
        #     current_game_state.fight_result,
        #     current_game_state.has_round_started,
        #     current_game_state.is_round_over,
        #     current_game_state.player1.player_id,
        #     current_game_state.player1.health,
        #     current_game_state.player1.x_coord,
        #     current_game_state.player1.y_coord,
        #     current_game_state.player1.is_jumping,
        #     current_game_state.player1.is_crouching,
        #     current_game_state.player1.is_player_in_move,
        #     current_game_state.player1.move_id,
        #     current_game_state.player1.player_buttons.up,
        #     current_game_state.player1.player_buttons.down,
        #     current_game_state.player1.player_buttons.right,
        #     current_game_state.player1.player_buttons.left,
        #     current_game_state.player1.player_buttons.Y,
        #     current_game_state.player1.player_buttons.B,
        #     current_game_state.player1.player_buttons.A,
        #     current_game_state.player1.player_buttons.X,
        #     current_game_state.player1.player_buttons.L,
        #     current_game_state.player1.player_buttons.R,
        #     current_game_state.player2.player_id,
        #     current_game_state.player2.health,
        #     current_game_state.player2.x_coord,
        #     current_game_state.player2.y_coord,
        #     current_game_state.player2.is_jumping,
        #     current_game_state.player2.is_crouching,
        #     current_game_state.player2.is_player_in_move,
        #     current_game_state.player2.move_id,
        #     current_game_state.player2.player_buttons.up,
        #     current_game_state.player2.player_buttons.down,
        #     current_game_state.player2.player_buttons.right,
        #     current_game_state.player2.player_buttons.left,
        #     current_game_state.player2.player_buttons.Y,
        #     current_game_state.player2.player_buttons.B,
        #     current_game_state.player2.player_buttons.A,
        #     current_game_state.player2.player_buttons.X,
        #     current_game_state.player2.player_buttons.L,
        #     current_game_state.player2.player_buttons.R
        # ])
        
        # if(str(current_game_state.fight_result) == "P2"):
        #     with open('./my_code/player2_dataset.csv', 'a', newline='') as csvfile:
        #         writer = csv.writer(csvfile, delimiter=',')
        #         for data in data_list:
        #             writer.writerow(data)
        #     data_list.clear()
        
        # if (str(current_game_state.fight_result) == "P1"):
        #     # Write the data to a CSV file
        #     with open('./my_code/player1_dataset.csv', 'a', newline='') as csvfile:
        #         writer = csv.writer(csvfile, delimiter=',')
        #         for data in data_list:
        #             writer.writerow(data)
        #     data_list.clear()
            
        return self.my_command

    def run_command(self, com, player):

        if self.exe_code-1 == len(self.fire_code):
            self.exe_code = 0
            self.start_fire = False
            #print("compelete")
            # exit()
            # print ( "left:",player.player_buttons.left )
            # print ( "right:",player.player_buttons.right )
            # print ( "up:",player.player_buttons.up )
            # print ( "down:",player.player_buttons.down )
            # print ( "Y:",player.player_buttons.Y )

        elif len(self.remaining_code) == 0:

            self.fire_code = com
            # self.my_command=Command()
            self.exe_code += 1

            self.remaining_code = self.fire_code[0:]

        else:
            self.exe_code += 1
            if self.remaining_code[0] == "v+<":
                self.buttn.down = True
                self.buttn.left = True
                print("v+<")
            elif self.remaining_code[0] == "!v+!<":
                self.buttn.down = False
                self.buttn.left = False
                print("!v+!<")
            elif self.remaining_code[0] == "v+>":
                self.buttn.down = True
                self.buttn.right = True
                print("v+>")
            elif self.remaining_code[0] == "!v+!>":
                self.buttn.down = False
                self.buttn.right = False
                print("!v+!>")

            elif self.remaining_code[0] == ">+Y":
                self.buttn.Y = True  # not (player.player_buttons.Y)
                self.buttn.right = True
                print(">+Y")
            elif self.remaining_code[0] == "!>+!Y":
                self.buttn.Y = False  # not (player.player_buttons.Y)
                self.buttn.right = False
                print("!>+!Y")

            elif self.remaining_code[0] == "<+Y":
                self.buttn.Y = True  # not (player.player_buttons.Y)
                self.buttn.left = True
                print("<+Y")
            elif self.remaining_code[0] == "!<+!Y":
                self.buttn.Y = False  # not (player.player_buttons.Y)
                self.buttn.left = False
                print("!<+!Y")

            elif self.remaining_code[0] == ">+^+L":
                self.buttn.right = True
                self.buttn.up = True
                self.buttn.L = not (player.player_buttons.L)
                print(">+^+L")
            elif self.remaining_code[0] == "!>+!^+!L":
                self.buttn.right = False
                self.buttn.up = False
                self.buttn.L = False  # not (player.player_buttons.L)
                print("!>+!^+!L")

            elif self.remaining_code[0] == ">+^+Y":
                self.buttn.right = True
                self.buttn.up = True
                self.buttn.Y = not (player.player_buttons.Y)
                print(">+^+Y")
            elif self.remaining_code[0] == "!>+!^+!Y":
                self.buttn.right = False
                self.buttn.up = False
                self.buttn.Y = False  # not (player.player_buttons.L)
                print("!>+!^+!Y")

            elif self.remaining_code[0] == ">+^+R":
                self.buttn.right = True
                self.buttn.up = True
                self.buttn.R = not (player.player_buttons.R)
                print(">+^+R")
            elif self.remaining_code[0] == "!>+!^+!R":
                self.buttn.right = False
                self.buttn.up = False
                self.buttn.R = False  # ot (player.player_buttons.R)
                print("!>+!^+!R")

            elif self.remaining_code[0] == ">+^+A":
                self.buttn.right = True
                self.buttn.up = True
                self.buttn.A = not (player.player_buttons.A)
                print(">+^+A")
            elif self.remaining_code[0] == "!>+!^+!A":
                self.buttn.right = False
                self.buttn.up = False
                self.buttn.A = False  # not (player.player_buttons.A)
                print("!>+!^+!A")

            elif self.remaining_code[0] == ">+^+B":
                self.buttn.right = True
                self.buttn.up = True
                self.buttn.B = not (player.player_buttons.B)
                print(">+^+B")
            elif self.remaining_code[0] == "!>+!^+!B":
                self.buttn.right = False
                self.buttn.up = False
                self.buttn.B = False  # not (player.player_buttons.A)
                print("!>+!^+!B")

            elif self.remaining_code[0] == "<+^+L":
                self.buttn.left = True
                self.buttn.up = True
                self.buttn.L = not (player.player_buttons.L)
                print("<+^+L")
            elif self.remaining_code[0] == "!<+!^+!L":
                self.buttn.left = False
                self.buttn.up = False
                self.buttn.L = False  # not (player.player_buttons.Y)
                print("!<+!^+!L")

            elif self.remaining_code[0] == "<+^+Y":
                self.buttn.left = True
                self.buttn.up = True
                self.buttn.Y = not (player.player_buttons.Y)
                print("<+^+Y")
            elif self.remaining_code[0] == "!<+!^+!Y":
                self.buttn.left = False
                self.buttn.up = False
                self.buttn.Y = False  # not (player.player_buttons.Y)
                print("!<+!^+!Y")

            elif self.remaining_code[0] == "<+^+R":
                self.buttn.left = True
                self.buttn.up = True
                self.buttn.R = not (player.player_buttons.R)
                print("<+^+R")
            elif self.remaining_code[0] == "!<+!^+!R":
                self.buttn.left = False
                self.buttn.up = False
                self.buttn.R = False  # not (player.player_buttons.Y)
                print("!<+!^+!R")

            elif self.remaining_code[0] == "<+^+A":
                self.buttn.left = True
                self.buttn.up = True
                self.buttn.A = not (player.player_buttons.A)
                print("<+^+A")
            elif self.remaining_code[0] == "!<+!^+!A":
                self.buttn.left = False
                self.buttn.up = False
                self.buttn.A = False  # not (player.player_buttons.Y)
                print("!<+!^+!A")

            elif self.remaining_code[0] == "<+^+B":
                self.buttn.left = True
                self.buttn.up = True
                self.buttn.B = not (player.player_buttons.B)
                print("<+^+B")
            elif self.remaining_code[0] == "!<+!^+!B":
                self.buttn.left = False
                self.buttn.up = False
                self.buttn.B = False  # not (player.player_buttons.Y)
                print("!<+!^+!B")

            elif self.remaining_code[0] == "v+R":
                self.buttn.down = True
                self.buttn.R = not (player.player_buttons.R)
                print("v+R")
            elif self.remaining_code[0] == "!v+!R":
                self.buttn.down = False
                self.buttn.R = False  # not (player.player_buttons.Y)
                print("!v+!R")

            else:
                if self.remaining_code[0] == "v":
                    self.buttn.down = True
                    print("down")
                elif self.remaining_code[0] == "!v":
                    self.buttn.down = False
                    print("Not down")
                elif self.remaining_code[0] == "<":
                    print("left")
                    self.buttn.left = True
                elif self.remaining_code[0] == "!<":
                    print("Not left")
                    self.buttn.left = False
                elif self.remaining_code[0] == ">":
                    print("right")
                    self.buttn.right = True
                elif self.remaining_code[0] == "!>":
                    print("Not right")
                    self.buttn.right = False

                elif self.remaining_code[0] == "^":
                    print("up")
                    self.buttn.up = True
                elif self.remaining_code[0] == "!^":
                    print("Not up")
                    self.buttn.up = False
            self.remaining_code = self.remaining_code[1:]
        return
