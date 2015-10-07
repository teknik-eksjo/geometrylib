#!/usr/bin/env python3
import os
import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--coverage', 'with_coverage', is_flag=True)
def test(with_coverage):
    if with_coverage:
        import coverage
        COV = coverage.coverage(branch=True, include='geometrylib/*')
        COV.start()

    click.echo('Running autodiscovered tests\n{}'.format('=' * 70))
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity = 2).run(tests)

    if with_coverage:
        COV.stop()
        COV.save()
        click.echo('\nCoverage Summary\n{}'.format('=' * 70))
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
#        click.echo('HTML version: file://{}/index.html'.format(covdir))
        COV.erase()

cli.add_command(test)

if __name__ == "__main__":
    cli()