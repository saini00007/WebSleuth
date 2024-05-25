#!/bin/bash

# Function to print "Domain Checker" in a big format with blue color
print_big_header() {
    
    echo -e "\033[35;5;1m 
 __          __  _      _____ _            _   _     
 \ \        / / | |    / ____| |          | | | |    
  \ \  /\  / /__| |__ | (___ | | ___ _   _| |_| |__  
   \ \/  \/ / _ \ '_ \ \___ \| |/ _ \ | | | __| '_ \ 
    \  /\  /  __/ |_) | ___) | |  __/ |_| | |_| | | |
     \/  \/ \___|_.__/ _____/|_|\___|\__,_|\__|_| |_|
                                                                              
                                                                                                                                                                         
\033[0m"
echo -e "\033[31;1m
          __                     __ __        _                       __                      ___       
|  | _|_ (_ | _   |_|_   .  |  ||_ |__)  | _ (_ _  _ _  _ |_. _  _   / _  _ |_|_  _ _. _  _    | _  _ | 
|/\|(-|_)__)|(-|_||_| )  .  |/\||__|__)  || )| (_)| |||(_||_|(_)| )  \__)(_||_| )(-| || )(_)   |(_)(_)| 
                                                                                         _/             


                                                                                             

\033[0m"



echo -e "\033[33;1m[==[[ ->>  Name     :          WebSleuth          <<- ]]==]\033[0m"
echo
echo -e "\033[34;1m[==[[ ->>  Telegram :    https://t.me/imnoone07   <<- ]]==]\033[0m"
echo
echo -e "\033[35;1m[==[[ ->>  Github   :    github.com/saini00007    <<- ]]==]\033[0m"
echo
echo -e "\033[36;1m[==[[ ->>  Author   :           NO_ONE            <<- ]]==]\033[0m"
echo
echo -e "\033[37;1m[==[[ ->>  Version  :             1.0             <<- ]]==]\033[0m"
echo
echo
}
check_url() {
    if curl --output /dev/null --silent --head --fail "$1"; then
        return 0
    else
        echo -e "\e[91m--->  URL is not reachable. Enter a valid URL or domain name...\e[0m"  # Printing error message in red color
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

    while true; do
        print_big_header

        echo -e "\e[33;1m--->Enter the URL like 'www.example.com' or https://example.com  :\e[0m"
        read url
        if [ "$url" = "exit" ]; then
            echo -e "\e[31;----Exiting...\e[0"
            exit 0
        fi
    modified_url=$(add_http "$url")  # Capture the modified URL
    check_url "$modified_url"
    if [ $? -eq 1 ]; then
        exit 1
    fi
    
 echo 
 echo
      # Rest of the script...
    echo -e "\e[1;31m ----------Choose an option: ----------\e[0m"
echo
echo
    echo -e "\e[1;32m1. ---> WHO_IS_Info \e[0m"
    echo 
    echo -e "\e[1;33m2. ---> Location_Info\e[0m"
    echo 
    echo -e "\e[1;34m3. ---> SSL_info\e[0m"
    echo 
    echo -e "\e[1;35m4. ---> DNS_Server_Info\e[0m"
    echo 
    echo -e "\e[1;36m5. ---> DNSSEC_Info\e[0m"
    echo 
    echo -e "\e[1;31m6. ---> HTTP_Security_Info\e[0m"
    echo 
    echo -e "\e[1;33m7. ---> Security_txt_Info\e[0m"
    echo 
    echo -e "\e[1;33m8. ---> Firewall_Info\e[0m"
    echo 
    echo -e "\e[1;34m9. ---> Block_Detection_Info\e[0m"
    echo 
    echo -e "\e[1;35m10.--->  HSTS_Info\e[0m"
    echo 
    echo -e "\e[1;36m11.--->  Linked_Pages_Info\e[0m"
    echo 
    echo -e "\e[1;31m12.--->  Archive_Info\e[0m"
    echo 
    echo -e "\e[1;32m13.--->  HeaderS_Info\e[0m"
    echo 
    echo -e "\e[1;33m14.--->  Port_scan_Info\e[0m"
    echo 
    echo -e "\e[1;34m15.--->  Tech_Stack_Info\e[0m"
    echo 
    echo -e "\e[1;35m16.--->  Social_tags_Info\e[0m"
    echo 
    echo -e "\e[1;36m17.--->  Crewl_rules_Info\e[0m"
    echo 
    echo -e "\e[1;31m18.--->  Cookies_Info\e[0m"
    echo 
    echo -e "\e[1;32m19.--->  Carbon_Info\e[0m"
    echo 
    echo -e "\e[1;33m20.--->  Get all Information\e[0m"
    echo 
    echo -e "\e[1;34m21.--->  Exit\e[0m"
    echo 
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
        *) echo -e "\e[31m---------Invalid choice---------\e[0m";;
    esac
    echo -e "\e[33;1m--->Do you want to perform another searches action ? (yes/no):\e[0m"
            read another_action
            if [ "$another_action" = "no" ]; then
                break
            fi
            
done
}


main
