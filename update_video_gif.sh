#!/bin/bash
# Script to ensure GIF is updated whenever video is updated

VIDEO_FILE="img/videos/game_showcase_extended.mp4"
GIF_FILE="img/videos/game_showcase_extended.gif"

if [ -f "$VIDEO_FILE" ]; then
    echo "Updating GIF from video..."
    ffmpeg -y -i "$VIDEO_FILE" -vf "fps=10,scale=800:-1:flags=lanczos" "$GIF_FILE"
    echo "GIF updated successfully"
    
    # Update README if needed
    if grep -q "game_showcase_extended.gif" README.md; then
        echo "README.md already references the latest GIF"
    else
        echo "Updating README.md to reference latest GIF"
        sed -i 's/game_showcase\.gif/game_showcase_extended.gif/g' README.md
    fi
else
    echo "Video file not found: $VIDEO_FILE"
fi
