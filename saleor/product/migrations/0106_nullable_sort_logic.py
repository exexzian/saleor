# Generated by Django 2.2.3 on 2019-07-25 13:11

from dataclasses import dataclass

from django.db import migrations, models
from django.db.models import F, Window
from django.db.models.functions import RowNumber


@dataclass(frozen=True)
class NewCollectionProductSortOrder:
    pk: int
    sort_order: int


def reorder_collection_products(apps, schema_editor):
    CollectionProduct = apps.get_model("product", "CollectionProduct")
    new_values = CollectionProduct.objects.values("id").annotate(
        sort_order=Window(
            expression=RowNumber(),
            order_by=(F("sort_order").asc(nulls_last=True), "id"),
        )
    )

    batch = [NewCollectionProductSortOrder(*row.values()) for row in new_values]
    CollectionProduct.objects.bulk_update(batch, ["sort_order"])


class Migration(migrations.Migration):

    dependencies = [("product", "0105_remove_dups")]

    operations = [
        migrations.RunPython(reorder_collection_products),
        migrations.AddField(
            model_name="attributeproduct",
            name="sort_order",
            field=models.IntegerField(db_index=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="attributevariant",
            name="sort_order",
            field=models.IntegerField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="attributevalue",
            name="sort_order",
            field=models.IntegerField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="collectionproduct",
            name="sort_order",
            field=models.IntegerField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="productimage",
            name="sort_order",
            field=models.IntegerField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterModelOptions(
            name="attributevalue", options={"ordering": ("sort_order", "id")}
        ),
    ]
