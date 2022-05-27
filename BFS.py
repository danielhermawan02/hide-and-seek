from turtle import clear, done
from graphics import *
import time
import random as rand

# Error Log

# IndexError: list index out of range

# print(parent[currPoint[0]][currPoint[1]])
# TypeError: 'NoneType' object is not subscriptable

# File "c:\Users\LENOVO\OneDrive\Desktop\VSCO\Python\KB_Hide & Seek\Artificial-Intelligence\BFS.py", line 167, in explore
#     for neighbour in adjencyDict[child]:
# KeyError: (8, 6)


# Invalid/Anomaly Occured
"""
Initial (x,y) :  1 , 2
End (x,y) :  10 , 5
"""


grid_side = 50
win = GraphWin("Hide & Seek", grid_side*10, grid_side*10)
#NOTE: In this list and other places, first point is y axis and second is x!!
wallsList = [(1,9), (1,10), (2,2), (2,4), (2,5), (2,7), (3,7), (3,9), (3,10),
            (4,3), (4,5), (4,7), (4,9), (5,3), (5,5), (5,7),(5,8),(5,9), (6,2),
            (6,3),(6,5),(6,8),(7,2),(7,5),(7,6),(7,8),(7,10),(8,2),(8,6),(8,8),
            (8,10),(9,4),(9,5),(9,6),(10,1),(10,2),(10,3)]

# loop = int(input('How many loop?'))
# loop = 1
# print('Looping for ', loop, ' time(s).\n')

# Initial Coordinate
# xBegin = 1
# yBegin = 1

# Destination Coordinate
# xEnd = 2
# yEnd = 10

# while(True):
#    xBegin = rand.randint(1,10)
#    yBegin = rand.randint(1,10)
#    xEnd = rand.randint(1,10)
#    yEnd = rand.randint(1,10)
#    checkEnd = (yEnd,xEnd)
#    checkStart = (xBegin,yBegin)
#    while checkEnd and checkStart in wallsList:
#       xBegin = rand.randint(1,10)
#       yBegin = rand.randint(1,10)
#       xEnd = rand.randint(1,10)
#       yEnd = rand.randint(1,10)
#       checkEnd = (yEnd,xEnd)
#       checkStart = (xBegin,yBegin)
#    else:
#       break

# print('Initial (x,y) : ', xBegin, ',', yBegin)
# print('End (x,y) : ', xEnd, ',', yEnd, '\n')

# manhattanDist = abs(xBegin-xEnd) + abs(yBegin-yEnd)

# startPoint = (yBegin,xBegin)
# endPoint = (yEnd,xEnd)

adjencyDict = {}

#In the beginning all nodes, except start, are not visited.

# nodeVisit = [[False for i in range(11)] for j in range(11)]
# nodeVisit[xBegin][yBegin] = True # nodeVisit[xBegin][yBegin]

parent = [[None for i in range(11)] for j in range(11)]

path = []
visitQueue = []

######################################################################
######################################################################

def clear():
   global adjencyDict
   global parent
   global path
   global visitQueue
   adjencyDict = {}
   parent = [[None for i in range(11)] for j in range(11)]
   path = []
   visitQueue = []

def check(list1, val1, val2):  
   # traverse in the list
   for x in list1:
      if val1 == x or val2 == x:
         return True 
   return False

