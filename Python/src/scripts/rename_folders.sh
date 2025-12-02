changeFolderName(){
    generateWildcard $1
    for folder in $(ls $path | grep "\-$1")
    do
        if test -d $folder 
        then
            mv "$folder" "${folder%$wildcard}"
        fi
    done
}

generateWildcard(){
    text=""
    i=0
    while [ $i -le ${#1} ]
    do
        text+="?"
        i=$(( $i + 1 ))
    done
    wildcard="$text"
}

changeFolderName "master"
changeFolderName "main"
