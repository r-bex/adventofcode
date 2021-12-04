I rarely get more than a week or two into AoC before getting too busy, so these folders aren't complete.

All in Python so far.

### How to use

1. Create a new folder for the day you're solving. See `How to use new_day.sh` section below.
2. Copy example data from AoC page into `example.txt`.
3. Copy real data from AoC page into `data.txt`.
3. Replace first `???` in script with example answer to part 1 from AoC page.
5. Write code in function `part1` to solve part 1 of problem & dev/test until solved.
6. Repeat for part2.

The `__main__` function of `script.py` looks like this, where you provide values in place of ??? from the AoC page.

```
if __name__ == "__main__":
    # load example and real input data
    example_input = load_input(path="example.txt")
    real_input = load_input()

    # part 1
    assert part1(example_input) == ???
    print("Part 1: {}".format(part1(values)))

    # part2
    # assert part2(example_input) = ???
    # print("Part 2: {}".format(part2(values)))
```

This means that running `python script.py` will load the example and real puzzle input, and run your `part1` and `part2` functions against the example data in `example.txt`, checking it matches the provided example answers. If it does, it will apply the functions to the real input and print out the answers for you to submit in the AoC page.

### Utils

* `template_script.py`: a template script for each day's exercise. Automatically renamed `script.py` in each day folder.
* `utils.py`: some functions that are useful in AoC, e.g. loading input data from file.

### How to use new_day.sh

If you don't already have a root level directory for the year you're working on, create that.

The following command will create a new directory `day2` in the `2021` folder and populate it with files for `data.txt`, `example.txt` and the template script, renamed to `script.py`.

```./new_day.sh 2021 day2```

