from argparse import ArgumentParser
 
def decorator(func):
    def graphical_parse_args(self, args=None, namespace=None):
        print "+-----------------+"
        print "| PSEUDO-GUI      |"
        print "+-----------------+"
        # TODO: This should build a proper widget
        values = [raw_input("Enter %s (%s):" % (a.dest, a.help)) for a in self._actions]
        # TODO: This should build a proper list of args from what we retrieve in the widgets
        arg_lst = []
        for v, a in zip(values, self._actions):
            opt_str = a.option_strings
            if v:
                if a.nargs == 0:
                    arg_lst.append(opt_str[0])
                else:
                    if opt_str:
                        arg_lst.append(opt_str[0])
                    arg_lst.append(v)
        print(arg_lst)
        raw_input('Press enter to start')
        # update new args with what you get from the graphical widgets
        return self.original_parse_args(arg_lst, namespace)
 
    def inner(*args, **kwargs):
        ArgumentParser.original_parse_args = ArgumentParser.parse_args
        ArgumentParser.parse_args = graphical_parse_args
        return func(*args, **kwargs)
    return inner
 
@decorator
def main():
    """Main"""
    bar = 'bar'
    foo = '-foo'
    parser = ArgumentParser(description='Desc')
    parser.add_argument(bar, help=('bar'))
    parser.add_argument(foo, help=('foo'))
    args = parser.parse_args()
    print(args)
    return True
 
 
if __name__ == '__main__':
    main()
