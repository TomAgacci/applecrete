#!/usr/bin/env python3
"""
PULP-CRETE v0.4 — INTERACTIVE GUIDE FOR ~4 MPa BIOCOMPOSITE
APPLE PULP • HYDRATED LIME • SAND • PARALLEL SALT BLEND

This script walks you step-by-step through:
- Choosing batch size
- Calculating material masses
- Preparing apple pulp
- Preparing parallel salt blend
- Mixing, casting, and curing
"""

import sys
from textwrap import dedent

def ask_float(prompt, default=None):
    while True:
        txt = input(f"{prompt}" + (f" [{default}]" if default is not None else "") + ": ").strip()
        if not txt and default is not None:
            return float(default)
        try:
            return float(txt)
        except ValueError:
            print("Please enter a number.")


def banner():
    print("=" * 60)
    print(" PULP-CRETE v0.4 — ~4 MPa BIOCOMPOSITE GUIDE")
    print("=" * 60)
    print(dedent("""
        Components (by mass ratio):
          - Fine sand (0–2 mm):        4.0 parts
          - Hydrated lime:            2.0 parts
          - Apple pulp (dried):       1.0 part
          - Parallel salt blend:      0.15 parts
          - Water:                    1.5–2.0 parts (tuned to workability)

        Parallel salt blend (by mass):
          - NaCl (non-iodized):       2 parts
          - CaCl₂:                    1 part
          - NaHCO₃:                   1 part
    """))


def choose_batch():
    print("\n--- BATCH SIZE SELECTION ---")
    print("You can define the mass corresponding to '1 part'.")
    print("Example: if 1 part = 1 kg, total dry mass ≈ 7.15 kg.")
    one_part = ask_float("Enter mass for 1 part (in kg)", default=1.0)

    sand = 4.0 * one_part
    lime = 2.0 * one_part
    pulp = 1.0 * one_part
    salt_blend = 0.15 * one_part
    water_min = 1.5 * one_part
    water_max = 2.0 * one_part

    print("\n--- CALCULATED MATERIAL MASSES ---")
    print(f"Fine sand:        {sand:.3f} kg")
    print(f"Hydrated lime:    {lime:.3f} kg")
    print(f"Apple pulp (dry): {pulp:.3f} kg")
    print(f"Salt blend:       {salt_blend:.3f} kg")
    print(f"Water (start):    {water_min:.3f} kg")
    print(f"Water (max):      {water_max:.3f} kg")

    return {
        "one_part": one_part,
        "sand": sand,
        "lime": lime,
        "pulp": pulp,
        "salt_blend": salt_blend,
        "water_min": water_min,
        "water_max": water_max,
    }


def salt_breakdown(salt_blend_mass):
    print("\n--- PARALLEL SALT BLEND BREAKDOWN ---")
    print("Salt blend ratio: NaCl : CaCl₂ : NaHCO₃ = 2 : 1 : 1")

    total_parts = 2 + 1 + 1
    part_mass = salt_blend_mass / total_parts

    nacl = 2 * part_mass
    cacl2 = 1 * part_mass
    nahco3 = 1 * part_mass

    print(f"Total salt blend: {salt_blend_mass:.3f} kg")
    print(f"  NaCl:           {nacl:.3f} kg")
    print(f"  CaCl₂:          {cacl2:.3f} kg")
    print(f"  NaHCO₃:         {nahco3:.3f} kg")

    return {
        "nacl": nacl,
        "cacl2": cacl2,
        "nahco3": nahco3,
    }


def pulp_prep_instructions(pulp_mass):
    print("\n=== STEP 1 — APPLE PULP PREPARATION ===")
    print(dedent(f"""
        Target dried pulp mass: {pulp_mass:.3f} kg

        1. Collect pulp from your raw apple juice filtration (coffee filters).
        2. Remove any paper fibers or foreign material.
        3. Spread pulp in a thin layer (5–10 mm) on trays.
        4. Air-dry 12–24 hours at room temperature (fan optional, no high heat).
        5. Moisture target:
           - Feels dry on the surface.
           - No free water when squeezed firmly.
           - Still slightly flexible inside.
        6. Break into granules ~2–8 mm.
           - Avoid powder; you want discrete particles.
        7. Store in a breathable container until mixing.
    """))
    input("Press ENTER when you are ready to continue to salt blend preparation...")


def salt_prep_instructions(salt_masses):
    print("\n=== STEP 2 — PARALLEL SALT BLEND PREPARATION ===")
    print(dedent(f"""
        Target salt blend mass: {salt_masses['nacl'] + salt_masses['cacl2'] + salt_masses['nahco3']:.3f} kg

        Weigh:
          - NaCl (non-iodized): {salt_masses['nacl']:.3f} kg
          - CaCl₂:              {salt_masses['cacl2']:.3f} kg
          - NaHCO₃:             {salt_masses['nahco3']:.3f} kg

        Steps:
        1. Combine all three in a dry container.
        2. Break up any lumps.
        3. Mix until visually uniform.
        4. Keep sealed and dry until use (CaCl₂ is hygroscopic).
    """))
    input("Press ENTER when you are ready to continue to dry mixing...")


