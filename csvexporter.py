# Created: 28-3-2023, Written by: Zehnter
# Please note that this is still a work in progress application, it might not give you the intended results.

with open('resultsexport.csv', 'w', newline='') as output_file:
    with open('resultssource.txt', 'r') as input_file:
        # Read in the contents of the input file
        input_text = input_file.read()

        # Replace all hash characters with a space
        no_hashes = input_text.replace('#', ' ')

        # Replace all whitespace characters with a comma separator
        cleaned_text = no_hashes.replace(' ', ',')

        # Add a newline character after each row of data
        cleaned_text = cleaned_text.replace('\n', ',\n')

        # Merge multiple sequential commas into one
        cleaned_text = ",".join(filter(None, cleaned_text.split(",")))

        # Check if a row starts with a comma and add a space before it
        cleaned_text = cleaned_text.replace('\n,', '\n ')

        # Write the cleaned text to the output file
        output_file.write(cleaned_text)

        # Print the cleaned text for debugging purposes
        print(cleaned_text)
