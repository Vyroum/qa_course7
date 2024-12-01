# Sample Python Project

## Table of Contents
- [Getting started](#getting-started)
- [Good to Know](#good-to-know)
- [Making code changes](#making-code-changes)

## Getting started

### On your Linux or Windows machine

1. Open your favorite shell, for example, good old
   [Bourne Again SHell, aka, `bash`](https://www.gnu.org/software/bash/),
   the somewhat newer
   [Z shell, aka, `zsh`](https://www.zsh.org/),
   or shiny new
   [`fish`](https://fishshell.com/). On Microsoft Windows, you may install [Git
   for Windows](https://gitforwindows.org) and use its Git BASH. Note that
   [PowerShell](https://docs.microsoft.com/en-us/powershell/) does not work.
1. Install [Git](https://git-scm.com/) by running
   `sudo apt install git-all` on [Debian](https://www.debian.org/)-based
   distributions like [Ubuntu](https://ubuntu.com/), or
   `sudo dnf install git` on [Fedora](https://getfedora.org/) and closely-related
   [RPM-Package-Manager](https://rpm.org/)-based distributions like
   [CentOS](https://www.centos.org/). For further information see
   [Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
1. Add the public key of an existing or new public and private key pair to your
   account on the
   [Fraunhofer GitLab](https://gitlab.cc-asp.fraunhofer.de/-/profile/keys)
   and add corresponding private key to the authentication agent by running
   `ssh-add ~/.ssh/${KEY}`, where `${KEY}` is the name of the private key.
1. Clone the source code by running
   `git clone git@gitlab.cc-asp.fraunhofer.de:ise621/sample-python-project.git`
   and navigate into the new directory `sample-python-project` by running
   `cd ./sample_python_project`. Stay in this directory and execute all commands
   from here. Because, for example, the command `make` reads GNU Make targets
   from the `Makefile` in the current working directory and this file is
   contained in the project root, and the Python virtual environment `./.venv`
   created later also lives in the project root, and the configuration files of
   various tools also live there, and relative paths used in this readme are
   always relative to the project root.
1. Prepare your environment by running `cp ./.env.sample ./.env` and adjusting
   the copied environment file to your needs.

#### With Docker and GNU Make (the easy way but only possible on developer computers)

6. Install [Docker Desktop](https://www.docker.com/products/docker-desktop), and
   [GNU Make](https://www.gnu.org/software/make/).
1. List all GNU Make targets, in particular those to communicate with Docker,
   by running `make help`.
1. Drop into `bash` with the working directory `/app`, which is mounted to the
   host's working directory, inside a fresh Docker container based on Debian
   Linux everything installed by running `make shell`. If necessary, the Docker
   image is (re)built automatically, which takes a while the first time.
1. List all project specific GNU Make targets, in particular those to run in
   the Docker container, by running `make help`.
1. Do something with the project like
   - printing the help text of the command-line interface with
     `sample_python_project`,
   - printing the help text of the raise command with
     `sample_python_project calculator raise --help`
   - raising `42` to the power of `7` with
     `sample_python_project calculator raise --base=42 --power=7`
   - entering the read–evaluate–print loop (REPL) with
     `sample_python_project repl`, executing
     `calculator raise --base=42 --power=7` there, and exiting it with the
     keyboard shortcut Ctrl+D.
   - running non-slow tests and doctests with `make tests`,
   - running slow and non-slow tests with `make slowtests`,
   - running doctests with `make doctests`,
   - type checking the code with `make types`,
   - linting the code with `make lint`,
   - finding dead code with `make dead`,
   - formatting the code with `make format`, and
   - generating documentation with `make docs`.
1. Drop out of the container by running `exit` or pressing `Ctrl-D`.

#### Without Docker (the hard way)

6. Install [Python](https://www.python.org/) version 3.10.4
   [pip](https://pip.pypa.io/en/stable/), and support for
   [Python virtual environments](https://docs.python.org/3/tutorial/venv.html)
   by running, at least on Debian "bookworm",
   `apt-get install python3 python3-pip python3-venv`.
1. Create a virtual environment by running
   `python3 -m venv ./.venv`.
1. Activate the environment by running, on Windows,
   `.venv\Scripts\activate.bat`, and, on Unix or MacOS, in
   a [`bash`](https://www.gnu.org/software/bash/) shell
   `source ./.venv/bin/activate`,
   in a [`csh`](https://en.wikipedia.org/wiki/C_shell) shell
   `source ./.venv/bin/activate.csh`,
   and in a [`fish`](https://fishshell.com/) shell
   `source ./.venv/bin/activate.fish`.
1. Upgrade `pip`, [setuptools](https://github.com/pypa/setuptools) and
   [wheel](https://github.com/pypa/wheel) by running
   `pip3 install --upgrade -r ./requirements-build.txt`.
1. Install development tools, namely

   - the code formatter [Black](https://github.com/psf/black),
   - the static type checker [mypy](http://mypy-lang.org),
   - the testing automator [pytest](https://docs.pytest.org)
   - the linter [Pylint](https://www.pylint.org/),
   - the dead code finder [Vulture](https://github.com/jendrikseipp/vulture), and
   - the documentation creator [Sphinx](http://www.sphinx-doc.org),

   with [pip](https://pip.pypa.io) by running
   `pip3 install -r ./requirements-development.txt` and
   `poetry self add poetry-plugin-export`.

1. Install the package's dependencies in `requirements.txt` with
   [pip](https://pip.pypa.io) by running
   `pip3 install -r ./requirements.txt`.
1. Install the package in editable mode by running
   `pip3 install --editable .`, making the project importable within Pyton
   under `sample_python_project` and installing its command-line interface
   as `sample_python_project`.
1. Enable
   [shell completion](https://click.palletsprojects.com/en/8.1.x/shell-completion/)
   for the command-line interface by running
   ```
   eval "$(_STANDARD_BIPV_SYSTEM_COMPLETE=bash_source standard_bipv_system)"
   ```
   in bash,
   ```
   eval "$(_STANDARD_BIPV_SYSTEM_COMPLETE=zsh_source standard_bipv_system)"
   ```
   in Zsh, and
   ```
   eval (env _STANDARD_BIPV_SYSTEM_COMPLETE=source-fish standard_bipv_system)
   ```
   in Fish.
1. Do something with the project like
   - printing the help text of the command-line interface with
     `sample_python_project`,
   - printing the help text of the raise command with
     `sample_python_project calculator raise --help`
   - raising `42` to the power of `7` with
     `sample_python_project calculator raise --base=42 --power=7`
   - entering the read–evaluate–print loop (REPL) with
     `sample_python_project repl`, executing
     `calculator raise --base=42 --power=7` there, and exiting it with the
     keyboard shortcut Ctrl+D.
   - running non-slow tests with `pytest ./tests`,
   - running slow and non-slow tests with `pytest --runslow ./tests`,
   - running doctests with
     ```
     pytest \
       --doctest-modules \
       --doctest-continue-on-failure \
       --assert=plain \
       -vvv \
       ./sample_python_project
     ```
   - type checking the code with `mypy --strict .`,
   - linting the code with `pylint ./sample_python_project`,
   - finding dead code with
     ```
     vulture \
       --exclude ./sample_python_project/__init__.py,./tests/conftest.py,./docs/source/conf.py \
       .
     ```
   - formatting the code with `black --target-version py310 .`, and
   - generating documentation with
     ```
     sphinx-apidoc -f -o ./docs/source ./sample_python_project
     sphinx-build -b html ./docs/source ./docs/html
     ```
1. Deactivate the virtual environment by running `deactivate`.

## Good to Know

### Tools

- Code Formatter: [Black](https://github.com/psf/black)
- Static Type Checker: [mypy](http://mypy-lang.org)
- Test Automation: [pytest](https://docs.pytest.org/en/latest/)
- Code Analysis: [Pylint](https://www.pylint.org)
- Dead Code Finder: [Vulture](https://github.com/jendrikseipp/vulture)

### Find Answers to Questions

- [Stack Overflow](https://stackoverflow.com/questions/tagged/python)
- [Python documentation](https://docs.python.org/3/)
- [Docker Documentation](https://docs.docker.com/)
- [GNU make Manual](https://www.gnu.org/software/make/manual/html_node/index.html)
  and [Concise introduction to GNU Make](https://swcarpentry.github.io/make-novice/reference.html)

### Reading List

- [Make a README](https://www.makeareadme.com)
- [Keep a CHANGELOG](https://keepachangelog.com)
- [Semantic Versioning](https://semver.org)
- [Choose an open source license](https://choosealicense.com)
- [Structuring Your Python Project](https://docs.python-guide.org/writing/structure/)

### Git

- [Resources to learn Git](https://try.github.io)
  and
  [Learn Git with Bitbucket Cloud](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
- [Understanding the GitHub flow](https://guides.github.com/introduction/flow/)
  or
  [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
  or
  [Introduction to GitLab Flow](https://docs.gitlab.com/ee/topics/gitlab_flow.html)
  or
  [A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)
- [Making a Pull Request](https://www.atlassian.com/git/tutorials/making-a-pull-request)
- [Merging vs. Rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)
- [Using branches](https://www.atlassian.com/git/tutorials/using-branches)
- [Git merge conflicts](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts)
- [Get started with GitLab](https://docs.gitlab.com/ee/intro/)
- [Removing a file added in the most recent unpushed commit](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github#removing-files-from-a-repositorys-history)
  and
  [Removing (sensitive) data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)

### Code Quality

- [Clean Code concepts adapted for Python](https://github.com/zedr/clean-code-python)
- [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org)
- [Support for type hints](https://docs.python.org/3/library/typing.html) or
  [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [Speed up your data science and scientific computing code](https://pythonspeed.com/datascience/)

### Testing

- [Doctest](https://docs.python.org/3/library/doctest.html)
- [pytest](https://docs.pytest.org)
- [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- [What is unit testing and what are its benefits?](https://stackoverflow.com/questions/1383/what-is-unit-testing/1398#1398)
- [Getting Started With Python Testing](https://realpython.com/python-testing/)
- [Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/)
- [5 Pytest Best Practices for Writing Great Python Tests](https://www.nerdwallet.com/blog/engineering/5-pytest-best-practices/)

### Documentation

- [Google Python Style Guide](http://google.github.io/styleguide/pyguide.html)
- [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [Example Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

### Docker

- [Production-ready Docker packaging for Python developers](https://pythonspeed.com/docker/)
- [Docker for development, why, and how?](https://www.reddit.com/r/docker/comments/982cag/docker_for_development_why_and_how/)
- [Why and How to Use Docker for Development](https://medium.com/travis-on-docker/why-and-how-to-use-docker-for-development-a156c1de3b24)
- [Efficient development with Docker and docker-compose](https://hackernoon.com/efficient-development-with-docker-and-docker-compose-e354b4d24831)
- [A Practical Introduction to Docker Compose](https://hackernoon.com/practical-introduction-to-docker-compose-d34e79c4c2b6)
- [Production-ready Docker packaging for Python developers](https://pythonspeed.com/docker/)
- [Dockerfile Best Practicies](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Docker Best Practices](https://gist.github.com/StevenACoffman/41fee08e8782b411a4a26b9700ad7af5)
- [Security best practices](https://docs.docker.com/develop/security-best-practices/)
- [21 Docker Security Best Practices: Deamon, Image & Container](https://spacelift.io/blog/docker-security)
- [Weblog about Docker](https://spacelift.io/blog/docker)

### GNU Make

- [Running Make](https://swcarpentry.github.io/make-novice/reference.html)
- [The Lost Art of the Makefile](https://www.olioapps.com/blog/the-lost-art-of-the-makefile/)

### Scientific Computing

- [Speed up your data science and scientific computing code](https://pythonspeed.com/datascience/)

## Making code changes

In a nutshell, you do the following:

1. `git checkout develop`: Check-out, that is, switch to, the branch `develop`.
1. `git pull -p`: Pull up-stream changes, that is, sync your local copy with
   the remote repository.
1. `git checkout -b feature-x`: Create a new feature branch
1. Make changes to the code and the tests (use [type
   hints](https://docs.python.org/3/library/typing.html) for both) and
   regularly
   - format the code with
     [Black](https://github.com/psf/black) by running `make format` or
     equivalently `black --target-version py310 .`,
   - check for code smells with
     [Pylint](https://www.pylint.org/) by running `make lint` or equivalently
     `pylint ./sample_python_project`,
   - find dead code with
     [Vulture](https://github.com/jendrikseipp/vulture) by running `make dead`
     or equivalently `vulture --exclude ./sample_python_project/__init__.py,./tests/conftest.py,./docs/source/conf.py
     .`,
   - do static type checks with
     [mypy](http://mypy-lang.org/) by running `make types` or equivalently `mypy --strict .`, and
   - test the code with [pytest](https://docs.pytest.org) by running
     `make tests` or equivalently `pytest ./tests` and `pytest --assert=plain --doctest-continue-on-failure --doctest-modules -vvv ./sample_python_project`.
   - document your code with
     [Google Style Python Docstrings](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings)
     (see also
     [this](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
     and
     [that](https://www.python.org/dev/peps/pep-0257/)),
     add
     [doctest](https://docs.python.org/3/library/doctest.html)
     usage examples, and generate HTML documentation by running `make docs` or
     equivalently `sphinx-apidoc -f -o docs/source . && sphinx-build -b html docs/source docs/html`
     and once in a while run slow but more elaborate tests with `make slowtests`
     or equivalently `pytest --runslow ./tests`.
1. `git add .`: Stage your changes.
1. `git status`: Review the staged files (which files are staged as having been
   changed, added, or deleted).
1. `git diff --cached`: Review the staged line changes.
1. `git commit -m '...'`: Commit the staged changes, where the given message
   describes the changes.
1. `git push -u origin feature-x` (or just `git push` on subsequent changes):
   Push the feature branch to the remote repository.
1. Open the
   [sample python project on GitLab](https://gitlab.cc-asp.fraunhofer.de/ise621/sample-python-project)
   in a web browser and create a merge request for the pushed branch marking
   the source branch to be deleted after successful merge and possibly linking
   the request to related issues. If the merge request is still work in
   progress, prefix its title with 'Draft'.
1. Add a changelog entry for your merge request, do some further changes `git add .` them, `git commit -m '...'` them, and `git push` them.
1. Once the feature is finished, on
   [sample python project](https://gitlab.cc-asp.fraunhofer.de/ise621/sample-python-project),
   remove the prefix 'Draft' from the merge request's title, ask for it to be
   reviewed, and, once it has been approved, merge it.

   If merging is not possible due to merge conflicts, then run `git fetch origin develop:develop` to pull up-stream changes of the `develop` branch
   into your local copy of it and `git rebase develop` to re-base your feature
   branch onto the new version of `develop`, that is, replay any changes you
   made on the new version of `develop`, which results in a history as if you
   had created the feature branch based on the new `develop` in the first
   place.

   The re-basing process is interactive: It stops at conflicts that cannot be
   resolved automatically and asks you to do so. Use `git status` to list
   files with non-resolved conflicts. Open those files, have a look at
   conflicting lines which are separated by the conflict dividers `<<<<<<< HEAD`, `=======`, and `>>>>>>> feature-x`, merge those lines manually and
   remove the dividers. Stage the manually merged files with `git add .` and
   continue the re-basing process with `git rebase --continue`. When the
   process is finished, run `make -k format lint dead types tests` to make
   sure that everything is fine and if it is force push the changes with `git push -f` which rewrites the upstream history with your shiny new local one
   that does not have any conflicts with the `develop` branch. Finally, merge
   the merge request. If for some reason you want to abort the re-basing
   process, then run `git rebase --abort`. For further details see
   [Git merge conflicts](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts).

1. `git checkout develop && git pull -p && git branch -d feature-x`: Check-out
   the branch `develop`, pull up-stream changes, and remove the local feature
   branch.
1. `make tests`: Run all tests. If some fail, which is possible due to changes
   that were merged into `develop` after the branch `feature-x` was created,
   then fix the code in a new branch `fixes-x` with the same workflow as above.

This way of working with `git` is known as the [Gitflow
workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
which you should internalize. You should also

- read excerpts of [Get started with GitLab](https://docs.gitlab.com/ee/intro/),
- familiarize yourself with [Semantic Versioning](https://semver.org/),
- know how to [Keep a changelog](https://keepachangelog.com/en/1.0.0/),
- learn [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/),
- learn how to [Use branches](https://www.atlassian.com/git/tutorials/using-branches),
- learn the differences between [Merging and Rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing),
- learn [Making a Pull Request](https://www.atlassian.com/git/tutorials/making-a-pull-request), and
- adhere to the [PEP8 Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).

The essence of the Gitflow workflow: There are two permanent branches `master`
and `develop`, where `master` is for releases and `develop` for active
development towards the next release. Features are developed in their own
branches based on `develop` and merged into `develop` when they are finished.
Hot-fixes are developed in their own branches based on `master` and merged into
`master` when they are finished. New releases are made by merging `develop`
into `master`. Each hot-fix and normal release is tagged with a version.

Each feature and hot-fix branch has an accompanying merge request, which,
when feasible, is linked to one or multiple
[issues as single sources of truth](https://about.gitlab.com/blog/2016/03/08/gitlab-tutorial-its-all-connected/).
Before a merge request is accepted, it is reviewed to make sure that the
changes are properly implemented, well tested, and a changelog entry has
been added.
