# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:53:47 2020

@author: Rybakov
"""

#---------------------------------------------------------------------------------------------------
# Functions.
#---------------------------------------------------------------------------------------------------

def get_masked_list(l, m):
    """
    Get list elements by mask.

    Arguments:
        l -- List,
        m -- Mask.

    Result:
        Masked list.
    """

    return [e for (i, e) in enumerate(l) if m & (1 << i)]

#---------------------------------------------------------------------------------------------------

def get_subsets_list(s):
    """
    Get list of all nonempty subsets.

    Arguments:
        s -- Set.

    Result:
        List of all nonempty subsets.
    """

    return [set(get_masked_list(list(s), m)) for m in range(2 ** len(s))]

#---------------------------------------------------------------------------------------------------
# Tests.
#---------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # Masked list.
    assert get_masked_list(['a', 'b', 'c'], 0) == []
    assert get_masked_list(['a', 'b', 'c'], 1) == ['a']
    assert get_masked_list(['a', 'b', 'c'], 2) == ['b']
    assert get_masked_list(['a', 'b', 'c'], 3) == ['a', 'b']
    assert get_masked_list(['a', 'b', 'c'], 4) == ['c']
    assert get_masked_list(['a', 'b', 'c'], 5) == ['a', 'c']
    assert get_masked_list(['a', 'b', 'c'], 6) == ['b', 'c']
    assert get_masked_list(['a', 'b', 'c'], 7) == ['a', 'b', 'c']

    # Subsets list.
    assert get_subsets_list(set()) == [set()]
    assert get_subsets_list({1}) == [set(), {1}]
    assert get_subsets_list({1, 2}) == [set(), {1}, {2}, {1, 2}]
    assert get_subsets_list({1, 2, 3}) == [set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]


#---------------------------------------------------------------------------------------------------
