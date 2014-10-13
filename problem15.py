# Starting in the top left corner of a 2x2 grid, and only being able to move 
# to the right and down, there are exactly 6 routes to the bottom right corner

# How many such routes are there in a 20x20 grid?

from collections import deque

def main():
  t = makeLatticeNet(20)
  root = t[0]
  print "The number of paths to the end-point of the lattice is: " + str(t[1])
  


class LatticeNode():

  def __init__(self):
    self.freq = 0;
    self.vertLinkIn = self.vertLinkOut = self.horizLinkIn = self.horizLinkOut = None


  def setVertLinks(self, LatticeNode):
    self.vertLinkIn = LatticeNode
    LatticeNode.vertLinkOut = self

  def setHorizLinks(self, LatticeNode):
    self.horizLinkIn = LatticeNode
    LatticeNode.horizLinkOut = self

  def updateFreq(self):
    if (self.horizLinkIn == None and self.vertLinkIn == None):
      self.freq = 0
    elif (self.horizLinkIn == None):
      self.freq = 1
    elif (self.vertLinkIn == None):
      self.freq = 1
    else:
      self.freq = (self.horizLinkIn.freq) + (self.vertLinkIn.freq)

def makeLatticeNet(size):

  root = LatticeNode()
  prev_horiz_node = prev_vert_node = root
  max_freq = -1;

  for x in range(0, size+1): #Builds first row and column of lattice
    next_horiz_node = LatticeNode()
    next_horiz_node.setHorizLinks(prev_horiz_node)
    next_horiz_node.updateFreq()

    next_vert_node = LatticeNode()
    next_vert_node.setVertLinks(prev_vert_node)
    next_vert_node.updateFreq()

    prev_horiz_node = next_horiz_node
    prev_vert_node = next_vert_node
    
    
  anchor = root

  for y in range(0, size):
    
    horiz_parent = anchor.vertLinkOut
    vert_parent = anchor.horizLinkOut

    for x in range(0, size):
      next = LatticeNode()
      next.setVertLinks(vert_parent)
      next.setHorizLinks(horiz_parent)
      next.updateFreq()
      if(next.freq > max_freq):
        max_freq = next.freq

      vert_parent = vert_parent.horizLinkOut
      horiz_parent = next


    anchor = anchor.vertLinkOut

  return (root, max_freq)



if __name__ == "__main__":
  main()