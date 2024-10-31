# This file exports selected data as csv file
source = "./resources/"
destination = './docs/export/training_materials.csv'

# We filter by specific content types
filter_types = ['course', 'tutorial', 'video', 'blog', 'workshop', 'notebook']

# We keep only selected columns
selected_columns = ["name", "authors", "url", "tags", "license", "description"]

# ------------------------------------------------------------------------------
# Do not modify anything further down
from generate_link_lists import load_dataframe

df = load_dataframe(source)

def array_to_string(arr):
    """
    Convert an array to a string.

    Parameters
    ----------
    arr : list or any type
        The array or element to convert to a string. If it's not a list,
        the element is converted to a string directly.

    Returns
    -------
    str
        A comma-separated string representation of the array or the string
        representation of the element if it's not an array.
    """
    if type(arr) != list:
        return str(arr)
    return ', '.join(map(str, arr))

df['tags'] = df['tags'].apply(array_to_string)
df['authors'] = df['authors'].apply(array_to_string)
df['type'] = df['type'].apply(array_to_string)
df['license'] = df['license'].apply(array_to_string)

def contains_filter_word(text, words):
    """
    Check if any of the filter words are present in the text.

    Parameters
    ----------
    text : str
        The text in which to search for filter words.
    words : list
        A list of words to check for in the text.

    Returns
    -------
    bool
        True if any filter word is found in the text, False otherwise.
    """
    return any(str(word).lower() in str(text).lower() for word in words)

df = df[df['type'].apply(lambda x: contains_filter_word(x, filter_types))]

# select columns
df = df[selected_columns]

# save selected data
df.to_csv(destination, index=False)

num_rows = df.shape[0]
print(f"Exported {num_rows} rows.")
