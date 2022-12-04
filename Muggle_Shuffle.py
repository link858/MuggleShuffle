import time
import pyautogui as py
from PIL import Image

print(r"""

  __  __                   _        __  __ _ _        _               
 |  \/  |                 | |      |  \/  (_| |      ( )              
 | \  / |_   _  __ _  __ _| | ___  | \  / |_| | _____|/ ___           
 | |\/| | | | |/ _` |/ _` | |/ _ \ | |\/| | | |/ / _ \ / __|          
 | |  | | |_| | (_| | (_| | |  __/ | |  | | |   |  __/ \__ \          
 |_|  |_|\__,_|\__, |\__, |_|\___| |_|__|_|_|_|\_\___| |___/__ _      
 |  \/  |       __/ | __/ | |       / ____| |          / _|/ _| |     
 | \  / |_   _ |___/ |___/| | ___  | (___ | |__  _   _| |_| |_| | ___ 
 | |\/| | | | |/ _` |/ _` | |/ _ \  \___ \| '_ \| | | |  _|  _| |/ _ \
 | |  | | |_| | (_| | (_| | |  __/  ____) | | | | |_| | | | | | |  __/
 |_|  |_|\__,_|\__, |\__, |_|\___| |_____/|_| |_|\__,_|_| |_| |_|\___|
                __/ | __/ |                                           
               |___/ |___/                                            

    """)

print('Script by Wreckin aka Muggle')
print('Check README for setup info.')
print('Warming the baby up...')







time.sleep(3)

## global variables... they are bad?
#global Total_Blue_Amount, Total_Green_Amount, Shitty_Green_Amount
# global Total_Blue_Amount
# global Total_Green_Amount
# global Shitty_Green_Amount

# Huge_Citrine_Amount = 0 
# Chalcedony_Amount = 0
# Bloodstone_Amount = 0
# Sun_Crystal_Amount = 0


# Dark_Jade_Amount = 0 
# Shadow_Crystal_Amount = 0

# Scarlet_Ruby_Amount = 0
# Monarch_Topaz_Amount = 0
# Twilight_Opal_Amount = 0
# Sky_Sapphire_Amount = 0
# Forest_Emerald_Amount = 0
# Autumns_Glow_Amount = 0


