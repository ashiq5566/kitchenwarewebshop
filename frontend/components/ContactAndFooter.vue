<template>
  <div>
    <!-- CONTACT / CTA -->
    <section id="contact" class="contact-section" ref="sectionRef">
      <div class="container">
        <div class="contact-card" :class="{ visible: inView }">
          <div class="contact-left">
            <span class="section-tag">Get in Touch</span>
            <h2 class="contact-title">Let's find the<br /><em>perfect</em> kitchenware<br />for your home</h2>
            <p class="contact-sub">Message us on WhatsApp and we'll help you pick the right products, answer any questions, and process your order — all in one simple chat.</p>
            <div class="contact-info-row">
              <div class="contact-info-item" v-for="c in contactInfo" :key="c.label">
                <span class="ci-icon">{{ c.icon }}</span>
                <div>
                  <div class="ci-label">{{ c.label }}</div>
                  <a :href="c.href" class="ci-value" target="_blank">{{ c.value }}</a>
                </div>
              </div>
            </div>
          </div>
          <div class="contact-right">
            <div class="wa-card">
              <div class="wa-header">
                <div class="wa-avatar">SN</div>
                <div>
                  <div class="wa-name">SteelNest</div>
                  <div class="wa-status">
                    <span class="online-dot"></span> Usually replies in minutes
                  </div>
                </div>
              </div>
              <div class="wa-messages">
                <div class="wa-msg received">
                  <p>👋 Hi! Welcome to SteelNest.</p>
                  <span class="msg-time">09:00</span>
                </div>
                <div class="wa-msg received">
                  <p>How can we help you today? Feel free to ask about any product or share your requirements!</p>
                  <span class="msg-time">09:00</span>
                </div>
                <div class="wa-msg sent">
                  <p>I need a 5L pressure cooker and a tiffin set. Do you deliver to Thrissur?</p>
                  <span class="msg-time">09:02</span>
                </div>
                <div class="wa-msg received">
                  <p>Absolutely! We deliver all across Kerala 🚀 Let me share our best options with pricing...</p>
                  <span class="msg-time">09:03</span>
                </div>
              </div>
              <a :href="waLink" target="_blank" class="wa-send-btn">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                Start Chatting on WhatsApp
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FOOTER -->
    <footer class="footer">
      <div class="container">
        <div class="footer-top">
          <div class="footer-brand">
            <div class="brand-row">
              <span class="brand-hex">⬡</span>
              <span class="brand-txt">SteelNest</span>
            </div>
            <p>Premium steel kitchenware for<br />the modern Indian kitchen.</p>
            <div class="social-links">
              <a href="#" class="social-btn">📘</a>
              <a href="#" class="social-btn">📸</a>
              <a :href="waLink" target="_blank" class="social-btn">💬</a>
            </div>
          </div>
          <div class="footer-col">
            <h4>Products</h4>
            <ul>
              <li><a href="#">Cookware Sets</a></li>
              <li><a href="#">Pressure Cookers</a></li>
              <li><a href="#">Tiffin Boxes</a></li>
              <li><a href="#">Serving Bowls</a></li>
              <li><a href="#">Water Bottles</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Company</h4>
            <ul>
              <li><a href="#">About Us</a></li>
              <li><a href="#">Our Products</a></li>
              <li><a href="#">Reviews</a></li>
              <li><a href="#">Contact</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Policies</h4>
            <ul>
              <li><a href="#">Shipping Policy</a></li>
              <li><a href="#">Return Policy</a></li>
              <li><a href="#">Privacy Policy</a></li>
              <li><a href="#">Terms of Service</a></li>
            </ul>
          </div>
        </div>
        <div class="footer-bottom">
          <p>© 2025 SteelNest. All rights reserved. Made with ♥ in Kerala.</p>
          <p class="footer-wa">
            <a :href="waLink" target="_blank">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
              +91 99999 99999
            </a>
          </p>
        </div>
      </div>
    </footer>

    <!-- Floating WhatsApp Button -->
    <a :href="waLink" target="_blank" class="float-wa">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
      <span class="float-wa-label">Order Now</span>
    </a>
  </div>
</template>

<script setup>
const sectionRef = ref(null)
const inView = ref(false)
const waLink = 'https://wa.me/919999999999?text=Hi%2C%20I%20want%20to%20order!'

const contactInfo = [
  { icon: '💬', label: 'WhatsApp', value: '+91 99999 99999', href: 'https://wa.me/919999999999' },
  { icon: '📧', label: 'Email', value: 'hello@steelnest.in', href: 'mailto:hello@steelnest.in' },
  { icon: '📍', label: 'Location', value: 'Kerala, India', href: '#' },
]

onMounted(() => {
  const o = new IntersectionObserver(([e]) => { if (e.isIntersecting) inView.value = true }, { threshold: 0.1 })
  if (sectionRef.value) o.observe(sectionRef.value)
})
</script>

