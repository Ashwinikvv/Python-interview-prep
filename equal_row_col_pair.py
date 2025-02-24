# Python3 code to implement the approach

# Function to count the row-column pairs
def equalPairs(grid) :

    # Initialize a map for mapping all
    # column with their frequency of
    # occurrence.
    unmap = {};

    # Iterate over all rows
    for i in range(len(grid)) :

        # Initialize an empty string s = ""
        s = "";

        # Keep appending all the element
        # into string s
        for j in range(len(grid[0])) :
            s += str(grid[i][j]);
            s += "*";
        
        if s in unmap :
            # Increment the frequency count of
            # string s in map
            unmap[s] += 1;     
        else :
            unmap[s] = 1;


    # Initialize a result variable for
    # storing the number of pair such that
    # row and column are equal
    result = 0;

    # Iterate over all the columns
    for j in range(len(grid[0])) :

        # Initialize an empty string s = ""
        s = "";

        # Keep appending all the element
        # into string s
        for i in range(len(grid)) :
            s += str(grid[i][j]);
            s += "*";

        # Add into result of frequency
        # count of s in map.
        result += unmap[s];

    # Return the result
    return result;

# Driver code
if __name__ == "__main__" :

    arr = [
        [ 2, 4, 1, 1 ],
        [ 4, 5, 6, 6 ],
        [ 1, 6, 4, 4 ],
        [ 1, 6, 4, 4 ],
    ];

    # Function Call
    print(equalPairs(arr));

    # This code is contributed by AnkThon
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
