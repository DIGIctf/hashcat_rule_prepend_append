import itertools
import sys

# Default values for prepend and append
default_prepend = 1
default_append = 1

# Allowed symbols
allowedsymbols = "012"

def generate_combinations(prepend=default_prepend, append=default_append):
    # Generate combinations for prepends
    prepend_combinations = [' '.join(['^' + s for s in ''.join(p)]) for p in itertools.product(allowedsymbols, repeat=prepend)]
    
    # Generate combinations for appends
    append_combinations = [' '.join(['$' + s for s in ''.join(a)]) for a in itertools.product(allowedsymbols, repeat=append)]
    
    # Output the combinations
    for p in prepend_combinations:
        for a in append_combinations:
            print(p + ' ' + a)

if __name__ == "__main__":
    # Parse command line arguments
    prepend = int(sys.argv[1]) if len(sys.argv) > 1 else default_prepend
    append = int(sys.argv[2]) if len(sys.argv) > 2 else default_append
    
    # Generate and output combinations
    generate_combinations(prepend, append)
