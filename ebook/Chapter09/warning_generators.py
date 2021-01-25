import sys

# generator expression
inname, outname = sys.argv[1:3]


# (venv) nguyendangtuan@Nguyens-MacBook-Pro Chapter09 % python warning_generators.py sample_log.txt warning_log.txt


def generator():
    with open(inname) as infile:
        with open(outname, 'w') as outfile:
            warnings = (l.replace("WARNING", "") for l in infile if 'WARNING' in l)
            for line in warnings:
                outfile.write(line)


generator()

outname = "normal_" + outname


def normal_loop():
    with open(inname) as infile:
        with open(outname, 'w') as outfile:
            for line in infile:
                if "WARNING" in line:
                    outfile.write(line.replace("\tWARNING", ""))


normal_loop()


class WarningFilter:
    def __init__(self, sequence):
        self.sequence = sequence

    def __iter__(self):
        return self

    def __next__(self):
        line = self.sequence.readline()
        while line and "WARNING" not in line:
            line = self.sequence.readline()
        if not line:
            raise StopIteration
        return line.replace("\tWARNING", "")


outname = "oop_" + outname


def oopReader():
    with open(inname) as infile:
        with open(outname, 'w') as outfile:
            filter = WarningFilter(infile)
            for line in filter:
                outfile.write(line)


oopReader()

outname = "yield_" + outname


def warning_filter(sequence):
    for line in sequence:
        if "WARNING" in line:
            yield line.replace("\tWARNING", "")


print(dir(warning_filter))


def generator_yield():
    with open(inname) as infile:
        with open(outname, "w") as outfile:
            filter = warning_filter(infile)
            for line in filter:
                outfile.write(line)


generator_yield()

outname = "yield_form_" + outname


def warning_filter_yield_from(inname):
    with open(inname) as infile:
        yield from (
            line.replace("\tWARNING", "") for line in infile if "WARNING" in line
        )


print(dir(warning_filter_yield_from))


def write_out_filter():
    filter = warning_filter_yield_from(inname)
    with open(outname, "w") as outfile:
        for line in filter:
            outfile.write(line)


write_out_filter()
#
# with open(inname) as infile:
#     with open(outname, "w") as outfile:
#         warnings = (
#             l.replace("\tWARNING", "") for l in infile if "WARNING" in l
#         )
#         for l in warnings:
#             outfile.write(l)
#
# # normal loop
# with open(inname) as infile:
#     with open(outname, "w") as outfile:
#         for l in infile:
#             if "WARNING" in l:
#                 outfile.write(l.replace("\tWARNING", ""))
#
#
# # object-oriented
# class WarningFilter:
#     def __init__(self, insequence):
#         self.insequence = insequence
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         l = self.insequence.readline()
#         while l and "WARNING" not in l:
#             l = self.insequence.readline()
#         if not l:
#             raise StopIteration
#         return l.replace("\tWARNING", "")
#
#
# with open(inname) as infile:
#     with open(outname, "w") as outfile:
#         filter = WarningFilter(infile)
#         for l in filter:
#             outfile.write(l)
#
#
# # Generator with yield
# def warnings_filter(insequence):
#     for l in insequence:
#         if "WARNING" in l:
#             yield l.replace("\tWARNING", "")
#
#
# with open(inname) as infile:
#     with open(outname, "w") as outfile:
#         filter = warnings_filter(infile)
#         for l in filter:
#             outfile.write(l)
#
#
# # Generator with yield from
# def warnings_filter(infilename):
#     with open(infilename) as infile:
#         yield from (
#             l.replace("\tWARNING", "") for l in infile if "WARNING" in l
#         )
#
#
# filter = warnings_filter(inname)
# with open(outname, "w") as outfile:
#     for l in filter:
#         outfile.write(l)
