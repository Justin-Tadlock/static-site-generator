def markdown_to_blocks(text):
    lines = list(filter(lambda x: x != '', text.lstrip('\n').split("\n")))

    blocks = []
    unordered_list = ''
    for line in lines:
        if line.startswith("#"):
            blocks.append(line)
            continue
        if line.startswith('* '):
            unordered_list += line
            continue
        if not line.startswith('* ') and len(unordered_list) > 0:
            blocks.append(unordered_list)
            unordered_list = ''
            continue
        blocks.append(line)        
    if len(unordered_list) > 0:
        blocks.append(unordered_list)

    return blocks