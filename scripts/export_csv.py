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

# Convert arrays to strings
def array_to_string(arr):
    if type(arr) != list:
        return str(arr)
    return ', '.join(map(str, arr))

df['tags'] = df['tags'].apply(array_to_string)
df['authors'] = df['authors'].apply(array_to_string)
df['type'] = df['type'].apply(array_to_string)
df['license'] = df['license'].apply(array_to_string)


# filter type by by
def contains_filter_word(text, words):
    return any(word in text for word in words)
df = df[df['type'].apply(lambda x: contains_filter_word(x, filter_types))]

# select columns
df = df[selected_columns]
df.head(5)

# save selected data
df.to_csv(destination, index=False)

num_rows = df.shape[0]
print(f"Exported {num_rows} rows.")
