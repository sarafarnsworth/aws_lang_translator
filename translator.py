import boto3

client = boto3.client('translate')

def translate_text(): 
    response = client.translate_text(
        Text='Hello! My name is Sara. I am learning to create code using AWS.',
        SourceLanguageCode='en', 
        TargetLanguageCode='es'
        #language codes available at https://docs.aws.amazon.com/translate/latest/dg/what-is.html
    )
    
    print(response)
    
translate_text()