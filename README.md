# Sudoku - version 1.0

You could use our implementations in order to solve Sudoku problems, generate non-symmetrical or symmetrical Sudoku, and rate Sudoku problems.

Moreover you could generate a printable pdf with as many problems from each difficulty level you desire.

We rate 5 levels of difficulty (very Easy, Easy, Medium, Hard, very Hard) and divide them inτο symmetrical and nonsymmetrical problems. 11 symmetrical patterns can be generated, but is very easy to add as many as you wish (in utils/GeneratorsUtils.py).

We use pyhton 3.5.2

Run main.py in src/main folder


1. Solvers

Our main solver is a recursive backtracking algorithm using two methods for input (Single candidate and Single position method). We implement a variaty of methods for cell rejection. You could build your own backtracking solver adding these methods.


2. Generators

Our main Generator uses a Top-Down technique with a Simulated Annealing variant and guarantees unique solution. It begins from a full-solved grid and randomly removes a cell only if outcomes a unique solution grid. If it is, the generator continues the removal proccess until we have a grid with the desirable number of known cells. Otherwise it returns to the previous recursive call and tries another removal.

That proccess can produce efficiently sudoku problems with 25-24 known cells at most. So we added a simulated annealing technique. That is: In every step there is a possibility p(n) (n is the number of known cells and if n1 <= n2 then p(n1) <= p(n2) ) that the generator would fill 2 cells at random. So this way we can exceed the local optimums (from the point of view of grid's structure). The parametrs of the simulated annealing may take improvment.

So we can generate sudoku problems with 21 known cells (or even 20 but it's slow).

In addition we implement a Bottom-down technique generator, but it's not very effective and needs a lot of improvement.


3. Rating Sudoku

For rating sudoku problems we follow Narendra Jussien method in his book "A to Z of SUDOKU". He gives a catalog of 10 rules that could be used to solve sudoku. You can sort this catalog from easiest to most difficult rule to understand and use. The difficulty level of a grid is defined by the  minimal required level of rules that is maximally needed to solve the grid.


-->To improve

(a) A gui for a sudoku grid and a menu bar. 
(b) Add generators (genetic for example), change and improve existing (speed, simulated annealing parametrs). 
(c) Add some different raters (genetic). 
(d) Add some more exotic solvers (hopfield neural network, integer programming).
