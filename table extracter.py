from docx import Document

# Load the Word document
doc = Document(r"S:\Downloads\IT.docx")

# Extract text
for paragraph in doc.paragraphs:
    print(paragraph.text)

# Extract tables
for table_index, table in enumerate(doc.tables):
    print(f"\nTable {table_index + 1}")
    print("=" * 50)
    for row in table.rows:
        row_data = " | ".join(cell.text.center(10) for cell in row.cells)
        print(row_data)
        print("-" * 50)  # Row separator

