#!/usr/bin/env python3
"""
RAW APPLE JUICE — NO HEAT, NO WATER
Interactive step-by-step guide for making cold-processed apple juice.

Equipment:
- Blender
- Coffee filters (paper)
- Bowl, jar, or funnel
- Clean apples (any variety)
"""

import sys
from textwrap import dedent

def pause():
    input("\nPress ENTER to continue...\n")

def banner():
    print("=" * 60)
    print(" RAW APPLE JUICE — NO HEAT, NO WATER (INTERACTIVE GUIDE) ")
    print("=" * 60)
    print(dedent("""
        This script will walk you through the entire process of making
        cold-processed apple juice using only:
          • Apples
          • Blender
          • Coffee filters
          • Bowl / jar / funnel

        No heat. No added water. Just pure apple extraction.
    """))

def step1():
    print("\nSTEP 1 — WASH APPLES")
    print(dedent("""
        1. Wash apples thoroughly under cold water.
        2. Remove stems and any damaged or bruised spots.
    """))
    pause()

def step2():
    print("\nSTEP 2 — CUT APPLES")
    print(dedent("""
        1. Cut apples into medium-sized chunks.
        2. Remove seeds if desired (optional).
    """))
    pause()

def step3():
    print("\nSTEP 3 — BLEND (NO WATER)")
    print(dedent("""
        1. Load apple chunks into the blender.
        2. DO NOT add water.
        3. Blend on high until the mixture becomes a smooth apple puree.
    """))
    pause()

def step4():
    print("\nSTEP 4 — SET UP FILTER")
    print(dedent("""
        1. Place a coffee filter inside a funnel OR over a jar/bowl.
        2. Make sure the filter is stable and won’t collapse.
    """))
    pause()

def step5():
    print("\nSTEP 5 — POUR PUREE INTO FILTER")
    print(dedent("""
        1. Slowly pour the apple puree into the coffee filter.
        2. Let gravity do the work — do NOT squeeze the filter.
           Squeezing forces pulp through and clouds the juice.
    """))
    pause()

def step6():
    print("\nSTEP 6 — WAIT FOR DRIP-THROUGH")
    print(dedent("""
        1. Allow 10–30 minutes for the juice to drip through naturally.
        2. If you want clearer juice:
           - Run the liquid through a second coffee filter.
    """))
    pause()

def step7():
    print("\nSTEP 7 — REFRIGERATE")
    print(dedent("""
        1. Transfer the finished juice to a clean container.
        2. Refrigerate immediately.
        3. Consume within 24–48 hours for best flavor.
    """))
    pause()

def final_output():
    print("\n=== OUTPUT ===")
    print(dedent("""
        You now have:
          • Cold-processed raw apple juice
          • Crisp, bright flavor
          • Naturally cloudy unless double-filtered

        Enjoy your fresh, no-heat apple juice!
    """))

def main():
    banner()
    step1()
    step2()
    step3()
    step4()
    step5()
    step6()
    step7()
    final_output()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting.")
        sys.exit(0)
