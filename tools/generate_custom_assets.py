import os, html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] if '__file__' in locals() else Path(r'd:\IbrahimElmasry\IbrahimElmasry')
ASSETS = ROOT / 'assets'
ASSETS.mkdir(parents=True, exist_ok=True)

# Common SVG styles and font
FONT_FAMILY = "system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
MONO_FAMILY = "'JetBrains Mono', 'Fira Code', ui-monospace, Menlo, Consolas, monospace"

def generate_hero():
    w, h = 1200, 320
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto" role="img" aria-label="Ibrahim Tarek — Lead Software Engineer and UI Architect">
  <defs>
    <!-- Background Gradients -->
    <radialGradient id="hero-glow" cx="60%" cy="40%" r="65%">
      <stop offset="0%" stop-color="#512BD4" stop-opacity="0.32" />
      <stop offset="45%" stop-color="#0078D4" stop-opacity="0.16" />
      <stop offset="100%" stop-color="#0B0F19" stop-opacity="0" />
    </radialGradient>
    <radialGradient id="cyan-glow" cx="15%" cy="85%" r="45%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.22" />
      <stop offset="100%" stop-color="#0B0F19" stop-opacity="0" />
    </radialGradient>
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0F19" />
      <stop offset="50%" stop-color="#0D1117" />
      <stop offset="100%" stop-color="#070A11" />
    </linearGradient>
    <linearGradient id="title-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="50%" stop-color="#F0F6FC" />
      <stop offset="100%" stop-color="#38BDF8" />
    </linearGradient>
    <linearGradient id="border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.6" />
      <stop offset="30%" stop-color="#512BD4" stop-opacity="0.4" />
      <stop offset="70%" stop-color="#1E293B" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#0284C7" stop-opacity="0.5" />
    </linearGradient>
    <linearGradient id="badge-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#512BD4" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#0078D4" stop-opacity="0.25" />
    </linearGradient>
    <!-- Pattern for modern tech grid -->
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#334155" stroke-width="0.75" stroke-opacity="0.25" />
      <circle cx="40" cy="40" r="1" fill="#38BDF8" fill-opacity="0.2" />
    </pattern>
    <filter id="glow-light" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <!-- Base container with rounded corners and border -->
  <rect width="{w}" height="{h}" rx="14" fill="url(#bg-grad)" />
  <rect width="{w}" height="{h}" rx="14" fill="url(#grid)" />
  <rect width="{w}" height="{h}" rx="14" fill="url(#hero-glow)" />
  <rect width="{w}" height="{h}" rx="14" fill="url(#cyan-glow)" />
  <rect width="{w}" height="{h}" rx="14" fill="none" stroke="url(#border-grad)" stroke-width="1.5" />

  <!-- Geometric decorative vectors on the right -->
  <g transform="translate(940, 160)" opacity="0.85">
    <circle cx="0" cy="0" r="110" fill="none" stroke="#38BDF8" stroke-width="1" stroke-dasharray="8 12" opacity="0.35" />
    <circle cx="0" cy="0" r="85" fill="none" stroke="#512BD4" stroke-width="1.2" opacity="0.45" />
    <circle cx="0" cy="0" r="60" fill="none" stroke="#38BDF8" stroke-width="1" stroke-dasharray="4 8" opacity="0.6" />
    <circle cx="0" cy="0" r="30" fill="none" stroke="#818CF8" stroke-width="1.5" opacity="0.7" />
    
    <circle cx="0" cy="0" r="14" fill="#512BD4" opacity="0.8" />
    <circle cx="0" cy="0" r="7" fill="#38BDF8" />
    
    <circle cx="60" cy="-60" r="4.5" fill="#38BDF8" filter="url(#glow-light)" />
    <line x1="0" y1="0" x2="60" y2="-60" stroke="#38BDF8" stroke-width="1" opacity="0.4" />
    <circle cx="-75" cy="40" r="3.5" fill="#A855F7" />
    <line x1="0" y1="0" x2="-75" y2="40" stroke="#A855F7" stroke-width="0.8" opacity="0.4" />
    <circle cx="45" cy="70" r="3" fill="#0284C7" />
    <line x1="0" y1="0" x2="45" y2="70" stroke="#0284C7" stroke-width="0.8" opacity="0.4" />
  </g>

  <!-- Left Content Area -->
  <g transform="translate(60, 48)">
    <!-- Top Status Badge -->
    <g transform="translate(0, 0)">
      <rect width="365" height="28" rx="14" fill="url(#badge-grad)" stroke="#38BDF8" stroke-opacity="0.4" stroke-width="1" />
      <circle cx="15" cy="14" r="4" fill="#10B981" />
      <circle cx="15" cy="14" r="8" fill="#10B981" opacity="0.25" />
      <text x="30" y="18.5" font-family="{MONO_FAMILY}" font-size="11.5" font-weight="600" fill="#38BDF8" letter-spacing="1.2">LEAD SOFTWARE ENGINEER &amp; UI ARCHITECT</text>
    </g>

    <!-- Main Title -->
    <text x="0" y="88" font-family="{FONT_FAMILY}" font-size="48" font-weight="800" fill="url(#title-grad)" letter-spacing="-0.5">IBRAHIM TAREK</text>

    <!-- Subtitle / Headline -->
    <text x="0" y="124" font-family="{FONT_FAMILY}" font-size="19" font-weight="500" fill="#94A3B8">
      Architecting Scalable Backend Ecosystems &amp; Modern UI
    </text>

    <!-- Philosophy sentence -->
    <text x="0" y="152" font-family="{FONT_FAMILY}" font-size="13.5" font-weight="400" fill="#64748B">
      Specializing in ASP.NET Core, Clean Architecture, High-Throughput Relational Systems &amp; Blazor
    </text>

    <!-- Tech Stack Pill Chips -->
    <g transform="translate(0, 185)">
      <g transform="translate(0, 0)">
        <rect width="78" height="26" rx="6" fill="#1E293B" stroke="#512BD4" stroke-width="1.2" />
        <text x="39" y="17" font-family="{MONO_FAMILY}" font-size="11" font-weight="600" fill="#A855F7" text-anchor="middle">.NET 8</text>
      </g>
      <g transform="translate(88, 0)">
        <rect width="128" height="26" rx="6" fill="#1E293B" stroke="#0078D4" stroke-width="1.2" />
        <text x="64" y="17" font-family="{MONO_FAMILY}" font-size="11" font-weight="600" fill="#38BDF8" text-anchor="middle">ASP.NET Core</text>
      </g>
      <g transform="translate(226, 0)">
        <rect width="115" height="26" rx="6" fill="#1E293B" stroke="#512BD4" stroke-width="1.2" />
        <text x="57" y="17" font-family="{MONO_FAMILY}" font-size="11" font-weight="600" fill="#C084FC" text-anchor="middle">Blazor WASM</text>
      </g>
      <g transform="translate(351, 0)">
        <rect width="154" height="26" rx="6" fill="#1E293B" stroke="#334155" stroke-width="1" />
        <text x="77" y="17" font-family="{MONO_FAMILY}" font-size="11" font-weight="500" fill="#CBD5E1" text-anchor="middle">Clean Architecture</text>
      </g>
      <g transform="translate(515, 0)">
        <rect width="105" height="26" rx="6" fill="#1E293B" stroke="#334155" stroke-width="1" />
        <text x="52" y="17" font-family="{MONO_FAMILY}" font-size="11" font-weight="500" fill="#CBD5E1" text-anchor="middle">SQL Server</text>
      </g>
      <g transform="translate(630, 0)">
        <rect width="80" height="26" rx="6" fill="#1E293B" stroke="#334155" stroke-width="1" />
        <text x="40" y="17" font-family="{MONO_FAMILY}" font-size="11" font-weight="500" fill="#CBD5E1" text-anchor="middle">Docker</text>
      </g>
    </g>
  </g>
