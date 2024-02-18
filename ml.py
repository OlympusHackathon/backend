from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Input text to be summarized
input_text = "Abstractive text summarization creates readable sentences from the complete text input. Large volumes of text are rewritten by producing acceptable representations, which are then analyzed and summarized using natural language processing. What distinguishes this technology is its almost AI-like capacity to parse text utilizing a machine’s semantic capabilities and iron out wrinkles using NLP. Although it is not as straightforward to utilize as the extractive technique, abstract summary is significantly more beneficial in many cases. In many ways, it is a forerunner to full-fledged AI authoring tools. This is not to say that extractive summarization is unnecessary. As the name implies, extractive text summarizing ‘extracts’ significant information from enormous amounts of text and arranges it into clear and succinct summaries. The approach is simple in that it extracts texts based on factors such the text to be summarized, the most essential sentences (Top K), and the importance of each of these phrases to the overall subject. This, however, implies that the approach is constrained to specified parameters, which might lead to biased retrieved text under certain scenarios. Extractive text summarizing is the most often utilized approach by automated text summarizers due to its simplicity in most use scenarios."

# Parse the input text
parser = PlaintextParser.from_string(input_text, Tokenizer("english"))

# Create an LSA summarizer
summarizer = LsaSummarizer()

# Generate the summary
summary = summarizer(parser.document, sentences_count=3)  # You can adjust the number of sentences in the summary

# Output the summary
print("Original Text:")
print(input_text)
print("\nSummary:")
for sentence in summary:
    print(sentence)