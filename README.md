# Eight Queen problem using Genetic Algorithms
## Eight Queen Problem
The 8 queens problem is a classic chess puzzle that involves placing eight queens on a standard 8x8 chessboard so that no two queens threaten each other. This means no two queens can share the same row, column, or diagonal.

## Gentic Algorithms
Genetic algorithms are problem-solving methods inspired by natural evolution. They work by creating a population of potential solutions and improving them through processes like crossover (combining parts of solutions) and mutation (randomly altering solutions). This helps find the best solution over time.
### Genetic Algorithm Components
- permutation encoding
- order crossover (OX)
- swap mutation
### Permutation Encoding
Here each chromosome has 8 genes each representing a row on the chessboard. The content of the gene indicates the column where the queen is placed. Using permutation encoding resolves the issue of queens threatening each other within the same row or column.  
For example the gene [6, 2, 0, 5, 7, 4, 1, 3] represents the board bellow:  

<p align="center">
  <img src="https://github.com/SabaKzmi/8-Queen-Problem-using-Genetic-Algorithms/blob/1991b21f426097c2861b493bad588511709721c7/example-board.png" alt="example board" />
</p>

