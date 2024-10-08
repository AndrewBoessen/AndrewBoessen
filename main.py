from books import readme_content

def profile_readme():
    readme_content = '''# Hi, I'm Andrew! 👋

## About Me
I'm a passionate Computer Science student at Boston College, with a minor in Finance. I'm deeply interested in software engineering, machine learning, and building innovative projects that solve real-world problems.

### 🎓 Education
- Boston College, Chestnut Hill, MA
  - Bachelor of Science in Computer Science, Minor in Finance
  - Expected graduation: May 2026

### 🚀 Projects
1. [Perfect Rep](link-to-repo) - 3D computer vision model for powerlifting analysis using PyTorch and Transformers
2. [Eagle Eval](link-to-repo) - Platform for Boston College course ratings using TypeScript, Angular, Express, and MongoDB
3. [Re-Clip](link-to-repo) - AI-powered mobile app for generating short-form video content from research papers and GitHub repos
4. [CUDAgrad](link-to-repo) - GPU-accelerated autograd engine and neural network library using CUDA and C
5. [BC Bites](link-to-repo) - Web app for Boston College dining options using JavaScript, Python, Flask, MongoDB, and React

### 🌱 I'm currently learning
- Advanced machine learning techniques
- GPU acceleration for neural networks
- Full-stack web development'''

    return readme_content

if __name__ == '__main__':
    output_file = 'README.md'

    profile = profile_readme()
    books = readme_content()

    # Write README file
    with open(output_file, 'w', encoding='utf-8') as readme_file:
        readme_file.write(profile)
        readme_file.write(books)
