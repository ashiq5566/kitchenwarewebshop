<template>
  <div>
    <!-- WHY US -->
    <section id="why-us" class="why-section" ref="whyRef">
      <div class="container">
        <div class="why-grid">
          <div class="why-left" :class="{ visible: inView }">
            <span class="section-tag">Why SteelNest</span>
            <h2 class="section-title">Built different.<br /><em>Priced fair.</em></h2>
            <p class="why-lead">We source directly from Indian steel manufacturers and pass the savings to you — no middlemen, no markups.</p>
            <a href="https://wa.me/919999999999?text=Tell%20me%20more%20about%20SteelNest!" target="_blank" class="btn-dark">
              Talk to us
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
          </div>
          <div class="why-features">
            <div
              v-for="(feat, i) in features"
              :key="feat.title"
              class="feat-card"
              :style="{ animationDelay: `${i * 0.1}s` }"
              :class="{ visible: inView }"
            >
              <div class="feat-icon">{{ feat.icon }}</div>
              <div>
                <h3 class="feat-title">{{ feat.title }}</h3>
                <p class="feat-desc">{{ feat.desc }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- HOW TO ORDER -->
    <section class="how-section" ref="howRef">
      <div class="container">
        <div class="section-header-centered" :class="{ visible: howInView }">
          <span class="section-tag">Simple as 1-2-3</span>
          <h2 class="section-title">Order in <em>60 seconds</em></h2>
        </div>
        <div class="steps-row">
          <div
            v-for="(step, i) in steps"
            :key="step.title"
            class="step-card"
            :style="{ animationDelay: `${i * 0.15}s` }"
            :class="{ visible: howInView }"
          >
            <div class="step-num">{{ String(i + 1).padStart(2, '0') }}</div>
            <div class="step-icon">{{ step.icon }}</div>
            <h3 class="step-title">{{ step.title }}</h3>
            <p class="step-desc">{{ step.desc }}</p>
            <div class="step-arrow" v-if="i < steps.length - 1">→</div>
          </div>
        </div>
        <div class="how-cta" :class="{ visible: howInView }">
          <a href="https://wa.me/919999999999?text=Hi%2C%20I%20want%20to%20place%20an%20order!" target="_blank" class="btn-wa-big">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            Start Ordering Now
          </a>
          <p class="how-note">Typically replied within 5 minutes · Mon–Sat, 9am–8pm</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
const whyRef = ref(null)
const howRef = ref(null)
const inView = ref(false)
const howInView = ref(false)

const features = [
  { icon: '⬡', title: '18/8 Surgical Steel', desc: 'Food-grade stainless steel, certified safe, rust-proof and toxin-free for your family.' },
  { icon: '◈', title: 'Factory Direct Pricing', desc: 'We cut out the middlemen. Get premium quality at prices that make sense.' },
  { icon: '◎', title: 'ISI & BIS Certified', desc: 'Every product carries mandatory Indian safety certifications. No compromises.' },
  { icon: '◑', title: 'Fast Local Delivery', desc: 'Same-day delivery in city, next-day across Kerala. Tracked and insured.' },
  { icon: '◐', title: 'Easy Returns', desc: '7-day no-questions return policy. If it\'s not perfect, we make it right.' },
  { icon: '◒', title: 'WhatsApp Support', desc: 'Real human support via WhatsApp. No bots, no IVR — just a quick chat.' },
]

const steps = [
  { icon: '💬', title: 'Browse & Choose', desc: 'Pick products from our catalogue on this site or ask us for more options on WhatsApp.' },
  { icon: '📲', title: 'Message Us', desc: 'Send us a quick WhatsApp message with your order. We confirm within minutes.' },
  { icon: '🚀', title: 'Pay & Relax', desc: 'Pay via UPI, card, or COD. We pack and deliver right to your doorstep.' },
]

onMounted(() => {
  const o1 = new IntersectionObserver(([e]) => { if (e.isIntersecting) inView.value = true }, { threshold: 0.1 })
  const o2 = new IntersectionObserver(([e]) => { if (e.isIntersecting) howInView.value = true }, { threshold: 0.1 })
  if (whyRef.value) o1.observe(whyRef.value)
  if (howRef.value) o2.observe(howRef.value)
})
</script>

<style scoped>
.why-section {
  padding: 100px 0;
  background: linear-gradient(180deg, var(--cream) 0%, #F0F4F8 100%);
}
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 32px;
}
.why-grid {
  display: grid;
  grid-template-columns: 380px 1fr;
  gap: 80px;
  align-items: start;
}
.why-left {
  position: sticky;
  top: 120px;
  opacity: 0;
  transform: translateX(-30px);
  transition: all 0.7s ease;
}
.why-left.visible { opacity: 1; transform: none; }
.section-tag {
  display: inline-block;
  font-size: 12px;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--warm-dark);
  font-weight: 600;
  margin-bottom: 12px;
}
.section-title {
  font-family: var(--font-display);
  font-size: clamp(36px, 4vw, 54px);
  font-weight: 300;
  color: var(--charcoal);
  margin-bottom: 16px;
  line-height: 1.15;
}
.section-title em { font-style: italic; color: var(--warm-dark); }
.why-lead {
  font-size: 16px;
  color: var(--steel-dark);
  line-height: 1.8;
  margin-bottom: 32px;
}
.btn-dark {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 13px 24px;
  background: var(--charcoal);
  color: white;
  text-decoration: none;
  border-radius: 50px;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.3s;
}
.btn-dark:hover {
  background: var(--charcoal-soft);
  transform: translateY(-2px);
}

