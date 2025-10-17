"""iPhone-style lyrics display app generator for 'Rock That Body' song."""

import webbrowser
import os

def create_html_file():
    """Create and open an iPhone-style lyrics display app in the browser."""
    html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>iPhone Lyrics - Rock That Body</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #000;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        
        .iphone {
            width: 375px;
            height: 812px;
            background: #1e3a8a;
            border-radius: 40px;
            padding: 0;
            box-shadow: 0 0 50px rgba(0,0,0,0.3);
            position: relative;
            overflow: hidden;
        }
        
        .status-bar {
            height: 44px;
            background: transparent;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
            color: white;
            font-weight: 600;
            font-size: 14px;
            position: relative;
            z-index: 10;
        }
        
        .time {
            font-weight: bold;
        }
        
        .status-icons {
            display: flex;
            gap: 5px;
        }
        
        .battery-icon {
            width: 20px;
            height: 10px;
            background: white;
            border: 1px solid #cccccc;
            border-radius: 1px;
            position: relative;
        }
        
        .dynamic-island {
            position: absolute;
            top: 8px;
            left: 50%;
            transform: translateX(-50%);
            width: 126px;
            height: 37px;
            background: #000;
            border-radius: 18.5px;
            z-index: 5;
        }
        
        .content {
            padding: 100px 20px 20px 20px;
            height: calc(100% - 44px);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        
        .lyrics-container {
            text-align: center;
        }
        
        .lyrics-line {
            font-size: 24px;
            line-height: 1.4;
            margin-bottom: 20px;
            color: white;
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.3s ease;
            font-weight: 500;
        }
        
        .lyrics-line.visible {
            opacity: 1;
            transform: translateY(0);
        }
        
        .lyrics-line.current {
            color: #ffffff;
            font-weight: bold;
            font-size: 26px;
        }
        

    </style>
</head>
<body>
    <div class="iphone">
        <div class="status-bar">
            <div class="time">10:02</div>
            <div class="status-icons">
                <div class="battery-icon"></div>
            </div>
        </div>
        
        <div class="dynamic-island"></div>
        
        <div class="content">
            <div class="lyrics-container" id="lyricsContainer">
                <!-- Lyrics will be populated here -->
            </div>
        </div>
    </div>

    <script>
        const lyrics = [
            { text: "(I wanna-", delay: 60 },
            { text: "I wanna rock right now)", delay: 50 },
            { text: "(I wanna-", delay: 70 },
            { text: "I wanna rock right now)", delay: 80 },
            { text: "(Now- now-", delay: 80 },
            { text: "rock right now)", delay: 68 },
            { text: "(I wanna-", delay: 70 },
            { text: "I wanna rock right now)", delay: 80 },
            { text: "(I wanna-", delay: 80 },
            { text: "I wanna rock right now)", delay: 68 },
            { text: "Rock that body", delay: 70 },
            { text: "Rock that body", delay: 80 },
            { text: "Rock that body", delay: 65 },
            { text: "Rock that body", delay: 35 },
            { text: "Bumping in your jeep, got the top dropped down", delay: 50 },
            { text: "Vroom, vroom, through the streets of the town", delay: 30 },
            { text: "Bass so loud, it's shaking the ground", delay: 49 },
            { text: "Everybody knows, we got the sound", delay: 35 },
            { text: "Rock that body", delay: 80 },
            { text: "Rock that body", delay: 80 },
            { text: "Rock that body", delay: 80 },
            { text: "Rock that body", delay: 80 },
            // Add more if needed
        ];
        let currentLine = 0;
        let isPlaying = false;
        let animationId = null;
        
        function createLyricsElements() {
            const container = document.getElementById('lyricsContainer');
            container.innerHTML = '';
            
            lyrics.forEach((lyric, index) => {
                const line = document.createElement('div');
                line.className = 'lyrics-line';
                line.id = `line-${index}`;
                line.textContent = lyric.text;
                container.appendChild(line);
            });
        }
        
        function typeLine(lineIndex) {
            if (lineIndex >= lyrics.length) {
                stopAnimation();
                return;
            }
            
            const lineElement = document.getElementById(`line-${lineIndex}`);
            const lyric = lyrics[lineIndex];
            let charIndex = 0;
            
            // Remove previous current line styling
            document.querySelectorAll('.lyrics-line.current').forEach(el => {
                el.classList.remove('current');
            });
            
            // Add current line styling
            lineElement.classList.add('current');
            lineElement.classList.add('visible');
            
            function typeChar() {
                if (charIndex < lyric.text.length && isPlaying) {
                    lineElement.textContent = lyric.text.substring(0, charIndex + 1);
                    charIndex++;
                    setTimeout(typeChar, lyric.delay);
                } else if (isPlaying) {
                    // Move to next line after a pause
                    setTimeout(() => {
                        if (isPlaying) {
                            typeLine(lineIndex + 1);
                        }
                    }, 300);
                }
            }
            
            typeChar();
        }
        
        function startAnimation() {
            isPlaying = true;
            currentLine = 0;
            createLyricsElements();
            typeLine(currentLine);
        }
        
        function stopAnimation() {
            isPlaying = false;
        }
        
        // Initialize and auto-start
        createLyricsElements();
        startAnimation();
    </script>
</body>
</html>
'''
    with open('iphone_lyrics.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    html_path = os.path.abspath('iphone_lyrics.html')

    webbrowser.open(f'file://{html_path}')
    print(f"HTML file saved as: {html_path}")

if __name__ == "__main__":
    create_html_file()
