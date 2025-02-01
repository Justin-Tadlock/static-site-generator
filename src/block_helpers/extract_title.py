def extract_title(markdown):
    lines = markdown.split('\n\n')
    
    if lines[0].startswith('# '):
        return lines[0][2:]
    raise ValueError("Invalid title markdown")