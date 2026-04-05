# SteelNest — Full Stack Kitchenware Store

**Nuxt 3 frontend + Django REST backend, both deployed on Vercel.**
Products and prices managed from Django Admin panel. Orders via WhatsApp.

```
steelkitchen-full/
├── frontend/    ← Nuxt 3 + Nuxt UI  (deployed as Vercel project #1)
└── backend/     ← Django + DRF      (deployed as Vercel project #2)
```

---

## 🗺️ How it works

```
Django Admin  →  add/edit products & prices
     ↓
Neon PostgreSQL  (stores product data)
Cloudinary       (stores product images)
     ↓
Django REST API  →  /api/products/  /api/categories/
     ↓
Nuxt frontend  →  fetches products, renders website
     ↓
Customer clicks "Quick Order"  →  WhatsApp opens with pre-filled message
```

---

## ✅ Step-by-step deployment

### Step 1 — Get free accounts (all free tier)

| Service | URL | What for |
|---------|-----|----------|
| Vercel | vercel.com | Host both frontend and backend |
| Neon | neon.tech | Free PostgreSQL database |
| Cloudinary | cloudinary.com | Product image storage |
| GitHub | github.com | Connect repos to Vercel |

---

### Step 2 — Set up Neon database

1. Sign up at **neon.tech**
2. Create a new project → name it `steelkitchen`
3. Go to **Connection Details** → copy these values:
   - Host, Database, User, Password
4. Save them — you'll need them in Step 4

---

### Step 3 — Set up Cloudinary

1. Sign up at **cloudinary.com**
2. From the Dashboard copy:
   - Cloud Name
   - API Key
   - API Secret
3. Save them — you'll need them in Step 4

---

### Step 4 — Deploy the Django backend

1. Push the `backend/` folder to a **new GitHub repo** (e.g. `steelnest-backend`)

2. Go to **vercel.com** → Add New Project → Import that repo

3. In Vercel project settings:
   - **Root Directory**: ` ` (leave empty / root)
   - **Build Command**: `bash build_files.sh`
   - **Output Directory**: ` ` (leave empty)

4. Add these **Environment Variables** in Vercel:

```
DJANGO_SECRET_KEY        = (generate: python -c "import secrets; print(secrets.token_urlsafe(50))")
DEBUG                    = False
DJANGO_ALLOWED_HOSTS     = your-backend.vercel.app
DB_NAME                  = (from Neon)
DB_USER                  = (from Neon)
DB_PASSWORD              = (from Neon)
DB_HOST                  = (from Neon)
DB_PORT                  = 5432
CLOUDINARY_CLOUD_NAME    = (from Cloudinary)
CLOUDINARY_API_KEY       = (from Cloudinary)
CLOUDINARY_API_SECRET    = (from Cloudinary)
CORS_ALLOWED_ORIGINS     = https://your-frontend.vercel.app,http://localhost:3000
```

5. Click **Deploy**

6. After deploy, visit:
   `https://your-backend.vercel.app/api/products/` → should return `[]`
   `https://your-backend.vercel.app/admin/` → Django admin login

7. Create a superuser by running locally:
```bash
cd backend
pip install -r requirements.txt
# Copy .env.example to .env and fill in your production DB values
cp .env.example .env
python manage.py createsuperuser
# Then seed sample products (optional):
python manage.py seed_data
```

---

### Step 5 — Deploy the Nuxt frontend

1. Push the `frontend/` folder to a **new GitHub repo** (e.g. `steelnest-frontend`)

2. Go to **vercel.com** → Add New Project → Import that repo

3. Vercel auto-detects Nuxt. Leave defaults.

4. Add these **Environment Variables** in Vercel:

```
NUXT_PUBLIC_API_BASE    = https://your-backend.vercel.app/api
NUXT_PUBLIC_WA_NUMBER   = 91XXXXXXXXXX   ← your WhatsApp number with country code
```

5. Click **Deploy** → your site is live!

---

### Step 6 — Add products via Django Admin

1. Go to `https://your-backend.vercel.app/admin/`
2. Log in with the superuser you created
3. Click **Categories** → add your product categories
4. Click **Products** → add products with:
   - Name, Description
   - Price (and optional Original Price for discount display)
   - Category
   - Badge (Best Seller / New / Popular / etc.)
   - Image (uploads directly to Cloudinary)
   - Toggle `is_active` to show/hide on website
   - `order` field to control display order

Changes appear on the website **immediately** (no rebuild needed).

---

## 💻 Local development

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env           # Fill in your values (or leave DB_HOST empty for SQLite)
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_data     # Optional: loads 6 sample products
python manage.py runserver     # → http://localhost:8000
```

Admin: http://localhost:8000/admin/
API:   http://localhost:8000/api/products/

### Frontend

```bash
cd frontend
npm install
cp .env.example .env           # Set NUXT_PUBLIC_API_BASE=http://localhost:8000/api
npm run dev                    # → http://localhost:3000
```

---

## 🔌 API Reference

| Endpoint | Description |
|----------|-------------|
| `GET /api/products/` | All active products |
| `GET /api/products/?category=cookware` | Filter by category slug |
| `GET /api/products/{id}/` | Single product |
| `GET /api/categories/` | All categories |
| `GET /admin/` | Django admin panel |

### Sample product response
```json
{
  "id": 1,
  "name": "Chef's Casserole Set",
  "description": "Triple-layered 18/8 stainless steel...",
  "category_name": "Cookware",
  "price": "1299.00",
  "original_price": "1799.00",
  "discount_percent": 28,
  "rating": "4.9",
  "badge": "Best Seller",
  "image_url": "https://res.cloudinary.com/your-cloud/image/upload/...",
  "is_active": true
}
```

---

## 🎨 Customisation

### Change WhatsApp number
Set `NUXT_PUBLIC_WA_NUMBER` environment variable in Vercel frontend project.
Format: `91XXXXXXXXXX` (country code + number, no + or spaces).

### Change brand name / colours
- Brand name: search `SteelNest` in frontend files
- Colours: `frontend/assets/css/main.css` → CSS variables at top of file
- Fonts: `frontend/nuxt.config.ts` → Google Fonts link

### Add more badge types
`backend/products/models.py` → `BADGE_CHOICES` list

---

## 🆓 Cost summary

| Service | Plan | Cost |
|---------|------|------|
| Vercel (frontend) | Hobby | Free |
| Vercel (backend) | Hobby | Free |
| Neon PostgreSQL | Free tier (3GB) | Free |
| Cloudinary images | Free tier (25GB) | Free |
| **Total** | | **₹0/month** |
