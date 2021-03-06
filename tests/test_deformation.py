#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import librosa
from amen.audio import Audio
from amen.utils import example_audio_file
from amen.deformation import harmonic_separation
from amen.deformation import percussive_separation

EXAMPLE_FILE = example_audio_file()
audio = Audio(EXAMPLE_FILE)
mono_audio = Audio(EXAMPLE_FILE, convert_to_mono=True, sample_rate=44100)

def test_harmonic():
    harmonic_audio = harmonic_separation(mono_audio)
    test_harmonic = librosa.effects.harmonic(librosa.to_mono(mono_audio.raw_samples), margin=3.0)
    test_harmonic_audio = Audio(raw_samples=test_harmonic, sample_rate=mono_audio.sample_rate)
    assert np.allclose(harmonic_audio.raw_samples, test_harmonic_audio.raw_samples, rtol=1e-3, atol=1e-4)

def test_percussive():
    percussive_audio = percussive_separation(mono_audio)
    test_percussive = librosa.effects.percussive(librosa.to_mono(mono_audio.raw_samples), margin=3.0)
    test_percussive_audio = Audio(raw_samples=test_percussive, sample_rate=mono_audio.sample_rate)
    assert np.allclose(percussive_audio.raw_samples, test_percussive_audio.raw_samples, rtol=1e-3, atol=1e-4)
