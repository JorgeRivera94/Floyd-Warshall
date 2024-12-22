import sys

def floyd_warshall(cost_matrix, k):
    #initialize the kth adjacency cost matrix
    k_matrix = eval(cost_matrix.replace("inf","float('inf')"))

    #only evaluate up until the kth node
    for inter in range(int(k)):
        #compare the distance from source every node to every destination node 
        for src in range(len(k_matrix)):
            for dest in range(len(k_matrix[0])):
                #if the distance through the intermediate node is shorter, replace it
                k_matrix[src][dest] = min(k_matrix[src][dest], k_matrix[src][inter] + k_matrix[inter][dest])
    
    return k_matrix
    
def main():
    if len(sys.argv) > 1:
        print(floyd_warshall(sys.argv[1], sys.argv[2]))
    
if __name__ == "__main__":
    main()