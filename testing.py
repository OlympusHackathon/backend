import fitz

doc = fitz.open('dbms_design.pdf')
current_state = ""
text_range = []
minima_font_size = 15
for page_number in range(len(doc)):
    page = doc.load_page(page_number)
    blocks = page.get_text("dict", flags=11)["blocks"]
    if len(blocks) == 0:
        continue
    for b in blocks:
        print(b)
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
print(text_range[0]['info'])