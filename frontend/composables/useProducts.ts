export const useProducts = () => {
  const config = useRuntimeConfig()
  const apiBase = config.public.apiBase

  const fetchProducts = async (categorySlug?: string) => {
    const url = categorySlug && categorySlug !== 'all'
      ? `${apiBase}/products/?category=${categorySlug}`
      : `${apiBase}/products/`
    try {
      const data: any = await $fetch(url)
      return Array.isArray(data) ? data : (data.results || [])
    } catch (e) {
      console.error('Failed to fetch products', e)
      return []
    }
  }

  const fetchCategories = async () => {
    try {
      const data: any = await $fetch(`${apiBase}/categories/`)
      return Array.isArray(data) ? data : (data.results || [])
    } catch (e) {
      console.error('Failed to fetch categories', e)
      return []
    }
  }

  return { fetchProducts, fetchCategories }
}
