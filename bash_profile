#!/usr/bin/env bash

export BASH_PROFILE_PATH=$HOME/bash_profile

# Bash aliases
source "$HOME/bash_profile/bash_aliases.bash"

# Git aliases
source "$HOME/bash_profile/git-tools/aliases.sh"

# Git aliases
source "$HOME/bash_profile/git-tools/display_gitbranch"


# dsutils to path
export PATH=$PATH:/$HOME/bash_profile/dsutils
