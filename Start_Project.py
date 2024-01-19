import pathlib

def create_project_directory(directory_name: str) -> None:
    """
    Creates a project sub-directory.

    :param directory_name: Name of the directory to be created, e.g., "html"
    """
    pathlib.Path(directory_name).mkdir(exist_ok=True)

def main() -> None:
    """
    Scaffold a web development project.
    """
    # Create directories for HTML, CSS, and JS
    create_project_directory(directory_name='html')
    create_project_directory(directory_name='css')
    create_project_directory(directory_name='js')
    create_project_directory(directory_name='images')  # Additional directory for images

    print("Web development project structure created successfully.")

if __name__ == '__main__':
    main()