# Checks for Saronite Ore and if found prospects it and detects and counts the results till it sees there is no more saronite left
def Prospect_Mode():

    print('Scanning Inventory for Saronite...')
    time.sleep(3.5)

    Saronite_Ore_Needle = Image.open("Images/Misc/Saronite_Ore.png", 'r')
    Saronite_Ore_Location = py.locateOnScreen(Saronite_Ore_Needle,confidence=.96)
    
    No_Saronite_Needle = Image.open("Images/Misc/No_Saronite.png", 'r')
    No_Saronite_Location = py.locateOnScreen(No_Saronite_Needle,confidence=0.95)
    Autumns_Glow_Count_Needle = Image.open("Images/Blue_Gems/Autumns_Glow_Count.png", 'r')
    Scarlet_Ruby_Count_Needle = Image.open("Images/Blue_Gems/Scarlet_Ruby_Count.png", 'r')
    Monarch_Topaz_Count_Needle = Image.open("Images/Blue_Gems/Monarch_Topaz_Count.png", 'r')
    Twilight_Opal_Count_Needle = Image.open("Images/Blue_Gems/Twilight_Opal_Count.png", 'r')
    Sky_Sapphire_Count_Needle = Image.open("Images/Blue_Gems/Sky_Sapphire_Count.png", 'r')
    Forest_Emerald_Count_Needle = Image.open("Images/Blue_Gems/Forest_Emerald_Count.png", 'r')

    
    Dark_Jade_Count_Needle = Image.open("Images/Green_Gems/Dark_Jade_Count.png", 'r')
    Shadow_Crystal_Count_Needle = Image.open("Images/Green_Gems/Shadow_Crystal_Count.png", 'r')
    Huge_Citrine_Count_Needle = Image.open("Images/Green_Gems/Huge_Citrine_Count.png", 'r')
    Chalcedony_Count_Needle = Image.open("Images/Green_Gems/Chalcedony_Count.png", 'r')
    Bloodstone_Count_Needle = Image.open("Images/Green_Gems/Bloodstone_Count.png", 'r')
    Sun_Crystal_Count_Needle = Image.open("Images/Green_Gems/Sun_Crystal_Count.png", 'r')
    
    Total_Blue_Amount = 0
    Total_Green_Amount = 0
    Shitty_Green_Amount = 0

    Huge_Citrine_Amount = 0 
    Chalcedony_Amount = 0
    Bloodstone_Amount = 0
    Sun_Crystal_Amount = 0


    Dark_Jade_Amount = 0 
    Shadow_Crystal_Amount = 0

    Scarlet_Ruby_Amount = 0
    Monarch_Topaz_Amount = 0
    Twilight_Opal_Amount = 0
    Sky_Sapphire_Amount = 0
    Forest_Emerald_Amount = 0
    Autumns_Glow_Amount = 0

    while Saronite_Ore_Location:
        print('Found Saronite')
        No_Saronite_Location = py.locateOnScreen(No_Saronite_Needle,confidence=0.95)
        if No_Saronite_Location:
            print('No More Saronite' + '\n***************')
            break
        else:
            print('Prospecting Item' + '\n***************')
            
            py.press('2')

            time.sleep(2.1)
        

            # Saronite_Ore_Location = py.locateOnScreen(Saronite_Ore_Needle,confidence=0.95)

            Autumns_Glow_Count_Location = py.locateOnScreen(Autumns_Glow_Count_Needle,confidence=0.95)
            Scarlet_Ruby_Count_Location = py.locateOnScreen(Scarlet_Ruby_Count_Needle,confidence=0.95)
            Monarch_Topaz_Count_Location = py.locateOnScreen(Monarch_Topaz_Count_Needle,confidence=0.95)
            Twilight_Opal_Count_Location = py.locateOnScreen(Twilight_Opal_Count_Needle,confidence=0.95)
            Sky_Sapphire_Count_Location = py.locateOnScreen(Sky_Sapphire_Count_Needle,confidence=0.95)
            Forest_Emerald_Count_Location = py.locateOnScreen(Forest_Emerald_Count_Needle,confidence=0.95)


            Dark_Jade_Count_Location = py.locateOnScreen(Dark_Jade_Count_Needle,confidence=0.95)
            Shadow_Crystal_Count_Location = py.locateOnScreen(Shadow_Crystal_Count_Needle,confidence=0.95)
            Huge_Citrine_Count_Location = py.locateOnScreen(Huge_Citrine_Count_Needle,confidence=0.95)
            Chalcedony_Count_Location = py.locateOnScreen(Chalcedony_Count_Needle,confidence=0.95)
            Bloodstone_Count_Location = py.locateOnScreen(Bloodstone_Count_Needle,confidence=0.95)
            Sun_Crystal_Count_Location = py.locateOnScreen(Sun_Crystal_Count_Needle,confidence=0.95)
            
            # Check and Count Blue Gems
            if Autumns_Glow_Count_Location or Scarlet_Ruby_Count_Location or Monarch_Topaz_Count_Location or Twilight_Opal_Count_Location or Sky_Sapphire_Count_Location or Forest_Emerald_Count_Location:
                Total_Blue_Amount+=1
                print('**************')
                # print('Counted: Blue Gem')
                # print('Total Blue Gems: ' + str(Total_Blue_Amount))
                if Autumns_Glow_Count_Location:
                    Autumns_Glow_Amount+=1
                    print('Counted: Autumn\'s Glow')
                if Scarlet_Ruby_Count_Location:
                    Scarlet_Ruby_Amount+=1
                    print('Counted: Scarlet Ruby')  
                if Monarch_Topaz_Count_Location:
                    Monarch_Topaz_Amount+=1
                    print('Counted: Monarch Topaz')
                if Twilight_Opal_Count_Location:
                    Twilight_Opal_Amount+=1
                    print('Counted: Twilight Opal')
                if Sky_Sapphire_Count_Location:
                    Sky_Sapphire_Amount+=1
                    print('Counted: Sky Sapphire')
                if Forest_Emerald_Count_Location:
                    Forest_Emerald_Amount+=1
                    print('Counted: Forest Emerald')


            #check and count Green Gems
            if Huge_Citrine_Count_Location or Chalcedony_Count_Location or Bloodstone_Count_Location or Sun_Crystal_Count_Location:
                Total_Green_Amount+=1
                print('**************')
                # print('Counted: Green Gem')
                # print('Total Green Gems: ' + str(Total_Green_Amount))
                if Huge_Citrine_Count_Location:
                    Huge_Citrine_Amount+=1
                    print('Counted: Huge Citrine')
                if Chalcedony_Count_Location:
                    Chalcedony_Amount+=1
                    print('Counted: Chalcedony')  
                if Bloodstone_Count_Location:
                    Bloodstone_Amount+=1
                    print('Counted: Bloodstone')
                if Sun_Crystal_Count_Location:
                    Sun_Crystal_Amount+=1
                    print('Counted: Sun Crystal')
            if Dark_Jade_Count_Location or Shadow_Crystal_Count_Location:
                Shitty_Green_Amount+=1
                if Dark_Jade_Count_Location:
                    Dark_Jade_Amount+=1
                    print('Counted: Dark Jade')
                if Shadow_Crystal_Count_Location:
                    Shadow_Crystal_Amount+=1
                    print('Counted: Shadow Crystal')

    print('Done Prospecting' + '\n***************')
    print('  BLUE GEMS')
    print(f'Scarlet Ruby: {Scarlet_Ruby_Amount}')
    print(f'Monarch Topaz: {Monarch_Topaz_Amount}')
    print(f'Twilight Opal: {Twilight_Opal_Amount}')
    print(f'Sky Sapphire: {Sky_Sapphire_Amount}')
    print(f'Forest Emerald: {Forest_Emerald_Amount}')
    print(f'Autumn Glow: {Autumns_Glow_Amount}')
    print(f'Total Blue Gems: {Total_Blue_Amount}' + '\n***************')
    

    print('  GREEN GEMS')
    print('Huge Citrine: ' + str(Huge_Citrine_Amount))
    print('Chalcedony: ' + str(Chalcedony_Amount))
    print('Bloodstone: ' + str(Bloodstone_Amount))
    print('Sun Crystal: ' + str(Sun_Crystal_Amount))
    print('Total Green Gems: ' + str(Total_Green_Amount) + '\n***************')

    print('  SHIT GEMS')
    print('Dark Jade: ' + str(Dark_Jade_Amount))
    print('Shadow Crystal: ' + str(Shadow_Crystal_Amount))
    print('Total Shit Gems: ' + str(Shitty_Green_Amount) + '\n***************')
    # Green_Craft_Mode()
    
    
    if No_Saronite_Location:
        print('No Saronite' + '\n***************')    
        Blue_List = [Total_Blue_Amount, Scarlet_Ruby_Amount, Monarch_Topaz_Amount, Twilight_Opal_Amount, Sky_Sapphire_Amount, Forest_Emerald_Amount, Autumns_Glow_Amount]
        Green_Craft_Mode(Total_Green_Amount, Huge_Citrine_Amount, Chalcedony_Amount, Bloodstone_Amount, Sun_Crystal_Amount, Blue_List)
    


