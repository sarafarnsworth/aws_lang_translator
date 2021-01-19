import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response)

kwargs={
       "Text":input("Please enter the text you would like to translate:  "),
        "SourceLanguageCode":'en',
        "TargetLanguageCode":'es'
        }    
def main():
    translate_text(**kwargs)

if __name__=="__main__":
    main()