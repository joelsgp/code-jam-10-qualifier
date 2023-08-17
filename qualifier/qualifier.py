def valid_input(image_size: tuple[int, int], tile_size: tuple[int, int], ordering: list[int]) -> bool:
    """
    Return True if the given input allows the rearrangement of the image, False otherwise.

    The tile size must divide each image dimension without remainders, and `ordering` must use each input tile exactly
    once.
    """
    horizontal_tiles, ht_remainder = divmod(image_size[0], tile_size[0])
    vertical_tiles, vt_remainder = divmod(image_size[1], tile_size[1])

    if ht_remainder != 0 or vt_remainder != 0:
        # doesn't divide properly
        return False

    tile_count = horizontal_tiles * vertical_tiles
    ordering_match = range(tile_count)
    sorted_ordering = sorted(ordering)

    try:
        for a, b in zip(ordering_match, sorted_ordering, strict=True):
            if a != b:
                return False
    except ValueError:
        # length of ordering is wrong
        return False

    return True


def rearrange_tiles(image_path: str, tile_size: tuple[int, int], ordering: list[int], out_path: str) -> None:
    """
    Rearrange the image.

    The image is given in `image_path`. Split it into tiles of size `tile_size`, and rearrange them by `ordering`.
    The new image needs to be saved under `out_path`.

    The tile size must divide each image dimension without remainders, and `ordering` must use each input tile exactly
    once. If these conditions do not hold, raise a ValueError with the message:
    "The tile size or ordering are not valid for the given image".
    """