## GREEN CRAFT MODE CRAFT GREENS BASED ON AMOUNT SEND MAIL IF INV GETS FULL
def Green_Craft_Mode(Greens, Citrines, Chalcedonys, Bloodstones, Sun_Crystals, Blue_List):
    Total_Greens = Greens
    Total_Blues = Blue_List
    Total_Huge_Citrine = Citrines
    Total_Chalcedony = Chalcedonys
    Total_Bloodstones = Bloodstones
    Total_Sun_Crystals = Sun_Crystals
    loop_Huge = 0
    loop_Chalce = 0
    loop_Blood = 0
    loop_Sun = 0
    Missing_Crystal_Needle = Image.open("Images/Green_Gems/Missing_Crystal.png", 'r')
    Missing_Eternal_Earth_Needle = Image.open("Images/Green_Gems/No_Eternal_Earth.png", 'r')
    Inventory_Full_Needle = Image.open("Images/Misc/Inventory_Full.png", 'r')
    
    
    print('Entering Green Craft Mode')
    print(f'Greens Counted: {Total_Greens}')
    #print(f'Blues Counted: {Total_Blues}')
    
    time.sleep(3)
    py.keyDown('shift')
    py.press('2')
    py.keyUp('shift')
    
    # Sun Rock Ring Loop GOES ON '4' DEFAULT
    print(f'Suns Counted: {Total_Sun_Crystals}')
    while loop_Sun < Total_Sun_Crystals:
        
        Missing_Eternal_Earth_Location = py.locateOnScreen(Missing_Eternal_Earth_Needle,confidence=0.95)
        
        if Missing_Eternal_Earth_Location:
            print('No Eternal Earths')
            break
        else:
            
            py.press('4')

            Missing_Crystal_Location = py.locateOnScreen(Missing_Crystal_Needle,confidence=0.55)
            if Missing_Crystal_Location:
                print('Crystallized Earth Missing')
                print('Pressing Earth Button')
                py.press('8', 4, 0.4)
                loop_Sun-=1


            time.sleep(5)
            Inventory_Full_Location = py.locateOnScreen(Inventory_Full_Needle,confidence=0.5)
            if Inventory_Full_Location:
                print('Inventory is Full')
                Send_Disenchant_Mode()

            loop_Sun+=1
            print(f'Created Sun Rock Ring: #{loop_Sun}')
            
    
    # Huge Citrine Necklace Loop GOES ON '5' DEFAULT
    print(f'Citrine Counted: {Total_Huge_Citrine}')
    while loop_Huge < Total_Huge_Citrine:
        
        Missing_Eternal_Earth_Location = py.locateOnScreen(Missing_Eternal_Earth_Needle,confidence=0.95)
        
        if Missing_Eternal_Earth_Location:
            print('No Eternal Earths')
            break
        else:
            
            py.press('5')

            Missing_Crystal_Location = py.locateOnScreen(Missing_Crystal_Needle,confidence=0.55)
            if Missing_Crystal_Location:
                print('Crystallized Earth Missing')
                print('Pressing Earth Button')
                py.press('8', 4, 0.4)
                loop_Huge-=1
            
            time.sleep(5)
            Inventory_Full_Location = py.locateOnScreen(Inventory_Full_Needle,confidence=0.5)
            if Inventory_Full_Location:
                print('Inventory is Full')
                Send_Disenchant_Mode()
            
            loop_Huge+=1
            print(f'Created Crystal Citrine Necklace: #{loop_Huge}')
            
    # Chalcedony Amulet loop GOES ON '6' DEFAULT
    print(f'Chalcedony Counted: {Total_Chalcedony}')
    while loop_Chalce < Total_Chalcedony:
        
        Missing_Eternal_Earth_Location = py.locateOnScreen(Missing_Eternal_Earth_Needle,confidence=0.95)
        
        if Missing_Eternal_Earth_Location:
            print('No Eternal Earths')
            break
        else:
            
            py.press('6')

            Missing_Crystal_Location = py.locateOnScreen(Missing_Crystal_Needle,confidence=0.55)
            if Missing_Crystal_Location:
                print('Crystallized Earth Missing')
                print('Pressing Earth Button')
                py.press('8', 4, 0.4)
                loop_Chalce-=1
            
            time.sleep(5)
            Inventory_Full_Location = py.locateOnScreen(Inventory_Full_Needle,confidence=0.5)
            if Inventory_Full_Location:
                print('Inventory is Full')
                Send_Disenchant_Mode()
                
            loop_Chalce+=1
            print(f'Created Crystal Chalcedony Amulet: #{loop_Chalce}')
    
    
    # Bloodstone Ring Loop GOES ON '8' DEFAULT
    print(f'Bloodstone Counted: {Total_Bloodstones}')
    while loop_Blood < Total_Bloodstones:
        
        Missing_Eternal_Earth_Location = py.locateOnScreen(Missing_Eternal_Earth_Needle,confidence=0.95)
        
        if Missing_Eternal_Earth_Location:
            print('No Eternal Earths')
            break
        else:
            
            py.press('7')

            Missing_Crystal_Location = py.locateOnScreen(Missing_Crystal_Needle,confidence=0.55)
            if Missing_Crystal_Location:
                print('Crystallized Earth Missing')
                print('Pressing Earth Button')
                py.press('8', 4, 0.4)
                loop_Blood-=1
            
            
            time.sleep(5)
            Inventory_Full_Location = py.locateOnScreen(Inventory_Full_Needle,confidence=0.5)
            if Inventory_Full_Location:
                print('Inventory is Full')
                Send_Disenchant_Mode()
            
            loop_Blood+=1
            print(f'Created Bloodstone Band: #{loop_Blood}')

    print('Done with Greens')
    Blue_Cut_Mode(Total_Blues)    



