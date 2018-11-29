import sys
import io

# Get input file via arguments
fileName = sys.argv[1]

# Create data structures needed


# Open input file for reading
inText = open(fileName, 'r')

# Main loop for reading line by line
while True:
    # currentLine is the line read by interpretative
    currentLine = inText.readline()

    # Parse commands and process them

    # End of file
    if not currentLine:
        exit(0)
