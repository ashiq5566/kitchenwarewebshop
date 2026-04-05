from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('original_price', models.DecimalField(
                    blank=True, decimal_places=2, max_digits=10, null=True,
                    help_text='Set this to show a strikethrough original price (for discounts)'
                )),
                ('rating', models.DecimalField(
                    decimal_places=1, default=5.0, max_digits=3,
                    help_text='Rating out of 5'
                )),
                ('badge', models.CharField(
                    blank=True, default='', max_length=50,
                    choices=[
                        ('', 'None'),
                        ('Best Seller', 'Best Seller'),
                        ('New', 'New'),
                        ('Popular', 'Popular'),
                        ('Top Rated', 'Top Rated'),
                        ('Sale', 'Sale'),
                        ('Limited', 'Limited'),
                    ],
                    help_text='Optional badge shown on the product card'
                )),
                ('image', models.ImageField(
                    blank=True, null=True, upload_to='products/',
                    help_text='Product image (uploaded to Cloudinary in production)'
                )),
                ('is_active', models.BooleanField(
                    default=True,
                    help_text='Uncheck to hide this product from the website'
                )),
                ('order', models.PositiveIntegerField(
                    default=0,
                    help_text='Lower number = shown first'
                )),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='products', to='products.category'
                )),
            ],
            options={
                'ordering': ['order', '-created_at'],
            },
        ),
    ]