def Blue_Cut_Mode(Blue_Amount_List):
    print('Entering Blue Cut Mode')
    py.keyDown('shift')
    py.press('3')
    py.keyUp('shift')
    Blue_List = Blue_Amount_List
    Total_Blues = Blue_List[0]
    Scarlet_Amount = Blue_List[1]
    Monarch_Amount = Blue_List[2]
    Twilight_Amount = Blue_List[3]
    Sky_Sapph_Amount = Blue_List[4]
    Forest_Amount = Blue_List[5]
    Autumn_Amount = Blue_List[6]
    loop_Scarlet = 0
    loop_Twilight = 0
    loop_Monarch = 0
    loop_Sky = 0
    loop_Forest = 0
    loop_Autumn = 0
    Inventory_Full_Needle = Image.open("Images/Misc/Inventory_Full.png", 'r')
    
    print(f"Total Blues: {Total_Blues}" + '\n**********')
    
    print(f'Scarlets Counted: {Scarlet_Amount}')





    # CREATE TWILIGHT OPAL CUT '1' BY DEFAULT
    print(f'Twilight Opals Counted: {Twilight_Amount}' + '\n**********')
    while loop_Twilight < Twilight_Amount:
        
            py.press('1')

            time.sleep(5)

            Inventory_Full_Location = py.locateOnScreen(Inventory_Full_Needle,confidence=0.5)
            if Inventory_Full_Location:
                print('Inventory is Full')
                Send_Disenchant_Mode()

            loop_Twilight+=1
            print(f'Created Twilight Opal Cut: #{loop_Twilight}')


    # CREATE MONARCH CUTS.. '2' and '3' DEFAULT
    print(f'Monarch Topaz Counted: {Monarch_Amount}' + '\n**********')
    while loop_Monarch < Monarch_Amount:
        
            py.press('2')

            time.sleep(5)

            Inventory_Full_Location = py.locateOnScreen(Inventory_Full_Needle,confidence=0.5)
            if Inventory_Full_Location:
                print('Inventory is Full')
                Send_Disenchant_Mode()

            loop_Monarch+=1
            print(f'Created Monarch Topaz Cut: #{loop_Monarch}')

            py.press('3')
            time.sleep(5)
            Inventory_Full_Location = py.locateOnScreen(Inventory_Full_Needle,confidence=0.5)
            if Inventory_Full_Location:
                print('Inventory is Full')
                Send_Disenchant_Mode()
            
            loop_Monarch+=1
            print(f'Created Monarch Topaz Cut: #{loop_Monarch}')
    
    # CREATE FOREST EMERALD CUTS '4' and '5' DEFAULT
    print(f'Forest Emerald Counted: {Forest_Amount}' + '\n**********')
    while loop_Forest < Forest_Amount:
        
            py.press('4')

            time.sleep(5)

            Inventory_Full_Location = py.locateOnScreen(Inventory_Full_Needle,confidence=0.5)
            if Inventory_Full_Location:
                print('Inventory is Full')
                Send_Disenchant_Mode()

            loop_Forest+=1
            print(f'Created Forest Emerald Cut: #{loop_Forest}')

            py.press('5')
            time.sleep(5)
            Inventory_Full_Location = py.locateOnScreen(Inventory_Full_Needle,confidence=0.5)
            if Inventory_Full_Location:
                print('Inventory is Full')
                Send_Disenchant_Mode()
            
            loop_Forest+=1
            print(f'Created Forest Emerald Cut: #{loop_Forest}')
    
    # CREATE SKY SAPPHIRE CUTS '6' DEFAULT
    print(f'Sky Sapphire Counted: {Sky_Sapph_Amount}' + '\n**********')
    while loop_Sky < Sky_Sapph_Amount:
        
            py.press('6')

            time.sleep(5)

            Inventory_Full_Location = py.locateOnScreen(Inventory_Full_Needle,confidence=0.5)
            if Inventory_Full_Location:
                print('Inventory is Full')
                Send_Disenchant_Mode()

            loop_Sky+=1
            print(f'Created Sky Sapphire Cut: #{loop_Sky}')
    Go_To_AH_Post_Mode(ah_loops)
    # # CREATE SCARLET RUBY CUTS '7' DEFAULT
    # while loop_Scarlet < Scarlet_Amount:
        
    #         py.press('7')

    #         time.sleep(5)

    #         Inventory_Full_Location = py.locateOnScreen(Inventory_Full_Needle,confidence=0.5)
    #         if Inventory_Full_Location:
    #             print('Inventory is Full')
    #             Send_Disenchant_Mode()

    #         loop_Scarlet+=1
    #         print(f'Created Scarlet Ruby Cut: #{loop_Scarlet}')

    # # CREATE AUTUMN GLOW CUTS '8' DEFAULT
    # while loop_Autumn < Autumn_Amount:
        
    #         py.press('8')

    #         time.sleep(5)

    #         Inventory_Full_Location = py.locateOnScreen(Inventory_Full_Needle,confidence=0.5)
    #         if Inventory_Full_Location:
    #             print('Inventory is Full')
    #             Send_Disenchant_Mode()

    #         loop_Autumn+=1
    #         print(f'Created Autumn Glow Cut: #{loop_Autumn}')

    




