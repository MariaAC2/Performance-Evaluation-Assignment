#!/bin/bash

INPUT_DIR="results"
OUTPUT_DIR="cleaned"

# Create top-level cleaned directory
mkdir -p "$OUTPUT_DIR"

# Find all CSV files recursively under results/
find "$INPUT_DIR" -type f -name "*.csv" | while read -r file; do
    # Extract relative path
    rel_path="${file#$INPUT_DIR/}"
    dir_path=$(dirname "$rel_path")
    filename=$(basename "$file")

    # Create corresponding output directory
    mkdir -p "$OUTPUT_DIR/$dir_path"

    output_file="$OUTPUT_DIR/$rel_path"

    echo "Cleaning $rel_path..."

    # Filter duplicates
    awk -F, '
    NR==1 { print; next }
    !seen[$1] || $8 > max[$1] {
        row[$1] = $0
        max[$1] = $8
        seen[$1] = NR
    }
    END {
        for (i = 1; i <= NR; i++) {
            for (s in seen)
                if (seen[s] == i)
                    print row[s]
        }
    }' "$file" > "$output_file"

    echo "Cleaned saved to: $output_file"
done