</svg>'''
    (ASSETS / 'hero-banner.svg').write_text(svg, encoding='utf-8')
    print("Generated assets/hero-banner.svg")

def generate_section(filename, number, title, subtitle):
    w, h = 900, 68
    esc_title = html.escape(title)
    esc_subtitle = html.escape(subtitle)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto" role="img" aria-label="{esc_title}">
  <defs>
    <linearGradient id="sec-line-{number}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.8" />
      <stop offset="35%" stop-color="#512BD4" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.05" />
    </linearGradient>
  </defs>
  <!-- Accent bar -->
  <rect x="0" y="18" width="4" height="32" rx="2" fill="#38BDF8" />
  <!-- Section Number -->
  <text x="18" y="40" font-family="{MONO_FAMILY}" font-size="16" font-weight="700" fill="#38BDF8" letter-spacing="1">{number}</text>
  <!-- Main Section Title -->
  <text x="58" y="40" font-family="{FONT_FAMILY}" font-size="20" font-weight="700" fill="#F1F5F9" letter-spacing="0.5">{esc_title}</text>
  <!-- Right subtitle / category -->
  <text x="{w - 20}" y="40" font-family="{MONO_FAMILY}" font-size="11.5" font-weight="500" fill="#64748B" text-anchor="end" letter-spacing="1.2">{esc_subtitle}</text>
  <!-- Bottom divider line -->
  <rect x="0" y="{h - 2}" width="{w}" height="1.5" fill="url(#sec-line-{number})" />
</svg>'''
    (ASSETS / filename).write_text(svg, encoding='utf-8')
    print(f"Generated assets/{filename}")

