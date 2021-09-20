import os


def create_main_dir(dir_name):
    try:
        os.mkdir(dir_name)
    except FileExistsError as er:
        print(f'dir exists: {er.filename}')
    return 0


def create_child_dirs(parent, *dirs):
    for el in dirs:
        try:
            dir_path = os.path.join(parent, el)
            os.mkdir(dir_path)
        except FileExistsError as er:
            print(f'dir exists: {er.filename}')
        return 0


def create_starter(main_dir):
    create_main_dir(main_dir)
    create_child_dirs('settings', 'mainapp', 'adminapp', 'authapp')


if __name__ == '__main__':
    create_starter('my_project')