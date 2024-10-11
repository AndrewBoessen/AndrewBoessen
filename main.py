from books import readme_content

def profile_readme():
    readme_content = '''# Hi, I'm Andrew!

## About Me
I'm a Computer Science student at Boston College, with a minor in Finance. I'm deeply interested in software engineering, machine learning, and building innovative projects that solve real-world problems.

### Projects
1. [Perfect Rep](https://github.com/AndrewBoessen/PerfectRep) - 3D computer vision model for powerlifting analysis using PyTorch and Transformers
2. [Eagle Eval](https://github.com/AndrewBoessen/EagleEval) - Platform for Boston College course ratings using TypeScript, Angular, Express, and MongoDB
3. [Re-Clip](https://github.com/AndrewBoessen/Re-Clip) - AI-powered mobile app for generating short-form video content from research papers and GitHub repos
4. [CUDAgrad](https://github.com/AndrewBoessen/CUDAgrad) - GPU-accelerated autograd engine and neural network library using CUDA and C
'''

    return readme_content

if __name__ == '__main__':
    output_file = 'README.md'

    profile = profile_readme()
    books = readme_content()

    # Write README file
    with open(output_file, 'w', encoding='utf-8') as readme_file:
        readme_file.write(profile)
        readme_file.write(books)
