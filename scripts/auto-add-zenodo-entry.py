# This script is executed when a new issue is created on our github repository. 
# In case the issue text consists only of a single line starting like a zenodo link, 
# it will retrieve all important details from the zenodo record, add it to a yml file
# and send a pull-request
import sys
from _github_utilities import create_branch, get_file_in_repository, get_issue_body, write_file, send_pull_request
import yaml
from generate_link_lists import complete_zenodo_data

def main():
    """
    Main function to handle the process of retrieving Zenodo data and appending
    it to a YAML file in a GitHub repository.

    This function takes command-line arguments for the repository name and issue number,
    retrieves the issue body, checks if it's a valid Zenodo link, retrieves corresponding
    data, and appends it to a specified YAML file by creating a new branch and submitting
    a pull request.

    Returns
    -------
    None
    """
    repository = sys.argv[1]
    issue = int(sys.argv[2])
    
    yml_filename = "resources/nfdi4bioimage.yml"
    
    
    issue_text = get_issue_body(repository, issue)
    if "\n" in issue_text or not issue_text.startswith("https://zenodo.org/records"):
        print(issue_text, " is not a zenodo link. I show myself out.")
        return

    zenodo_url = issue_text
    
    # read data from zenodo
    zenodo_data_dict = complete_zenodo_data(zenodo_url)
    zenodo_yml = "\n- " + yaml.dump(zenodo_data_dict).replace("\n", "\n  ")

    # read "database"
    branch = create_branch(repository)
    file_content = get_file_in_repository(repository, branch, yml_filename).decoded_content.decode()
    
    print("yml file content length:", len(file_content))

    # add entry
    file_content += zenodo_yml

    # save back to github
    write_file(repository, branch, yml_filename, file_content, "Add " + zenodo_url)
    res = send_pull_request(repository, branch, "Add " + zenodo_url, f"closes #{issue}") 

    print("Done.", res)
    



if __name__ == "__main__":
    main()