def generate_card(filename, project_name, category, description, stack_chips, icon_type, border_color="#38BDF8", accent_color="#0284C7"):
    w, h = 440, 210
    esc_project = html.escape(project_name)
    esc_cat = html.escape(category)
    
    # Generate SVG icon based on type
    if icon_type == "erp":
        icon_svg = f'''
        <g stroke="{border_color}" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round">
          <ellipse cx="20" cy="11" rx="14" ry="5" />
          <path d="M6 11v8c0 2.76 6.27 5 14 5s14-2.24 14-5v-8" />
          <path d="M6 19v8c0 2.76 6.27 5 14 5s14-2.24 14-5v-8" />
          <circle cx="28" cy="27" r="8" fill="#0B0F19" stroke="{border_color}" stroke-width="1.5" />
          <path d="M28 23v8 M24 27h8" stroke="{border_color}" stroke-width="1.5" />
        </g>'''
    elif icon_type == "law":
        icon_svg = f'''
        <g stroke="{border_color}" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round">
          <path d="M20 6v30 M10 36h20 M6 12h28" />
          <path d="M10 12l-5 11h10z" fill="{border_color}" fill-opacity="0.15" />
          <path d="M30 12l-5 11h10z" fill="{border_color}" fill-opacity="0.15" />
          <circle cx="20" cy="6" r="2.5" fill="{border_color}" />
        </g>'''
    elif icon_type == "knowledge":
        icon_svg = f'''
        <g stroke="{border_color}" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="20" cy="20" r="14" />
          <path d="M20 6c4 4 6 9 6 14s-2 10-6 14 M20 6c-4 4-6 9-6 14s2 10 6 14 M6 20h28" />
          <circle cx="30" cy="11" r="3" fill="#38BDF8" />
          <circle cx="10" cy="29" r="3" fill="#818CF8" />
        </g>'''
    else: # "blazor"
        icon_svg = f'''
        <g stroke="{border_color}" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round">
          <rect x="6" y="8" width="28" height="24" rx="4" />
          <path d="M6 15h28 M12 12h.01 M16 12h.01" />
          <path d="M14 26l6-8 1 3 5-5" stroke="#38BDF8" stroke-width="2" />
        </g>'''

    # Build stack chips SVG
    chips_svg = ""
    cx = 24
    for chip in stack_chips:
        chip_esc = html.escape(chip)
        chip_w = len(chip) * 7.5 + 16
        chips_svg += f'''
        <g transform="translate({cx}, 162)">
          <rect width="{chip_w}" height="24" rx="5" fill="#1E293B" stroke="#334155" stroke-width="0.9" />
          <text x="{chip_w/2}" y="15.5" font-family="{MONO_FAMILY}" font-size="10" font-weight="500" fill="#94A3B8" text-anchor="middle">{chip_esc}</text>
        </g>'''
        cx += chip_w + 8

    desc0_esc = html.escape(description[0])
    desc1_esc = html.escape(description[1])

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto" role="img" aria-label="{esc_project}">
  <defs>
    <linearGradient id="card-grad-{icon_type}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="60%" stop-color="#0B0F19" />
      <stop offset="100%" stop-color="#070A11" />
    </linearGradient>
    <linearGradient id="card-border-{icon_type}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{border_color}" stop-opacity="0.65" />
      <stop offset="40%" stop-color="{border_color}" stop-opacity="0.15" />
      <stop offset="100%" stop-color="#334155" stop-opacity="0.3" />
    </linearGradient>
    <radialGradient id="card-glow-{icon_type}" cx="0%" cy="0%" r="60%">
      <stop offset="0%" stop-color="{accent_color}" stop-opacity="0.16" />
      <stop offset="100%" stop-color="#0B0F19" stop-opacity="0" />
    </radialGradient>
  </defs>

  <!-- Card Background -->
  <rect width="{w}" height="{h}" rx="12" fill="url(#card-grad-{icon_type})" />
  <rect width="{w}" height="{h}" rx="12" fill="url(#card-glow-{icon_type})" />
  <rect width="{w}" height="{h}" rx="12" fill="none" stroke="url(#card-border-{icon_type})" stroke-width="1.2" />

  <!-- Top bar / icon badge -->
  <g transform="translate(24, 22)">
    <rect width="40" height="40" rx="8" fill="#1E293B" stroke="#334155" stroke-width="1" />
    <g transform="translate(0, 0)">
      {icon_svg}
    </g>

    <g transform="translate(52, 2)">
      <rect width="{len(category)*6.8 + 14}" height="20" rx="4" fill="{accent_color}" fill-opacity="0.12" stroke="{accent_color}" stroke-opacity="0.35" stroke-width="1" />
      <text x="{(len(category)*6.8 + 14)/2}" y="13.5" font-family="{MONO_FAMILY}" font-size="9" font-weight="600" fill="{border_color}" text-anchor="middle" letter-spacing="0.8">{esc_cat}</text>
    </g>

    <text x="52" y="36" font-family="{FONT_FAMILY}" font-size="20" font-weight="700" fill="#F8FAFC">{esc_project}</text>
  </g>

  <!-- Description text -->
  <text x="24" y="94" font-family="{FONT_FAMILY}" font-size="12.5" fill="#94A3B8">
    <tspan x="24" dy="0">{desc0_esc}</tspan>
    <tspan x="24" dy="18">{desc1_esc}</tspan>
  </text>

  <!-- Divider -->
  <line x1="24" y1="144" x2="{w - 24}" y2="144" stroke="#1E293B" stroke-width="1" />

  <!-- Stack Chips -->
  {chips_svg}

  <!-- External link icon arrow in top right -->
  <g transform="translate({w - 38}, 22)" stroke="#64748B" stroke-width="1.5" fill="none">
    <path d="M0 10 L10 0 M3 0 H10 V7" />
  </g>
