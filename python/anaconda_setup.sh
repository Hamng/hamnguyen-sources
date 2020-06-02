# Use: source anaconda[23]_setup.sh
# (with anaconda[23]_setup.sh being symlinks to anaconda_setup.sh

__anaconda=$(basename ${BASH_SOURCE} _setup.sh)
#echo "BASH_SOURCE=<${BASH_SOURCE}>" "__anaconda=${__anaconda}"
#exit 0

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('${HOME}/${__anaconda}/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "${HOME}/${__anaconda}/etc/profile.d/conda.sh" ]; then
        . "${HOME}/${__anaconda}/etc/profile.d/conda.sh"
	# Above prepends ${__anaconda}/condabin to $PATH
	#$SHELL -cx 'echo prepend condabin ${PATH}'
    else
        export PATH="${HOME}/${__anaconda}/bin:$PATH"
	# Above prepends ${__anaconda}/bin to $PATH
	$SHELL -cx 'echo prepend bin ${PATH}'
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

conda activate
#$SHELL -cx 'echo ${PATH}; which python; python --version; which pip'
$SHELL -cx 'which python; python --version; which pip'
