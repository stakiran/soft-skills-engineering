#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

def get_title(filepath):
    with open(filepath, encoding='utf-8') as f:
        first_line = f.readline().strip()
    # Remove leading "# " if present
    if first_line.startswith('# '):
        return first_line[2:].strip()
    return first_line

def main():
    # Pattern: 00_name.md or 00_name_EN.md
    pattern = re.compile(r'^(?P<number>\d{2})_(?P<base>.+?)(?P<lang>_EN)?\.md$')
    entries = {}

    for fname in os.listdir('.'):
        m = pattern.match(fname)
        if not m:
            continue
        num = m.group('number')
        lang = 'en' if m.group('lang') else 'ja'
        title = get_title(fname)
        entries.setdefault(num, {})[lang] = (fname, title)

    # Sort by number (keys are zero-padded strings)
    sorted_nums = sorted(entries.keys())

    # Write index.md
    with open('index.md', 'w', encoding='utf-8') as out:
        # Header
        out.write('# Soft Skills Engineering\n')
        out.write('- [GitHub](https://github.com/stakiran/soft-skills-engineering)\n\n')
        out.write('## TOC\n\n')
        # Body
        for num in sorted_nums:
            out.write(f'- {num}\n')
            data = entries[num]
            # Japanese version first
            if 'ja' in data:
                fname, title = data['ja']
                out.write(f'    - [{title}]({fname})\n')
            # English version if exists
            if 'en' in data:
                fname, title = data['en']
                out.write(f'    - [{title}]({fname})\n')
        # Footer (empty)
        out.write('\n')

if __name__ == '__main__':
    main()
