import requests
import os
import sys
import glob
import shutil
import urllib
import numpy as np
import warnings
warnings.simplefilter("ignore")

path_list = os.path.dirname(os.path.abspath(
    __file__)) + '/temp_paths.npy'


class Notelate:
    def __init__(self, template_list):
        if os._exists(path_list):
            self.template_path_list = np.load(path_list)
        else:
            path = os.path.dirname(os.path.abspath(
                __file__)).replace('\\scripts', '')
            self.template_path_list = np.array([path + '\\templates\\'])
            np.save(path_list, self.template_path_list)
        print('template folder is {}'.format(self.template_path_list))

        self.template_list = template_list
        self.init_template()

    def init_template(self):
        for t in self.template_list:
            if self.check_local(t):
                pass
            else:
                self.fetch_template(t)

    def fetch_template(self, template_name):
        base_url = 'https://raw.githubusercontent.com/punisuke/notelate/master/notelate/templates/'
        try:
            url = f'{base_url}{template_name}.ipynb'
            filename = f'{self.template_path_list[0]}{template_name}.ipynb'
            urllib.request.urlretrieve(url, filename)
        except Exception as e:
            print(e)
            print(f'error in downloading template {template_name}')

    def print_list(self, local=True):
        temp_list = []
        if local:
            for tp in self.template_path_list:
                temp_list += glob.glob(tp+'*.ipynb')
        else:
            for tp in self.template_path_list:
                temp_list += glob.glob(tp+'*.ipynb')

        for t in temp_list:
            print(t.split('\\')[-1].replace('.ipynb', ''))

    def check_local(self, template_name):
        for tp in self.template_path_list:
            if os.path.exists(tp + '{}.ipynb'.format(template_name)):
                return tp
        return False

    def add_template_path(self, path):
        self.template_path_list = np.append(self.template_path_list, path)
        np.save(path_list, self.template_path_list)
        print('template folder is {}'.format(self.template_path_list))

    def copy_template(self, template_name):
        e = self.check_local(template_name)
        if e:
            template_name += '.ipynb'
            old_path = e + template_name
            new_path = os.getcwd() + '/' + template_name
            shutil.copyfile(old_path, new_path)
            print('"{}" is generated'.format(template_name))
        else:
            print('"{}" does not exist'.format(template_name))


if __name__ == '__main__':
    nl = Notelate(['basic'])
    nl.init_template()
