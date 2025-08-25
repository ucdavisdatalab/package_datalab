# DataLab Python Package

[top]: #datalab-python-package

_Maintainer: Nick Ulle <<naulle@ucdavis.edu>>_

This is the repository for the `datalab` Python package. The package is a
[namespace package][], which means that it's a collection of multiple
semi-independent sub-packages. You don't need to install all of the
sub-packages to install the package, and most of the sub-packages are not in
this repository.

[namespace package]: https://packaging.python.org/en/latest/guides/packaging-namespace-packages/

As of writing, the only sub-package in this repository is `datalab.utilities`,
which contains functions that are useful across a variety of projects.

Nick recommends creating a sub-package for every project that uses Python in
the project's repo (NOT this repo).


## Usage

To use the sub-packages in this repo in your project, add this to your
project's `pyproject.toml`:

```toml
[tool.pixi.pypi-dependencies]
datalab = { git = "https://github.com/ucdavisdatalab/package_datalab.git" }
```

Then run `pixi install` in a terminal to install the environment.

### `datalab.utilities`

This sub-package provides the following modules:

* `cli`: functions to create command-line interfaces to modules and scripts.
* `datetime`: functions to get dates and times in ISO 8601 format.
* `hashing`: functions to compute hashes (fingerprints) for data.
* `io`: functions to read files in various formats.
* `logging`: functions to manage logging via Loguru.
* `notebook`: functions for working with Jupyter notebooks.
* `pathing`: functions to work with paths and set the working directory.

Read the docstrings with Python's `help` function for more details.


([back to top][top])


## Files & Directories

The files and directories in this repository are:
```
src/                Python source code
└── datalab/        The `datalab` namespace package
    └── utilities/  The `utilities` sub-package
.gitattributes      Paths Git should give special treatment
.gitignore          Paths Git should ignore
LICENSE             License for the project
pixi.lock           Exact description of Pixi environment (Python dependencies)
pyproject.toml      Package metadata file (including Python dependencies)
README.md           This file
```

([back to top][top])


## Contributing

> [!IMPORTANT]
>
> Do not commit large files (> 1 MB) to the repository. Upload these to cloud
> storage (such as Google Drive or Box) instead.

You can add modules and functions to the `datalab.utilities` sub-package.

If you want to add a whole collection of closely related modules, it might be
more appropriate to create a new sub-package. Check with the maintainer if
you're not sure. To create a new sub-package, make a subdirectory under
`src/datalab/` that contains an `__init__.py` file. For example, if you want to
create a sub-package called `datalab.moo`, the directory structure should be:

```
src/
└── datalab/
    ├── moo/
    │   ├── __init__.py
    │   └── ...
    └── utilities/
        ├── __init__.py
        └── ...
```

Work on a new branch and make a pull request to incorporate your changes, even
if you have write access to the `main` branch.

Please follow [PEP 8][], write [docstrings][], and follow [the NumPy docstring
standard][numpydoc]. Lint your code with [ruff][]. It's also good but not
required to put [type annotations][typing] on function definitions.

[PEP 8]: https://peps.python.org/pep-0008/
[docstrings]: https://peps.python.org/pep-0257/
[numpydoc]: https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard
[ruff]: https://docs.astral.sh/ruff/
[typing]: https://docs.python.org/3/library/typing.html


([back to top][top])


## Installation (for Contributors)

Open a terminal (Git Bash on Windows) and clone a copy of this repo:

```
git clone git@github.com:ucdavisdatalab/package_datalab.git
```

### Pixi

We *strongly recommend* using [Pixi][], a fast package manager based on the
conda ecosystem, to install the packages required by this repo. To install
Pixi, follow [the official instructions][pixi]. If you prefer not to use Pixi,
it's also possible to manually install the packages using conda or mamba.

[pixi]: https://pixi.sh/

The `pixi.toml` file in this repo lists required packages, while the
`pixi.lock` file lists package versions for each platform. When the lock file
is present, Pixi will attempt to install the exact versions listed. Deleting
the lock file allows Pixi to install other versions, which might help if
installation fails (but beware of inconsistencies between package versions).

To install the required packages, open a terminal and navigate to this repo's
directory. Then run:

```sh
pixi install
```

This will automatically create a virtual environment and install the packages.

To open a shell in the virtual environment, run:

```sh
pixi shell
```

You can run the `pixi shell` command from the repo directory or any of its
subdirectories. Use the virtual environment to run any commands related to this
repo. When you're finished using the virtual environment, you can use the
`exit` command to exit the shell.

([back to top][top])
