
<script setup>
const sectionRef = ref(null)
const inView = ref(false)
const hoveredId = ref(null)
const activeSlug = ref('all')
const products = ref([])
const categories = ref([{ name: 'All', slug: 'all' }])
const loading = ref(true)

const config = useRuntimeConfig()
const apiBase = config.public.apiBase
const waNumber = config.public.waNumber || '919999999999'

const selectCategory = async (slug) => {
  activeSlug.value = slug
  loading.value = true
  try {
    const url = slug === 'all'
      ? `${apiBase}/products/`
      : `${apiBase}/products/?category=${slug}`
    const data = await $fetch(url)
    products.value = Array.isArray(data) ? data : (data.results || [])
  } catch (e) {
    console.error('Failed to fetch products:', e)
    products.value = []
  }
  loading.value = false
}

const getWaLink = (product) => {
  const msg = `Hi, I want to order *${product.name}* (₹${Number(product.price).toLocaleString('en-IN')}). Please confirm availability.`
  return `https://wa.me/${waNumber}?text=${encodeURIComponent(msg)}`
}

onMounted(async () => {
  const observer = new IntersectionObserver(([e]) => {
    if (e.isIntersecting) inView.value = true
  }, { threshold: 0.1 })
  if (sectionRef.value) observer.observe(sectionRef.value)

  try {
    const [prodsData, catsData] = await Promise.all([
      $fetch(`${apiBase}/products/`),
      $fetch(`${apiBase}/categories/`)
    ])
    products.value = Array.isArray(prodsData) ? prodsData : (prodsData.results || [])
    const cats = Array.isArray(catsData) ? catsData : (catsData.results || [])
    categories.value = [{ name: 'All', slug: 'all' }, ...cats]
  } catch (e) {
    console.error('Failed to fetch data:', e)
    products.value = []
  }
  loading.value = false
})
</script>
<template>
  <section id="products" class="products-section" ref="sectionRef">
    <div class="container">
      <div class="section-header" :class="{ visible: inView }">
        <span class="section-tag">Our Collection</span>
        <h2 class="section-title">Steel that <em>speaks</em> for itself</h2>
        <p class="section-sub">Handpicked kitchenware for every Indian kitchen — from daily cooking to festive feasts.</p>
      </div>

      <!-- Category Filters -->
      <div class="filters" :class="{ visible: inView }">
        <button
          v-for="cat in categories"
          :key="cat.slug"
          class="filter-btn"
          :class="{ active: activeSlug === cat.slug }"
          @click="selectCategory(cat.slug)"
        >{{ cat.name }}</button>
      </div>

      <!-- Loading skeleton -->
      <div v-if="loading" class="loading-grid">
        <div v-for="n in 6" :key="n" class="skeleton-card">
          <div class="skeleton-img"></div>
          <div class="skeleton-body">
            <div class="skeleton-line short"></div>
            <div class="skeleton-line"></div>
            <div class="skeleton-line medium"></div>
          </div>
        </div>
      </div>

      <!-- Product Grid -->
      <div v-else-if="products.length" class="products-grid">
        <div
          v-for="(product, i) in products"
          :key="product.id"
          class="product-card"
          :style="{ animationDelay: `${i * 0.07}s` }"
          :class="{ visible: inView }"
          @mouseenter="hoveredId = product.id"
          @mouseleave="hoveredId = null"
        >
          <div class="card-img">
            <img v-if="product.image_url" :src="product.image_url" :alt="product.name" class="product-photo" />
            <div v-else class="product-icon-wrap">
              <svg viewBox="0 0 80 60" fill="none" xmlns="http://www.w3.org/2000/svg" class="fallback-svg">
                <path d="M12 22 Q12 52 40 52 Q68 52 68 22 Z" fill="url(#fp1)"/>
                <rect x="10" y="18" width="60" height="8" rx="4" fill="url(#fp2)"/>
                <path d="M14 18 Q14 8 40 8 Q66 8 66 18 Z" fill="url(#fp3)"/>
                <rect x="36" y="2" width="8" height="8" rx="4" fill="#C5CDD6"/>
                <rect x="4" y="22" width="10" height="5" rx="2.5" fill="#C5CDD6"/>
                <rect x="66" y="22" width="10" height="5" rx="2.5" fill="#C5CDD6"/>
                <defs>
                  <linearGradient id="fp1" x1="12" y1="22" x2="68" y2="52" gradientUnits="userSpaceOnUse">
                    <stop offset="0%" stop-color="#C5CDD6"/><stop offset="100%" stop-color="#4A5568"/>
                  </linearGradient>
                  <linearGradient id="fp2" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">
                    <stop offset="0%" stop-color="#D6DDE4"/><stop offset="100%" stop-color="#8B9DAF"/>
                  </linearGradient>
                  <linearGradient id="fp3" x1="14" y1="8" x2="66" y2="18" gradientUnits="userSpaceOnUse">
                    <stop offset="0%" stop-color="#B0BECA"/><stop offset="100%" stop-color="#6B7F8F"/>
                  </linearGradient>
                </defs>
              </svg>
            </div>
            <div class="card-badge" v-if="product.badge">{{ product.badge }}</div>
            <div class="card-hover-actions" :class="{ show: hoveredId === product.id }">
              <a :href="getWaLink(product)" target="_blank" class="quick-order">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                Quick Order
              </a>
            </div>
          </div>
          <div class="card-body">
            <span class="card-cat">{{ product.category_name }}</span>
            <h3 class="card-name">{{ product.name }}</h3>
            <p class="card-desc">{{ product.description }}</p>
            <div class="card-footer">
              <div class="price-block">
                <span class="card-price">₹{{ Number(product.price).toLocaleString('en-IN') }}</span>
                <span v-if="product.original_price" class="card-original">
                  ₹{{ Number(product.original_price).toLocaleString('en-IN') }}
                </span>
              </div>
              <div class="card-rating"><span>★</span> {{ product.rating }}</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Empty state -->
      <div v-else class="empty-state">
        <p>No products found in this category.</p>
      </div>

      <!-- CTA -->
      <div class="products-cta" :class="{ visible: inView }">
        <p>Don't see what you need? We have 500+ products in our catalogue.</p>
        <a :href="`https://wa.me/${waNumber}?text=${encodeURIComponent('Hi, please share your full product catalogue!')}`" target="_blank" class="btn-wa-full">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
          Request Full Catalogue on WhatsApp
        </a>
      </div>
    </div>
  </section>
