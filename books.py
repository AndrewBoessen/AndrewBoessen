import csv
import requests
import isbnlib

def get_book_info(isbn):
    try:
        # Get metadata using isbnlib
        book_meta = isbnlib.meta(isbn)
        
        # Get cover image URL
        cover_url = f"https://covers.openlibrary.org/b/isbn/{isbn}-S.jpg"
        
        return {
            'title': book_meta.get('Title', 'Unknown'),
            'authors': ', '.join(book_meta.get('Authors', ['Unknown'])),
            'year': book_meta.get('Year', 'Unknown'),
            'isbn': isbn,
            'cover_url': cover_url
        }
    except Exception as e:
        print(f"Error fetching data for ISBN {isbn}: {str(e)}")
        return None

def generate_readme(books):
    readme_content = "## My Current Reading List\n\n"
    
    for book in books:
        if book:
            readme_content += f"### {book['title']}\n\n"
            readme_content += "| Cover | Details |\n"
            readme_content += "| ----- | ------- |\n"
            readme_content += f"| ![Book Cover]({book['cover_url']}) | "
            readme_content += f"**Author(s)**: {book['authors']}<br>"
            readme_content += f"**Year**: {book['year']}<br>"
            readme_content += f"**ISBN**: {book['isbn']} |\n\n"
    
    return readme_content

def main():
    input_file = 'isbn_list.csv'
    output_file = 'README.md'
    
    books = []
    
    # Read ISBNs from CSV file
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row:
                isbn = row[0].strip()
                book_info = get_book_info(isbn)
                if book_info:
                    books.append(book_info)
    
    # Generate README content
    readme_content = generate_readme(books)
    
    # Write README file
    with open(output_file, 'w', encoding='utf-8') as readme_file:
        readme_file.write(readme_content)
    
    print(f"README.md has been generated with information for {len(books)} books.")

if __name__ == "__main__":
    main()