def Go_To_AH_Post_Mode(looplimit):

    i = 0
    print('Pathing to AH')
    py.keyDown('shift')
    py.press('2')
    py.keyUp('shift') 
    time.sleep(3)
    py.keyDown('d')
    time.sleep(0.55)
    py.keyUp('d')
    print('derp')

    time.sleep(0.5)

    py.keyDown('w')
    time.sleep(1.5)
    py.keyUp('w')

    time.sleep(0.25)

    py.press('0')
    time.sleep(0.25)
    py.press('f')
    time.sleep(12)

    time.sleep(2)
    while i < looplimit:
        print(f'Entering Post Mode for {i}/{looplimit} cycles')
        Post_Mode()
        i+=1

    # py.keyDown('w')
    # py.countdown(5)
    # py.keyUp('w')








def Post_Mode():
    print('Scanning Inventory...')
    run_post_scan = Image.open("Images/AH/run_post_scan.png",'r')
    run_post_scan_location = py.locateOnScreen(run_post_scan,confidence=0.7)
    py.moveTo(run_post_scan_location, None, 0.5)
    time.sleep(.5)
    py.leftClick()
    time.sleep(7)
    Check_Post_Button()


def Check_Post_Button():

    print('Looking for items to post...')
    skip_button = Image.open("Images/AH/skip_button.png",'r')
    skip_button_location = py.locateOnScreen(skip_button)
    done_posting_button2 = Image.open("Images/AH/done_posting_button2.png",'r')

    while skip_button_location:
        done_posting_button_location = py.locateOnScreen(done_posting_button2,confidence=0.80)
        if done_posting_button_location:
            break
        else:
            print('Posting Item')
            time.sleep(.30)
            py.press('3')
    print('Done posting')
    Exit_Scan_Mode()
        
    
