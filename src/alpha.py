# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 13:17:27 2020

@author: Rybakov
"""

# Outer modules.
import functools

# Own modules.
import maths
import combinatorics

#---------------------------------------------------------------------------------------------------
# Functions.
#---------------------------------------------------------------------------------------------------

def get_traces_list(log):
    """
    Get list of traces.

    Arguments:
        log -- Log.

    Result:
        Traces list.
    """

    return [trace for (trace, count) in log]

#---------------------------------------------------------------------------------------------------

def is_subsets_relate(sa, sb, al, r, t):
    """
    Check if two subsets relate with given type of relation.

    Arguments:
        sa -- First subset,
        sb -- Second subset,
        al -- Activities list,
        r -- Relation table,
        t - Relation type.

    Result:
        If first subset relates to second subset with given type of relation.
    """

    for a in sa:
        for b in sb:
            if r[al.index(a)][al.index(b)] != t:
                return False

    return True

#---------------------------------------------------------------------------------------------------

def is_subset_clique(s, al, r, t):
    """
    Check if subset is clique of given type.

    Arguments:
        s -- Subset,
        al -- Activities list,
        r -- Relation table,
        t -- Clique type.

    Result:
        True -- If subset is a clique of given type,
        Fals -- Otherwise.
    """

    return is_subsets_relate(s, s, al, r, t)

#---------------------------------------------------------------------------------------------------

def apply_alpha_algorithm(log):
    """
    Apply alpha algorithm.

    Arguments:
        log -- Log.

    Result:
        Configuration of WF-net.
    """

    traces_list = get_traces_list(log)

    # Total activities, input and output activities.
    activities_set = set(functools.reduce(lambda x, y: x + y, traces_list))
    input_activities_set = set([t[0] for t in traces_list])
    output_activities_set = set([t[-1] for t in traces_list])

    #print('Activities : ', activities_set, input_activities_set, output_activities_set)

    # Generate G-table.
    activities_list = sorted(list(activities_set))
    activities_count = len(activities_list)
    g_table = maths.generate_zero_matrix(activities_count)

    # Fill G-table.
    for trace in traces_list:
        for i in range(len(trace) - 1):
            g_table[activities_list.index(trace[i])][activities_list.index(trace[i + 1])] = 1

    #print('G-table : ', g_table)

    # Generate R-table.
    #   0 - not initialized,
    #   1 - "->"
    #   2 - "<-"
    #   3 - "#"
    #   4 - "||"
    r_table = maths.generate_zero_matrix(activities_count)
    for i in range(activities_count):
        for j in range(activities_count):
            r_table[i][j] = 0
            g_dir = g_table[i][j]
            g_inv = g_table[j][i]
            if (g_dir == 1) and (g_inv == 0):
                r_table[i][j] = 1
                r_table[j][i] = 2
            elif (g_dir == 0) and (g_inv == 1):
                r_table[i][j] = 2
                r_table[j][i] = 1
            elif (g_dir == 0) and (g_inv == 0):
                r_table[i][j] = 3
                r_table[j][i] = 3
            elif (g_dir == 1) and (g_inv == 1):
                r_table[i][j] = 4
                r_table[j][i] = 4
            else:
                raise Exception('wrong values from G-table')

    #print('R-table : ', r_table)

    # Form X set.
    x_list = []
    subsets_list = combinatorics.get_subsets_list(activities_set)
    subsets_list = [s for s in subsets_list if s != set()]
    for sa in subsets_list:
        for sb in subsets_list:
            if sa & sb == set():
                if is_subset_clique(sa, activities_list, r_table, 3):
                    if is_subset_clique(sb, activities_list, r_table, 3):
                        if is_subsets_relate(sa, sb, activities_list, r_table, 1):
                            x_list.append((sa, sb))

    #print('X-list : ', x_list)

    # Form Y set.
    y_list = []
    for (sa, sb) in x_list:
        is_max = True
        for (sa1, sb1) in x_list:
            if (sa1 >= sa) and (sb1 >= sb) and ((sa1 > sa) or (sb1 > sb)):
                is_max = False
                break
        if is_max:
            y_list.append((sa, sb))

    #print('Y-list : ', y_list)

    return (activities_list,
            list(input_activities_set),
            list(output_activities_set),
            y_list)

#---------------------------------------------------------------------------------------------------
# Run.
#---------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # Example log.
    log = \
        [
            (['a', 'b', 'e', 'f'], 2),
            (['a', 'b', 'e', 'c', 'd', 'b', 'f'], 3),
            (['a', 'b', 'c', 'e', 'd', 'b', 'f'], 2),
            (['a', 'b', 'c', 'd', 'e', 'b', 'f'], 4),
            (['a', 'e', 'b', 'c', 'd', 'b', 'f'], 3)
        ]

    # Check alpha.
    assert apply_alpha_algorithm(log) == (['a', 'b', 'c', 'd', 'e', 'f'],
                                          ['a'],
                                          ['f'],
                                          [({'c'}, {'d'}), ({'a'}, {'e'}),
                                           ({'b'}, {'c', 'f'}), ({'e'}, {'f'}),
                                           ({'a', 'd'}, {'b'})])

#---------------------------------------------------------------------------------------------------