def initfirstgoal():
   global manhattanDist
   global startPoint
   global endPoint
   global nodeVisit
   global xBegin
   global yBegin
   global xEnd
   global yEnd
   print("masuk\n")
   xBegin = rand.randint(1,10)
   yBegin = rand.randint(1,10)
   xEnd = rand.randint(1,10)
   yEnd = rand.randint(1,10)
   checkEnd = (yEnd,xEnd)
   checkStart = (xBegin,yBegin)
   while(check(wallsList, checkEnd, checkStart)):
      # print("masuk wa\n")
      xBegin = rand.randint(1,10)
      yBegin = rand.randint(1,10)
      xEnd = rand.randint(1,10)
      yEnd = rand.randint(1,10)
      checkStart = (xBegin,yBegin)
      checkEnd = (yEnd,xEnd)
   print('Initial (x,y) : ', xBegin, ',', yBegin)
   print('End (x,y) : ', xEnd, ',', yEnd, '\n')
   manhattanDist = abs(xBegin-xEnd) + abs(yBegin-yEnd)
   startPoint = (yBegin,xBegin)
   endPoint = (yEnd,xEnd)
   nodeVisit = [[False for i in range(11)] for j in range(11)]
   nodeVisit[xBegin][yBegin] = True # nodeVisit[xBegin][yBegin]

######################################################################
######################################################################

def initnewgoal():
   global manhattanDist
   global startPoint
   global endPoint
   global nodeVisit
   global xBegin
   global yBegin
   global xEnd
   global yEnd
   print("masuk new goal\n")
   xBegin = xEnd
   yBegin = yEnd
   xEnd = rand.randint(1,10)
   yEnd = rand.randint(1,10)
   checkEnd = (yEnd,xEnd)
   checkStart = (xBegin,yBegin)
   if(check(wallsList, checkEnd, checkStart)):
      print("masuk while\n")
      # print("masuk wa\n")
      xEnd = rand.randint(1,10)
      yEnd = rand.randint(1,10)
      checkStart = (xBegin,yBegin)
      checkEnd = (yEnd,xEnd)
   print('Initial (x,y) : ', xBegin, ',', yBegin)
   print('End (x,y) : ', xEnd, ',', yEnd, '\n')
   manhattanDist = abs(xBegin-xEnd) + abs(yBegin-yEnd)
   startPoint = (yBegin,xBegin)
   endPoint = (yEnd,xEnd)
   nodeVisit = [[False for i in range(11)] for j in range(11)]
   nodeVisit[xBegin][yBegin] = True # nodeVisit[xBegin][yBegin]

def createAdjencyDict():
   for y in range(1,11):
      for x in range(1,11):
         point = (y,x)
         if point in wallsList:
            continue
         else:
            adjencyDict[point] = []
            if((y-1 != 0)):
               if (y-1,x) not in wallsList:
                  currList = adjencyDict[point]
                  currList.insert(0,(y-1,x))
            if((y+1 != 11)):
               if (y+1,x) not in wallsList:
                  currList = adjencyDict[point]
                  currList.insert(0,(y+1,x))
            if((x-1 != 0)):
               if (y,x-1) not in wallsList:
                  currList = adjencyDict[point]
                  currList.insert(0,(y,x-1))
            if((x+1 != 11)):
               if (y,x+1) not in wallsList:
                  currList = adjencyDict[point]
                  currList.insert(0,(y,x+1))
               
######################################################################
######################################################################
                  
def initializeGame():
   """
   This function initializes the board with walls and place the seeker at start and
   marks the end position.

   """
   #Coloring the background black
   # initnewgoal()
   win.setBackground(color_rgb(0,0,0)) 

   for i in range(1,11):
      for j in range(1,11):
         center = Point((i-0.5)*grid_side,(j-0.5)*grid_side)
         cir = Circle(center, 1)
         cir.setFill(color_rgb(255,255,255))
         cir.draw(win)

   #Drawing the walls
   for a in wallsList:
      pt1 = Point((a[1]-1)*grid_side, (a[0]-1)*grid_side)
      pt2 = Point((a[1])*grid_side, (a[0])*grid_side)
      rect1 = Rectangle(pt1, pt2)
      rect1.setFill(color_rgb(0,102,248))
      rect1.draw(win)

   center = Point((startPoint[1]-0.5)*grid_side,(startPoint[0]-0.5)*grid_side)
   cir = Circle(center, 25)
   cir.setFill(color_rgb(255,255,0))
   cir.draw(win)
   
   
   rect1 = Rectangle(Point((endPoint[1]-1)*grid_side, (endPoint[0]-1)*grid_side),
                     Point((endPoint[1])*grid_side, (endPoint[0])*grid_side))
   rect1.setFill(color_rgb(255,0,0))
   rect1.draw(win)

