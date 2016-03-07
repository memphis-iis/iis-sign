#!/bin/bash

images=$(identify -format '%f\n' * 2>/dev/null)

IFS=$'\n'
set -e

max_dims=$(
  identify -format '%w %h\n' $images 2>/dev/null |
  awk '($1>w){w=$1} ($2>h){h=$2} END{print w"x"h}'
  )

set +e

for image in $images; do
  convert -- "$image" -gravity Center -resize "$max_dims" "../$image"
  convert -- "../$image" -gravity Center -resize '50%' "../$image"
done
