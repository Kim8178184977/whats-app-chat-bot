import pyautogui as pc
import pyperclip as pt
from time import sleep
from whats_bot import respose

class whats_app :
    
    def __init__(self,speed = 0.5,click_speed = 0.3):
        self.speed = speed
        self.click_speed = click_speed
        self.messege = ''
        self.last_messege = ''

    def nav_green_dot(self):
        try:
            position = pc.locateOnScreen('D:\chatbot\Screenshot 2022-09-14 164355.png',confidence = 0.5)
            pc.moveTo(position[0:2],duration=self.speed)
            pc.moveRel(-200,0,duration=self.speed)
            pc.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Error in nav_green_dot',e)
            
    def nav_input_box (self):
        try:
            position = pc.locateOnScreen('D:\chatbot\Screenshot 2022-09-17 153035.png')
            pc.moveTo(position[0:2],duration=self.speed)
            pc.moveRel((100,10),duration=self.speed)
            pc.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Error in nav_input_box',e)
    def nav_message(self):
        try:
            position = pc.locateOnScreen('D:\chatbot\Screenshot 2022-09-17 153035.png')
            pc.moveTo(position[0:2],duration=self.speed)
            pc.moveRel((70,-50),duration=self.speed)
        except Exception as e:
            print('Error in nav_messege',e)
    def get_messege(self):
        pc.tripleClick(interval=self.click_speed)
        pc.rightClick(interval=self.click_speed)
        pc.moveRel((10,10),duration=self.speed)
        pc.rightClick(interval=self.click_speed)
        self.messege = pt.paste()
        print('user says :-',self.messege)
    def input_message(self):
        try:
            position = pc.locateOnScreen('D:\chatbot\Screenshot 2022-09-17 153035.png',confidence = 0.5)
            pc.moveTo(position[0:2],duration=self.speed)
            pc.moveRel(200,20,duration=self.speed)
            pc.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Error in nav_green_dot',e)
    def send_message(self):
        try:
            if self.messege != self.last_messege :
                bot_responses = respose(self.messege)
                print('you say :- ',bot_responses)
                pc.typewrite(bot_responses,interval=.2)
                pc.typewrite('\n')
                self.last_messege = self.messege
        except Exception as e:
            print('Error in send message',e)
    def nav_x(self):
        try:
            position = pc.locateOnScreen('D:\chatbot\Screenshot 2022-09-17 171724.png',confidence=0.7)
            pc.moveTo(position[0:2],duration=self.speed)
            pc.moveRel((12,12),duration=self.speed)
            pc.click(interval=self.speed)
        except Exception as e:
            print('Error in nav_x',e)


while True:
    wa_bot = whats_app(speed=0.5,click_speed=0.3)
    sleep(2)
    wa_bot.nav_green_dot()
    wa_bot.nav_x()
    wa_bot.nav_input_box()
    wa_bot.nav_message()
    wa_bot.get_messege()
    wa_bot.input_message()
    wa_bot.send_message() 

    sleep(5)
