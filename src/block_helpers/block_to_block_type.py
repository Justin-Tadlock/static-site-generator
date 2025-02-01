import re

def block_to_block_type(block_text):
    headings = ['# ', '## ', '### ', '#### ', '##### ', '##### ', '###### ']

    for h in headings:
        if block_text.startswith(h):
            return 'Heading'
    if block_text.startswith('```'):
        return 'Code'
    if block_text.startswith('> '):
        return 'Quote'
    if block_text.startswith('* ') or block_text.startswith('- '):
        return 'Unordered List'
    if re.match(r"(\d+\.\ )", block_text) is not None:
        return 'Ordered List'
    return 'Paragraph'
    