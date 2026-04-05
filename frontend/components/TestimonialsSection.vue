<template>
  <section id="testimonials" class="testimonials-section" ref="sectionRef">
    <div class="container">
      <div class="section-header" :class="{ visible: inView }">
        <span class="section-tag">Customer Stories</span>
        <h2 class="section-title">Real kitchens. <em>Real love.</em></h2>
      </div>

      <div class="reviews-grid">
        <div
          v-for="(review, i) in reviews"
          :key="i"
          class="review-card"
          :style="{ animationDelay: `${i * 0.1}s` }"
          :class="{ visible: inView }"
        >
          <div class="stars">
            <span v-for="n in 5" :key="n">★</span>
          </div>
          <blockquote class="review-text">"{{ review.text }}"</blockquote>
          <div class="reviewer">
            <div class="reviewer-avatar">{{ review.initials }}</div>
            <div>
              <div class="reviewer-name">{{ review.name }}</div>
              <div class="reviewer-loc">{{ review.location }}</div>
            </div>
            <div class="verified-badge">✓ Verified</div>
          </div>
        </div>
      </div>

      <!-- Trust bar -->
      <div class="trust-bar" :class="{ visible: inView }">
        <div class="trust-item" v-for="t in trust" :key="t.label">
          <div class="trust-icon">{{ t.icon }}</div>
          <div class="trust-label">{{ t.label }}</div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const sectionRef = ref(null)
const inView = ref(false)

const reviews = [
  {
    text: 'Ordered a casserole set and a tiffin box — both arrived the next day, perfectly packed. The steel quality is noticeably better than what I used to buy at the local store.',
    name: 'Priya Nair', initials: 'PN', location: 'Ernakulam, Kerala'
  },
  {
    text: 'Just messaged on WhatsApp, shared what I needed, and they guided me to the right products. Whole process was so easy. The pressure cooker is absolutely solid.',
    name: 'Rahul Menon', initials: 'RM', location: 'Thrissur, Kerala'
  },
  {
    text: 'Bought a full serving set for my daughter\'s wedding. Got a bulk discount, delivered on time. Family loved the quality. Will definitely order again.',
    name: 'Geetha Krishnan', initials: 'GK', location: 'Kozhikode, Kerala'
  },
  {
    text: 'The water bottles are amazing — stays cold for hours even in summer. My whole office switched after seeing mine. Great customer support too.',
    name: 'Arun Thomas', initials: 'AT', location: 'Trivandrum, Kerala'
  },
  {
    text: 'Really appreciate the honest communication. They told me one item was out of stock and suggested a better alternative. That level of service is rare.',
    name: 'Sujatha Pillai', initials: 'SP', location: 'Kottayam, Kerala'
  },
  {
    text: 'Bought the kadai and casserole as a gift. The packaging was premium and the steel was visibly high quality. My mother was very impressed.',
    name: 'Vishnu Dev', initials: 'VD', location: 'Palakkad, Kerala'
  }
]

const trust = [
  { icon: '🏆', label: '8,000+ Orders Delivered' },
  { icon: '⭐', label: '4.8 / 5 Average Rating' },
  { icon: '✅', label: '100% ISI Certified Products' },
  { icon: '🔄', label: '7-Day Easy Returns' },
  { icon: '🚚', label: 'All Kerala Delivery' },
]

onMounted(() => {
  const observer = new IntersectionObserver(([e]) => {
    if (e.isIntersecting) inView.value = true
  }, { threshold: 0.1 })
  if (sectionRef.value) observer.observe(sectionRef.value)
})
</script>

<style scoped>
.testimonials-section {
  padding: 100px 0;
  background: linear-gradient(180deg, #F0F4F8 0%, var(--cream) 100%);
}
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 32px;
}
.section-header {
  text-align: center;
  margin-bottom: 56px;
  opacity: 0;
  transform: translateY(24px);
  transition: all 0.7s ease;
}
.section-header.visible { opacity: 1; transform: none; }
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
}
.section-title em { font-style: italic; color: var(--warm-dark); }

.reviews-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 20px;
  margin-bottom: 60px;
}
.review-card {
  background: white;
  border-radius: 20px;
  padding: 28px;
  border: 1px solid rgba(139,157,175,0.12);
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.5s ease, transform 0.5s ease, box-shadow 0.3s;
}
.review-card.visible { opacity: 1; transform: none; }
.review-card:hover { box-shadow: 0 12px 40px rgba(28,33,40,0.07); }
.stars {
  color: var(--warm);
  font-size: 15px;
  letter-spacing: 2px;
  margin-bottom: 14px;
}
.review-text {
  font-family: var(--font-display);
  font-size: 17px;
  font-style: italic;
  color: var(--charcoal-soft);
  line-height: 1.7;
  margin-bottom: 20px;
  border: none;
}
.reviewer {
  display: flex;
  align-items: center;
  gap: 12px;
}
.reviewer-avatar {
  width: 40px; height: 40px;
  min-width: 40px;
  background: linear-gradient(135deg, var(--steel-light), var(--steel));
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 700;
  color: white;
}
.reviewer-name {
  font-size: 14px;
  font-weight: 600;
  color: var(--charcoal);
}
.reviewer-loc {
  font-size: 12px;
  color: var(--steel);
}
.verified-badge {
  margin-left: auto;
  font-size: 11px;
  color: #25D366;
  font-weight: 700;
  background: rgba(37,211,102,0.08);
  padding: 4px 10px;
  border-radius: 50px;
  white-space: nowrap;
}

.trust-bar {
  display: flex;
  gap: 0;
  background: var(--charcoal);
  border-radius: 20px;
  overflow: hidden;
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.6s ease 0.3s;
}
.trust-bar.visible { opacity: 1; transform: none; }
.trust-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 28px 16px;
  border-right: 1px solid rgba(255,255,255,0.06);
  transition: background 0.3s;
}
.trust-item:last-child { border-right: none; }
.trust-item:hover { background: rgba(255,255,255,0.04); }
.trust-icon { font-size: 26px; }
.trust-label {
  font-size: 12px;
  color: rgba(255,255,255,0.55);
  text-align: center;
  font-weight: 500;
}

@media (max-width: 768px) {
  .reviews-grid { grid-template-columns: 1fr; }
  .trust-bar { flex-wrap: wrap; }
  .trust-item { flex: 1 0 40%; }
}
</style>
