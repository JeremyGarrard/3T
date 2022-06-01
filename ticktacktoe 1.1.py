# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:19:38 2022

@author: JeremyGarrard
"""
#class for each cell
class cell:
    def __init__(self,name,cell_index,x_cor,y_cor,value = ""): #,slow_down_mode,time_traveled,miles_traveled,finished,car_pass_count,want_to_pass,have_passed):
        #want to establish default values
        #want to extend for trucks and tractor trailers
        self.name = name
        self.cell_index  = cell_index
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.value = value
        
    def update_value(self,value):
        if self.value == "":
            self.value = value
        else:
            self.value= self.value


class player:
    def __init__(self,name,sign):
        self.name = name
        self.sign = sign
    
    def take_turn(self):
        print ("{} its time to take your turn!".format(self.name))
        cell_index = int(input ("{} enter your cell: ".format(self.name)))
        for i in cell_list:
            if i.cell_index == cell_index:
                i.value = self.sign
        output_status()
        stop_game = win_check()
        if stop_game:
            print("{} you just won the game!".format(c.name))
        return stop_game 
        
        

#function to make cells when we need them
def cell_maker(cell_index, x_cor,y_cor):
    name = 'cell:' + str(cell_index)#+ str(int(x_cor)) + "," + str(int(y_cor))
    cell_name = cell(name= name, cell_index = cell_index,x_cor = x_cor, y_cor= y_cor, value = "-")
    cell_list.append(cell_name)
    
    
#Create all the cells
cell_list = []
c=1
for x in range(3):
    for y in range(3):
        cell_maker(c,x+1,y+1)
        c+=1

#create players
player_list = []
player_1 = player ((input ("Player 1 enter your name: ")),"X")
player_list.append(player_1)
player_2 = player ((input ("Player 2 enter your name: ")),"O")
player_list.append(player_2)


def output_status():
    mini_list = []
    for x in cell_list:
        mini_list.append (x.value)
        if x.cell_index%3 == 0:
            print(mini_list)
            mini_list = []
            
def win_check():
    for x in cell_list:
        if x.cell_index == 1:
            if cell_list[1].value == x.value and cell_list[2].value == x.value:
                print("Winner!!!")
                return True
            else:
                return False
            
stop_game = False

while stop_game == False:
    c = player_1
    stop_game = c.take_turn()
    if stop_game:
        break

    
    c = player_2
    stop_game = c.take_turn()
    if stop_game:
        break

    
    
    
    