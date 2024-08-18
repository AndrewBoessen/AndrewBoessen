from books import readme_content

def profile_readme():
    readme_content = '# Hey 👋 I\'m Andrew\n\n\
I am an undergrad student at Boston College studying computer science and finance\n\n\
Currently working on machine learning and embeded systems programming\n\n'

    return readme_content

if __name__ == '__main__':
    output_file = 'README.md'

    profile = profile_readme()
    books = readme_content()

    # Write README file
    with open(output_file, 'w', encoding='utf-8') as readme_file:
        readme_file.write(profile)
        readme_file.write(books)