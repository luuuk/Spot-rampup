from google.cloud import language, language_v1
from google.cloud.language import enums
from google.cloud.language import types


def analyzeDescription(description):
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    document = types.Document(
        content=description,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    if sentiment.score > 0.5:
        print("Description has mostly positive sentiment")
    elif sentiment.score < -.05:
        print("Description has mostly negative sentiment")
    else:
        print("Description is neutral")


def analyzeKeywords(text_content, lang):
    client = language_v1.LanguageServiceClient()

    type_ = enums.Document.Type.PLAIN_TEXT
    document = {"content": text_content, "type": type_, "language": lang}
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_entities(document, encoding_type=encoding_type)

    print("Keywords: ")
    for entity in response.entities:
        if entity.salience > .05:
            print(entity.name)
