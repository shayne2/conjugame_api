#!/usr/bin/env python3

from data_structs.verbs import VerbForm, Mood, Tempo, Person, Number
from classify.verbs import VerbFormClassifier

class VerbConjugator:
    def __init__(self, before: str, verb: str, after: str) -> None:
        self.infinitive = verb

        self.frame = "{} _ {}".format(before, after)
        self.verb_form = self.get_verb_form()

    def get_verb_form(self) -> VerbForm:
        classifier = VerbFormClassifier(self.frame)
        return classifer.get_verb_form()

    def conjugate_verb(self) -> str:
        mood = self.verb_form.mood
        if mood == Mood.INDICATIVE
            return self.conjugate_indicative()
        elif mood == Mood.SUBJUNCTIVE:
            return self.conjugate_subjunctive()
        else:
            return self.conjugate_imperative()

    def conjugate_indicative(self) -> str:
        tempo = self.verb_form.tempo
        if tempo == Tempo.PRESENT
            return self.conjugate_indicative_simple_present()
        elif tempo == Tempo.PRETERITE_PERFECT:
            raise NotImplementedError
        elif tempo == Tempo.PRETERITE_IMPERFECT:
            raise NotImplementedError
        elif tempo == Tempo.PRETERITE_MAIS_QUE_PERFEITO:
            raise NotImplementedError
        elif tempo == Tempo.PRESENT_PERFECT:
            raise NotImplementedError
        elif tempo == Tempo.PRETERITE_PERFECT_PERFECT:
            raise NotImplementedError
        elif tempo == Tempo.PRETERITE_IMPERFECT_PERFECT:
            raise NotImplementedError
        elif tempo == Tempo.FUTURE_PERFECT:
            raise NotImplementedError
        elif tempo == Tempo.CONDITIONAL_PERFECT:
            raise NotImplementedError
        else:
            raise NotImplementedError

    def conjugate_indicative_simple_present(self) -> str:
        # Put this somewhere else
        lookup = {
            'ar': [
                'o',
                'a',
                'amos',
                'am'
            ]
            'er': [
                'o',
                'e',
                'emos',
                'em'
            ]
            'ir': [
                'o',
                'e',
                'imos',
                'em'
            ]
        }
        last_two_letters = self.infinitive[-2:]
        if last_two_letters not in lookup:
            raise ValueError("Not a valid infinitive supplied")
        person = self.verb_form.person
        number = self.verb_form.number
        person_number_idx = person + 2 * number
        suffix = lookup[last_two_letters][person_number_idx]
        return "{}{}".format(self.infinitive[:-2], suffix)

    def get_past_participle(self) -> str:
        raise NotImplementedError

    def get_present_progressive(self) -> str:
        raise NotImplementedError

    def conjugate_subjunctive(self) -> str:
        raise NotImplementedError

    def conjugate_imperative(self) -> str:
        raise NotImplementedError
