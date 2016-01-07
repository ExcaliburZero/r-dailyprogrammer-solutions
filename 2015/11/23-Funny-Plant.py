# Problem: 242 [Easy] Funny Plant
# https://www.reddit.com/r/dailyprogrammer/comments/3twuwf/20151123_challenge_242_easy_funny_plant/
# Author: ExcaliburZero
# License: MIT

import fileinput


def main():
    # Iterate over each of the input lines
    for line in fileinput.input():
        # Get the input values
        line_contents = line.split()
        people = int(line_contents[0])
        starting_fruits = int(line_contents[1])
        # Create a list of the plants
        plants = [0] * starting_fruits
        # Create a counter for weeks
        weeks = 1
        # Keep simulating weeks until there is enough food
        while(people > sum(plants)):
            # Increment the week counter
            weeks += 1
            # Increase the growth amount of each of the plants
            for i in range(len(plants)):
                plants[i] += 1
            # Record the number of seeds
            seeds = sum(plants)
            # Create new plants from the seeds
            plants = plants + [0] * seeds
        # Print out the calculated result
        print(weeks)


# Run the main function
if __name__ == '__main__':
    main()