</template>

<style scoped>
.products-section { padding: 100px 0; background: var(--cream); }
.container { max-width: 1200px; margin: 0 auto; padding: 0 32px; }
.section-header {
  text-align: center; margin-bottom: 48px;
  opacity: 0; transform: translateY(30px); transition: all 0.7s ease;
}
.section-header.visible { opacity: 1; transform: none; }
.section-tag {
  display: inline-block; font-size: 12px; letter-spacing: 0.15em;
  text-transform: uppercase; color: var(--warm-dark); font-weight: 600; margin-bottom: 12px;
}
.section-title { font-family: var(--font-display); font-size: clamp(36px, 4vw, 54px); font-weight: 300; color: var(--charcoal); margin-bottom: 16px; }
.section-title em { font-style: italic; color: var(--warm-dark); }
.section-sub { font-size: 16px; color: var(--steel-dark); max-width: 480px; margin: 0 auto; line-height: 1.7; }

.filters {
  display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; margin-bottom: 48px;
  opacity: 0; transform: translateY(20px); transition: all 0.6s ease 0.2s;
}
.filters.visible { opacity: 1; transform: none; }
.filter-btn {
  padding: 9px 20px; border: 1.5px solid var(--steel-light); border-radius: 50px;
  background: transparent; color: var(--charcoal-soft); font-size: 13px; font-weight: 500;
  cursor: pointer; transition: all 0.25s; font-family: var(--font-body);
}
.filter-btn:hover, .filter-btn.active { background: var(--charcoal); border-color: var(--charcoal); color: white; }