</svg>'''
    (ASSETS / filename).write_text(svg, encoding='utf-8')
    print(f"Generated assets/{filename}")

def generate_buttons():
    buttons = [
        ('button-portfolio.svg', 'Live Portfolio', '#0284C7', '#38BDF8', 'M12 2a10 10 0 100 20 10 10 0 000-20zm0 18a8 8 0 110-16 8 8 0 010 16z M2 12h20 M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z'),
        ('button-linkedin.svg', 'LinkedIn', '#0A66C2', '#38BDF8', 'M19 3a2 2 0 012 2v14a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h14m-.5 15.5v-5.3a3.26 3.26 0 00-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 011.4 1.4v4.93h2.75M6.88 8.56a1.68 1.68 0 001.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 00-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z'),
        ('button-whatsapp.svg', 'Direct WhatsApp', '#059669', '#34D399', 'M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0012.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.23 8.23 0 012.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.45 0-2.87-.38-4.12-1.1l-.3-.17-3.12.82.83-3.04-.19-.31a8.21 8.21 0 01-1.26-4.44c0-4.54 3.7-8.24 8.24-8.24'),
        ('button-facebook.svg', 'Facebook', '#1877F2', '#60A5FA', 'M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z')
    ]
    w, h = 180, 42
    for fname, label, brand_col, text_col, icon_path in buttons:
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{label}">
  <rect width="{w}" height="{h}" rx="8" fill="#0F172A" stroke="#334155" stroke-width="1.2" />
  <rect width="{w}" height="{h}" rx="8" fill="{brand_col}" fill-opacity="0.08" />
  <g transform="translate(14, 12)" fill="{text_col}" stroke="none">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="{text_col}">
      <path d="{icon_path}" />
    </svg>
  </g>
  <text x="44" y="26" font-family="{FONT_FAMILY}" font-size="13" font-weight="600" fill="#F1F5F9">{label}</text>
</svg>'''
        (ASSETS / fname).write_text(svg, encoding='utf-8')
        print(f"Generated assets/{fname}")

