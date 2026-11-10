"""Utility functions for Laboratory 8: Functions."""


def add_vat(price, vat_percent=18):
    """Return the price after adding VAT."""
    return price + price * vat_percent / 100


def build_username(first, last, year=""):
    """Return a username in first.last format, optionally with a year."""
    username = first.lower() + "." + last.lower()
    if year:
        username += str(year)
    return username


def add_bonus(scores, bonus):
    """Increase each score by bonus, without exceeding 100."""
    for i in range(len(scores)):
        scores[i] = min(scores[i] + bonus, 100)


def with_bonus(scores, bonus):
    """Return a new list with bonus added; leave the original list unchanged."""
    new_scores = scores[:]
    add_bonus(new_scores, bonus)
    return new_scores


def average(*numbers):
    """Return the average of the given numbers, or 0 if none are given."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def make_course(code, **details):
    """Return a course dictionary containing its code and extra details."""
    course = {"code": code}
    course.update(details)
    return course
