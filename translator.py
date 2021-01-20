
import argparse
import json
import boto3

# Arguments
parser = argparse.ArgumentParser(description="Provides translation between one source language and another of the same set of languages.")
parser.add_argument(
    '--file',
    dest="filename",
    type=str,
    help="The path to the input file. The file should be valid json",
    required=True
    )
    
args = parser.parse_args()

# FUNCTIONS

# Returns a dictionary containing the contents of the Input section in hte input file
def open_input():
    with open(args.filename) as file_object:
        contents = json.load(file_object)
        return contents['Input']

# Boto3 function to use Amazon Translate to translate the text and only return the Translated Text
def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response['TranslatedText']) 

# Loop to iterate over the json file
def translate_loop():
    input_text = open_input()
    for item in input_text:
        translate_text(**item)

# Main Function - use to call other functions
def main():
    translate_loop()

if __name__ == "__main__":
    main()
    
    
