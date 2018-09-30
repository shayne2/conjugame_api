#!/usr/bin/env python3

import nlpnet
import re

from data_structs.verbs import VerbForm, Mood, Tempo, Person, Number
from typing import Tuple

A0 = 'A0'

first_person_pattern = re.compile("((^|\s)(nos|eu|a\sgente)($|\s))|(.*([a-z]+\se\seu($|\s))|(eu\se\s[a-z]+).*)")
plural_pattern = re.compile("((^|\s)(nos|eles|elas|esses|essas)($|\s))|(.*[a-z]+\se\s[a-z]+.*)")

class VerbFormClassifier:
    # TODO: Add ctor that pulls in some sort of a universal resource hehe
    def __init__(self):
        self.tagger = nlpnet.SRLTagger('models/srl-pt')

    # TODO: Enforce that only valid states are returned
    # AKA Valid (Mood, Tempo) tuple
    def classify_by_frame(
        self,
        before: str,
        infinitive: str,
        after: str
    ) -> VerbForm:
        person = self.classify_person(before, infinitive, after)
        number = self.classify_number(before, infinitive, after)
        return VerbForm(
            # Placeholder
            mood=Mood.INDICATIVE,
            tempo=Tempo.PRESENT,
            person=person,
            number=number
        )

    def classify_person(
        self,
        before: str,
        infinitive: str,
        after: str
    ) -> Tuple[Person, Number]:
        subj = self.get_subj(before, infinitive, after)
        if subj:
            processed_subj_str = subj.lower().replace('ó', 'o')
            if first_person_pattern.match(processed_subj_str):
                return Person.FIRST
        return Person.THIRD

    def classify_number(
        self,
        before: str,
        infinitive: str,
        after: str
    ) -> Tuple[Person, Number]:
        subj = self.get_subj(before, infinitive, after)
        if subj:
            processed_subj_str = subj.lower()
            if plural_pattern.match(processed_subj_str):
                return Number.PLURAL
        return Number.SINGULAR

    def get_subj(
            self,
            before: str,
            infinitive: str,
            after: str
        ) -> str:
        # TODO: Try-Catch
        return before
        filled_frame = '{} {} {}'.format(before, infinitive, after)
        arg_struct = self.tagger.tag(filled_frame)[0].arg_structures
        for verb, pred_arg_dict in arg_struct:
            if verb == infinitive and A0 in pred_arg_dict:
                return ''.join(pred_arg_dict[A0])
        return before
