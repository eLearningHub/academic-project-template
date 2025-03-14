"""Nox sessions."""

import tempfile

import nox
from nox.sessions import Session

nox.options.sessions = ["lint", "mypy", "tests"]
python_versions = ["3.11"]


@nox.session(python=python_versions)
def tests(session: Session) -> None:
    """Run the test suite."""
    session.install(".")
    session.install("pytest", "pytest-cov", "pytest-mock")
    session.run("pytest", "--cov=src", "--cov-report=xml", "--cov-report=term")


@nox.session(python=python_versions)
def lint(session: Session) -> None:
    """Lint using flake8."""
    args = ["--max-line-length=100"]
    session.install("flake8", "flake8-black", "flake8-isort")
    session.run("flake8", *args, "src", "tests", "noxfile.py")


@nox.session(python=python_versions)
def black(session: Session) -> None:
    """Run black code formatter."""
    session.install("black")
    session.run("black", "src", "tests", "noxfile.py")


@nox.session(python=python_versions)
def isort(session: Session) -> None:
    """Run isort import sorter."""
    session.install("isort")
    session.run("isort", "src", "tests", "noxfile.py")


@nox.session(python=python_versions)
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    session.install(".")
    session.install("mypy")
    session.run("mypy", "src", "tests", "noxfile.py")


@nox.session(python=python_versions)
def xdoctest(session: Session) -> None:
    """Run examples with xdoctest."""
    session.install(".")
    session.install("xdoctest")
    session.run("python", "-m", "xdoctest", "src", "all")


@nox.session(python=python_versions)
def docs(session: Session) -> None:
    """Build the documentation."""
    session.install(".")
    session.install("sphinx", "sphinx-click", "furo", "myst-parser")
    session.run("sphinx-build", "docs", "docs/_build")


@nox.session(python=python_versions)
def coverage(session: Session) -> None:
    """Upload coverage data."""
    session.install("coverage[toml]", "codecov")
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov", *session.posargs)


@nox.session(python=python_versions)
def safety(session: Session) -> None:
    """Scan dependencies for insecure packages."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")
