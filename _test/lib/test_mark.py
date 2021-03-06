from __future__ import absolute_import
from __future__ import print_function

import ruamel.yaml as yaml
from ruamel.yaml.compat import text_type, PY3


def test_marks(marks_filename, verbose=False):
    with open(marks_filename, 'r' if PY3 else 'rb') as fp0:
        inputs = fp0.read().split('---\n')[1:]
    for input in inputs:
        index = 0
        line = 0
        column = 0
        while input[index] != '*':
            if input[index] == '\n':
                line += 1
                column = 0
            else:
                column += 1
            index += 1
        mark = yaml.Mark(marks_filename, index, line, column, text_type(input), index)
        snippet = mark.get_snippet(indent=2, max_length=79)
        if verbose:
            print(snippet)
        assert isinstance(snippet, str), type(snippet)
        assert snippet.count('\n') == 1, snippet.count('\n')
        data, pointer = snippet.split('\n')
        assert len(data) < 82, len(data)
        assert data[len(pointer) - 1] == '*', data[len(pointer) - 1]


test_marks.unittest = ['.marks']

if __name__ == '__main__':
    import test_appliance

    test_appliance.run(globals())
