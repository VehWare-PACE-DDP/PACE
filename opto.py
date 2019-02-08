import time
import sys
import pygame
import pandas as pd
import csv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


red = (255,0,0)
black = (0,0,0)
green = (0,255,0)

class rectObj:
	xCoord = 0
	color = red

(width, height) = (1000, 300)
screen_color = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
screen.fill(screen_color)
pygame.display.set_caption('Optokinetic Tape Test')
pygame.display.flip()



numBlocks = int(width/100)+2
blockList = []

count = 0
toggle = 0
# 0 -> red
# 1 -> black
for x in range(numBlocks):
    tempBlock = rectObj()

    if toggle == 0 :
        tempBlock.xCoord = (x*100)-100
        toggle = 1
        blockList.append(tempBlock)
        continue

    if toggle == 1 :
        tempBlock.xCoord = (x*100)-100
        tempBlock.color = black
        count += 1
        blockList.append(tempBlock)
        if count == 3 :
            count = 0
            toggle = 0



surf = pygame.Surface((300,150))
surf.fill((255,255,255))
pygame.draw.rect(surf, green, (0, 0, 300, 150), 7)
screen.blit(surf, (350, 75))

blockFile = open("blockPos.txt", "w")
eyeFile = open("eyePos.txt", "w")
dfBlock=pd.DataFrame()
dfEye=pd.DataFrame() 



running = True
speed = 5
runs = 0
forward = 1
rowNum = 1
start_time = time.time()
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	#sets num runs in each direction and flips direction when needed
	if runs == 500:
		if forward == 0:
			running = False
		runs = 0
		forward = 0
	if forward == 0:
		if speed > 0:
			time.sleep(.5)
			speed = speed*(-1)

#want to track when block in in xCoords 350 - 650
	tempBlock = rectObj()
	for block in blockList:
		pygame.draw.rect(screen, block.color, (block.xCoord, 100, 100, 100))

		if block.xCoord > 350 and block.xCoord < 650 and block.color == red:
			tempBlock = block

		block.xCoord += speed
		if block.xCoord == 1100:
			block.xCoord = -100
		if block.xCoord == -200:
			block.xCoord = 1000


        #sleep needed to fine tune speed depending on system
	time.sleep(.005)
	pygame.display.update()
	
	#updateTime = time.time()


	blockFile.write("Block in Focus Zone at Coords:\n")
	#if tempBlock.xCoord  < 350:
	if tempBlock.xCoord > 350 and tempBlock.xCoord < 650:
		#blockFile.write("%i %s %i %s %i\n" % (tempBlock.xCoord, "to", (tempBlock.xCoord+100), "at time:", (time.time() - start_time)))
		dfBlock.at[rowNum, 'X coordinate'] = tempBlock.xCoord
		dfBlock.at[rowNum, 'Y coordinate'] = tempBlock.xCoord+100
		dfBlock.at[rowNum, 'Time'] = (time.time() - start_time)
		
	mouseX,mouseY = pygame.mouse.get_pos()
	#eyeFile.write("%i%s%i %s %i\n" % (mouseX, ",", mouseY, "at time:", (time.time() - start_time)))
	dfEye.at[rowNum, 'X coordinate'] = mouseX
	dfEye.at[rowNum, 'Y coordinate'] = mouseY
		
	if (mouseX in range(350,651)):
		dfEye.at[rowNum, 'Bool'] = 1
	else:
		dfEye.at[rowNum, 'Bool'] = 0

	dfEye.at[rowNum, 'Time'] = (time.time() - start_time)
		#print(mouseX,mouseY)

	#elif tempBlock.xCoord > 550:
		#blockFile.write("%i %s %i %s %i\n" % (tempBlock.xCoord, "to", 650, "at time:", (time.time() - start_time)))
		#dfBlock.at[rowNum, 'X coordinate'] = tempBlock.xCoord
		#dfBlock.at[rowNum, 'Y coordinate'] = tempBlock.xCoord+100
		#dfBlock.at[rowNum, 'Time'] = (time.time() - start_time)
	#else:
		#blockFile.write("%i %s %i %s %i\n" % (tempBlock.xCoord, "to", (tempBlock.xCoord+100), "at time:", (time.time() - start_time)))
		#dfBlock.at[rowNum, 'X coordinate'] = tempBlock.xCoord
		#dfBlock.at[rowNum, 'Y coordinate'] = tempBlock.xCoord+100
		#dfBlock.at[rowNum, 'Time'] = (time.time() - start_time)


	runs += 1
	rowNum +=1

print()
#print('Block dataframe results:')
#print(dfBlock)
print()
#print('Eye position dataframe results:')
#print(dfEye)

dfBlock.to_csv('Block_Log.csv', encoding='utf-8')
dfEye.to_csv('Cursor_Log.csv', encoding='utf-8')



#plt.plot(dfEye.loc[:, 'Time'], dfEye.loc[:, 'Bool'], marker='*',linestyle='-',label='Test Results')
#plt.xlabel = 'Time'
#plt.ylabel = 'Accuracy'
#plt.show()













