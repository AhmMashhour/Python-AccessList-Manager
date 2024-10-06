
# This script automates the process of updating an "allow_list.txt" file by removing IP addresses listed in a "remove_list.txt".
# Make sure both 'allow_list.txt' and 'remove_list.txt' are present in the same directory as this script.

def update_allow_list(allow_list_file='allow_list.txt', remove_list_file='remove_list.txt'):
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

# If you want to run this script directly, uncomment the next two lines.
# update_allow_list()

# To run the function, simply call update_allow_list() in your Python environment.
# Ensure that 'allow_list.txt' and 'remove_list.txt' are in the same folder as this script.

