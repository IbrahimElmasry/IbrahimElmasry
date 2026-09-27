# Ibrahim Tarek asset maintenance

The profile is ordinary GitHub Markdown with self-contained SVG images. No JavaScript, external fonts, statistics endpoints or scheduled jobs are required.

## Edit

- Edit profile copy, project destinations and credentials in `README.md`.
- Edit labels, colors and animation in `tools/build_cinema.py`.
- Run `python tools/build_cinema.py` to regenerate all 20 SVG assets. Dependencies: Pillow and fonttools. The default font is DejaVu Sans (`tools/DejaVuSans.ttf`); set `CINEMA_FONT` to a TrueType font path on other systems if needed.
- Keep the seven `-mobile.svg` variants paired with their desktop assets. The README selects them at viewport widths of 640px or less.

The PNGs in `assets/cinema/source/` are the original key art production inputs. The SVGs embed optimized JPEG copies, so visitors do not need to download the full-resolution PNGs. Project posters are symbolic key art representing Ibrahim Tarek's enterprise and full-stack projects: DevERP, Elwakeel-LawFirm, rawafid, and Blazor Portfolio.

## Motion

The hero has a one-time light-ribbon TAREKFLIX ident, followed by looping energy traces and particles. DevERP (`dafesteel.svg`) has an inspection sweep. Elwakeel-LawFirm (`neuroscope.svg`) has network pulses. rawafid (`signal.svg`) has flowing paths. Blazor Portfolio (`nebula.svg`) has a floating wireframe world; rawafid Portal (`jobpulse.svg`) has a moving chart highlight. All animations are decorative and respect `prefers-reduced-motion`. The essential content is visible when CSS animation is unavailable or disabled.

## Content provenance

Roles follow Ibrahim Tarek's current instruction: Lead Software Engineer / ASP.NET & Full Stack Developer / UI Architect. Project facts and technologies come from Ibrahim's public projects and repositories: DevERP, Elwakeel-LawFirm, rawafid, and Blazor Portfolio. There are no invented skill percentages or artificial ratings.