######################################################################
######################################################################
# BFS algorithm:
# node is coordinate in (y,x) way.

def explore(node):
   global path
   endReached = False
  
   time.sleep(0.1)
   if node != startPoint:
      colorNode(node,0,175,0) # Green

   queue = []
   queue.append(node)

   while len(queue) != 0:
      child = queue.pop(0)
      print("length, current node = ",len(queue), child)
      nodeVisit[child[0]][child[1]] = True
      if child ==  endPoint:
         endReached = True
         break
      if child != startPoint:
         colorNode(child,0,175,0) # Green
      
      for neighbour in adjencyDict[child]:
         if (nodeVisit[neighbour[0]][neighbour[1]] == False):
            queue.append(neighbour)
            parent[neighbour[0]][neighbour[1]] = child
            
   return

def getPathBacktracking():
   print("Getting path")
   currPoint = endPoint
   path.insert(0,endPoint)
   while currPoint != startPoint:
      print(parent[currPoint[0]][currPoint[1]])
      path.insert(0,parent[currPoint[0]][currPoint[1]])
      currPoint = parent[currPoint[0]][currPoint[1]]

   path.insert(0, startPoint)

def colorNode(node,r,g,b):
   pt1 = Point((node[1]-1)*grid_side, (node[0]-1)*grid_side)
   pt2 = Point((node[1])*grid_side, (node[0])*grid_side)
   rect1 = Rectangle(pt1, pt2)
   rect1.setFill(color_rgb(r,g,b))
   rect1.draw(win)

def colorPathBlack():
   for node in path:
      pt1 = Point((node[1]-1)*grid_side, (node[0]-1)*grid_side)
      pt2 = Point((node[1])*grid_side, (node[0])*grid_side)
      rect1 = Rectangle(pt1, pt2)
      rect1.setFill(color_rgb(0,0,0))
      rect1.draw(win)
      
      rect1 = Rectangle(Point((endPoint[1]-1)*grid_side, (endPoint[0]-1)*grid_side),
                     Point((endPoint[1])*grid_side, (endPoint[0])*grid_side))
      rect1.setFill(color_rgb(255,0,0))
      rect1.draw(win)

def movePackMan():
   for i in range(0, len(path) - 1):
      time.sleep(0.1)
      #Put a circle in next cell:
      cell = path[i+1]
      center = Point((cell[1]-0.5)*grid_side,(cell[0]-0.5)*grid_side)
      cir = Circle(center, 25)
      cir.setFill(color_rgb(255,255,0)) # YELLOW COLOR
      cir.draw(win)

      #Turn current circle green
      colorNode(path[i],255,20,147)
      

def main():
   initfirstgoal()
   initializeGame()
   for i in range (1,3):
      print(i)
      if i == 1:
         print("masuk firstgoal\n")
         initfirstgoal()
         print("masuk initgame\n")
         initializeGame()
      else:
         print("masuk newgoal\n")
         initnewgoal()
         print("keluar newgoal\n")
         print("masuk clear\n")
         clear()
         print("masuk initgame\n")
         initializeGame()
      print("masuk adj\n")
      createAdjencyDict()
      print("masuk expl\n")
      explore(startPoint)
      print("masuk pathback\n")
      getPathBacktracking()
      # colorPathBlack()
      print("masuk movpac\n")
      movePackMan()
      print("keluar movpac\n")
   
   #getMounse() + close(): It wait untilsomeone clicks and doing so closes it
   win.getMouse()
   # win.close()

main()

print('Initial (x,y) : ', xBegin, ',', yBegin, '\n')
print('End (x,y) : ', xEnd, ',', yEnd, '\n')