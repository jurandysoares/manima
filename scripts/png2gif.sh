#!/bin/bash

# Convert PNG to GIF

for size in 32 72 128 512; do
    cd "${size}"

    for img in *.png; do
        convert "${img}" "../../animal/${size}/_${img%.png}.gif"
        convert "${img}" -flop "../../animal/${size}/${img%.png}_.gif"
    done

    cd -
done