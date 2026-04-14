"""
Point of Sale (POS) system implementation.
"""

products = {
    "12345": 7.25,
    "23456": 12.50,
}


def _get_price(barcode):
    return products.get(barcode, None)


def _calculate_total(barcodes):
    total_price = 0.0
    for barcode in barcodes:
        price = _get_price(barcode)
        if price is None:
            continue
        total_price += price
    return f"${total_price:.2f}"


def scan_barcode(barcode):
    """
    Scans a barcode and returns the price or an error message.
    If a list of barcodes is provided, it calculates the total price.
    """

    if isinstance(barcode, list):
        return _calculate_total(barcode)

    if not barcode:
        return "Error: empty barcode"

    price = _get_price(barcode)

    if price is None:
        return "Error: Barcode not found"

    return f"${price:.2f}"
