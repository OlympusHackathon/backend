import fitz
import os
from ml import summarize
def parseBook():
    document = os.path.join('/Users/sabrinababakulova/Desktop/hackathon/backend/', 'received_pdf.pdf')
    doc = fitz.open(document)
    current_state = ""
    text_range = []
    minima_font_size = 15
    for page_number in range(len(doc)):
        page = doc.load_page(page_number)
        blocks = page.get_text("dict", flags=11)["blocks"]
        if len(blocks) == 0:
            continue
        for b in blocks:
            for l in b["lines"]:
                for s in l["spans"]:
                    if "chapter" in s["text"].lower() and s["size"] >= minima_font_size:
                        current_state = "none"
                        text_range.append({
                            "chapter_name":s["text"],
                            "chapter_number":s["text"][8:]+'.',
                            "info":"",
                        })
                    elif "references for chapter" in s["text"].lower():
                        break 
                    elif "exercises for section" in s["text"].lower():
                        break 
                    else:
                        if len(text_range) != 0:
                            text_range[-1]["info"] += s["text"]
    return text_range

def get_chapter_info():
    text_range = parseBook()
    final = ""
    for i in range(3):
        final += summarize(text_range[i]['info'])
    return final