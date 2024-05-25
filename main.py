from src.Algorithms.Searching import binary_search
from src.DataStructures.Tree.BST import BST
from src.OOAD.Parking.ParkingLot import ParkingLot

from src.OOAD.Connect4.Game import Game
from src.OOAD.Connect4.Grid import Grid

if __name__ == '__main__':
    grid = Grid(6, 7)
    game = Game(grid, 4, 2)
    game.play()

