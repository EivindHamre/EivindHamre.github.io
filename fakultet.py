import eh_lib
import sys

n = int(sys.argv[1])
svar = eh_lib.fakultet(n)
if svar >= 0:
    print ("fakulteten er: %d" % (svar))
else:
    print ("ikke lov!!!")