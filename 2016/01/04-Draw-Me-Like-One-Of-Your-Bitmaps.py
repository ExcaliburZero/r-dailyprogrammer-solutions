# Problem: 248 [Easy] Draw Me Like One Of Your Bitmaps
# https://www.reddit.com/r/dailyprogrammer/comments/3zfajl/20160104_challenge_248_easy_draw_me_like_one_of/
# Author: ExcaliburZero
# License: MIT

import fileinput


def display_image(image):
    """
    A function which prints out the PPM file of the image.

    :param dict image: The image to be printed out.
    """
    print("P3")
    # Print the size of the image
    print(str(image["columns"]) + " " + str(image["rows"]))
    # Print the max color
    print("255")
    # Iterate over the pixels of the image
    for x in range(image["rows"]):
        for y in range(image["columns"]):
            # Get the color of the pixel
            if (x, y) in image:
                colors = image[(x, y)]
            # Handle if the pixel has been left unaltered
            else:
                colors = (0, 0, 0)

            # Print out the color information of the pixel
            print(str(colors[0]) + "\t" + str(colors[1]) + "\t" + str(colors[2]) + "\t", end="")
        print("\n")


def draw_point(image, command):
    """
    A function which draws a point on the given image.

    :param dict image: The image on which to draw the point.
    :param list command: The command given for the point draw.
    """
    # Get the location of the point
    location = (int(command[4]), int(command[5]))
    # Set the color of the point on the image
    image[location] = (int(command[1]), int(command[2]), int(command[3]))


def draw_line(image, command):
    """
    A function which draws a line on the given image.

    :param dict image: The image on which to draw the line.
    :param list command: The command given for the line to draw.
    """
    # Get the color of the line
    color = (int(command[1]), int(command[2]), int(command[3]))
    # Get the starting and ending point for the line
    start_point = (int(command[5]), int(command[4]))
    end_point = (int(command[7]), int(command[6]))
    # Get the slope of the line
    slope = (start_point[1] - end_point[1]) / (start_point[0] - end_point[0])

    # Draw each of the points on the line onto the image
    if start_point[0] < end_point[0]:
        smaller_x = start_point[0]
        larger_x = end_point[0]
    else:
        smaller_x = end_point[0]
        larger_x = start_point[0]
    for y in range(smaller_x, larger_x + 1):
        # Calculate the y position based on the x position
        x = round((slope * (y - start_point[0])) + start_point[1])
        # Draw the point on the image
        image[(x, y)] = color


def draw_rect(image, command):
    """
    A function which draws a rectange on the given image.

    :param dict image: The image on which to draw the rectangle.
    :param list command: The command given for the rectangle to draw.
    """
    # Get the color of the rectangle
    color = (int(command[1]), int(command[2]), int(command[3]))
    # Get the starting and ending point for the rectangle
    start_point = (int(command[4]), int(command[5]))
    size = (int(command[6]), int(command[7]))

    # Draw each of the points in the rectangle onto the image
    for x in range(start_point[0], start_point[0] + size[0]):
        for y in range(start_point[1], start_point[1] + size[1]):
            image[(x, y)] = color


def main():
    """
    A function which creates a PPM image based on a set of commands.
    """
    image = {}
    # Iterate over the commands in standard input
    for line in fileinput.input():
        # Get the size from the first line
        if fileinput.isfirstline():
            columns = line.split()[0]
            rows = line.split()[1]
            # Set the size of the image
            image["columns"] = int(columns)
            image["rows"] = int(rows)

        # Handle the commands in the lines after the first
        else:
            command = line.split()
            if command[0] == "point":
                draw_point(image, command)
            elif command[0] == "line":
                draw_line(image, command)
            elif command[0] == "rect":
                draw_rect(image, command)

    # Display the finished image
    display_image(image)


# Run the main function of the script
if __name__ == '__main__':
    main()
