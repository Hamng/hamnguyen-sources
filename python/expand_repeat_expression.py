# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 14:43:34 2021

@author: Ham
Cisco interview test: expand a repeat (string) expression

"""

import io

# 3rd line == expected result
STDIN_SIO = io.StringIO("""
abcde{-1}{-2}{-3}
(ab){3}WX(YZ){2}
(){200}
(((X){4}a){2}(bcde){3})
(d(X)e(ab(c){2}d){3})
((2){2}(3){3})(44){-4}(555){0}666{-7}
abc(de){3}
abc){2}
ab(12345){-2}cd
fg(abc)de
123{4}45{2}67
{25}abc
""".strip())

def get_count_and_move(s: str, pos: list) -> int:
    """
    Extract a repeat {count} from s[pos[0]:]

    Args:
        s (str): the string to extract from.
        pos (list): pos[0] points to the next char in s to start extracting.

    Returns:
        int: the repeat count that was extracted.
        pos[0]: since it's pass-by-reference, this function advances pos[0],
        then implicitly returns pos[0] to the caller.

    """

    if pos[0] >= len(s) or s[pos[0]] != '{':
        return 1

    # Extract the substring that begins after '{' and ends before '}',
    # then cast that substring to an integer.
    # Advance pos[0] to the position after '}'
    pos[0] += 1
    end = s.index('}', pos[0])
    count = int(s[pos[0]:end])
    pos[0] = end + 1
    return count


def expand_repeat_expr(s: str, pos: list = None) -> str:
    """
    Expand a parenthesized string, s, which may be immediately
    followed by a repeat count {N}
    But if {N} is preceded not by a parenthesized expr,
    then it'll repeat the preceding single char N times.
    A 0 or negative {N} replaces the preceding parenthesized expr
    or single char (if non-empty) with an empty string,
    so effectively removes the preceding.

    Args:
        s (str): the input string to be expanded.
        pos (list): pos[0] points to the next char in s to be expanded.

    Returns:
        str: the expanded string.
        pos[0]: since it's pass-by-reference, this function advances pos[0],
        then implicitly returns pos[0] to the caller.

    Limitations:
        {N} must be a proper integer (which also means it must not nest).
        s must be properly balanced.
        (Bug: the very first '(' might be omitted; e.g. "123)456")
    """

    res = ""
    if pos is None:
        pos = [0]
    #print(s, pos)
    while pos[0] < len(s):
        cur = s[pos[0]]
        pos[0] += 1
        if cur == '(':
            # Recursively call this same function to process a nested expr
            # Implicitly, callee already advanced pos[0] to the next char in s.
            res += expand_repeat_expr(s, pos)
            #print(pos, cur, "nested", res)
            continue
        elif cur == ')':
            # End of a parenthesized expr,
            # see if it's possibly followed by a repeat {count}.
            # If 0 or negative count, return an empty string.
            # Else return res after repeating it count times.
            # Implicitly, callee already advanced pos[0] to the next char in s,
            # so return it as-is to caller
            count = get_count_and_move(s, pos)
            if count < 1:
                res = ""
            elif count > 1 and res:
                res *= count
            #print(pos, cur, "returning", res)
            return res
        elif cur == '{':
            # Hit a repeat {count} that is not preceded by a parenthesized
            # expr, so backoff 1 char before extracting {count}
            # If 0 or negative count, delete the last char in res.
            # Else repeat the last char count-1 times, then append to res.
            # Implicitly, callee already advanced pos[0] to the next char in s.
            pos[0] -= 1
            count = get_count_and_move(s, pos)
            if count < 1:
                # ""[:-X] yields ""
                res = res[:-1]
            elif count > 1 and res:
                res += (res[-1] * (count - 1))
            continue
        else:
            # None of the above, just append cur to res
            res += cur
    return res


def get_repeat_count(s: list) -> int:
    #if not s:
    #    return 1
    #print('Count =', s)
    res = s.pop(0)
    if res == '{':
        res = ""
    while s:
        c = s.pop(0)
        if c == '}':
            break
        res += c
    #print("Got x" + res)
    return int(res)

def expand_repeat_expr_pop(s: list) -> str:
    """
    Expand a parenthesized string, s, which may be immediately
    followed by a repeat count {N}
    A 0 or negative {N} replaces the preceding parenthesized expr
    (if non-empty) with an empty string, so effectively removes it.

    Args:
        s (list): the input string to be expanded, but given as a list[].

    Returns:
        str: the expanded string.

    Limitations:
        s must be properly balanced.
        (Bug: the very first '(' might be omitted; e.g. "123)456")
        {N} must be a proper integer (which also means it must not nest).
        (Bug: {N} not immediately preceded by a parenthesized expr is ignored
         and left as-is; e.g. "123{4}56" returns as-is.)
    """
    if type(s) is not list:
        # s isn't a list[], then rerun this function but cast s to a list[]
        return expand_repeat_expr_pop(list(s))
    #print('Str', s)
    #res = s.pop(0)
    #if res == '(':
    #    res = ""
    # Assumption: s[0] is right after a '(', and s[0] itself could be a '(' too
    res = ""
    while s:
        c = s.pop(0)
        if c == ')':
            # got a parenthesized string, see if followed by a repeat count
            if s and s[0] == '{':
                # it's immediately followed by a repeat count {N}, so get it
                count = get_repeat_count(s)
                if count <= 0:
                    res = ""
                elif count > 1 and res:
                    # dup'ing res only if count > 1 and res is non-empty
                    res *= count
                    #print("after repeat", res)
            return res
        elif c == '(':
            # Recursively call this same function to handle a nested expr
            #s.insert(0, c)
            res += expand_repeat_expr_pop(s)
            #print("after nest res=", res)
        else:
            res += c
    #print('Returning', res)
    return "".join(res)


if __name__ == '__main__':
    while True:
        if not (line := STDIN_SIO.readline().strip()):
            break
        print('"' + line + '" -> "' + expand_repeat_expr(line) + '"')
