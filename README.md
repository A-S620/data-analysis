[![CodeQL](https://github.com/A-S620/data-science/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/A-S620/data-science/actions/workflows/codeql-analysis.yml)
[![deploy-book](https://github.com/A-S620/data-science/actions/workflows/deploy-book.yaml/badge.svg)](https://github.com/A-S620/data-science/actions/workflows/deploy-book.yaml)
[![pages-build-deployment](https://github.com/A-S620/data-science/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/A-S620/data-science/actions/workflows/pages/pages-build-deployment)
# data-science
This Repo stores my data science notes and projects.

You can access the notes [here](https://a-s620.github.io/data-science)

## Installation
To install the dependencies:

```pip install -r requirements.txt```

To build the notebook:

```jupyter-book build .```

To serve the notebook locally:

```jupyter notebook```


## Useful Commands

| Syntax                              | Description                                                   |
|-------------------------------------|---------------------------------------------------------------|
| ```pip freeze```                    | To check all installed dependencies                           |
| ```pip freeze > requirements.txt``` | Creating a requirements.txt file, with installed dependencies |
| ```pip list```                      | List all installed packages                                   |
| ```pip list -o```                   | Show outdated packages                                        |
| ```pip list -u```                   | Show all up-to-date packages                                  |
| ```pip check```                     | Check all dependencies are working                            |
| ```pip uninstall PACKAGE_NAME```    | Uninstall a package                                           |
| ```pip --help```                    | Get help with pip                                             |


## Useful Links

| Link | Description                                                           |
|------|-----------------------------------------------------------------------|
| [Jupyter GitHub Pages and Actions](https://jupyterbook.org/en/stable/publish/gh-pages.html) | Information for using GitHub Pages and Actions with Jupyter notebook. |