def Exit_Scan_Mode():
    print('Exiting Scan')
    exit_scan_button = Image.open("Images/AH/exit_scan_button.png",'r')
    exit_scan_button_location = py.locateOnScreen(exit_scan_button, confidence=.8)
    py.moveTo(exit_scan_button_location, None, 0.5)
    time.sleep(.5)
    py.leftClick()

    Under_Cut_Mode()


def Under_Cut_Mode():
    print('Undercut Mode')
    run_cancel_scan = Image.open("Images/AH/run_cancel_scan.png",'r')
    run_cancel_scan_location = py.locateOnScreen(run_cancel_scan, confidence=.8)
    py.moveTo(run_cancel_scan_location, None, 0.5)
    time.sleep(.5)
    py.leftClick()
    print('Sleeping for 10 seconds to allow scan to complete')
    time.sleep(10)    
    Under_Cut_Post_Mode()


def Under_Cut_Post_Mode():
    print('Time to Undercut!')
    print(f'Undercut Limit: {undercut_limit}')
    items_canceled = 0
    # items_skipped = 0
    
    skip_button = Image.open("Images/AH/skip_button.png",'r')
    
    done_posting_button = Image.open("Images/AH/done_posting_button.png",'r')
    exit_scan_button = Image.open("Images/AH/exit_scan_button.png",'r')
    exit_scan_button_location = py.locateOnScreen(exit_scan_button, confidence=.8)
    done_posting_button_location = py.locateOnScreen(done_posting_button)
    skip_button_location = py.locateOnScreen(skip_button)

    while skip_button_location:

        done_posting_button_location = py.locateOnScreen(done_posting_button)
        if done_posting_button_location:
            print('Exiting Scan')
            exit_scan_button_location = py.locateOnScreen(exit_scan_button, confidence=.8)
            py.moveTo(exit_scan_button_location)
            time.sleep(.5)
            py.leftClick()
            break

        else:
            print('Cancelling Undercut Post')
            items_canceled+= 1
            time.sleep(0.3)
            py.press('3')
                

            if items_canceled >= undercut_limit:
                print(f'Cancel Limit Reached: {items_canceled} of {undercut_limit}')
                Mailbox_Mode()
            # else:
            #     items_skipped = items_skipped + 1
            #     skip_button_location = py.locateOnScreen(skip_button,confidence=0.9)
            #     py.moveTo(skip_button_location)
            #     py.leftClick()
            #     new_mouse_location = py.center(skip_button_location)
            #     new_mouse_location = (new_mouse_location.x + 100, new_mouse_location.y )
            #     py.moveTo(new_mouse_location)
    print(f'\nItems Canceled: {items_canceled}')



