# What is notelate

generate jupyter notebook/lab template via command line

# How to use

## Install package

```
pip install notelate
```

## Use notelate

With command line tool, type "notelate" and template name.
Then, template notebook is generated at current directory

If template name is empty, basic template is generated

```
notelate [template name]
```

## Check templates

Type "notelate list", then the installed templates are printed.

## Add your template

There is two ways to add your original template

1.Contribute to github
You can contribute this module with [github](https://github.com/punisuke/notelate/)

please add your notebook template to notelate/templates/ and raise pull requests.

We are waiting your great template!

2.Add your template path
With below command you can add your original template path

```
notelate add [template_folder]
```

and you can check the path is included

```
notelate list
```

# Todo

separate a space to store templates and download it only when a template is requested
