@echo off
setlocal
set cmdline=start python translator.py --prompt prompt.md --input

%cmdline% 00_about.md
%cmdline% 01_what_is.md
%cmdline% 02_overview.md
%cmdline% 03_value.md
%cmdline% 04_case_study.md
%cmdline% 05_soft_skills_development.md
%cmdline% 06_exploratory.md
%cmdline% 07_creative_thinking.md
%cmdline% 08_development_tools.md
%cmdline% 09_qwincs.md
%cmdline% 10_block_writing.md
%cmdline% 11_clear_collaboration.md
%cmdline% 12_mandalanguage.md
%cmdline% 13_naming.md