if __name__ == '__main__':
    generate_hero()
    generate_section('section-enterprise.svg', '01', 'ENTERPRISE & DISTRIBUTED SYSTEMS', 'CORE ARCHITECTURE')
    generate_section('section-interfaces.svg', '02', 'CLIENT EXPERIENCES & WEB INTERFACES', 'UI & FULL STACK')
    generate_buttons()
    
    generate_card(
        'card-deverp.svg',
        'DevERP',
        'ENTERPRISE ERP & WORKFLOWS',
        ['Modular Enterprise Resource Planning system engineered for', 'internal operations, inventory, and business process automation.'],
        ['C#', '.NET 8', 'Clean Architecture', 'SQL Server'],
        'erp',
        border_color='#38BDF8',
        accent_color='#0284C7'
    )

    generate_card(
        'card-elwakeel.svg',
        'Elwakeel-LawFirm',
        'LEGAL PRACTICE MANAGEMENT',
        ['Corporate legal practice suite with granular role-based access,', 'court session scheduling, and secure document archiving.'],
        ['ASP.NET Core', 'Web API', 'SQL Server', 'RBAC'],
        'law',
        border_color='#818CF8',
        accent_color='#6366F1'
    )

    generate_card(
        'card-rawafid.svg',
        'rawafid',
        'KNOWLEDGE & PUBLISHING PLATFORM',
        ['Multilingual community publishing & distribution network', 'designed for high-volume cross-border content and events.'],
        ['Modular Backend', 'REST APIs', 'MySQL', 'CMS'],
        'knowledge',
        border_color='#34D399',
        accent_color='#059669'
    )

    generate_card(
        'card-portfolio.svg',
        'IbrahimElmasry.github.io',
        'BLAZOR WEBASSEMBLY PORTFOLIO',
        ['Interactive personal portfolio engine built purely in client-side', 'Blazor WebAssembly with C# component-driven architecture.'],
        ['Blazor WASM', '.NET 8', 'C#', 'Tailwind CSS'],
        'blazor',
        border_color='#F43F5E',
        accent_color='#E11D48'
    )
