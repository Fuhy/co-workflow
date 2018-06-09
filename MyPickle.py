try:
    import cPickle as pickle
except:
    import pickle
from io import *
from Database import DataManager


def write_to_stream(data):
    # Simulate a file with StringIO
    out_s = BytesIO()
    # Write to the stream
    for o in data:
        # print("WRITING: %s (%s)" % (o.name, o.name_backwards))
        pickle.dump(o, out_s)
        out_s.flush()
    # Set up a read-able stream
    return bytes(out_s.getvalue())

def read_from_stream(in_s):
    result = []
    while True:
        try:
            o = pickle.load(in_s)
        except EOFError:
            return result
        else:
            # Do something for each object
            result.append(o)


# a = DataManager()
# b = a.select_from_where('*','DAG').fetchall()
# result = write_to_stream(b)
# c = read_from_stream(result)

# print(c)