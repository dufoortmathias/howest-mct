# Howest MCT Samenvattingen

## Hoe bijdragen?

Deze samenvattingen zijn geschreven in LaTeX (.tex bestanden) en worden gecompileerd naar .pdf bestanden. Onderstaande voorbeelden staan gecompileerd in de [how-to-contribute/](how-to-contribute/) map.

Hier een korte tutorial van LaTeX:

### Headings

```tex
% Voor een hoofdstuk:
\section{Dit is een section}

% Voor een subsection:
\subsection{Dit is een subsection}

% Voor een subsubsection
\subsubsection{Dit is een subsubsection}

Hello world
```

### Text styling

```tex
\url{https://www.example.com} % creëert een klikbare link
\underline{onderlijnde tekst}
\textit{Schuine tekst}
\textbf{Vette tekst}

% ik zet volgende lijn in het begin van elk .tex bestand: 
\newcommand{\bold}[1]{\textbf{#1}}
% om 
\bold{Vette tekst} 
% te kunnen gebruiken
```

### Lijsten

#### Ongeordend

```tex
\begin{itemize}
    \item Eerste item
    \item Tweede item
    \item Derde item
\end{itemize}
```

#### Geordend

```tex
\begin{enumerate}
    \item Eerste item
    \item Tweede item
    \item Derde item
\end{enumerate}
```

#### Lijsten kan je nesten

```tex
\begin{itemize}
    \item Eerste item
    \begin{itemize}
        \item Genest item
    \end{itemize}
    \item Tweede item
    \item Derde item
    \begin{enumerate}
        \item Genest item 1
        \item Genest item 2
        \item Genest item 3
    \end{enumerate}
\end{itemize}
```

### Afbeeldingen

```tex
\begin{figure}[H] % deze [H] is nodig om de afbeelding op de juiste plaats te zetten
    \centering % dit centreert de afbeelding horizontaal
    \includegraphics[width=0.5\textwidth]{images/test.jpg}
    % breedte afbeelding = 0.5 * breedte van het scherm
    % pad is relatief t.o.v. .tex bestand
    \caption{Dit is een caption onder de afbeelding}
\end{figure}
```

### Code

```tex
% Gebruik het minted commando met de taal tussen de {}:
\begin{minted}{python}
def function():
    for i in range(10):
        print("Huidige nummer: {}".format(i))

if __name__ == "__main__":
    function()
\end{minted}
```
