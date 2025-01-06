<!-- README.md -->

# Python Snake Game

Dies ist die Musterlösung für ein einfaches, gut strukturiertes Snake-Spiel in Python als Docker-Applikation.

## Features
- **Professionelle Struktur:** Projekt-Struktur gemäss den erlernten Konztepten.
- **Anpassbarkeit des Spiels:** Screengrösse, Zellengrösse und Geschwindigkeit können einfach angepasst werden.
- **Skalierbarkeit:** Konstanten sind in `utils.py`; `main.py` führt das Spiel aus.

## Installation
1. **Clone** das Repository auf Deinen lokalen Rechner
2. **Installiere** Docker, falls notwendig
3. **Build** das Docker Image mit `docker build -t snake-game .` 


## Ausführung
**Starte** den Docker Container mit `docker run -it snake-game`

Benutze die Pfeile auf der Tastatur, um die Schlange zu bewegen, vermeide Kollisionen und esse Nahrung.

## Projektstruktur
```bash
.
├── README.md
├── LICENSE
├── requirements.txt
├── main.py
└── snake_game/
    ├── utils.py
    └── game.py
