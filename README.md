# Manim Slides workspace

Local environment for [manim-slides](https://eertmans.be/manim-slides/) presentations with [Manim Community](https://www.manim.community/).

## Prerequisites

- **Python 3.14** (venv in `.venv`)
- **ffmpeg** (already on your PATH)

## Activate the environment

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Workflow

### 1. Write a scene

Subclass `Slide` from `manim_slides` and call `self.next_slide()` where you want a pause (see `slides/hello_slides.py`).

### 2. Render

```powershell
manim-slides render slides/hello_slides.py HelloSlides -ql
```

Use `-qh` for high quality when exporting final videos.

### 3. Present

```powershell
manim-slides HelloSlides
```

Keyboard (defaults): **→** next slide, **←** previous, **Space** play/pause loop, **Esc** quit. Run `manim-slides wizard` to remap keys.

### 4. Export HTML (optional)

```powershell
manim-slides convert HelloSlides slides.html --open
```

## Project layout

```
slides/           # Your slide scenes (.py)
.slides/          # Generated slide data (gitignored)
media/            # Manim render output (gitignored)
.venv/            # Python virtual environment
```

## Reinstall dependencies

```powershell
python -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
```

## Docs

- [manim-slides documentation](https://eertmans.be/manim-slides/latest/)
- [Manim Community docs](https://docs.manim.community/)
