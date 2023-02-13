import re


def parse_invoice_item(item_string):
    # Use regular expression to match the item string and extract the quantity, item name, and item price
    match = re.match(r"(\d+) (.+) at ([\d.]+)", item_string)
    quantity = int(match.group(1))
    item_name = match.group(2)
    item_price = float(match.group(3))

    # Calculate the sales tax
    tax_rate = 0.1
    tax = round(item_price * tax_rate, 2)

    # Round up the tax to the nearest 5 cent
    tax = round(tax * 20, 0) / 20

    # Calculate the total price
    total_price = item_price + tax

    # Generate the new item string
    new_item_string = f"{quantity} {item_name}: {total_price:.2f}"

    return new_item_string


def main():
    item_string = "1 music CD at 14.99"
    new_item_string = parse_invoice_item(item_string)
    print(new_item_string)
    # Output: "1 music CD: 16.49"

if __name__ == "__main__":
    main()
