from google.cloud import language
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

    #print('Text: {}'.format(description))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))


if __name__ == '__main__':
    analyzeDescription("Lol")
