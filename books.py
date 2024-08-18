import requests
import re
import isbnlib

def get_book_info(isbn):
    try:
        book_meta = isbnlib.meta(isbn)
        cover_url = f"https://covers.openlibrary.org/b/isbn/{isbn}-M.jpg"
        
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
    if not books:
        return "No books found."

    readme_content = "## My Reading List\n\n"

    # Currently Reading
    current_book = books[0]
    readme_content += "### Currently Reading\n\n"
    readme_content += f"#### {current_book['title']}\n\n"
    readme_content += "| Cover | Details |\n"
    readme_content += "| ----- | ------- |\n"
    readme_content += f"| ![Book Cover]({current_book['cover_url']}) | "
    readme_content += f"**Author(s)**: {current_book['authors']}<br>"
    readme_content += f"**Year**: {current_book['year']}<br>"
    readme_content += f"**ISBN**: {current_book['isbn']} |\n\n"

    # Backlog
    if len(books) > 1:
        readme_content += "### Backlog\n\n"
        readme_content += "| Cover | Title | Author(s) | Year | ISBN |\n"
        readme_content += "| ----- | ----- | --------- | ---- | ---- |\n"
        for book in books[1:]:
            readme_content += f"| ![Book Cover]({re.sub('M.jpg', 'S.jpg', book['cover_url'])}) | {book['title']} | {book['authors']} | {book['year']} | {book['isbn']} |\n"

    return readme_content

def readme_content():
    input_file = 'isbn_list.txt'
    
    books = []
    
    # Read ISBNs from txt file
    with open(input_file, 'r') as txt_file:
        for line in txt_file:
            isbn = line.strip()
            if isbn:
                book_info = get_book_info(isbn)
                if book_info:
                    books.append(book_info)
    
    # Generate README content
    readme_content = generate_readme(books)

    print(f"README.md has been generated with information for {len(books)} books.")

    return readme_content

def main():
    output_file = 'README.md'
    
    # Generate README content
    content = readme_content()
    
    # Write README file
    with open(output_file, 'w', encoding='utf-8') as readme_file:
        readme_file.write(content)

if __name__ == "__main__":
    main()