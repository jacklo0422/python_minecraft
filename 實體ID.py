from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import choice
mineral=[56]
r = choice(mineral)

myID=mc.getPlayerEntityIds()
x,y,z=mc.entity.getTilePos(myID)
mc.setBlock(x,y,z,r)