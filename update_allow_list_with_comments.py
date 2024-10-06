
"""
Script to update the allow_list.txt by removing IPs listed in remove_list.txt.
Make sure both 'allow_list.txt' and 'remove_list.txt' are present in the same directory as this script.
"""

def update_allow_list(allow_list_file='allow_list.txt', remove_list_file='remove_list.txt'):
    """
    Function to update the allow list by removing IPs found in the remove list.
    - allow_list_file: Path to the allow list file.
    - remove_list_file: Path to the remove list file.
    """
    # Step 1: Open and read the allow_list.txt file
    with open(allow_list_file, 'r') as file:
        ip_addresses = file.read()

    # Step 2: Convert the IP addresses string into a list
    ip_addresses = ip_addresses.split()

    # Step 3: Open and read the remove_list.txt file
    with open(remove_list_file, 'r') as file:
        remove_ips = file.read().split()

    # Step 4: Remove IPs from the allow list if they exist in the remove list
    for ip in remove_ips:
        if ip in ip_addresses:
            ip_addresses.remove(ip)

    # Step 5: Write the updated IP addresses back to the allow_list.txt file
    with open(allow_list_file, 'w') as file:
        file.write("\n".join(ip_addresses))

    print(f"Updated {allow_list_file}. The following IPs were removed: {', '.join(remove_ips)}")

# Uncomment the line below to run the function directly
# update_allow_list()

# To run this script, call the update_allow_list() function. Ensure that 'allow_list.txt' 
# and 'remove_list.txt' are present in the same folder as this script.

