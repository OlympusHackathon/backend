from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Input text to be summarized
def summarize(input_text, count = 10):
    print(input_text)
    finalSummary = ""
    parser = PlaintextParser.from_string(input_text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count=count)
    for sentence in summary:
        finalSummary += sentence.__str__()
    return finalSummary