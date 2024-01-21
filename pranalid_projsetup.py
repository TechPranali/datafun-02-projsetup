''' This module provides functions for creating a series of project folders using pathlib. '''

import pathlib
import time
# import stellar_analytics_utils  # Uncomment if you have this module from a previous project

def create_folders_for_range(start, end):
    '''Create folders for a given range of years.'''
    for year in range(start, end + 1):
        path = pathlib.Path.cwd().joinpath(str(year))
        path.mkdir(exist_ok=True)

def create_folders_from_list(folder_list, to_lowercase=False, remove_spaces=False):
    '''Create folders from a list of names with options for formatting.'''
    for name in folder_list:
        if to_lowercase:
            name = name.lower()
        if remove_spaces:
            name = name.replace(" ", "")
        path = pathlib.Path.cwd().joinpath(name)
        path.mkdir(exist_ok=True)

def create_prefixed_folders(folder_list, prefix):
    '''Create folders with a prefix from a list of names using list comprehension.'''
    paths = [pathlib.Path.cwd().joinpath(prefix + name) for name in folder_list]
    for path in paths:
        path.mkdir(exist_ok=True)

def create_folders_periodically(duration):
    '''Create folders periodically every 'duration' seconds.'''
    end_time = time.time() + duration
    count = 0
    while time.time() < end_time:
        folder_name = f"folder_{count}"
        path = pathlib.Path.cwd().joinpath(folder_name)
        path.mkdir(exist_ok=True)
        count += 1
        time.sleep(duration)

def main():
    ''' Main function to demonstrate module capabilities. '''
    # Print byline from an imported module
    # print(f"Byline: {stellar_analytics_utils.byline}")

    # Demonstration of function 1
    create_folders_for_range(2020, 2023)

    # Demonstration of function 2
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Demonstration of function 3
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Demonstration of function 4
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Testing additional options in function 2
    regions = ["North America", "South America", "Europe", "Asia", "Africa", "Oceania", "Middle East"]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

if __name__ == '__main__':
    main()
