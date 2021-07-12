import random
from datetime                                           import datetime
from string                                             import ascii_uppercase, digits, ascii_lowercase

from django.utils.text import slugify


def get_timenow():

    today   = datetime.now().strftime('%y%m%d-%H%M%S').split('-')
    date    = today[0]
    now     = today[1]

    return date, now


def randcode_gen():

    date, now   = get_timenow()
    randcode    = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode    = (''.join(randcode))
    new_code    = f"ZIG{date}{randcode}{now}"

    return new_code


def bank_randcode_gen():

    date, now   = get_timenow()
    randcode    = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode    = (''.join(randcode))
    new_code    = f"ZIG{date}{randcode}{now}BNK"

    return new_code


def categ_randcode_gen():

    date, now   = get_timenow()
    randcode    = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode    = (''.join(randcode))
    new_code    = f"ZIG{date}{randcode}{now}CAT"

    return new_code


def color_randcode_gen():

    date, now   = get_timenow()
    randcode    = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode    = (''.join(randcode))
    new_code    = f"ZIG{date}{randcode}{now}COL"

    return new_code


def coup_randcode_gen():

    date, now   = get_timenow()
    randcode    = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode    = (''.join(randcode))
    new_code    = f"ZIG{date}{randcode}{now}CPN"

    return new_code


def item_randcode_gen():

    date, now   = get_timenow()
    randcode    = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode    = (''.join(randcode))
    new_code    = f"ZIG{date}{randcode}{now}ITM"

    return new_code


def ord_randcode_gen():

    date, now   = get_timenow()
    randcode    = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode    = (''.join(randcode))
    new_code    = f"ZIG{date}{randcode}{now}ORD"

    return new_code


def pay_randcode_gen():

    date, now   = get_timenow()
    randcode    = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode    = (''.join(randcode))
    new_code    = f"ZIG{date}{randcode}{now}PAY"

    return new_code


def prod_randcode_gen():

    date, now   = get_timenow()
    randcode    = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode    = (''.join(randcode))
    new_code    = f"ZIG{date}{randcode}{now}PROD"

    return new_code


def receipt_randcode_gen():

    date, now   = get_timenow()
    randcode    = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode    = (''.join(randcode))
    new_code    = f"ZIG{date}{randcode}{now}RCP"

    return new_code


def refund_randcode_gen():

    date, now   = get_timenow()
    randcode    = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode    = (''.join(randcode))
    new_code    = f"ZIG{date}{randcode}{now}RFN"

    return new_code


def size_randcode_gen():

    date, now   = get_timenow()
    randcode    = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode    = (''.join(randcode))
    new_code    = f"ZIG{date}{randcode}{now}SIZ"

    return new_code


def store_randcode_gen():

    date, now   = get_timenow()
    randcode    = random.sample(digits, 4) + random.sample(ascii_uppercase, 1)
    randcode    = (''.join(randcode))
    new_code    = f"ZIG{date}{randcode}{now}STR"

    return new_code


def random_string_generator(size=10, chars=ascii_lowercase + digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(slug=slug, randstr=random_string_generator(size=4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