def Go_To_AH_Normal():
    
    print('Pathing back to AH')
    time.sleep(3)
    py.keyDown('shift')
    py.press('2')
    py.keyUp('shift')
    time.sleep(0.4) 
    py.keyDown('d')
    time.sleep(0.55)
    py.keyUp('d')
    print('derp')

    time.sleep(0.5)

    py.keyDown('w')
    time.sleep(1.5)
    py.keyUp('w')

    time.sleep(0.25)

    py.press('0')
    time.sleep(0.25)
    py.press('f')
    time.sleep(12)

    time.sleep(2)

    Mailbox_Mode()






def Mailbox_Mode():
    Cancel_Button_Needle = Image.open("Images/Mail_Box/Cancel_Mail_Button.png", 'r')
    print('Entering MailBoxMode')
    time.sleep(2)
    py.keyDown('d')
    time.sleep(0.88)
    py.keyUp('d')
    print('derp')

    time.sleep(0.5)

    py.keyDown('w')
    time.sleep(5)
    py.keyUp('w')
    py.press('-')
    time.sleep(0.25)
    py.press('f')
    time.sleep(12)
    Check_Mailbox_Click()
    time.sleep(2.5)
    print('Grabbing Cancelled Auctions')
    Cancel_Button_Location = py.locateOnScreen(Cancel_Button_Needle,confidence=0.9)
    py.moveTo(Cancel_Button_Location)
    py.rightClick()
    time.sleep(11)
    Go_To_AH_Normal()



    

    
    return()






    
    




