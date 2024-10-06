from olympics.__main__ import main
import pytest
import argparse

def test_countries():
    argv = ['countries']
    main(argv)

def test_collective():
    argv = ['collective']
    main(argv)

def test_individual():
    argv = ['individual']
    main(argv)

def test_negative_top_2():
    with pytest.raises(argparse.ArgumentTypeError):
        argv = ['individual', '--top', '-5']
        main(argv)