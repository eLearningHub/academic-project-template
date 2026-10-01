"""Nox sessions."""

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
    """Lint and check formatting with ruff."""
    session.install("ruff")
    session.run("ruff", "check", ".")
    session.run("ruff", "format", "--check", ".")


@nox.session(python=python_versions)
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    session.install(".")
    session.install("mypy")
    session.install("pytest", "nox")
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
    session.install(".[docs]")
    session.run("sphinx-build", "docs", "docs/_build")


@nox.session(python=python_versions)
def coverage(session: Session) -> None:
    """Upload coverage data."""
    session.install("coverage[toml]", "codecov")
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov", *session.posargs)


@nox.session(python=python_versions)
def audit(session: Session) -> None:
    """Scan the installed dependencies for known vulnerabilities."""
    session.install(".")
    session.install("pip-audit")
    session.run("pip-audit")
