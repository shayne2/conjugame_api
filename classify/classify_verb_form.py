#!/usr/bin/env python3

from data_structs.verbs import VerbForm, Mood, Tempo, Person, Number


class VerbFormClassifier:
    # TODO: Add ctor that pulls in some sort of a universal resource hehe
    def classify_by_frame(self, before: str, after: str) -> VerbForm:
        frame = '{} _ {}'.format(before, after)
        # Placeholder
        return VerbForm(
            mood=Mood.INDICATIVE,
            tempo=Tempo.PRESENT,
            person=Person.FIRST,
            number=Number.SINGULAR
        )
    # TODO: Enforce that only valid states are returned
    # AKA Valid (Mood, Tempo) tuple
