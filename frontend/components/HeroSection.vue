<template>
  <section class="hero">
    <div class="hero-bg">
      <div class="grid-lines"></div>
      <div class="orb orb-1"></div>
      <div class="orb orb-2"></div>
    </div>

    <div class="hero-inner">
      <div class="hero-content">
        <div class="badge animate-fade-up opacity-0">
          <span class="badge-dot"></span>
          Free delivery on orders above ₹999
        </div>
        <h1 class="hero-title animate-fade-up opacity-0 delay-100">
          Kitchen essentials<br />
          <em>built to last</em><br />
          <span class="title-steel">generations</span>
        </h1>
        <p class="hero-sub animate-fade-up opacity-0 delay-200">
          Premium stainless steel kitchenware for the modern Indian kitchen.
          Built with precision. Ordered in seconds via WhatsApp.
        </p>
        <div class="hero-actions animate-fade-up opacity-0 delay-300">
          <a :href="waLink" target="_blank" class="btn-whatsapp">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            Order via WhatsApp
          </a>
          <a href="#products" @click.prevent="scrollTo('#products')" class="btn-outline">
            Explore Products
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>
        </div>

        <div class="hero-stats animate-fade-up opacity-0 delay-400">
          <div class="stat" v-for="s in stats" :key="s.label">
            <span class="stat-num">{{ s.num }}</span>
            <span class="stat-label">{{ s.label }}</span>
          </div>
        </div>
      </div>

      <div class="hero-visual animate-slide-left opacity-0 delay-200">
        <div class="visual-ring ring-3"></div>
        <div class="visual-ring ring-2"></div>
        <div class="visual-ring ring-1"></div>
        <div class="visual-center">
          <div class="steel-icon">
            <svg viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
              <!-- Pot body -->
              <ellipse cx="60" cy="85" rx="42" ry="12" fill="url(#grad1)" opacity="0.3"/>
              <path d="M20 45 Q20 88 60 88 Q100 88 100 45 Z" fill="url(#grad1)"/>
              <rect x="18" y="38" width="84" height="12" rx="6" fill="url(#grad2)"/>
              <!-- Lid -->
              <path d="M22 38 Q22 22 60 22 Q98 22 98 38 Z" fill="url(#grad3)"/>
              <ellipse cx="60" cy="22" rx="38" ry="5" fill="url(#grad2)"/>
              <!-- Knob -->
              <rect x="54" y="10" width="12" height="14" rx="6" fill="url(#grad2)"/>
              <!-- Handles -->
              <rect x="6" y="48" width="16" height="8" rx="4" fill="url(#grad2)"/>
              <rect x="98" y="48" width="16" height="8" rx="4" fill="url(#grad2)"/>
              <!-- Shine -->
              <ellipse cx="42" cy="55" rx="6" ry="16" fill="white" opacity="0.15" transform="rotate(-15 42 55)"/>
              <defs>
                <linearGradient id="grad1" x1="20" y1="38" x2="100" y2="88" gradientUnits="userSpaceOnUse">
                  <stop offset="0%" stop-color="#C5CDD6"/>
                  <stop offset="50%" stop-color="#8B9DAF"/>
                  <stop offset="100%" stop-color="#4A5568"/>
                </linearGradient>
                <linearGradient id="grad2" x1="0" y1="0" x2="1" y2="1" gradientUnits="objectBoundingBox">
                  <stop offset="0%" stop-color="#D6DDE4"/>
                  <stop offset="100%" stop-color="#8B9DAF"/>
                </linearGradient>
                <linearGradient id="grad3" x1="22" y1="22" x2="98" y2="38" gradientUnits="userSpaceOnUse">
                  <stop offset="0%" stop-color="#B0BECA"/>
                  <stop offset="100%" stop-color="#6B7F8F"/>
                </linearGradient>
              </defs>
            </svg>
          </div>
          <div class="float-tag tag-1">
            <span>🇮🇳</span> Made in India
          </div>
          <div class="float-tag tag-2">
            <span>✦</span> ISI Certified
          </div>
          <div class="float-tag tag-3">
            <span>♻</span> Rust-free steel
          </div>
        </div>
      </div>
    </div>

    <!-- Scroll indicator -->
    <div class="scroll-hint animate-fade-in opacity-0 delay-700">
      <span>Scroll to explore</span>
      <div class="scroll-line"></div>
    </div>
  </section>
</template>

<script setup>
const waLink = 'https://wa.me/919999999999?text=Hi%2C%20I%20want%20to%20order%20kitchenware!'

const stats = [
  { num: '500+', label: 'Products' },
  { num: '8K+', label: 'Happy Customers' },
  { num: '5★', label: 'Avg Rating' },
]

const scrollTo = (sel) => document.querySelector(sel)?.scrollIntoView({ behavior: 'smooth' })
</script>