.why-features {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}
.feat-card {
  background: white;
  border-radius: 16px;
  padding: 24px;
  border: 1px solid rgba(139,157,175,0.15);
  display: flex;
  gap: 16px;
  align-items: flex-start;
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.5s ease, transform 0.5s ease, box-shadow 0.3s;
}
.feat-card.visible { opacity: 1; transform: none; }
.feat-card:hover { box-shadow: 0 8px 30px rgba(28,33,40,0.08); }
.feat-icon {
  width: 40px; height: 40px;
  min-width: 40px;
  background: linear-gradient(135deg, rgba(201,169,110,0.1), rgba(139,157,175,0.15));
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  color: var(--warm-dark);
}
.feat-title {
  font-size: 15px;
  font-weight: 600;
  color: var(--charcoal);
  margin-bottom: 4px;
}
.feat-desc {
  font-size: 13px;
  color: var(--steel-dark);
  line-height: 1.6;
}

/* HOW TO ORDER */
.how-section {
  padding: 100px 0;
  background: var(--charcoal);
  position: relative;
  overflow: hidden;
}
.how-section::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
  background-size: 60px 60px;
}
.section-header-centered {
  text-align: center;
  margin-bottom: 60px;
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.6s ease;
  position: relative;
}
.section-header-centered.visible { opacity: 1; transform: none; }
.section-header-centered .section-tag { color: var(--warm); }
.section-header-centered .section-title { color: white; }

.steps-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  position: relative;
  margin-bottom: 56px;
}
.step-card {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 20px;
  padding: 36px 28px;
  text-align: center;
  position: relative;
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease, transform 0.6s ease, background 0.3s;
}
.step-card.visible { opacity: 1; transform: none; }
.step-card:hover { background: rgba(255,255,255,0.07); }
.step-num {
  font-family: var(--font-display);
  font-size: 64px;
  font-weight: 700;
  color: rgba(255,255,255,0.04);
  position: absolute;
  top: 12px; right: 20px;
  line-height: 1;
}
.step-icon { font-size: 40px; margin-bottom: 16px; }
.step-title {
  font-size: 18px;
  font-weight: 600;
  color: white;
  margin-bottom: 10px;
}
.step-desc {
  font-size: 14px;
  color: rgba(255,255,255,0.5);
  line-height: 1.7;
}
.step-arrow {
  position: absolute;
  right: -18px;
  top: 50%;
  transform: translateY(-50%);
  color: rgba(255,255,255,0.2);
  font-size: 24px;
  z-index: 2;
}

.how-cta {
  text-align: center;
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.6s ease 0.4s;
  position: relative;
}
.how-cta.visible { opacity: 1; transform: none; }
.btn-wa-big {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  padding: 18px 40px;
  background: #25D366;
  color: white;
  text-decoration: none;
  border-radius: 50px;
  font-size: 17px;
  font-weight: 700;
  transition: all 0.3s;
  box-shadow: 0 8px 40px rgba(37,211,102,0.3);
}
.btn-wa-big:hover {
  background: #128C7E;
  transform: translateY(-3px);
  box-shadow: 0 14px 50px rgba(37,211,102,0.4);
}
.how-note {
  margin-top: 16px;
  font-size: 13px;
  color: rgba(255,255,255,0.4);
}

@media (max-width: 900px) {
  .why-grid { grid-template-columns: 1fr; gap: 40px; }
  .why-left { position: static; }
  .why-features { grid-template-columns: 1fr; }
  .steps-row { grid-template-columns: 1fr; }
  .step-arrow { display: none; }
}
</style>
