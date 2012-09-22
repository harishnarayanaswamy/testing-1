def reverse(lst):
    return lst[::-1]

def test_reverse1():
    input = [1, 2, 3, 4]
    output = [4, 3, 2, 1]
    ev = reverse(input)
    if output == ev:
        return True, None
    else:
        return False, "Four Element Case failed"
    
def test_reverse2():
    input = [1, 2, 3, 4, 5]
    output = [5, 4, 3, 2, 1]
    ev = reverse(input)
    if output == ev:
        return True, None
    else:
        return False, "Five Element Test Case failed"

def test_reverse():
     status, message = test_reverse1()
     if status == False:
            return status, message
     status, message = test_reverse2()
     if status == False:
            return status, message
     return True, None

def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
# Unncomment the 2 lines below            
#    result += left[i:]
#    result += right[j:]
    return result
    
def mergesort(list):
    if len(list) < 2:
        return list
    else:
        middle = len(list) / 2
        left = mergesort(list[:middle])
        right = mergesort(list[middle:])
        return merge(left, right)
     
def test_mergesort():
    input = [1, 7, 3, 8, 4]
    output = [1, 3, 4, 7, 8]
    ev = mergesort(input)
    if output == ev:
        return True, None
    else:
        return False, "When I pass %s to your mergesort function I get %s" % (input, ev)

def test_bsearch1():
    input = [1, 2, 3, 4]
    key = 2
    output = 1
    ev = bsearch(input, key)
    if output == ev:
        return True, None
    else:
        return False, "Key Error"

def test_bsearch2():
    input = [1, 2, 3, 4]
    key = 5
    output = -1
    ev = bsearch(input, key)
    if output == ev:
        return True, None
    else:
        return False, "Second Key Error"

def test_bsearch():
    
    status, message = test_bsearch1()
    if status == False:
        return status, message
    status, message = test_bsearch2()
    if status == False:
        return status, message
    return True, None

def test(method_name):
    state = False
    if method_name == "reverse":
        state, message = test_reverse()
        if not state:
            return "FAIL", message
    if method_name == "bsearch":
        state, message = test_bsearch()
        if not state:
            return "FAIL", message
    if method_name == "mergesort":
        state, message = test_mergesort()
        if not state:
            return "FAIL", message
    if state:
        return "SUCCESS"
    else:
        return "FAIL"
        
print test('mergesort')