<style scoped>
.hero {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 120px 0 60px;
  position: relative;
  overflow: hidden;
}
.hero-bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
}
.grid-lines {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(139,157,175,0.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(139,157,175,0.06) 1px, transparent 1px);
  background-size: 60px 60px;
}
.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
}
.orb-1 {
  width: 500px; height: 500px;
  background: radial-gradient(circle, rgba(201,169,110,0.12), transparent 70%);
  top: -100px; right: -100px;
}
.orb-2 {
  width: 400px; height: 400px;
  background: radial-gradient(circle, rgba(139,157,175,0.12), transparent 70%);
  bottom: -80px; left: -80px;
}

.hero-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 32px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
  align-items: center;
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: rgba(201,169,110,0.1);
  border: 1px solid rgba(201,169,110,0.3);
  border-radius: 50px;
  font-size: 13px;
  color: var(--warm-dark);
  font-weight: 500;
  margin-bottom: 24px;
}
.badge-dot {
  width: 7px; height: 7px;
  border-radius: 50%;
  background: var(--warm);
  animation: pulse-glow 2s infinite;
}

.hero-title {
  font-family: var(--font-display);
  font-size: clamp(48px, 6vw, 76px);
  font-weight: 300;
  line-height: 1.1;
  color: var(--charcoal);
  margin-bottom: 24px;
}
.hero-title em {
  font-style: italic;
  color: var(--warm-dark);
}
.title-steel {
  background: linear-gradient(135deg, var(--steel-dark) 0%, var(--steel) 50%, var(--steel-light) 100%);
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: shimmer 3s linear infinite;
}

.hero-sub {
  font-size: 17px;
  line-height: 1.7;
  color: var(--steel-dark);
  margin-bottom: 36px;
  max-width: 440px;
}

.hero-actions {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  margin-bottom: 52px;
}

.btn-whatsapp {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 15px 28px;
  background: #25D366;
  color: white;
  text-decoration: none;
  border-radius: 50px;
  font-size: 15px;
  font-weight: 600;
  transition: all 0.3s;
  box-shadow: 0 8px 32px rgba(37,211,102,0.3);
}
.btn-whatsapp:hover {
  background: #128C7E;
  transform: translateY(-3px);
  box-shadow: 0 12px 40px rgba(37,211,102,0.4);
}

.btn-outline {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 15px 28px;
  border: 1.5px solid var(--steel);
  color: var(--charcoal);
  text-decoration: none;
  border-radius: 50px;
  font-size: 15px;
  font-weight: 500;
  transition: all 0.3s;
}
.btn-outline:hover {
  border-color: var(--charcoal);
  background: var(--charcoal);
  color: var(--cream);
  transform: translateY(-3px);
}

.hero-stats {
  display: flex;
  gap: 40px;
}
.stat { display: flex; flex-direction: column; gap: 4px; }
.stat-num {
  font-family: var(--font-display);
  font-size: 28px;
  font-weight: 600;
  color: var(--charcoal);
}
.stat-label {
  font-size: 12px;
  color: var(--steel-dark);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

/* Visual */
.hero-visual {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 480px;
}
.visual-ring {
  position: absolute;
  border-radius: 50%;
  border: 1px solid;
  animation: rotateSlow linear infinite;
}
.ring-1 {
  width: 320px; height: 320px;
  border-color: rgba(201,169,110,0.2);
  animation-duration: 20s;
}
.ring-2 {
  width: 400px; height: 400px;
  border-color: rgba(139,157,175,0.15);
  animation-duration: 30s;
  animation-direction: reverse;
}
.ring-3 {
  width: 460px; height: 460px;
  border-color: rgba(139,157,175,0.08);
  animation-duration: 50s;
}
.visual-center {
  position: relative;
  z-index: 2;
}
.steel-icon {
  width: 220px; height: 220px;
  animation: float 4s ease-in-out infinite;
  filter: drop-shadow(0 20px 40px rgba(74,85,104,0.25));
}
.steel-icon svg { width: 100%; height: 100%; }

.float-tag {
  position: absolute;
  background: white;
  border: 1px solid rgba(139,157,175,0.2);
  border-radius: 50px;
  padding: 8px 14px;
  font-size: 12px;
  font-weight: 600;
  color: var(--charcoal-soft);
  display: flex;
  align-items: center;
  gap: 6px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
  white-space: nowrap;
}
.tag-1 { top: 20px; left: -30px; animation: float 3s ease-in-out infinite; }
.tag-2 { top: 60px; right: -20px; animation: float 3.5s ease-in-out infinite 0.5s; }
.tag-3 { bottom: 40px; left: -10px; animation: float 4s ease-in-out infinite 1s; }

.scroll-hint {
  position: absolute;
  bottom: 32px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--steel);
}
.scroll-line {
  width: 1px; height: 48px;
  background: linear-gradient(to bottom, var(--steel), transparent);
  animation: float 2s ease-in-out infinite;
}

@media (max-width: 900px) {
  .hero-inner { grid-template-columns: 1fr; gap: 40px; }
  .hero-visual { height: 300px; }
  .ring-1 { width: 220px; height: 220px; }
  .ring-2 { width: 280px; height: 280px; }
  .ring-3 { width: 320px; height: 320px; }
  .steel-icon { width: 160px; height: 160px; }
}
@media (max-width: 480px) {
  .hero-title { font-size: 42px; }
  .hero-visual { display: none; }
}
</style>
