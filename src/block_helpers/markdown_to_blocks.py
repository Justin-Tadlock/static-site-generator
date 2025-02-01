def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')

    filtered_blocks = list(
        map(lambda b: b.strip(),
            filter(lambda b: b != '',
                   blocks)
        ))

    return filtered_blocks