:set viminfo=
:set ul=0
:set ttyfast
:%s/\([A-Za-z0-9_\-\.]*\)\.\<c\>/$(USER_BIN_DIR)\1/e
:%s/\([A-Za-z0-9_\-\.]*\)\.\<C\>/$(USER_BIN_DIR)\1/e
:%s/\([A-Za-z0-9_\-\.]*\)\.\<cxx\>/$(USER_BIN_DIR)\1/e
:%s/\([A-Za-z0-9_\-\.]*\)\.\<cpp\>/$(USER_BIN_DIR)\1/e
:%s/\([A-Za-z0-9_\-\.]*\)\.\<cc\>/$(USER_BIN_DIR)\1/e
:%s/^/        /e
:%s/\([^ ][^ ]*\) */\1 \\/e
:%s/ *$//ge
:%s/ *$//ge
:$s/ *\\ *//e
:1s/.*/USER_PROGRAMS = \\&/e
:wq
