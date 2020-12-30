'''
Guilherme Michel Lima de Carvalho

Implemententation of the Conway Game of Life!

Rules of the game:
- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

Or:
- Any live cell with two or three live neighbours survives.
- Any dead cell with three live neighbours becomes a live cell.
- All other live cells die in the next generation. Similarly, all other dead cells stay dead.

'''

import numpy as np

class ConwayGame:
    def __init__(self,N,live_cells,num_iter):
        self.N = N
        self.live_cells = live_cells
        self.num_iter = num_iter
    
    def initial_state(self):
        initial_matrix = np.zeros((self.N,self.N))
        for i in self.live_cells:
            initial_matrix[i] = 1
        return initial_matrix

    def get_neighbors(self,i,j):
        neighbors = [(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i-1,j-1),(i+1,j+1),(i-1,j+1),(i+1,j-1)]
        return neighbors
        
    def actions(self,matrix,i,j):
        if(matrix[i,j]==1):
            atual_state = 'Alive'
        else:
            atual_state = 'Dead'
        neighbors = self.get_neighbors(i,j)
        alive_cells = 0
        for i in neighbors:
            if(matrix[i]==1):
                alive_cells += 1
        dead_cells = len(neighbors) - alive_cells
        if(atual_state == 'Alive'):
            if(alive_cells==2 or alive_cells==3):
                action = 'Survive'
            else:
                action = 'Death'
        else:
            if(alive_cells == 3):
                action = 'Born'
            else:
                action = 'Death'
        return action
    
    def iteration(self,matrix):
        matrix_state = matrix.copy()
        for i in range(1,len(matrix[0])-1):
            for j in range(1,len(matrix[0])-1):
                neighbors = self.get_neighbors(i,j)
                for k in neighbors:
                    action = self.actions(matrix,i,j)
                    if (action == 'Born' or action == 'Survive'):
                        matrix_state[i,j] = 1
                    else:
                        matrix_state[i,j] = 0
        return matrix_state

    def simulation(self):
        matrix = self.initial_state()
        states = [matrix]
        for i in range(self.num_iter):
            updated_matrix = self.iteration(states[i])
            states.append(updated_matrix)
        return states
