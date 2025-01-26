#/bin/bash

# loop4ever.sh secs_to_sleep command ...

secs_to_sleep=$1
shift

c=0
while true;
do
    ((c++))
    #echo -e "\n$(date +'%F %T:') ===== Iteration #$c =====\n$@"
    # Fancier way to show heading using Bash builtin printf
    # '%(datefmt)T' -1: display current time in datefmt format
    # "$*": quote all args as a single string to show
    printf "\n%(%F %T)T: ===== Iteration #%u =====\n%s\n" -1 $c "$*"
    "$@"
    sleep $secs_to_sleep
    echo -e "\n\n"
done
