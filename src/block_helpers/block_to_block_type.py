import re
from enum import Enum

class BlockType(Enum):
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    U_LIST = 'unordered_list'
    O_LIST = 'ordered_list'
    PARAGRAPH = 'paragraph'

def block_to_block_type(block):
    lines = block.split('\n')

    if block.startswith(('# ', '## ', '### ', '#### ', '##### ', '##### ', '###### ')):
        return BlockType.HEADING
    if len(lines) > 0 and lines[0].startswith('```') and lines[-1].startswith('```'):
        return BlockType.CODE
    if block.startswith('> '):
        for line in lines:
            if not line.startswith('>'):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith('* '):
        for line in lines:
            if not line.startswith('* '):
                return BlockType.PARAGRAPH
        return BlockType.U_LIST
    if block.startswith('- '):
        for line in lines:
            if not line.startswith('- '):
                return BlockType.PARAGRAPH
        return BlockType.U_LIST
    if block.startswith('1. '):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.O_LIST
    return BlockType.PARAGRAPH
    