
import pygame, sys
from pygame.locals import *
pygame.init()

# Settings
WIDTH = 500
HEIGHT = 500
FPS = 60

# Screen Setup
WINDOW = pygame.display.set_mode([WIDTH,HEIGHT])
CAPTION = pygame.display.set_caption('SUDOKU')
SCREEN = pygame.display.get_surface()
TRANSPARENT = pygame.Surface([WIDTH,HEIGHT])
TRANSPARENT.set_alpha(0)
TRANSPARENT.fill((255,0,0))

# Misc stuff
validate_num=[]
validate_rect=[]
existing_pos=[2,3,4,8,13,14,17,18,21,23,26,27,28,31,34,36,37,38,39,40,44,48,51,52,54,55,56,57,58,59,60,62,63,68,70,72,73,74,75,78]
validate_pos=[]
rect_list=[]
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (0,0, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (0,30, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (0,60, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (0,95, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (0,125, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (0,155, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (0,190, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (0,220, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (0,250, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (30,0, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (30,30, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (30,60, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (30,95, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (30,125, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (30,155, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (30,190, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (30,220, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (30,250, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (60,0, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (60,30, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (60,60, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (60,95, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (60,125, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (60,155, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (60,190, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (60,220, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (60,250, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (95,0, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (95,30, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (95,60, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (95,95, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (95,125, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (95,155, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (95,190, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (95,220, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (95,250, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (125,0, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (125,30, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (125,60, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (125,95, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (125,125, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (125,155, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (125,190, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (125,220, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (125,250, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (155,0, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (155,30, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (155,60, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (155,95, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (155,125, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (155,155, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (155,190, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (155,220, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (155,250, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (190,0, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (190,30, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (190,60, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (190,95, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (190,125, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (190,155, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (190,190, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (190,220, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (190,250, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (220,0, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (220,30, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (220,60, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (220,95, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (220,125, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (220,155, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (220,190, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (220,220, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (220,250, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (250,0, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (250,30, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (250,60, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (250,95, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (250,125, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (250,155, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (250,190, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (250,220, 25, 25)))
rect_list.append(pygame.draw.rect(SCREEN, (255, 255, 255), (250,250, 25, 25)))

# initialize font; 
myfont = pygame.font.SysFont("monospace", 15)

# render text
text1 = SCREEN.blit(myfont.render("9", 1, (255,0,0)), (6, 66))
text2 = SCREEN.blit(myfont.render("4", 1, (255,0,0)), (6, 101))
text3 = SCREEN.blit(myfont.render("8", 1, (255,0,0)), (6, 131))
text4 = SCREEN.blit(myfont.render("7", 1, (255,0,0)), (6, 256))
text5 = SCREEN.blit(myfont.render("5", 1, (255,0,0)), (36, 131))
text6 = SCREEN.blit(myfont.render("3", 1, (255,0,0)), (36, 161))
text7 = SCREEN.blit(myfont.render("1", 1, (255,0,0)), (36, 256))
text8 = SCREEN.blit(myfont.render("5", 1, (255,0,0)), (66, 6))
text9 = SCREEN.blit(myfont.render("1", 1, (255,0,0)), (66, 101))
text10 = SCREEN.blit(myfont.render("2", 1, (255,0,0)), (66, 161))
text11 = SCREEN.blit(myfont.render("4", 1, (255,0,0)), (66, 256))
text12 = SCREEN.blit(myfont.render("7", 1, (255,0,0)), (101, 6))
text13 = SCREEN.blit(myfont.render("3", 1, (255,0,0)), (101, 36))
text14 = SCREEN.blit(myfont.render("4", 1, (255,0,0)), (101, 131))
text15 = SCREEN.blit(myfont.render("2", 1, (255,0,0)), (101, 226))
text16 = SCREEN.blit(myfont.render("6", 1, (255,0,0)), (131, 6))
text17 = SCREEN.blit(myfont.render("1", 1, (255,0,0)), (131, 36))
text18 = SCREEN.blit(myfont.render("5", 1, (255,0,0)), (131, 66))
text19 = SCREEN.blit(myfont.render("7", 1, (255,0,0)), (131, 101))
text20 = SCREEN.blit(myfont.render("2", 1, (255,0,0)), (131, 131))
text21 = SCREEN.blit(myfont.render("3", 1, (255,0,0)), (131, 256))
text22 = SCREEN.blit(myfont.render("6", 1, (255,0,0)), (161, 101))
text23 = SCREEN.blit(myfont.render("5", 1, (255,0,0)), (161, 196))
text24 = SCREEN.blit(myfont.render("7", 1, (255,0,0)), (161, 226))
text25 = SCREEN.blit(myfont.render("3", 1, (255,0,0)), (196, 6))
text26 = SCREEN.blit(myfont.render("5", 1, (255,0,0)), (196, 36))
text27 = SCREEN.blit(myfont.render("6", 1, (255,0,0)), (196, 66))
text28 = SCREEN.blit(myfont.render("8", 1, (255,0,0)), (196, 101))
text29 = SCREEN.blit(myfont.render("9", 1, (255,0,0)), (196, 131))
text30 = SCREEN.blit(myfont.render("7", 1, (255,0,0)), (196, 161))
text31 = SCREEN.blit(myfont.render("4", 1, (255,0,0)), (196, 196))
text32 = SCREEN.blit(myfont.render("2", 1, (255,0,0)), (196, 256))
text33 = SCREEN.blit(myfont.render("9", 1, (255,0,0)), (226, 6))
text34 = SCREEN.blit(myfont.render("4", 1, (255,0,0)), (226, 161))
text35 = SCREEN.blit(myfont.render("3", 1, (255,0,0)), (226, 226))
text36 = SCREEN.blit(myfont.render("2", 1, (255,0,0)), (256, 6))
text37 = SCREEN.blit(myfont.render("4", 1, (255,0,0)), (256, 36))
text38 = SCREEN.blit(myfont.render("7", 1, (255,0,0)), (256, 66))
text39 = SCREEN.blit(myfont.render("3", 1, (255,0,0)), (256, 101))
text40 = SCREEN.blit(myfont.render("6", 1, (255,0,0)), (256, 196))

#function to know which key is pressed
pos222=()
def get_key():
  while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
          return event.key
        elif event.type == MOUSEBUTTONUP:
          for g in range(81):
            pygame.draw.rect(SCREEN,(255,255,255),(rect_list[g].left,rect_list[g].top,25,25),1)
          pos222 = pygame.mouse.get_pos()
          onmuseclick(pos222)
          return 'MOUSECLICK'
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
          pass
def get_key1():
  while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
          return event.key
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
          pass

#function to check the entered values
def validate():
  error=0
  print (validate_pos)
  print (validate_num)
  pygame.draw.rect(SCREEN,(255,255,255),(rect_list[validate_pos[len(validate_pos)-1]].left,rect_list[validate_pos[len(validate_pos)-1]].top,25,25),1)
  for l in range(len(validate_pos)):
    if validate_pos[l]==0 and validate_num[l]!='1':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==1 and validate_num[l]!='2':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==5 and validate_num[l]!='6':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==6 and validate_num[l]!='3':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==7 and validate_num[l]!='5':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==9 and validate_num[l]!='8':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==10 and validate_num[l]!='7':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==11 and validate_num[l]!='4':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==12 and validate_num[l]!='9':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==15 and validate_num[l]!='2':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==16 and validate_num[l]!='6':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==19 and validate_num[l]!='6':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==20 and validate_num[l]!='3':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==22 and validate_num[l]!='7':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==24 and validate_num[l]!='8':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==25 and validate_num[l]!='9':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==29 and validate_num[l]!='8':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==30 and validate_num[l]!='5':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==32 and validate_num[l]!='9':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==33 and validate_num[l]!='1':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==35 and validate_num[l]!='6':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==41 and validate_num[l]!='8':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==42 and validate_num[l]!='9':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==43 and validate_num[l]!='4':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==45 and validate_num[l]!='4':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==46 and validate_num[l]!='9':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==47 and validate_num[l]!='2':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==49 and validate_num[l]!='3':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==50 and validate_num[l]!='1':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==53 and validate_num[l]!='8':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==61 and validate_num[l]!='1':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==64 and validate_num[l]!='8':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==65 and validate_num[l]!='1':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==66 and validate_num[l]!='2':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==67 and validate_num[l]!='6':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==69 and validate_num[l]!='7':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==71 and validate_num[l]!='5':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==76 and validate_num[l]!='1':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==77 and validate_num[l]!='5':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==79 and validate_num[l]!='8':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
    if validate_pos[l]==80 and validate_num[l]!='9':
      pygame.draw.rect(SCREEN,(255,0,0),(rect_list[validate_pos[l]].left,rect_list[validate_pos[l]].top,25,25),2)
      error+=1
  return error

#function to get the position of the cursor and to enter values
def onmuseclick(pos):
  count=0
  count1=0
  for i in range(81):
      if rect_list[i].collidepoint(pos[0],pos[1])==1:
          for j in range (len(validate_pos)):
              pygame.draw.rect(SCREEN,(255,255,255),(rect_list[validate_pos[j]].left,rect_list[validate_pos[j]].top,25,25),1)
              if i==validate_pos[j]:
                  count+=1
          for k in range (len(existing_pos)):
                  if i==existing_pos[k]:
                      count1+=1
          if count ==0 and count1==0:        
              pygame.draw.rect(SCREEN,(0,255,0),(rect_list[i].left,rect_list[i].top,25,25),1)
              pygame.draw.rect(SCREEN, (0, 0, 0), (0,400, 500, 100))
              pygame.display.flip()
              inkey = get_key()
              #print inkey
              if inkey!='MOUSECLICK' and inkey<256:
                  number=chr(inkey)
                  if number.isdigit() and number !='0':
                      SCREEN.blit(myfont.render(number, 1, (0,0,255)), (rect_list[i].left+6,rect_list[i].top+6))
                      validate_num.append(number)
                      validate_rect.append(rect_list[i])
                      validate_pos.append(i)
                      print (validate_pos)
                      print (validate_num)
                      if len(validate_pos)==41:
                          SCREEN.blit(pygame.font.SysFont("monospace", 23).render("Press enter to submit or any other",1,(255,0,0)),(0,420))
                          SCREEN.blit(pygame.font.SysFont("monospace", 23).render("key to make changes",1,(255,0,0)),(0,450))
                          pygame.display.flip()
                          inkey1=get_key1()
                          if inkey1 == K_RETURN:
                              pygame.draw.rect(SCREEN, (0, 0, 0), (0,400, 500, 100))
                              error_count=validate()
                              print (error_count)
                              if error_count==0:
                                SCREEN.blit(pygame.font.SysFont("monospace", 25).render("BINGO!!!!!", 1, (255,0,0)), (0, 420))
                                SCREEN.blit(pygame.font.SysFont("monospace", 25).render("Press any key to exit", 1, (255,0,0)), (0,450))
                                pygame.display.flip()
                              else:
                                SCREEN.blit(pygame.font.SysFont("monospace", 22).render("BAD LUCK!!!!!Errors are marked in red.",1,(255,0,0)),(0,420))
                                SCREEN.blit(pygame.font.SysFont("monospace", 22).render("Press any key to exit", 1, (255,0,0)), (0,450))
                                pygame.display.flip()
                              inkey2=get_key1()
                              if inkey2!=0:
                                pygame.quit()
                                sys.exit()
                              pygame.display.flip()
                              '''print validate_pos
                              print validate_num
                              print validate_rect'''
                          elif inkey1 != K_RETURN:
                            pygame.draw.rect(SCREEN, (0, 0, 0), (0,400, 500, 100))
                            pygame.display.flip()
                            
                      pygame.display.flip()
                      #print 'abc'
                  else:
                      pygame.draw.rect(SCREEN,(255,255,255),(rect_list[i].left,rect_list[i].top,25,25),1)
                      SCREEN.blit(pygame.font.SysFont("monospace", 24).render("Wrong input.Please input a number.", 1, (255,0,0)), (0, 450))
                      pygame.display.flip()
              elif inkey!='MOUSECLICK':
                  pygame.draw.rect(SCREEN,(255,255,255),(rect_list[i].left,rect_list[i].top,25,25),1)
                  SCREEN.blit(pygame.font.SysFont("monospace", 24).render("Wrong input.Please input a number", 1, (255,0,0)), (0, 450))
                  pygame.display.flip()
          else:
              if count1==0:
                  pygame.draw.rect(SCREEN,(0,255,0),(rect_list[i].left,rect_list[i].top,25,25),1)
                  pygame.draw.rect(SCREEN, (0, 0, 0), (0,400, 500, 100))
                  pygame.display.flip()
                  inkey = get_key()
                  if inkey == K_BACKSPACE:
                      pygame.draw.rect(SCREEN,(255,255,255),(rect_list[i].left,rect_list[i].top,25,25),0)
                      xxx=validate_pos.index(i)
                      print (i)
                      print (xxx)
                      validate_pos.remove(i)
                      #validate_num.remove(validate_num[xxx])
                      del validate_num[xxx]
                      validate_rect.remove(rect_list[i])
                      pygame.display.flip()
                      print (validate_pos)
                      print (validate_num)
                  else:
                    pass
  
# Refresh Display
pygame.display.flip()
count=0
while True:
    # your main loop
      # get all events
    ev = pygame.event.get()
      # proceed events
    for event in ev:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos1 = pygame.mouse.get_pos()
            onmuseclick(pos1)





           
