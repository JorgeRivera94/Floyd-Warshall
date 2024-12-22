Using FLoyd-Warshall algorithm, implement a python code that takes 2 command line imputs:
    Cost Adjacency Matrix => Matrix that will represent any graph cost adjacency matrix.
    k => Integer that will represent the matrix that your function will return, if zero it
        will return the same cost adjacency matrix, if 1 the Floyd-Warshall matrix at node 1, etc
    
The function must return the K matrix of the Floyd-Warshall algorithm. You can leverage
    the Floyd-Warshall algorithm shared on the class videos.

The first argument  will be in the form of [[...],[...],[...],...]. Remember the cost adjacency
    matrix is a squared matrix. "inf" represents no connection between nodes.

The output format is expected to be the same as the input cost adjacency matrix: 
    [[...],[...],[...],...]

Notes:
- For some reason Moodle is calling the code twice during the first test case, the first 
    call doesn't have any command line parameters.  Encapsulate your code inside an 
    if len(sys.argv) > 1: to avoid receiving an Index error when saving the inputs from the 
    command line.

- Use the ast library to be able to evaluate the strings as lists.  This will save you a lot 
    of time when processing the adjacency matrix from input #1.  However, you will need to 
    do some manipulations with the "inf" strings on the command line inputs.

Example:
in comand line:
python3 floyd.py [[0,3,inf,7],[8,0,2,inf],[5,inf,0,1],[2,inf,inf,0]] 1

output:
[[0, 3, inf, 7], [8, 0, 2, 15], [5, 8, 0, 1], [2, 5, inf, 0]]

# Test cases
python3 floyd.py [[0,3,inf,7],[8,0,2,inf],[5,inf,0,1],[2,inf,inf,0]] 1 
    => [[0, 3, inf, 7], [8, 0, 2, 15], [5, 8, 0, 1], [2, 5, inf, 0]]

python3 floyd.py [[0,3,inf,7],[8,0,2,inf],[5,inf,0,1],[2,inf,inf,0]] 2
    [[0, 3, 5, 7], [8, 0, 2, 15], [5, 8, 0, 1], [2, 5, 7, 0]]

python3 floyd.py [[0,3,inf,7],[8,0,2,inf],[5,inf,0,1],[2,inf,inf,0]] 3
    [[0, 3, 5, 6], [7, 0, 2, 3], [5, 8, 0, 1], [2, 5, 7, 0]]
    
python3 floyd.py [[0,3,inf,7],[8,0,2,inf],[5,inf,0,1],[2,inf,inf,0]] 4
    [[0, 3, 5, 6], [5, 0, 2, 3], [3, 6, 0, 1], [2, 5, 7, 0]]
