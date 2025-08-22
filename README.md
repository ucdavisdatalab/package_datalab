# DataLab Python Package

[top]: #datalab-python-package

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


## Installation

To get started, open a terminal (Git Bash on Windows) and clone a copy of this
repo:

```
git clone git@github.com:ucdavisdatalab/package_datalab.git
```

Then follow the instructions in the next section to set up the necessary
software environment.


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


## Contributing

> [!IMPORTANT]
>
> Do not commit large files (> 1 MB) to the repository. Upload these to cloud
> storage (such as Google Drive or Box) instead.

([back to top][top])


## File & Directory Structure

The directory structure for this repository is:
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