def dry_mix_instructions(batch):
    print("\n=== STEP 3 — DRY MIXING (SAND + LIME + SALT BLEND) ===")
    print(dedent(f"""
        Weigh:
          - Fine sand:        {batch['sand']:.3f} kg
          - Hydrated lime:    {batch['lime']:.3f} kg
          - Salt blend:       {batch['salt_blend']:.3f} kg

        Steps:
        1. Add sand and lime to your mixing tub or mortar mixer.
        2. Dry-mix 2–3 minutes until color is uniform.
        3. Sprinkle the salt blend evenly over the surface.
        4. Mix another 2–3 minutes.
        5. Goal: no visible pockets of lime or salt.
    """))
    input("Press ENTER when you are ready to add apple pulp...")


def add_pulp_instructions(batch):
    print("\n=== STEP 4 — ADDING APPLE PULP ===")
    print(dedent(f"""
        Target dried pulp mass: {batch['pulp']:.3f} kg

        Steps:
        1. Add the dried apple pulp granules to the dry mix.
        2. Fold and toss until all pulp particles are coated.
        3. Check a handful:
           - Pulp behaves like lightweight aggregate.
           - No large uncoated clumps.
    """))
    input("Press ENTER when you are ready to hydrate the mix...")


def hydration_instructions(batch):
    print("\n=== STEP 5 — HYDRATION & WORKABILITY ===")
    print(dedent(f"""
        Initial water target:
          - Start with: {batch['water_min']:.3f} kg
          - Do not exceed: {batch['water_max']:.3f} kg without adjusting solids.

        Steps:
        1. Add water gradually in 3–4 increments.
        2. After each addition, mix 1–2 minutes.
        3. Desired consistency:
           - Stiff, cohesive.
           - Holds shape when squeezed in a gloved hand.
           - Slight surface sheen.
           - No free water pooling at the bottom.

        If too dry and crumbly:
          - Add water in small increments (e.g., 0.1–0.2 kg).

        If too soupy:
          - Add small amounts of sand and lime (maintain 2:4 lime:sand ratio).
    """))
    input("Press ENTER when you are ready to cast into molds...")


def casting_instructions():
    print("\n=== STEP 6 — CASTING INTO MOLDS ===")
    print(dedent("""
        Recommended molds:
          - 50 mm cubes or cylinders (e.g., 50×100 mm) for compressive tests.
          - Larger blocks/panels for practical evaluation.

        Steps:
        1. Prepare molds:
           - Clean.
           - Lightly oil or apply release agent compatible with lime-based mixes.
        2. Fill molds in 2–3 lifts:
           - Place material.
           - Lightly tamp each lift to remove large voids.
           - Avoid heavy vibration or over-compaction.
        3. Strike off the top flush with mold edges.
        4. Optionally trowel smooth or leave textured.
    """))
    input("Press ENTER when you are ready to start curing...")


def curing_instructions():
    print("\n=== STEP 7 — CURING REGIME FOR ~4 MPa ===")
    print(dedent("""
        PHASE 1 — INITIAL SET (0–24 HOURS):
          - Keep molds in shaded, ventilated area.
          - Cover loosely (plastic sheet or damp cloth) to prevent rapid drying.
          - Avoid direct sun and strong wind.

        PHASE 2 — EARLY CURE (DAY 1–7):
          - Demold after 24–48 hours if firm.
          - Place specimens on racks with airflow.
          - Maintain moderate humidity:
            - Nearby water trays or light misting of surrounding air.
          - Do NOT soak the specimens.

        PHASE 3 — MAIN CURE (DAY 7–28):
          - Store in dry, ventilated environment.
          - Avoid immersion or heavy wetting.
          - Lime binder needs CO₂ from air for carbonation.

        Notes:
          - Temperature 18–25 °C and RH 40–70% are ideal.
          - Very low humidity or high temperature can cause cracking and lower strength.
    """))
    input("Press ENTER to see testing and adjustment guidelines...")


def testing_instructions():
    print("\n=== STEP 8 — TESTING & ADJUSTMENT TOWARD 4 MPa ===")
    print(dedent("""
        TESTING:
          - At 7 days:
            - Perform preliminary compressive tests (expect <4 MPa).
          - At 28 days:
            - Perform main compressive tests.
            - Record:
              - Failure load.
              - Failure mode (brittle, shear, etc.).
              - Density (mass/volume).

        ADJUSTMENT RULES:
          If strength <4 MPa:
            - Increase mineral fraction:
              - Sand: 4.5 parts
              - Pulp: 0.8 parts
              - Lime: 2.0 parts
            - Keep salt blend at 0.15 parts.

          If mix is too brittle:
            - Increase pulp slightly:
              - Pulp: 1.2 parts
              - Sand: 3.8 parts
            - Keep lime at 2.0 parts.

          If excessive salt efflorescence:
            - Reduce salt blend to 0.10 parts.
    """))
    print("\n=== SAFETY REMINDER ===")
    print(dedent("""
        - Wear gloves, mask, and eye protection.
        - Avoid inhaling dust from lime, sand, and salts.
        - Wash skin after contact with wet lime mixes (alkaline).
        - Do NOT use this material for load-bearing structural elements
          without proper engineering validation.
    """))
    print("\nGuide complete. You now have a full interactive walkthrough for pulp-crete v0.4.\n")


def main():
    banner()
    batch = choose_batch()
    salt_masses = salt_breakdown(batch["salt_blend"])
    pulp_prep_instructions(batch["pulp"])
    salt_prep_instructions(salt_masses)
    dry_mix_instructions(batch)
    add_pulp_instructions(batch)
    hydration_instructions(batch)
    casting_instructions()
    curing_instructions()
    testing_instructions()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        sys.exit(0)
