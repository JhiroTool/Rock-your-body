const colorSchemes = {
    A: ["#00ffff", "#00ffff", "#ff00ff", "#ff00ff"],
    B: ["#ffff00", "#ffff00", "#ff8000", "#ff8000"],
};

const lyrics = [
    { text: "(I wanna-", delay: 60, colors: "A" },
    { text: "I wanna rock right now)", delay: 80, colors: "A" },
    { text: "(I wanna-", delay: 70, colors: "A" },
    { text: "I wanna rock right now)", delay: 80, colors: "A" },
    { text: "(Now- now-", delay: 80, colors: "A" },
    { text: "rock right now)", delay: 68, colors: "A" },
    { text: "(I wanna-", delay: 70, colors: "A" },
    { text: "I wanna rock right now)", delay: 80, colors: "A" },
    { text: "(I wanna-", delay: 69, colors: "A" },
    { text: "I wanna rock right now)", delay: 35, colors: "A" },
    { text: "Rock that body", delay: 50, colors: "B" },
    { text: "Rock that body", delay: 30, colors: "B" },
    { text: "Rock that body", delay: 49, colors: "B" },
    { text: "Rock that body", delay: 35, colors: "B" },
    { text: "Bumping in your jeep, got the top dropped down", delay: 80, colors: "A" },
    { text: "Vroom, vroom, through the streets of the town", delay: 80, colors: "A" },
    { text: "Bass so loud, it's shaking the ground", delay: 80, colors: "A" },
    { text: "Everybody knows, we got the sound", delay: 80, colors: "A" },
    { text: "Rock that body", delay: 50, colors: "B" },
    { text: "Rock that body", delay: 30, colors: "B" },
    { text: "Rock that body", delay: 49, colors: "B" },
    { text: "Rock that body", delay: 35, colors: "B" },
    // Add more as needed
];

let currentLine = 0;
let isPlaying = false;
let caretLine = 0;

function createLyricsElements() {
    const container = document.getElementById("lyricsContainer");
    container.innerHTML = "";

    lyrics.forEach((lyric, index) => {
        const line = document.createElement("div");
        line.className = "lyrics-line";
        line.id = `line-${index}`;

        if (lyric.text !== "") {
            const cursor = document.createElement("span");
            cursor.className = "cursor";
            cursor.style.display = "none";
            line.appendChild(cursor);
        } else {
            line.classList.add("no-text");
        }

        container.appendChild(line);
    });
}

function moveCaretToNextLine() {
    const currentCaret = document.querySelector(`#line-${caretLine} .cursor`);
    if (currentCaret) {
        currentCaret.style.display = "none";
    }

    caretLine++;

    while (caretLine < lyrics.length && lyrics[caretLine].text === "") {
        caretLine++;
    }

    if (caretLine < lyrics.length && lyrics[caretLine].text !== "") {
        const newCaret = document.querySelector(`#line-${caretLine} .cursor`);
        if (newCaret) {
            newCaret.style.display = "inline-block";
        }
    }
}

function typeLine(lineIndex) {
    if (lineIndex >= lyrics.length) {
        console.log("Animation complete - all lines finished");
        return;
    }

    const lineElement = document.getElementById(`line-${lineIndex}`);
    const lyric = lyrics[lineIndex];

    if (!lineElement) {
        console.error(`Line element not found for index ${lineIndex}`);
        return;
    }

    if (!lyric || lyric.text === "") {
        console.log(`Waiting for empty line delay at index ${lineIndex}`);
        setTimeout(() => {
            typeLine(lineIndex + 1);
        }, lyric.delay || 200);
        return;
    }

    let charIndex = 0;

    document.querySelectorAll(".lyrics-line.current").forEach((el) => {
        el.classList.remove("current");
    });

    lineElement.classList.add("current");

    const cursor = lineElement.querySelector(".cursor");
    if (cursor) {
        cursor.style.display = "inline-block";
    }

    function typeChar() {
        if (charIndex < lyric.text.length) {
            const textSpan = document.createElement("span");
            textSpan.textContent = lyric.text[charIndex];

            if (lyric.colors && colorSchemes[lyric.colors]) {
                const colors = colorSchemes[lyric.colors];

                let colorCharIndex = 0;
                for (let i = 0; i < charIndex; i++) {
                    if (lyric.text[i] !== " ") {
                        colorCharIndex++;
                    }
                }

                if (lyric.text[charIndex] === " ") {
                    textSpan.style.color = "white";
                } else {
                    const colorIndex = colorCharIndex % colors.length;
                    textSpan.style.color = colors[colorIndex];
                }
            } else {
                textSpan.style.color = "white";
            }

            lineElement.insertBefore(textSpan, cursor);

            charIndex++;
            setTimeout(typeChar, lyric.delay);
        } else {
            moveCaretToNextLine();
            setTimeout(() => {
                typeLine(lineIndex + 1);
            }, 300);
        }
    }

    typeChar();
}

function startAnimation() {
    isPlaying = true;
    currentLine = 0;
    caretLine = 0;
    createLyricsElements();
    console.log("Starting animation with", lyrics.length, "lines");
    typeLine(currentLine);
}

function restartAnimation() {
    console.log("Restarting animation...");
    isPlaying = false;
    currentLine = 0;
    caretLine = 0;
    startAnimation();
}

document.addEventListener("DOMContentLoaded", function () {
    createLyricsElements();
    startAnimation();

    document.addEventListener("click", function () {
        if (!isPlaying) {
            restartAnimation();
        }
    });

    document.addEventListener("keydown", function (e) {
        if (e.code === "Space") {
            e.preventDefault();
            restartAnimation();
        }
    });
});
