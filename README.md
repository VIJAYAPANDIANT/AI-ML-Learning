# 🌌 Cyber-Holographic 3D Portfolio

> [!NOTE]
> **Reference & Demo Model**: This website and repository serve as a reference and demo model of the Cyber-Holographic 3D Portfolio. It is designed to showcase the integration of modern WebGL/3D interfaces, interactive animations, and responsive components in a futuristic cyberpunk aesthetic.

A premium, state-of-the-art interactive developer portfolio featuring a futuristic **Cyberpunk Heads-Up Display (HUD)** design and real-time 3D elements. Built using **React 19**, **Vite**, **TypeScript**, **Tailwind CSS v4**, **Three.js** (`@react-three/fiber`), and **Framer Motion** (`motion/react`).

---

## 🚀 Key Highlights & Interactive Features

- **Interactive 3D WebGL Canvas**:
  - A responsive 3D particle field that scales and pans dynamically as you scroll.
  - A central morphing liquid sphere using `MeshDistortMaterial` with roughness and metalness settings for a premium glassmorphic/liquid metal appearance.
- **Dynamic HUD Overlay**:
  - Futuristic scanlines and scrolling grid-bg overlays.
  - Pulse animations, sci-fi bracket borders, and animated system status feeds (latency tracker, AI module state, system telemetry logs).
- **Glassmorphic UI Elements**:
  - Modern panels using backdrop-blur utility classes and subtle borders (`border-white/10`) to provide high-end visual polish.
- **Interactive Mouse Light**:
  - Real-time mouse coordinate tracking rendering a localized holographic radial spotlight.
- **Micro-Animations & Transitions**:
  - Glitch text animation headings that warp on load.
  - Spring-based entrance animations with temporary skews, creating organic scroll transitions.
  - Hover effects on cards, links, and buttons that expand letter spacing and trigger glowing box-shadow reflections.
- **Audio Feedback**:
  - Low-latency ambient clicks on page interaction utilizing browser audio pipelines.

---

## 🛠️ Tech Stack

This project is built using a modern, performant, and type-safe front-end architecture:

- **Core & Build**: [React 19](https://react.dev/), [Vite 6](https://vitejs.dev/), [TypeScript 5.8](https://www.typescriptlang.org/)
- **3D Render Engine**: [Three.js](https://threejs.org/), [@react-three/fiber](https://r3f.docs.pmnd.rs/) (R3F), [@react-three/drei](https://github.com/pmndrs/drei) (Drei helpers)
- **Styling**: [Tailwind CSS v4](https://tailwindcss.com/) (modern CSS-first engine utilizing `@theme` directives)
- **Animations**: [Motion v12 / Framer Motion](https://motion.dev/)
- **Icons**: [Lucide React](https://lucide.dev/)
- **Text Animation**: [react-simple-typewriter](https://github.com/indrajitbhalerao/react-simple-typewriter)
- **AI Extension Boilerplate**: [@google/genai](https://github.com/google/generative-ai-js) (installed for Gemini API developer integration)

---

## 📂 Project Architecture

```
Portfolio-Model/
├── src/
│   ├── components/
│   │   ├── Navbar.tsx         # Responsive sci-fi top nav with link state highlights
│   │   ├── Hero.tsx           # Title landing, typewriter subtitles, CTA actions
│   │   ├── About.tsx          # Profile details, bio, and fluid glow blob profile card
│   │   ├── Skills.tsx         # Skill matrix with interactive power meters and symbols
│   │   ├── Projects.tsx       # Tech archive categorized by All/AI/Web/Backend
│   │   ├── Experience.tsx     # Timeline log with work history and education logs
│   │   ├── Contact.tsx        # Secure SMTP/VOIP/GEO Comms Channel contact form
│   │   ├── Footer.tsx         # Core attribution and timestamp tracker
│   │   ├── HUD.tsx            # Sci-fi corner brackets, telemetry readouts & grid-bg
│   │   ├── Scene.tsx          # Canvas element hosting the 3D particles & central sphere
│   │   └── LoadingScreen.tsx  # Initial neural interface loading overlay
│   ├── lib/
│   │   └── utils.ts           # Styling combination & tailwind-merge helper
│   ├── App.tsx                # App layout wrapper, scroll listener & sound triggers
│   ├── main.tsx               # App entrypoint
│   └── index.css              # Custom Tailwind v4 theme, keyframes, scrollbars, HUD-grid
├── package.json               # Dependency declarations
├── tsconfig.json              # TypeScript compilation options
└── vite.config.ts             # Vite server and tailwind plugins config
```

---

## ⚙️ Environment Configuration

To set up localized variables, copy `.env.example` into a new `.env` file in the root directory:

```bash
cp .env.example .env
```

Define the variables in your `.env`:
* `GEMINI_API_KEY`: Required if you extend this template with Gemini Generative AI features. Configure this in AI Studio or local secrets.
* `APP_URL`: The URL where the application or API endpoints are hosted.

---

## 🚀 Getting Started

Follow these steps to run the project locally on your machine.

### 1. Install Dependencies

```bash
npm install
```

### 2. Launch Local Dev Server

Run the development server locally:

```bash
npm run dev
```

The application will launch on your local host (usually `http://localhost:3000`).

### 3. Build for Production

Compile and bundle assets for optimized production hosting:

```bash
npm run build
```

This generates production-ready code inside the `/dist` directory.

### 4. Type Checking

Validate TypeScript signatures across files:

```bash
npm run lint
```

---

## 🎨 Theme Details

The design system uses a dark mode setup custom-tailored with the following neon HSL colors (configured in [index.css](file:///c:/Portfolio-Model/Portfolio-Model/src/index.css)):
- **Neon Blue**: `#00f3ff` (Primary highlights, lasers, grids)
- **Neon Purple**: `#bc13fe` (Subtle gradients, background glows)
- **Neon Pink**: `#ff00ff` (Decorative accents)
- **AI Green**: `#00ff41` (Terminal typewriter outputs, code signs)
- **Font Face**: Inter (San-Serif headers), JetBrains Mono (Terminal/Monospace readouts)

---

## 📄 License

This project is licensed under the Apache 2.0 License. See the header of source files for detailed attribution.
