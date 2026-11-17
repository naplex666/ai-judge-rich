# ai-judge-rich-01 entrypoint (Python 3.13, standard library only).
#
# The program writes one fixed plan to /output/entry.txt: the plan an AI
# agent would follow to turn $100, a computer with internet access and
# 30 days into the most money. The plan is a constant, so both grader runs
# write identical bytes. It is 989 characters, inside the 1-1000 gate. Outside the grader, MAKEFUN_OUTPUT_DIR stands in
# for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The plan was picked by judging candidate plans against the judge's own
# rubric (executable by an agent alone, most-likely day-30 money, works
# today, concrete, edge). The winner: a narrow, paid-in-advance service
# for online stores, with a free sample before payment and zero ad spend.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Plan: clean product spreadsheets for small online stores, $25 a job, paid in advance.",
        "Day 1: put up a one-page site offering to clean, merge and de-duplicate a store's product spreadsheet \u2014 fix broken SKUs, prices and variants \u2014 for $25, paid in advance through a payment link. Find buyers where they already ask for help: r/shopify, r/EtsySellers and the Shopify community forum.",
        "Days 2-7: answer every post from a store owner with a messy spreadsheet, and do their first 50 rows free as a sample before they pay. Do each paid job with code within a day.",
        "Days 8-30: ask every buyer for a review, raise the price to $35 after ten reviews, and keep a script of every fix so each next job is faster. Spend nothing on ads; drop any channel that brings no paying buyer within a week.",
        "Edge: a narrow niche with money \u2014 store owners, not anyone with a spreadsheet \u2014 a free sample that proves value before payment, and code delivery in hours. Target: 20 jobs, about $600, with the $100 untouched.",
    ]
)


def main():
    data = PLAN.encode("utf-8")
    if not 1 <= len(PLAN) <= 1000:
        raise ValueError("plan must be 1 to 1000 characters")
    if not PLAN.strip():
        raise ValueError("plan must not be only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
