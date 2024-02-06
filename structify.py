# function to pair chords up by id
def preprocess_chords(radians, chord_ids):
    chord_mapping = {}
    for radian, chord_id in zip(radians, chord_ids):
        chord_num = chord_id[2]
        if chord_num not in chord_mapping:
            chord_mapping[chord_num] = {}
        if "s" in chord_id:
            chord_mapping[chord_num]["start"] = radian
        else:
            chord_mapping[chord_num]["end"] = radian
    # print(chord_mapping)
    return list(chord_mapping.values())


# helper to check if point of one chord is in between the other chord
def is_between(start, mid, end):
    if start < end:
        return start < mid < end
    # chord crosses the 0 radian 
    else:
        return mid > start or mid < end

# helper to check if the chords intersect
def has_intersection(chord1, chord2):
    A_s, A_e = chord1["start"], chord1["end"]
    B_s, B_e = chord2["start"], chord2["end"]

    # Check if A's start or end is between B's start and end, and vice versa to check for intersecting chords
    return is_between(B_s, A_s, B_e) != is_between(B_s, A_e, B_e) and is_between(
        A_s, B_s, A_e
    ) != is_between(A_s, B_e, A_e)

# main function to count intersections 
def count_intersections(chords):
    intersection_count = 0

    # loop through pairs without redundantly counting
    for i in range(len(chords)):
        for j in range(i + 1, len(chords)):
            if has_intersection(chords[i], chords[j]):
                intersection_count += 1

    return intersection_count


# test cases
testcase_1 = (
    [0.78, 1.47, 1.77, 3.92], 
    ["s_1", "s_2", "e_1", "e_2"], 
    1
)

testcase_2 = (
    [0.1, 0.2, 2.9, 3.0, 5.9, 6.0],
    ["s_1", "e_1", "s_2", "e_2", "s_3", "e_3"],
    0
)

testcase_3 = (
    [6.0, 0.5, 3.0, 3.5], 
    ["s_1", "e_1", "s_2", "e_2"],
    0
)

testcase_4 = (
    [0.2, 1.2, 0.4, 1.4, 2.0, 3.0, 2.2, 3.2, 4.0, 5.0],
    ["s_1", "e_1", "s_2", "e_2", "s_3", "e_3", "s_4", "e_4", "s_5", "e_5"],
    2
)

testcase_5 = (
    [0.1, 2.5, 0.3, 2.7, 1.0, 3.5, 1.2, 3.7, 4.0, 5.5, 4.2, 5.7, 6.0, 0.5],
    ["s_1", "e_1", "s_2", "e_2", "s_3", "e_3", "s_4", "e_4", "s_5", "e_5", "s_6", "e_6", "s_7", "e_7"],
    9
)

testcase_6 = (
    [0.2, 1.8, 0.4, 2.0, 3.1, 4.7, 3.3, 4.9, 5.0, 6.6, 5.2, 6.8, 0.6, 2.2, 3.5, 5.1, 3.7, 5.3, 6.0, 0.8],
    ["s_1", "e_1", "s_2", "e_2", "s_3", "e_3", "s_4", "e_4", "s_5", "e_5", "s_6", "e_6", "s_7", "e_7", "s_8", "e_8", "s_9", "e_9", "s_10"],
    15
)

testcase_list = [testcase_1, testcase_2, testcase_3, testcase_4, testcase_5, testcase_6]
all_tests_passed = True
for i, (radians_list, chord_ids, expected) in enumerate(testcase_list):
    chords = preprocess_chords(radians_list, chord_ids)
    result = count_intersections(chords)
    try:
        assert result == expected, f"Testcase {i+1} failed: Expected {expected}, got {result}"
    except AssertionError as e:
        all_tests_passed = False
        print(e)

if all_tests_passed:
    print("All test cases passed successfully!")
