#!/bin/bash

# Function to print "Domain Checker" in a big format with blue color
print_big_header() {
    echo -e "\e[34m
 ______   _______  _______  _______ _________ _              _______           _______  _______  _        _______  _______ 
(  __  \ (  ___  )(       )(  ___  )\__   __/( (    /|      (  ____ \|\     /|(  ____ \(  ____ \| \    /\(  ____ \(  ____ )
| (  \  )| (   ) || () () || (   ) |   ) (   |  \  ( |      | (    \/| )   ( || (    \/| (    \/|  \  / /| (    \/| (    )|
| |   ) || |   | || || || || (___) |   | |   |   \ | |      | |      | (___) || (__    | |      |  (_/ / | (__    | (____)|
| |   | || |   | || |(_)| ||  ___  |   | |   | (\ \) |      | |      |  ___  ||  __)   | |      |   _ (  |  __)   |     __)
| |   ) || |   | || |   | || (   ) |   | |   | | \   |      | |      | (   ) || (      | |      |  ( \ \ | (      | (\ (   
| (__/  )| (___) || )   ( || )   ( |___) (___| )  \  |      | (____/\| )   ( || (____/\| (____/\|  /  \ \| (____/\| ) \ \__
(______/ (_______)|/     \||/     \|\_______/|/    )_)      (_______/|/     \|(_______/(_______/|_/    \/(_______/|/   \__/
                                                                                                                                                                          
\e[0m"
}

check_url() {
    if curl --output /dev/null --silent --head --fail "$1"; then
        return 0
    else
        echo -e "\e[91mURL is not reachable. Enter a valid URL or domain name...\e[0m"  # Printing error message in red color
        return 1
    fi
}

# Function to add "http://" to URL if not present
add_http() {
    if [[ $1 != http://* && $1 != https://* ]]; then
        url="https://$1"
    else
        url="$1"
    fi
    echo "$url"  # Print the modified URL
}


# Function to run Python script with URL as argument
run_python_scripts() {
    python SRC/who_is.py "$1" &
    wait
    python SRC/location.py "$1" &
    wait
    python SRC/ssl_info.py "$1" &
    wait
    python SRC/DNS_Server.py "$1" &
    wait
    python SRC/DNSSEC.py "$1" &
    wait
    python SRC/HTTP_Security.py "$1" &
    wait
    python SRC/Security_txt.py "$1" &
    wait
    python SRC/Firewall.py "$1" &
    wait
    python SRC/Block_Detection.py "$1" &
    wait
    python SRC/HSTS.py "$1" &
    wait

    python SRC/Linked_Pages.py "$1" &
    wait
    python SRC/Archive.py "$1" &
    wait
    python SRC/header.py "$1" &
    wait
    python SRC/port_scan.py "$1" &

    wait
    python SRC/Tech_Stack.py "$1" &
    wait
    python SRC/Social_tags.py "$1" &
    wait
    python SRC/crewl_rules.py "$1" &
    wait
    python SRC/cookies.py "$1" &
    wait
    python SRC/carbon.py "$1" &
    wait # Wait for the background process to finish
}

# Main function
main() {
    print_big_header
   
    echo -e "\e[33mEnter the URL like 'www.example.com' or https://example.com  :\e[0m" 
    read url
    modified_url=$(add_http "$url")  # Capture the modified URL
    check_url "$modified_url"
    if [ $? -eq 1 ]; then
        exit 1
    fi
    echo "URL is reachable."
 
      # Rest of the script...
 echo "Choose an option:"

    echo "1. WHO_IS_Info"
    echo "2. Location_Info"
    echo "3. SSL_info"
    echo "4. DNS_Server_Info"
    echo "5. DNSSEC_Info"
    echo "6. HTTP_Security_Info"
    echo "7. Security_txt_Info"
    echo "8. Firewall_Info"
    echo "9. Block_Detection_Info"
    echo "10. HSTS_Info"
    echo "11. Linked_Pages_Info"
    echo "12. Archive_Info"
    echo "13. HeaderS_Info"
    echo "14. Port_scan_Info"
    echo "15. Tech_Stack_Info"
    echo "16. Social_tags_Info"
    echo "17. Crewl_rules_Info"
    echo "18. Cookies_Info"
    echo "19. Carbon_Info"
    echo "20. Get all Information"
    echo "21. Exit"
    read choice
    case $choice in
        1) python3 "SRC/who_is.py" "$modified_url";;
        2) python3 "SRC/location.py" "$modified_url";;
        3) python3 "SRC/ssl_info.py" "$modified_url";;
        4) python3 "SRC/DNS_Server.py" "$modified_url";;
        5) python3 "SRC/DNSSEC.py" "$modified_url";;
        6) python3 "SRC/HTTP_Security.py" "$modified_url";;
        7) python3 "SRC/Security_txt.py" "$modified_url";;
        8) python3 "SRC/Firewall.py" "$modified_url";;
        9) python3 "SRC/Block_Detection.py" "$modified_url";;
        10)python3 "SRC/HSTS.py" "$modified_url";;
        11)python3 "SRC/Linked_Pages.py" "$modified_url";;
        12)python3 "SRC/Archive.py" "$modified_url";;
        13)python3 "SRC/header.py" "$modified_url";;
        14)python3 "SRC/port_scan.py" "$modified_url";;
        15)python3 "SRC/Tech_Stack.py" "$modified_url";;
        16)python3 "SRC/Social_tags.py" "$modified_url";;
        17)python3 "SRC/crewl_rules.py" "$modified_url";;
        18)python3 "SRC/cookies.py" "$modified_url";;
        19)python3 "SRC/carbon.py" "$modified_url";;
        20) run_python_scripts "$modified_url";;  # Corrected the function call here
        21) echo "Exiting..."; exit;;
        *) echo "Invalid choice";;
    esac
}


main
