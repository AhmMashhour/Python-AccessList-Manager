# IP Allow List Updater

This project automates the process of updating an `allow_list.txt` by removing IP addresses listed in `remove_list.txt`.

## How to Use

1. Place the `allow_list.txt` and `remove_list.txt` files in the same directory as the Python script.
   - `allow_list.txt`: Contains the list of allowed IP addresses (one per line).
   - `remove_list.txt`: Contains the list of IP addresses to be removed.

2. Run the script by executing the following command in your terminal:
   ```bash
   python update_allow_list.py
   ```

3. The script will update the `allow_list.txt` by removing the IP addresses listed in `remove_list.txt`.

## Requirements

- Python 3.x

## Example

### Before running the script:

**allow_list.txt**:
```
192.168.1.1
192.168.1.2
192.168.1.3
192.168.1.4
192.168.1.5
```

**remove_list.txt**:
```
192.168.1.2
192.168.1.4
```

### After running the script:

**allow_list.txt**:
```
192.168.1.1
192.168.1.3
192.168.1.5
```

By following the steps above, you can easily maintain your allow list by removing unwanted IP addresses.