/* Skeleton */
.loading-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 24px; margin-bottom: 56px; }
.skeleton-card { background: white; border-radius: 20px; overflow: hidden; border: 1px solid rgba(139,157,175,0.15); }
.skeleton-img { height: 200px; background: linear-gradient(90deg, #f0f0f0 25%, #e8e8e8 50%, #f0f0f0 75%); background-size: 200% 100%; animation: shimmer 1.4s infinite; }
.skeleton-body { padding: 20px 24px; display: flex; flex-direction: column; gap: 10px; }
.skeleton-line { height: 14px; border-radius: 6px; background: linear-gradient(90deg, #f0f0f0 25%, #e8e8e8 50%, #f0f0f0 75%); background-size: 200% 100%; animation: shimmer 1.4s infinite; }
.skeleton-line.short { width: 40%; }
.skeleton-line.medium { width: 60%; }

.products-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 24px; margin-bottom: 56px; }
.product-card {
  background: white; border-radius: 20px; overflow: hidden;
  border: 1px solid rgba(139,157,175,0.15);
  opacity: 0; transform: translateY(30px);
  transition: opacity 0.6s ease, transform 0.6s ease, box-shadow 0.3s;
}
.product-card.visible { opacity: 1; transform: none; }
.product-card:hover { box-shadow: 0 20px 60px rgba(28,33,40,0.1); transform: translateY(-4px) !important; }

.card-img {
  background: linear-gradient(135deg, #F0F4F8, #E8EDF2); height: 200px;
  display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;
}
.product-photo { width: 100%; height: 100%; object-fit: cover; }
.product-icon-wrap { display: flex; align-items: center; justify-content: center; width: 100%; height: 100%; }
.fallback-svg { width: 120px; height: 100px; }

.card-badge { position: absolute; top: 14px; left: 14px; padding: 5px 12px; background: var(--warm); color: white; font-size: 11px; font-weight: 700; border-radius: 50px; }
.card-hover-actions { position: absolute; bottom: 0; left: 0; right: 0; padding: 16px; background: linear-gradient(transparent, rgba(28,33,40,0.7)); transform: translateY(100%); transition: transform 0.3s; }
.card-hover-actions.show { transform: translateY(0); }
.quick-order { display: flex; align-items: center; justify-content: center; gap: 8px; width: 100%; padding: 10px; background: #25D366; color: white; text-decoration: none; border-radius: 10px; font-size: 13px; font-weight: 600; }
.quick-order:hover { background: #128C7E; }

.card-body { padding: 20px 24px; }
.card-cat { font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--steel); font-weight: 600; }
.card-name { font-family: var(--font-display); font-size: 22px; font-weight: 500; color: var(--charcoal); margin: 6px 0 8px; }
.card-desc { font-size: 13px; color: var(--steel-dark); line-height: 1.6; margin-bottom: 16px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.card-footer { display: flex; align-items: center; justify-content: space-between; }
.price-block { display: flex; align-items: baseline; gap: 8px; }
.card-price { font-family: var(--font-display); font-size: 24px; font-weight: 600; color: var(--charcoal); }
.card-original { font-size: 14px; color: var(--steel); text-decoration: line-through; }
.card-rating { font-size: 13px; color: var(--warm-dark); font-weight: 600; }

.empty-state { text-align: center; padding: 60px; color: var(--steel-dark); font-size: 16px; }

.products-cta { text-align: center; padding: 40px; background: linear-gradient(135deg, #1C2128, #2D3748); border-radius: 24px; opacity: 0; transform: translateY(20px); transition: all 0.6s ease 0.3s; }
.products-cta.visible { opacity: 1; transform: none; }
.products-cta p { color: rgba(255,255,255,0.7); font-size: 16px; margin-bottom: 20px; }
.btn-wa-full { display: inline-flex; align-items: center; gap: 10px; padding: 14px 32px; background: #25D366; color: white; text-decoration: none; border-radius: 50px; font-size: 15px; font-weight: 600; transition: all 0.3s; }
.btn-wa-full:hover { background: #128C7E; transform: translateY(-2px); box-shadow: 0 8px 30px rgba(37,211,102,0.4); }
</style>
