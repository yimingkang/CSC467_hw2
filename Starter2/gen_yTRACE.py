import re
import sys

def gen(fname):
    """
    Add yTRACE output
    """
    l_matcher = re.compile('^(\S+)')
    r_matcher = re.compile('\s+(\:|\|)\s+(.*)')
    empty_matcher = re.compile('\s+(\:|\|)\s*$')
    current_rule = None

    with open(fname, "r") as f:
        for line in f:
            line = line.strip("\n")
            l_match = l_matcher.match(line)
            r_match = r_matcher.match(line)
            e_match = empty_matcher.match(line)
            if l_match is not None:
                # start of new rule
                current_rule = l_match.group(0)
                print line
            elif r_match is not None:
                # yTRACE the output
                print get_newline(line, current_rule, r_match.group(2))
            elif e_match is not None:
                # add an empty comment
                print line, " /*empty*/"

def get_newline(line, current_rule, matched_rule):
    # formated print -- also removes trailing spaces
    part = "{oline} {{ yTRACE(\"{rule} -> {matched}\\n\");}}".format(
        oline=line.rstrip(),
        rule=current_rule,
        matched=matched_rule.strip(),
    )
    return part

if __name__ == '__main__':
    gen(sys.argv[1])
