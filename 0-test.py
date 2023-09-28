import getopt, sys
opts, args = getopt.getopt(sys.argv[1:], 'f:m:', ['name', 'msg'])
print(opts, args)