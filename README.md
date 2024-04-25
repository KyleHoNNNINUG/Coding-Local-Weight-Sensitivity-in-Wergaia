# Coding Local Weight-Sensitivity in Wergaia
## Function
This code takes a Wergaia word without any marks as input and prints the word with correct stress markings.

Stress notations precede the stressed syllable.

_ˈ_ denotes primary stress; _ˌ_ denotes secondary stress.

## Background
Wergaia is an Aboriginal Australian language, which has the stressing pattern that
 * stresses on odd-indexed syllables,
 * unstresses the final syllable (even if it is odd-indexed) if it does not have a _coda_, and
 * has the first/leftmost stress as _primary stress_ and the rest as _secondary stress_.

A syllable is defined as
1. Onset: consonant
2. Nucleus: vowel(s)
3. Coda: consonant

together in order, where the priority of presence is nucleus > onset > coda.
For example, _delguna_ broken down would be _del-gu-na_.

## Output
Continuing with _delguna_ again for the code, it would print _ˈdelguna_ since
 * _del_ is the first syllable which receives primary stress;
 * _na_ is an odd-indexed but final syllable without a coda that is thus unstressed.

More example data is provided in _Stress.pdf_.

## Publication
The code is published in Volume 12 Issue 4 (2023) of the Journal of Student Research - High School Edition. However, there are incorrect pieces of information on the published version, which is requested to (2024/3/31) but still not resolved up to this update (2024/4/25). Therefore, the file and link is not provided here yet.
