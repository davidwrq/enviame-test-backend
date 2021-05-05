def find_palindromes_in_sub_string(input, j, k):
    """Find substring palindromes 

    Args:
        input (string): input string
        j (int): pointer  J
        k (int): pointer K

    Returns:
        count  : palindrome substring count
    """
    count = 0
    while j >= 0 and k < len(input):
        if input[j] != input[k]:
            break
        count += 1

        j -= 1
        k += 1

    return count


def find_all_palindrome_substrings(input):
    """Find all palindrome substrings

    Args:
        input (string): input string to find palindromes

    Returns:
        int: Total palindrome substring
    """
    count = 0
    for i in range(0, len(input)):
        print(i - 1, i + 1)
        count += find_palindromes_in_sub_string(input, i - 1, i + 1)
        count += find_palindromes_in_sub_string(input, i, i + 1)

    return count


s = "afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood"
print("Total palindrome substrings: ", find_all_palindrome_substrings(s))
