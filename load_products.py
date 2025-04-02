import os
from django.contrib.auth import get_user_model
from products.models import Product
from django.utils.text import slugify

User = get_user_model()

# 1. Creating a user from a env-variables (Railway Variables)
username = os.environ.get("DJANGO_SUPERUSER_NAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASS")

if username and email and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print("✅ The Superuser created.")
    else:
        print("ℹ️ The superuser already exists.")
else:
    print("⚠️ The superuser isn't created — No environment variables found.")

# 2. Import images of products.
image_filenames = [
    "air_freshener_arm-cob.jpg",
    "box_kerdis_sku_kr-4820.jpg",
    "cat_vader.png",
    "henger_for_clothes_sku_PK17-002.jpg",
    "keychain_auto_techteile_sku_cl1.jpg",
    "keychain_auto_techteile_sku_mb4.jpg",
    "keychain_auto_techteile_sku_MB7.jpg",
    "keychain_mitsubishi_sku_mm-0681.jpg",
    "keychain_toyota_chr_sku_tch-0001.jpg",
    "keychain_vag_audi_sku_vag-3181.jpg",
    "keychain_vag_volkswagen_sku_vag-8701.jpg",
    "organizer_bag_poputchik_volkswagen_sku_03-125-1d.jpg",
    "phone_holder_baseus_gravity_sku_suyl-01.jpg",
    "phone_holder_baseus_metal_age_gravity_sku_suyl-j01.jpg",
    "pillow_black_with_logo_audi_statuscase_ap-3002.jpg",
    "pillow_black_with_logo_mitsubishi_statuscase_sku_ap-4302.jpg",
    "pillow_black_with_logo_toyota_statuscase_sku_ap-5002.jpg",
    "pillow_black_with_logo_volkswagen_statuscase_sku_ap-3003.jpg",
    "pillow_burgundy_color_with_logo_citroen_statuscase_sku_ap-3102.jpg",
    "usb_charger_baseus_sku_ccall-m01.jpeg",
    "usd_charger_baseus_sku_ccbx0s.jpg",
    "vacuum_cleaner_black_plus_decker_sku_bhhv520bt.jpeg",
    "vacuum_cleaner_voin_sku_vl-330.jpg",
]

for filename in image_filenames:
    name_raw = os.path.splitext(filename)[0].replace("_", " ").replace("-", " ")
    name = name_raw.title()
    slug = slugify(name)
    image_path = f'accessories_photo/{filename}'

    product, created = Product.objects.get_or_create(
        slug=slug,
        defaults={
            'name': name,
            'description': f'Test description for the product {name}',
            'stock': 10,
            'price': 99.99,
            'image': image_path,
        }
    )

    if created:
        print(f"✅ The product created: {name}")
    else:
        print(f"ℹ️ The product already exists: {name}")
