"""
Day 8 - 2026-10-14
Tool: Word & Character Counter
What it does: Counts the words, characters (with and without spaces),
sentences and paragraphs in a piece of text, and estimates how long it
takes to read it aloud.
Who it helps: Students checking an assignment's word limit, writers and
job applicants checking a cover letter, and anyone preparing a speech.
"""

import re


def count_words(text):
    return len(text.split())


def count_characters(text, include_spaces=True):
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def count_sentences(text):
    # A sentence ends with ., ! or ? (Bangla dari "।" also counts).
    return len([s for s in re.split(r"[.!?।]+", text) if s.strip()])


def count_paragraphs(text):
    return len([p for p in text.split("\n") if p.strip()])


def reading_time_minutes(text, words_per_minute=150):
    """Average speaking pace is about 130-150 words per minute."""
    words = count_words(text)
    if words == 0:
        return 0.0
    return round(words / words_per_minute, 1)


def summarise(text):
    """Return all the counts as one easy-to-read dictionary."""
    return {
        "words": count_words(text),
        "characters_with_spaces": count_characters(text, True),
        "characters_without_spaces": count_characters(text, False),
        "sentences": count_sentences(text),
        "paragraphs": count_paragraphs(text),
        "reading_time_minutes": reading_time_minutes(text),
    }


if __name__ == "__main__":
    # Example 1: checking a short assignment paragraph
    paragraph = ("Education is the most powerful tool for changing a life. "
                 "It opens doors that money alone cannot.")
    print("Assignment paragraph:", summarise(paragraph))

    # Example 2: a two-paragraph cover-letter opening
    letter = ("Dear Sir, I am writing to apply for the position.\n"
              "I have three years of experience and I would love to join your team!")
    print("Cover letter:", summarise(letter))

    # Example 3: timing a speech before presenting it
    speech = "Good morning everyone. Thank you for being here today. " * 10
    print("Speech reading time (minutes):", reading_time_minutes(speech))
