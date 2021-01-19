import boto3

client = boto3.client('translate')

def translate_text(text, source_language_code, target_language_code): 
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text,
        SourceLanguageCode=source_language_code, 
        TargetLanguageCode=target_language_code
        #Amazon Translate language codes available at https://docs.aws.amazon.com/translate/latest/dg/what-is.html
    )
    
    print(response)
    
def main():
    translate_text(input("Please enter the text you would like to translate:  "),'en','es')

if __name__=="__main__":
    main()