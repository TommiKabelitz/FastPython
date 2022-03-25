"""
Example script for profiling code or a module
"""
# Modules you need
import pstats, cProfile

# for sorting output
import io
from pstats import SortKey

# Initialise the profiler
prof = cProfile.Profile()

# The overall function to profile. Can be anything, output will
# include calls to all functions called by main and those called
# by those functions, etc.
# Could be imported from another module of course
def main():
    # Do stuff



if __name__ == "__main__":

    # start profiler
    prof.enable()

    main()

    # stop profiler
    prof.disable()

    # Sorting the output.
    # s is the object which will actually contain the stats at
    # the end
    s = io.StringIO()
    # Options: TIME, CUMULATIVE, PERCALL, etc. See pstats docs
    sortby = SortKey.TIME
    ps = pstats.Stats(prof, stream=s).sort_stats(sortby)

    # 100 denotes inclusion of only first 100 functions
    ps.print_stats(100)

    # Printing stats to terminal
    print(s.getvalue())

    # Saving stats to a file
    with open("profile_out.txt", "w") as f:
        f.write(s.getvalue())
