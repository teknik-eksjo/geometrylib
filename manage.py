#!/usr/bin/env python3
import click

APP_FOLDER = 'geometrylib'

@click.group()
def cli():
    pass

@click.command()
@click.option('--coverage', 'with_coverage', is_flag=True)
@click.option('--no-html', is_flag=True)
@click.option('--no-report', is_flag=True)
def test(with_coverage, no_html, no_report):
    if with_coverage:
        # Initialize coverage.py.
        import coverage
        COV = coverage.coverage(branch=True, include='{}}/*'.format(APP_FOLDER))
        COV.start()

    # Run all unit tests found in tests folder.
    click.echo('Running autodiscovered tests\n{}'.format('=' * 70))
    import unittest
    tests = unittest.TestLoader().discover('tests')
    results = unittest.TextTestRunner(verbosity = 2).run(tests)

    if with_coverage:
        # Sum up the results of the code coverage analysis.
        COV.stop()
        COV.save()

        if not no_html:
            # Generate HTML report and move to tmp directory.
            import os
            basedir = os.path.abspath(os.path.dirname(__file__))
            covdir = os.path.join(basedir, 'tmp/coverage')
            COV.html_report(directory = covdir)

        if not no_report:
            # Show the report and clean up.
            click.echo('\nCoverage Summary\n{}'.format('=' * 70))
            COV.report()
            COV.erase()

    if not results.wasSuccessful():
        # Make sure to get a non-zero exit code when failing.
        raise click.ClickException('Test suite failed.')


@click.command()
def lint():
    from flake8 import main as flake8
    import sys

    click.echo('Running Linter\n{}'.format('=' * 70))
    sys.argv = ['flake8', APP_FOLDER]
    flake8.main()


cli.add_command(test)
cli.add_command(lint)

if __name__ == "__main__":
    cli()
