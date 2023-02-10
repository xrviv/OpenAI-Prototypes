import csv
import os

def csv_to_markdown_table(csv_file):
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        table = [header]
        table.extend(list(csv_reader))
        
    column_widths = [max(len(str(cell)) for cell in column) for column in zip(*table)]
    markdown_table = ' | '.join(f'{header: <{width}}' for header, width in zip(header, column_widths))
    markdown_table += '\n' + '-|-'.join(f'{"":-<{width}}' for width in column_widths) + '\n'
    for row in table[1:]:
        markdown_table += ' | '.join(f'{cell: <{width}}' for cell, width in zip(row, column_widths)) + '\n'
    return markdown_table

if __name__ == '__main__':
    markdown_table = csv_to_markdown_table('OpenAI-Prototype7-Scrapers/data/grants_data.csv')
    if not os.path.exists("OpenAI-Prototype7-Scrapers/data"):
        os.makedirs("OpenAI-Prototype7-Scrapers/data")
    with open('OpenAI-Prototype7-Scrapers/data/bitcoingrants.md', 'w') as file:
        file.write(markdown_table)
    print("Table saved to OpenAI-Prototype7-Scrapers/data/bitcoingrants.md")