<style scoped>
/* CONTACT */
.contact-section {
  padding: 100px 0;
  background: var(--cream);
}
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 32px;
}
.contact-card {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
  align-items: center;
  opacity: 0;
  transform: translateY(30px);
  transition: all 0.7s ease;
}
.contact-card.visible { opacity: 1; transform: none; }
.section-tag {
  display: inline-block;
  font-size: 12px;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--warm-dark);
  font-weight: 600;
  margin-bottom: 12px;
}
.contact-title {
  font-family: var(--font-display);
  font-size: clamp(36px, 4vw, 52px);
  font-weight: 300;
  color: var(--charcoal);
  line-height: 1.2;
  margin-bottom: 20px;
}
.contact-title em { font-style: italic; color: var(--warm-dark); }
.contact-sub {
  font-size: 15px;
  color: var(--steel-dark);
  line-height: 1.8;
  margin-bottom: 36px;
}
.contact-info-row { display: flex; flex-direction: column; gap: 20px; }
.contact-info-item {
  display: flex;
  align-items: center;
  gap: 14px;
}
.ci-icon {
  width: 44px; height: 44px;
  background: rgba(201,169,110,0.1);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  flex-shrink: 0;
}
.ci-label {
  font-size: 11px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--steel);
  margin-bottom: 2px;
}
.ci-value {
  font-size: 15px;
  font-weight: 500;
  color: var(--charcoal);
  text-decoration: none;
}
.ci-value:hover { color: var(--warm-dark); }

/* WhatsApp mockup */
.wa-card {
  background: #ECE5DD;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(28,33,40,0.12);
}
.wa-header {
  background: #075E54;
  padding: 16px 20px;
  display: flex;
  align-items: center;
  gap: 12px;
}
.wa-avatar {
  width: 42px; height: 42px;
  background: #25D366;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 700;
  color: white;
}
.wa-name { font-size: 15px; font-weight: 600; color: white; }
.wa-status { display: flex; align-items: center; gap: 6px; font-size: 12px; color: rgba(255,255,255,0.7); }
.online-dot {
  width: 7px; height: 7px;
  border-radius: 50%;
  background: #25D366;
  animation: pulse-glow 2s infinite;
}
.wa-messages {
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  min-height: 220px;
}
.wa-msg {
  max-width: 80%;
  padding: 10px 14px;
  border-radius: 12px;
  position: relative;
}
.wa-msg.received {
  background: white;
  align-self: flex-start;
  border-radius: 0 12px 12px 12px;
}
.wa-msg.sent {
  background: #DCF8C6;
  align-self: flex-end;
  border-radius: 12px 0 12px 12px;
}
.wa-msg p { font-size: 13px; color: #111; line-height: 1.5; margin: 0; }
.msg-time {
  font-size: 10px;
  color: rgba(0,0,0,0.4);
  display: block;
  text-align: right;
  margin-top: 4px;
}
.wa-send-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  width: 100%;
  padding: 16px;
  background: #25D366;
  color: white;
  text-decoration: none;
  font-size: 14px;
  font-weight: 700;
  transition: background 0.3s;
}
.wa-send-btn:hover { background: #128C7E; }

/* FOOTER */
.footer {
  background: #0F1419;
  padding: 80px 0 32px;
}
.footer-top {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 60px;
  margin-bottom: 56px;
}
.footer-brand p {
  font-size: 14px;
  color: rgba(255,255,255,0.4);
  line-height: 1.8;
  margin-bottom: 20px;
}
.brand-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 14px;
}
.brand-hex { font-size: 22px; color: var(--warm); }
.brand-txt {
  font-family: var(--font-display);
  font-size: 22px;
  color: white;
  font-weight: 600;
}
.social-links { display: flex; gap: 10px; }
.social-btn {
  width: 38px; height: 38px;
  background: rgba(255,255,255,0.06);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  text-decoration: none;
  transition: background 0.2s;
}
.social-btn:hover { background: rgba(255,255,255,0.12); }
.footer-col h4 {
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.5);
  font-weight: 600;
  margin-bottom: 16px;
}
.footer-col ul { list-style: none; display: flex; flex-direction: column; gap: 10px; }
.footer-col a {
  font-size: 14px;
  color: rgba(255,255,255,0.35);
  text-decoration: none;
  transition: color 0.2s;
}
.footer-col a:hover { color: rgba(255,255,255,0.8); }
.footer-bottom {
  border-top: 1px solid rgba(255,255,255,0.06);
  padding-top: 28px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}
.footer-bottom p { font-size: 13px; color: rgba(255,255,255,0.3); }
.footer-wa a {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #25D366;
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
}

/* Floating WA Button */
.float-wa {
  position: fixed;
  bottom: 28px; right: 28px;
  background: #25D366;
  color: white;
  text-decoration: none;
  border-radius: 50px;
  padding: 14px 20px 14px 16px;
  display: flex;
  align-items: center;
  gap: 10px;
  box-shadow: 0 8px 30px rgba(37,211,102,0.4);
  animation: pulse-glow 2.5s infinite;
  z-index: 999;
  transition: all 0.3s;
}
.float-wa:hover {
  background: #128C7E;
  transform: translateY(-3px);
}
.float-wa-label {
  font-size: 13px;
  font-weight: 700;
}

@media (max-width: 900px) {
  .contact-card { grid-template-columns: 1fr; gap: 40px; }
  .footer-top { grid-template-columns: 1fr 1fr; }
  .footer-bottom { flex-direction: column; text-align: center; }
}
@media (max-width: 480px) {
  .footer-top { grid-template-columns: 1fr; }
  .float-wa-label { display: none; }
  .float-wa { border-radius: 50%; padding: 14px; }
}
</style>
