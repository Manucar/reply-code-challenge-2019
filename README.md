# Reply Code Challenge 2019

<p align="center">
	<img src="img/reply-corporate-logo.png">
</p>

# Problem statement
Given the map of the world, the terrain features, and the locations of Headquarters of our Customers, you need to build a number of Reply Offices that minimize the overall distance between the Offices and the Customer Headquarters. You can choose to place an office only on areas suitable for construction.
For each Reply Office you are going to build, you need to:
- provide its position on the map
- connect it with one or more Customer Headquarters

The world map is a grid composed by 'terrain cells' of different types. If a cell is non-walkable, you cannot build Offices in it and no path can cross it. Every other cell is walkable and suitable for construction. You cannot build Offices in the same cell of a Customer Headquarter. A path is a series of consecutive cells going from a Reply Office to a Customer Headquarter. From a cell you can only step UP, RIGHT, DOWN, LEFT to the next cell. No diagonal steps are allowed. Each step has a cost based on the type of the terrain of the next cell.
Each reached client generates a reward. The score for a client is computed as the reward of the client minus the cost to reach it. Your total score is computed as the sum of the scores for each connected client. Each Office built must have a path to at least a Customer. Given a pair (Office O, Customer C) it can’t exist more than one path from O to C.

# Input format
Input data will be provided in plain ASCII text file.
On the first line you will find four integers separated by a whitespace character:
- N: the width of the map
- M: the height of the map
- C: the number of Customer Headquarters
- R: representing the maximum number of Reply Offices that can be built

C lines follow, each one built of three integers describing the X coordinate, the Y coordinate, and the reward associated with Customer Headquarter.
Then, M lines follow, describing a row of N terrain cells. The top-left cell is the origin of the map and is thus assigned “(0, 0)” coordinates. In the world map columns are represented by the X coordinate, while rows by the Y coordinate.
# Constraints
1 ≤ 𝑅 < 𝐶 ≤ 500
1 ≤ 𝑁 ≤ 2.000
1 ≤ 𝑀 ≤ 2.000

# Output format
For each path going from a Reply Office to a Customer Headquarter, output a single line built of the Reply Office X coordinate, Y coordinate, and a string representing the sequence of steps to reach the Customer Headquarter. Separate each of these three components by a single whitespace character. The Reply office coordinates are integer numbers. The sequence of steps is a string composed by the ASCII characters U, R, D, L (UP, RIGHT, DOWN, LEFT).


## First approach
Our first approach was to use [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) in order to find the shortest path between every Reply Office to each Customer Headquarter.

Scores:
 - 1: 3.103
 - 2: 3.651.108
 - 3: 890.096
 - 4: 432.714
 - 5: 2.198.099

**Total score:** 7.175.120

## Second approach
Since the first approach was pretty naive, we decided to switch to an informed search strategy like [A*](https://en.wikipedia.org/wiki/A*_search_algorithm) with [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry) as heuristics(multiplied by 50, the minimum cell cost).

Scores:
 - 1: 246.932.664
 - 2: 963.859.312
 - 3: 1111
 - 4: 111111
 - 5: 

**Total score:** 1.210.791.976