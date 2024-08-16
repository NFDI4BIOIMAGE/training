import os
import yaml

def load_and_merge_yaml_files(folder):
    merged_data = {}

    # Iterate through all files in the directory
    for file_name in os.listdir(folder):
        if file_name.endswith('.yml'):
            file_path = os.path.join(folder, file_name)
            with open(file_path, 'r') as f:
                yaml_data = yaml.safe_load(f)
                
                # If the yaml_data is a dictionary, update the merged_data dictionary
                if isinstance(yaml_data, dict):
                    for key, value in yaml_data.items():
                        if key in merged_data:
                            # Merge dictionaries recursively
                            if isinstance(merged_data[key], dict) and isinstance(value, dict):
                                merged_data[key] = merge_dicts(merged_data[key], value)
                            elif isinstance(merged_data[key], list) and isinstance(value, list):
                                merged_data[key] = merge_lists(merged_data[key], value)  # Handle list of dictionaries
                            else:
                                merged_data[key] = value  # Overwrite with the last value if not mergeable
                        else:
                            merged_data[key] = value
                
                # Handle lists and other types separately
                elif isinstance(yaml_data, list):
                    merged_data.setdefault('merged_lists', []).extend(yaml_data)  # Extend lists without removing duplicates
                else:
                    merged_data.setdefault('merged_items', []).append(yaml_data)  # Handle individual items

    # Deduplicate lists of items
    if 'merged_lists' in merged_data:
        merged_data['merged_lists'] = deduplicate_list(merged_data['merged_lists'])
        if not merged_data['merged_lists']:  # Remove if empty
            del merged_data['merged_lists']
    if 'merged_items' in merged_data:
        merged_data['merged_items'] = deduplicate_list(merged_data['merged_items'])
        if not merged_data['merged_items']:  # Remove if empty
            del merged_data['merged_items']

    return merged_data

def merge_dicts(dict1, dict2):
    """Recursively merges dict2 into dict1, removing duplicates in lists."""
    for key, value in dict2.items():
        if key in dict1:
            if isinstance(dict1[key], dict) and isinstance(value, dict):
                dict1[key] = merge_dicts(dict1[key], value)
            elif isinstance(dict1[key], list) and isinstance(value, list):
                dict1[key] = merge_lists(dict1[key], value)  # Handle list of dictionaries
            else:
                dict1[key] = value  # Overwrite with the last value if not mergeable
        else:
            dict1[key] = value
    return dict1

def merge_lists(list1, list2):
    """Merges two lists, removing duplicates. Handles lists of mixed types."""
    combined_list = list1 + list2
    deduped_list = []
    seen = set()

    for item in combined_list:
        item_hashable = make_hashable(item)
        if item_hashable not in seen:
            deduped_list.append(item)
            seen.add(item_hashable)

    return deduped_list

def make_hashable(item):
    """Helper function to make a list or dict hashable."""
    if isinstance(item, dict):
        return tuple(sorted((k, make_hashable(v)) for k, v in item.items()))
    if isinstance(item, list):
        return tuple(make_hashable(i) for i in item)
    return item

def deduplicate_list(lst):
    """Deduplicates a list while preserving order, handles mixed types."""
    seen = set()
    deduped_list = []
    for item in lst:
        item_hashable = make_hashable(item)
        if item_hashable not in seen:
            deduped_list.append(item)
            seen.add(item_hashable)
    return deduped_list

def save_merged_yaml(output_file, data):
    with open(output_file, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

# Set the folder path and output file path
resources_folder = os.path.join('..', 'resources')
output_file = os.path.join('..', 'resources', 'merged_output.yml')

# Load, merge, and save data
merged_data = load_and_merge_yaml_files(resources_folder)
save_merged_yaml(output_file, merged_data)

print(f"Merged YAML files saved to {output_file}")
