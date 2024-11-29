import pytest
from assertpy import assert_that

from coding_exercise.application.splitter import Splitter
from coding_exercise.domain.model.cable import Cable


def test_should_not_return_none_when_splitting_cable():
    assert_that(Splitter().split(Cable(10, "coconuts"), 1)).is_not_none()


def test_should_split_cable_correctly():
    cable = Cable(10, "coconuts")
    result = Splitter().split(cable, 1)

    assert_that(result).is_equal_to(
        [
            Cable(5, "coconuts-0"),
            Cable(5, "coconuts-1"),
        ]
    )


def test_splitter_validation():
    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(10, "coconuts"), 65)
    
    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(10, "coconuts"), -1)

    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(10, "coconuts"), 0)

    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(1, "coconuts"), 1)

    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(1, "coconuts-0"), 1)

    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(0, "coconuts-0"), 1)

    assert_that(Splitter().split).raises(ValueError).when_called_with(Cable(1025, "coconuts-0"), 1)


def test_splitting_with_remainder():
    result = Splitter().split(Cable(5, "coconuts"), 2)
    assert_that(result).is_equal_to(
        [
            Cable(1, "coconuts-0"),
            Cable(1, "coconuts-1"),
            Cable(1, "coconuts-2"),
            Cable(1, "coconuts-3"),
            Cable(1, "coconuts-4"),
        ]
    )


def test_splitting_with_small_remainder():
    result = Splitter().split(Cable(11, "coconuts"), 3)
    assert_that(result).is_equal_to(
        [
            Cable(2, "coconuts-0"),
            Cable(2, "coconuts-1"),
            Cable(2, "coconuts-2"),
            Cable(2, "coconuts-3"),
            Cable(2, "coconuts-4"),
            Cable(1, "coconuts-5"),
        ]
    )


def test_splitting_more_than_ten_chunks():
    result = Splitter().split(Cable(11, "coconuts"), 10)
    assert_that(result).is_equal_to(
        [
            Cable(1, "coconuts-00"),
            Cable(1, "coconuts-01"),
            Cable(1, "coconuts-02"),
            Cable(1, "coconuts-03"),
            Cable(1, "coconuts-04"),
            Cable(1, "coconuts-05"),
            Cable(1, "coconuts-06"),
            Cable(1, "coconuts-07"),
            Cable(1, "coconuts-08"),
            Cable(1, "coconuts-09"),
            Cable(1, "coconuts-10"),
        ]
    )
