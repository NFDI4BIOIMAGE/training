# Training materials

This repository contains a collection of training materials. The collection can be browsed under this URL:

https://haesleinhuepf.github.io/training

It is maintained using [Jupyter lab](https://jupyterlab.readthedocs.io/en/stable/) and build using [Jupyter book](https://jupyterbook.org/intro.html).

To edit this book, install depencencies like this:

```
pip install jupyterlab
pip install jupyter-book
pip install jupyterlab-spellchecker

git clone https://github.com/haesleinhuepf/training
cd training
jupyter lab
```

To build the book, you can run this from the same folder (tested on MacOS only):
```
chmod u+x ./build.sh
./build.sh
```

To clear the build, e.g. before committing using git, run this:
```
chmod u+x ./clean.sh
./clean.sh
```

## Acknowledgements

R.H. acknowledges support by the Deutsche Forschungsgemeinschaft under Germany’s Excellence Strategy—EXC2068–Cluster of Excellence Physics of Life of TU Dresden.



