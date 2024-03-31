from inventory.data import models


def create_movement(
    item: models.Item, bin_from: models.Bin, bin_to: models.Bin
) -> models.Movement:
    movement = models.Movement.objects.create(
        item=item, bin_from=bin_from, bin_to=bin_to
    )

    return movement
