import requests
import os
import sys
import glob
import shutil


class Notelate:
    def __init__(self):
        path = os.path.dirname(os.path.abspath(
            __file__)).replace('\\scripts', '')
        self.template_path = path + '\\templates\\'
        print('template folder is [{}]'.format(self.template_path))

    def fetch_template(self, tempalte_name):
        base_url = ''

    def print_list(self, local=True):
        if local:
            temp_list = glob.glob(self.template_path+'*.ipynb')
        else:
            temp_list = glob.glob(self.template_path+'*.ipynb')

        for t in temp_list:
            print(t.split('\\')[-1].replace('.ipynb', ''))

    def check_local(self, template_name):
        if os.path.exists(self.template_path+'{}.ipynb'.format(template_name)):
            return True
        else:
            return False

    def copy_template(self, template_name):
        if self.check_local(template_name):
            template_name += '.ipynb'
            old_path = self.template_path + template_name
            new_path = os.getcwd() + '/' + template_name
            shutil.copyfile(old_path, new_path)
            print('"{}" is generated'.format(template_name))
        else:
            print('"{}" does not exist'.format(template_name))


def main():
    nl = Notelate()
    if len(sys.argv) == 0:
        templat_name = 'basic'
        nl.copy_template(templat_name)

    if sys.argv[1] == 'list':
        print('printing template list in local')
        nl.print_list(local=False)
    elif sys.argv[1] == 'local':
        print('printing template list in local')
        nl.print_list(local=True)
    else:
        templat_name = sys.argv[1]
        nl.copy_template(templat_name)


if __name__ == '__main__':
    main()
