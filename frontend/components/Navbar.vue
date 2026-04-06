<template>
  <nav class="navbar" :class="{ scrolled: isScrolled }">
    <div class="nav-inner">
      <a href="#" class="brand">
        <span class="brand-icon">⬡</span>
        <span class="brand-name">KC Home Bazar</span>
      </a>
      <ul class="nav-links">
        <li><a href="#products" @click.prevent="scrollTo('#products')">Products</a></li>
        <li><a href="#why-us" @click.prevent="scrollTo('#why-us')">Why Us</a></li>
        <li><a href="#testimonials" @click.prevent="scrollTo('#testimonials')">Reviews</a></li>
        <li><a href="#contact" @click.prevent="scrollTo('#contact')">Contact</a></li>
      </ul>
      <a :href="whatsappLink" target="_blank" class="nav-cta">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
        Order Now
      </a>

      <!-- Mobile menu button -->
      <button class="mobile-toggle" @click="mobileOpen = !mobileOpen" :class="{ open: mobileOpen }">
        <span></span><span></span><span></span>
      </button>
    </div>

    <!-- Mobile Menu -->
    <div class="mobile-menu" :class="{ open: mobileOpen }">
      <a href="#products" @click="scrollTo('#products'); mobileOpen=false">Products</a>
      <a href="#why-us" @click="scrollTo('#why-us'); mobileOpen=false">Why Us</a>
      <a href="#testimonials" @click="scrollTo('#testimonials'); mobileOpen=false">Reviews</a>
      <a href="#contact" @click="scrollTo('#contact'); mobileOpen=false">Contact</a>
      <a :href="whatsappLink" target="_blank" class="mobile-cta">Order on WhatsApp</a>
    </div>
  </nav>
</template>

<script setup>
const isScrolled = ref(false)
const mobileOpen = ref(false)
const whatsappLink = 'https://wa.me/919999999999?text=Hi%2C%20I%20would%20like%20to%20order%20kitchenware!'

const scrollTo = (selector) => {
  document.querySelector(selector)?.scrollIntoView({ behavior: 'smooth' })
}

onMounted(() => {
  window.addEventListener('scroll', () => {
    isScrolled.value = window.scrollY > 30
  })
})
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 1000;
  padding: 20px 0;
  transition: all 0.4s ease;
}
.navbar.scrolled {
  background: rgba(250, 247, 242, 0.95);
  backdrop-filter: blur(20px);
  padding: 12px 0;
  box-shadow: 0 1px 40px rgba(28,33,40,0.08);
}
.nav-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 32px;
  display: flex;
  align-items: center;
  gap: 40px;
}
.brand {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  flex-shrink: 0;
}
.brand-icon {
  font-size: 22px;
  color: var(--warm);
  line-height: 1;
}
.brand-name {
  font-family: var(--font-display);
  font-size: 24px;
  font-weight: 600;
  color: var(--charcoal);
  letter-spacing: 0.02em;
}
.nav-links {
  display: flex;
  list-style: none;
  gap: 36px;
  margin-left: auto;
}
.nav-links a {
  text-decoration: none;
  color: var(--charcoal-soft);
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  transition: color 0.2s;
  position: relative;
}
.nav-links a::after {
  content: '';
  position: absolute;
  bottom: -4px; left: 0;
  width: 0; height: 1px;
  background: var(--warm);
  transition: width 0.3s;
}
.nav-links a:hover { color: var(--warm-dark); }
.nav-links a:hover::after { width: 100%; }

.nav-cta {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  background: #25D366;
  color: white;
  text-decoration: none;
  border-radius: 50px;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.02em;
  transition: all 0.3s;
  flex-shrink: 0;
  animation: pulse-glow 2.5s infinite;
}
.nav-cta:hover {
  background: #128C7E;
  transform: translateY(-2px);
}

.mobile-toggle {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
  margin-left: auto;
}
.mobile-toggle span {
  display: block;
  width: 24px;
  height: 2px;
  background: var(--charcoal);
  transition: all 0.3s;
  transform-origin: center;
}
.mobile-toggle.open span:nth-child(1) { transform: rotate(45deg) translate(5px, 5px); }
.mobile-toggle.open span:nth-child(2) { opacity: 0; }
.mobile-toggle.open span:nth-child(3) { transform: rotate(-45deg) translate(5px, -5px); }

.mobile-menu {
  display: none;
  flex-direction: column;
  background: var(--cream);
  padding: 20px 32px;
  gap: 16px;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s ease;
}
.mobile-menu.open { max-height: 400px; }
.mobile-menu a {
  text-decoration: none;
  color: var(--charcoal-soft);
  font-size: 16px;
  font-weight: 500;
  padding: 8px 0;
  border-bottom: 1px solid rgba(139,157,175,0.15);
}
.mobile-cta {
  background: #25D366 !important;
  color: white !important;
  text-align: center;
  padding: 14px !important;
  border-radius: 8px;
  border: none !important;
  margin-top: 8px;
}

@media (max-width: 768px) {
  .nav-links, .nav-cta { display: none; }
  .mobile-toggle, .mobile-menu { display: flex; }
}
</style>
