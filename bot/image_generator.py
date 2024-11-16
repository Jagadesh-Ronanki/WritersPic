# bot/image_generator.py

import os, re
import subprocess
from datetime import datetime
from pdf2image import convert_from_path

def generate_latex_code(heading, content):
    """
    Generate LaTeX code for the provided heading and content.
    """
    latex_code = r"""\documentclass[11pt]{article}
    \usepackage{graphicx}
    \usepackage{xcolor}
    \usepackage{geometry}
    \usepackage{datetime}
    \usepackage{titlesec}
    \usepackage{helvet}
    \usepackage{setspace}
    \usepackage{microtype}
    \geometry{a4paper, left=0.6in, right=0.6in, top=0.8in, bottom=0.8in}
    \usepackage{soul}
    \usepackage{enumitem}

    % Color definitions
    \definecolor{backgroundcolor}{HTML}{FFEAC5}
    \definecolor{textcolor}{HTML}{603F26}
    \definecolor{headingcolor}{HTML}{603F26}
    \definecolor{customgray}{HTML}{6C4E31}

    % Set the background color
    \pagecolor{backgroundcolor}
    \color{textcolor}

    % Set letter and line spacing globally
    \setstretch{1.2}
    \SetTracking{encoding=*}{10}

    % Custom section font and format
    \titleformat{\section}
    {\color{headingcolor}\LARGE\bfseries\sffamily}
    {}
    {0em}
    {}

    % Custom font sizes and colors for different elements
    \newcommand{\heading}[1]{\section*{#1}}
    \newcommand{\subheading}[1]{\noindent\fontsize{14pt}{16pt}\textbf{\sffamily #1}\par\vspace{0.3em}}
    \newcommand{\content}[1]{\noindent\fontsize{14pt}{18pt}\selectfont\sffamily\textls[10]{#1}\par\vspace{1.3em}}
    \newcommand{\boldcontent}[1]{\textbf{\textls[10]{#1\hspace{0.2em}}}}
    \newcommand{\bullets}[1]{\begin{itemize}\color{textcolor}\sffamily #1\end{itemize}}
    \newcommand{\letterspace}[1]{\textls[60]{#1}}

    \setlist[itemize]{itemsep=0pt, topsep=1em}

    \begin{document}
    \pagestyle{empty}
    \heading{""" + heading + r"""}

    \begin{flushleft}
    \textcolor{customgray}{\textit{\sffamily\itshape \today \, by\, @thedankoe}}
    \end{flushleft}
    """

    for paragraph in content:
        lines = paragraph.splitlines()
        for line in lines:
            if line.startswith("bt["):
                latex_code += r"\boldcontent{" + line[3:-1] + r"}"
            elif line.startswith("Items["):
                items = line[6:-1].split(",")
                latex_code += r"\bullets{ "
                for item in items:
                    latex_code += r"\item " + item.strip() + r" "
                latex_code += r"}"
            elif line.startswith("st["):
                latex_code += r"\subheading{" + line[3:-1] + r"}"
            else:
                if re.search(r"bt\[(.*?)\]", line):
                    bold_matches = re.findall(r"bt\[(.*?)\]", line)
                    for match in bold_matches:
                        line = line.replace("bt[" + match + "]",
                                            r"\boldcontent{" + match + r"}")
                latex_code += r"\content{" + line + r"}"

    latex_code += r"\end{document}"
    return latex_code

def compile_latex(latex_code, heading):
    """
    Compile LaTeX code to PDF and generate images.
    """
    current_date = datetime.now().strftime("%d-%m-%Y")
    folder_name = f"[{current_date}] {heading}"

    if not os.path.exists("./" + folder_name):
        os.makedirs(folder_name)

    tex_file_path = os.path.join("./" + folder_name, f"{heading}.tex")
    pdf_file_path = os.path.join("./" + folder_name, f"{heading}.pdf")
    images_path = os.path.join("./" + folder_name + "/images")

    with open(tex_file_path, "w") as f:
        f.write(latex_code)

    result = subprocess.run(["latexmk", "-f", "-pdf", tex_file_path],
                            capture_output=True)

    if result.returncode != 0:
        print("Error during compilation:")
        print(result.stderr.decode())
    else:
        print("Compiled successfully")
        subprocess.run(["mv", f"{heading}.pdf", pdf_file_path])

    subprocess.run([
        "rm", f"{heading}.aux", f"{heading}.log", f"{heading}.fls",
        f"{heading}.fdb_latexmk"
    ], capture_output=True)

    if not os.path.exists("./" + folder_name + "/images"):
        os.makedirs(images_path)

    convert_pdf_to_images(pdf_file_path, images_path)

def convert_pdf_to_images(pdf_path, output_folder):
    """
    Convert the generated PDF to images.
    """
    pages = convert_from_path(pdf_path, dpi=300)

    for i, page in enumerate(pages):
        filename = f"page_{i+1}.jpg"
        page.save(os.path.join(output_folder, filename))
