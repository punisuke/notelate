import requests
import os
import sys
import glob


class Notelate:
    def __init__(self):
        path = os.path.dirname(os.path.abspath(
            __file__)).replace('\\scripts', '')
        self.template_path = path + '\\templates\\'

    def fetch_template(self, tempalte_name):
        base_url = ''

    def print_list(self, local=True):
        if local:
            temp_list = glob.glob(self.template_path+'*.ipynb')
        else:
            temp_list = ['fa', 'b']
        for t in temp_list:
            print(t.split('\\')[-1].replace('.ipynb', ''))

    def check_local(self, template_name):
        if os.path.exists(self.template_path+'{}.ipynb'.format(template_name)):
            return True
        else:
            return False


def main():
    nl = Notelate()
    if len(sys.argv) == 0:
        templat_name = 'basic'

    if sys.argv[1] == 'list':
        print('printing template list in github')
        nl.print_list(local=False)
    elif sys.argv[1] == 'local':
        print('printing template list in local')
        nl.print_list(local=True)
    else:
        templat_name = sys.argv[1]
        print(templat_name)


if __name__ == '__main__':
    main()
