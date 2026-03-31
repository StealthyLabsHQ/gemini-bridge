#!/usr/bin/env python3
"""
gemini_bridge.py — Query Google Gemini from the command line.

Usage:
    python gemini_bridge.py "question"               # défaut : pro (deep)
    python gemini_bridge.py --tier lite "question"   # Gemini 3.1 Flash Lite Preview (light)
    python gemini_bridge.py --tier flash "question"  # Gemini 3 Flash Preview (medium)
    python gemini_bridge.py --tier pro "question"    # Gemini 3.1 Pro Preview (deep)

Tiers :
    lite   → gemini-3.1-flash-lite-preview   (léger, rapide, économique)
    flash  → gemini-3-flash-preview          (équilibré, vitesse + intelligence)
    pro    → gemini-3.1-pro-preview          (SOTA, raisonnement max)

Réglages appliqués (pro & flash) :
    temperature    = 2       (créativité/exploration maximale)
    thinking_level = high    (raisonnement profond)
    media_resolution = high  (résolution média haute)
    top_p          = 0.95
    max_output_tokens = 65536

Requires:
    pip install google-genai python-dotenv
    GEMINI_API_KEY dans .env ou variable d'environnement
"""

import sys
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

TIERS = {
    "lite":  "gemini-3.1-flash-lite-preview",
    "flash": "gemini-3-flash-preview",
    "pro":   "gemini-3.1-pro-preview",
}

# Réglages haute performance (thinking high, température élevée)
HIGH_PERF_CONFIG = {
    "temperature": 2.0,
    "top_p": 0.95,
    "max_output_tokens": 65536,
}

def build_config(genai_types, tier: str):
    cfg = dict(HIGH_PERF_CONFIG)

    # Thinking high pour flash et pro (lite ne supporte pas le thinking)
    if tier in ("flash", "pro"):
        cfg["thinking_config"] = genai_types.ThinkingConfig(
            thinking_budget=8192,   # budget élevé = thinking "High"
            include_thoughts=False, # on n'affiche que la réponse finale
        )

    # Résolution média haute
    cfg["media_resolution"] = genai_types.MediaResolution.MEDIA_RESOLUTION_HIGH

    return genai_types.GenerateContentConfig(**cfg)


def main():
    args = sys.argv[1:]

    # Parsing --tier
    tier = "pro"
    if "--tier" in args:
        idx = args.index("--tier")
        if idx + 1 >= len(args):
            print("Error: --tier nécessite une valeur : lite | flash | pro", file=sys.stderr)
            sys.exit(1)
        tier = args[idx + 1].lower()
        args = args[:idx] + args[idx + 2:]

    if tier not in TIERS:
        print(f"Error: tier inconnu '{tier}'. Choisir parmi : lite, flash, pro", file=sys.stderr)
        sys.exit(1)

    if not args:
        print(__doc__, file=sys.stderr)
        sys.exit(1)

    prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY non défini (ni dans .env, ni en variable d'environnement).", file=sys.stderr)
        sys.exit(1)

    try:
        from google import genai
        from google.genai import types as genai_types
    except ImportError:
        print("Error: google-genai non installé. Lancer : pip install google-genai", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key)
    model  = TIERS[tier]

    try:
        config   = build_config(genai_types, tier)
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=config,
        )
        sys.stdout.buffer.write(response.text.encode("utf-8"))
        sys.stdout.buffer.write(b"\n")
    except Exception as e:
        print(f"Error [{model}]: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
