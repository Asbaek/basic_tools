def compare_sw_names(str1,str2):
    """Takes two software names and compares each word and version numbers.
       Returns true if all parts of one of the str can be found in the other 
    """
    str1=str1.lower()
    str2=str2.lower()
    wordlist1 = str1.split()
    wordlist2 = str2.split()
    def left_compare_strings(str1,str2):
        """Compares strings, such as 1.1.1 and 1.1 and returns True
           if one is contained in the other. Otherwise False.
        """
        if len(str1)<=len(str2):
            str2 = str2[:len(str1)] 
        else:
            str1 = str1[:len(str2)]
        return (str1==str2)
    def lookup(list1,list2):
        result = []
        for w1 in list1:
            found=False
            for w2 in list2:
                if left_compare_strings(w1,w2):
                   found=True
                   break
            result.append(found)
        is_match = False not in result
        return is_match 
    return lookup(wordlist1,wordlist2) or lookup(wordlist2,wordlist1)


def test_compare_sw_names():
    """Perform a unit test by 'py.test filename.py' """
    assert compare_sw_names("test 1.2.3","THIS IS A TEST 1.2.3")==True #Extra words
    assert compare_sw_names("THIS IS A TEST 1.2.3.4","test 1.2.3")==True #Extra words
    assert compare_sw_names("test","tset")==False #Different texts
    assert compare_sw_names("tset","test")==False #Different texts
    assert compare_sw_names("test 1.2.3", "test 1.1.2.3")==False # Different sw versions
    assert compare_sw_names("test 1.1.2.3", "test 1.2.3")==False # Different sw versions
    assert compare_sw_names("test 1.2.3","test 1.2")==True #Same sw subversions
    assert compare_sw_names("test 1.2","test 1.2.3")==True #Same sw subversions
