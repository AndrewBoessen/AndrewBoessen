import requests


def get_book_info(isbn):
    try:
        url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
        response = requests.get(url)
        data = response.json()

        if 'items' in data and len(data['items']) > 0:
            book = data['items'][0]['volumeInfo']
            return {
                'title': book.get('title', 'Unknown'),
                'authors': ', '.join(book.get('authors', ['Unknown'])),
                'year': book.get('publishedDate', 'Unknown')[:4],
                'isbn': isbn,
                'cover_url': book.get('imageLinks', {}).get('thumbnail', '')
            }
        else:
            print(f"No data found for ISBN {isbn}")
            return None
    except Exception as e:
        print(f"Error fetching data for ISBN {isbn}: {str(e)}")
        return None


def generate_readme(books):
    if not books:
        return "No books found."

    readme_content = "## Currently Reading\n\n"

    # Currently Reading
    current_book = books[0]
    readme_content += f"### {current_book['title']}\n\n"
    readme_content += "| Cover | Details |\n"
    readme_content += "| ----- | ------- |\n"
    readme_content += f"| ![Book Cover]({current_book['cover_url']}) | "
    readme_content += f"**Author(s)**: {current_book['authors']}<br>"
    readme_content += f"**Year**: {current_book['year']}<br>"
    readme_content += f"**ISBN**: {current_book['isbn']} |\n\n"

    # Bookshelf
    if len(books) > 1:
        readme_content += "## Bookshelf\n\n"
        readme_content += "| Cover | Title | Author(s) | Year | ISBN |\n"
        readme_content += "| ----- | ----- | --------- | ---- | ---- |\n"
        for book in books[1:]:
            readme_content += f"| ![Book Cover]({book['cover_url']}) | {book['title']} | {
                book['authors']} | {book['year']} | {book['isbn']} |\n"

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

    print(f"README.md has been generated with information for {
          len(books)} books.")

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
