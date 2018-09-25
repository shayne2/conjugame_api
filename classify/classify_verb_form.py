#!/usr/bin/env python3

from data_structs.verbs import VerbForm, Mood, Tempo, Person, Number

class VerbFormClassifier:
    def __init__(self, frame: str) -> None:
        self.frame = frame
        self.verb_form = self.classify_by_frame()

    def classify_by_frame(self) -> VerbForm:
        # Placeholder
        return VerbForm(
            mood=Mood.INDICATIVE,
            tempo=Tempo.PRESENT,
            person=Peron.FIRST,
            number=Number.SINGULAR
        )

    def get_verb_form(self) -> VerbForm:
        return self.verb_form
