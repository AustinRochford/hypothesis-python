# coding=utf-8
#
# This file is part of Hypothesis (https://github.com/DRMacIver/hypothesis)
#
# Most of this work is copyright (C) 2013-2015 David R. MacIver
# (david@drmaciver.com), but it contains contributions by others. See
# https://github.com/DRMacIver/hypothesis/blob/master/CONTRIBUTING.rst for a
# full list of people who may hold copyright, and consult the git log if you
# need to determine who owns an individual contribution.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.
#
# END HEADER

from __future__ import division, print_function, absolute_import

import pytest

from hypothesis import find, given, settings
from hypothesis.errors import InvalidArgument
from hypothesis.strategies import sets, lists, floats, randoms, integers, \
    frozensets


def test_can_clone_same_length_items():
    ls = find(
        lists(frozensets(integers(), min_size=10, max_size=10)),
        lambda x: len(x) >= 20
    )
    assert len(set(ls)) == 1


def test_unique_lists_error_on_too_large_average_size():
    with pytest.raises(InvalidArgument):
        lists(integers(), unique=True, average_size=10, max_size=5).example()


@given(randoms())
@settings(max_examples=5)
def test_can_draw_sets_of_hard_to_find_elements(rnd):
    rarebool = floats(0, 1).map(lambda x: x <= 0.01)
    find(
        sets(rarebool, min_size=2), lambda x: True,
        random=rnd, settings=settings(database=None))
