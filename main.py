from graph.Graph import Graph
from windows.menu.MenuWindow import MenuWindow
from tkinter import *
from statsForGraph.Stats import Stats
from visualisation.GraphVisualization import GraphVisualization
from pathVisualisation.GridBoard import *
from pathVisualisation.GridVisualisation import *
if __name__ == '__main__':
    graph = Graph()
    graph.randomTree(11,3)  # tworzenie grafu 3 stopnia(ilosc, stopnien)
    # graph.randomTree(10,2)  # tworzenie drzewa dowolnego stopnia (ilosc, stopnien)


    # GraphVisualization.visualizationGraph(graph)    #metoda statyczna, bez potrzeby tworzenia instancji
    # graph.visualizationGraph()
    root = Tk()
    root.title("Path")
    root.geometry("1280x900+100+50")
    root.wm_protocol('WM_DELETE_WINDOW', root.quit)
    menu = MenuWindow(root)

    root.mainloop()
