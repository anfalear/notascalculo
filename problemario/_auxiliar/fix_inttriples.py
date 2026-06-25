content = open('inttriples.tex', 'r', encoding='utf-8') .read()

n_before = content.count('\\end{example}\n\n\\begin{myproof}')
print(f"Orphaned myproof patterns found: {n_before}")

# Fix structural bug: move \end{example} to after \end{myproof}
content = content.replace('\\end{example}\n\n\\begin{myproof}', '\\begin{myproof}')

# Add \end{example} after each example myproof
# (prob myproofs follow immediately with \end{prob}, no blank line — safe to use \n\n)
content = content.replace('\\end{myproof}\n\n', '\\end{myproof}\n\\end{example}\n\n')

open('inttriples.tex', 'w', encoding='utf-8').write(content)
print(f"Fixed {n_before} structural bugs")
print(f"\\\\begin{{example}}: {content.count(chr(92)+'begin{example}')}")
print(f"\\\\end{{example}}:   {content.count(chr(92)+'end{example}')}")
print(f"\\\\begin{{myproof}}: {content.count(chr(92)+'begin{myproof}')}")
