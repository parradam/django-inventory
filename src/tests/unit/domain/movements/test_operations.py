import pytest
from inventory.data import models
from inventory.domain.movements import operations


@pytest.mark.django_db
def test_movement_is_created() -> None:
    area = models.Area.objects.create(name="Area1", is_external=False)
    bin1 = models.Bin.objects.create(name="Bin1", area=area)
    bin2 = models.Bin.objects.create(name="Bin2", area=area)
    item = models.Item.objects.create(name="Item1", description="A test item")

    assert models.Movement.objects.all().count() == 0
    movement = operations.create_movement(item=item, bin_from=bin1, bin_to=bin2)
    assert models.Movement.objects.all().count() == 1

    assert movement.item.name == "Item1"
    assert movement.bin_from.name == "Bin1"
    assert movement.bin_to.name == "Bin2"
