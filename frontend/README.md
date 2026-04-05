# SteelNest — WhatsApp-First Kitchenware Store

A production-ready static Nuxt 3 + Nuxt UI website for a steel kitchenware shop with WhatsApp-based ordering.

## Features

- 🎨 **Premium steel/warm gold aesthetic** with Cormorant Garamond + DM Sans fonts
- ⚡ **Smooth scroll-triggered animations** using IntersectionObserver throughout
- 📱 **Fully responsive** — mobile-first, tablet, and desktop
- 💬 **WhatsApp-first ordering** — buttons throughout that deep-link to WhatsApp chat with pre-filled messages
- 🛍️ **Product catalog** with category filters and quick-order hover actions
- ⭐ **Social proof** — 6 customer reviews + trust bar
- 🧭 **Sticky navbar** with blur effect on scroll + mobile hamburger menu
- 🔄 **Animated floating WA button** always visible for quick access
- 🌐 **Fully static** — generates to plain HTML/CSS/JS via `nuxt generate`

## Setup

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production (SSR)
npm run build

# Generate static site (recommended for deployment)
npm run generate
```

## Configuration — Update before launch

### 1. WhatsApp Number
Replace `919999999999` with your actual WhatsApp number (with country code, no + or spaces):
- Files to update: `Navbar.vue`, `HeroSection.vue`, `ProductsSection.vue`, `WhyAndHowSection.vue`, `ContactAndFooter.vue`
- Search and replace: `919999999999` → your number (e.g., `919876543210`)

### 2. Business Info
In `ContactAndFooter.vue`, update:
- Email: `hello@steelnest.in`
- Location: `Kerala, India`
- Social media links

### 3. Business Name & Meta
In `nuxt.config.ts`, update the `title` and `description` meta tags.

### 4. Products
In `ProductsSection.vue`, update the `products` array with your real:
- Product names, descriptions, categories
- Prices
- Ratings
- WhatsApp order messages

## Deployment

### Netlify (Recommended — Free)
1. Push to GitHub
2. Connect repo to Netlify
3. Build command: `npm run generate`
4. Publish directory: `.output/public`

### Vercel
1. Push to GitHub
2. Import to Vercel
3. Framework: Nuxt.js
4. It will auto-detect settings

### cPanel / Traditional Hosting
1. Run `npm run generate` locally
2. Upload contents of `.output/public/` to your web root

## Color Customization

All colors are CSS variables in `assets/css/main.css`:
```css
--warm: #C9A96E;        /* Gold accent */
--steel: #8B9DAF;       /* Steel blue-grey */
--cream: #FAF7F2;       /* Background */
--charcoal: #1C2128;    /* Dark text/sections */
```

## Tech Stack
- **Nuxt 3** — Vue-based full-stack framework
- **Nuxt UI** — Component library
- **Pure CSS animations** — No extra animation libraries
- **IntersectionObserver** — Scroll-triggered reveals
- **Google Fonts** — Cormorant Garamond + DM Sans