def Send_Disenchant_Mode():
    time.sleep(1)
    # Mailbox_Needle = Image.open("Images/Mail_Box/Mailbox_flag.png", 'r')
    
    Mail_Other_Button_Needle = Image.open("Images/Mail_Box/Mail_Other_Button.png", 'r')
    Send_Disenchant_Button_Needle = Image.open("Images/Mail_Box/Send_Disenchant_Button.png", 'r')
   
    # Check_Mailbox_Click()
    image_found = Check_Mailbox_Click();
    if image_found:
            time.sleep(0.5)
            Mail_Other_Button_Needle_Location = py.locateOnScreen(Mail_Other_Button_Needle,confidence=0.95)
            py.moveTo(Mail_Other_Button_Needle_Location, None, 0.5)
            py.click()

            Send_Disenchant_Button_Needle_Location = py.locateOnScreen(Send_Disenchant_Button_Needle,confidence=0.95)
            py.moveTo(Send_Disenchant_Button_Needle_Location, None, 0.5)
            py.click()
            time.sleep(6)
            py.press('escape')
    else:
        print('Couldnt Find MailBox, Check Confidence level or Take new/Make more needles')
    




def Check_Mailbox_Click():
    print('Searching for Mail_Box')
    IF_Mailbox_Needle0 = Image.open("Images/Mail_Box/IF_Mail_Box.png", 'r')
    IF_Mailbox_Needle1 = Image.open("Images/Mail_Box/IF_Mail_Box1.png", 'r')
    IF_Mailbox_Needle2 = Image.open("Images/Mail_Box/IF_Mail_Box2.png", 'r')
    IF_Mailbox_Needle3 = Image.open("Images/Mail_Box/IF_Mail_Box3.png", 'r')
    IF_Mailbox_Needle4 = Image.open("Images/Mail_Box/IF_Mail_Box4.png", 'r')
    IF_Mailbox_Needle5 = Image.open("Images/Mail_Box/IF_Mail_Box5.png", 'r')
    IF_Mailbox_Needle6 = Image.open("Images/Mail_Box/IF_Mail_Box6.png", 'r')
    IF_Mailbox_Needle7 = Image.open("Images/Mail_Box/IF_Mail_Box7.png", 'r')
    IF_Mailbox_Needle8 = Image.open("Images/Mail_Box/IF_Mail_Box8.png", 'r')
    
    time.sleep(1)
    image_list = [IF_Mailbox_Needle0, IF_Mailbox_Needle1, IF_Mailbox_Needle2, IF_Mailbox_Needle3, IF_Mailbox_Needle4, IF_Mailbox_Needle5, IF_Mailbox_Needle6, IF_Mailbox_Needle7, IF_Mailbox_Needle8]
    # Loop through list to find all the images
    for image in image_list:
        
        image_found = py.locateOnScreen(image,confidence=0.65)
        if image_found:
            print('Found Mailbox')
            py.moveTo(image_found, None, 0.5)
            py.rightClick()
            break
        else:
            print('Searching...')
    return(image_found)
    

    
        


loops = input('Enter a number of loop cycles for the entire script: ')
ah_loops = input('Enter AH loop Limit: ')
undercut_limit = input('Enter Undercut Cancel Limit to go to mailbox: ')
loops = int(loops)
ah_loops = int(ah_loops)
undercut_limit = int(undercut_limit)

for i in range(loops):
    # Mailbox_Mode()
    #Send_Disenchant_Mode()
    # Go_To_AH_Normal()
    Prospect_Mode()
    # py.displayMousePosition()
    i = i + 1
    if i == 1:
        print('This script has cycled {} time\n'.format(i))
    else:
        print('This script has cycled {} times'.format(i))

