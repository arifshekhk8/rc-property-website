from decimal import Decimal

from django.core.management.base import BaseCommand

from projects.models import FAQ, Project


class Command(BaseCommand):
    help = "Create the two illustrative listings without overwriting existing staff edits."

    def handle(self, *args, **options):
        for n, katha, sqft, price in [(1, "3", "2160", "4500000"), (2, "5", "3600", "7500000")]:
            project, created = Project.objects.get_or_create(
                slug=f"project-{n:02d}",
                defaults={
                    "title_en": f"Project {n:02d}",
                    "title_bn": f"প্রকল্প {n:02d}",
                    "location_en": "Dhaka · Sample location",
                    "location_bn": "ঢাকা · নমুনা অবস্থান",
                    "description_en": "A space to imagine your next chapter. Explore the sample details and media below. Actual project information will be added after company review.",
                    "description_bn": "আগামী দিনের ঠিকানা কল্পনা করুন। নিচে নমুনা তথ্য ও ছবি দেখুন। কোম্পানির পর্যালোচনার পর প্রকল্পের প্রকৃত তথ্য যোগ করা হবে।",
                    "price_bdt": Decimal(price),
                    "area_katha": Decimal(katha),
                    "area_sqft": Decimal(sqft),
                    "publication": "published",
                    "is_sample": True,
                    "sample_asset": f"project-{n:02d}",
                    "order": n,
                },
            )
            self.stdout.write(f"{'Created' if created else 'Kept existing'} {project}")
        FAQ.objects.get_or_create(
            question_en="Can I see the project before contacting the team?",
            defaults={
                "question_bn": "যোগাযোগের আগে কি প্রকল্প দেখতে পারি?",
                "answer_en": "Yes. Browse the photos, sample video and 360° preview on each project page. These are illustrative until actual media is supplied.",
                "answer_bn": "হ্যাঁ। প্রতিটি প্রকল্পের ছবি, নমুনা ভিডিও ও ৩৬০° ভিউ দেখুন। প্রকৃত মিডিয়া দেওয়ার আগ পর্যন্ত এগুলো নমুনা।",
                "published": True,
                "order": 1,
            },
        )
