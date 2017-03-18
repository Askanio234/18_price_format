import argparse


def format_price(price):
    default = "n/a"
    try:
        float_price = float(price)
    except (ValueError, TypeError):
        return default
    if float_price == 0:
        return default
    result = "{:,.{prec}f}".format(float_price,
                                    prec=0 if float_price == int(float_price)
                                    else 2).replace(",", " ")
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("price", help="Значение цены для форматирования")
    args = parser.parse_args()
    print(format_price(args.price))
