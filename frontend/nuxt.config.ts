export default defineNuxtConfig({
  compatibilityDate: '2026-04-21',
  ssr: false,
  modules: ['@nuxtjs/tailwindcss'],
  nitro: {
    preset: 'static',
    prerender: {
      failOnError: false,    // ← don't crash on prerender errors
      routes: ['/']
    }
  },
  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000/api',
      waNumber: process.env.NUXT_PUBLIC_WA_NUMBER || '919999999999'
    }
  },
  app: {
    head: {
      title: 'SteelNest — Premium Steel Kitchenware',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'Premium steel kitchenware for modern Indian kitchens.' }
      ],
      link: [
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600;700&family=DM+Sans:wght@300;400;500;600&display=swap' }
      ]
    }
  }
})