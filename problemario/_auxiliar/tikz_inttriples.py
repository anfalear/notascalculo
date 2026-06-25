# -*- coding: utf-8 -*-
with open('inttriples.tex', 'r', encoding='utf-8') as f:
    content = f.read()

results = []

def R(content, old, new, label):
    if old in content:
        results.append(f'OK  {label}')
        return content.replace(old, new, 1)
    else:
        results.append(f'MISS {label}')
        return content

# ================================================================
# FIGURE 1: Circle r=2sinθ (center (0,1), r=1) — L.480-484
# ================================================================
OLD1 = r"""\psset{xunit=1.0cm,yunit=1.0cm,algebraic=true,dimen=middle,dotstyle=o,dotsize=5pt 0,linewidth=1.6pt,arrowsize=3pt 2,arrowinset=0.25}
\begin{pspicture*}(-1.8946903563440303,-1.2649627211224348)(2.3108673063338365,3.0019899439302904)
\psaxes[labelFontSize=\scriptstyle,xAxis=true,yAxis=true,Dx=1.,Dy=1.,ticksize=-2pt 0,subticks=2]{->}(0,0)(-1.8946903563440303,-1.2649627211224348)(2.3108673063338365,3.0019899439302904)
\pscircle[linewidth=2.pt,hatchcolor=black,fillstyle=dots*,hatchangle=45.0,hatchsep=0.15348750593714833](0.,1.){1.}
\end{pspicture}"""

NEW1 = r"""\begin{tikzpicture}[scale=0.9]
  \draw[->] (-2,0) -- (2.5,0) node[right] {$x$};
  \draw[->] (0,-1.3) -- (0,3.1) node[above] {$y$};
  \fill[gray!25] (0,1) circle (1);
  \draw[thick] (0,1) circle (1);
  \foreach \x in {-1,1} \draw (\x,2pt) -- (\x,-2pt) node[below] {\small$\x$};
  \foreach \y in {1,2} \draw (2pt,\y) -- (-2pt,\y) node[left] {\small$\y$};
\end{tikzpicture}"""

content = R(content, OLD1, NEW1, 'Fig1 circle r=2sinθ')

# ================================================================
# FIGURE 2: Two arcs (r=3) + two lines — L.506-525
# ================================================================
OLD2 = r"""\newrgbcolor{qqzzqq}{0. 0.6 0.}
\newrgbcolor{ttqqqq}{0.2 0. 0.}
\psset{xunit=1.0cm,yunit=1.0cm,algebraic=true,dimen=middle,dotstyle=o,dotsize=5pt 0,linewidth=1.6pt,arrowsize=3pt 2,arrowinset=0.25}
\begin{pspicture*}(-1.74,-2.38)(7.9,4.82)
\psaxes[labelFontSize=\scriptstyle,xAxis=true,yAxis=true,Dx=1.,Dy=1.,ticksize=-2pt 0,subticks=2]{->}(0,0)(-1.74,-2.38)(7.9,4.82)
\rput[tl](0.1,1.7){$\red{x^{2} + y^{2} = 9}$}
\rput[tl](-0.48,3.76){$\blue{(x - 3)^{2} + y^{2} = 9}$}
\rput[tl](4.14,2.62){$\qqzzqq{y = - x + 6}$}
\parametricplot[linewidth=2.pt,linecolor=red]{0.0}{1.0471975511965979}{1.*3.*cos(t)+0.*3.*sin(t)+0.|0.*3.*cos(t)+1.*3.*sin(t)+0.}
\parametricplot[linewidth=2.pt,linecolor=blue]{1.5707963267948966}{2.0943951023931957}{1.*3.*cos(t)+0.*3.*sin(t)+3.|0.*3.*cos(t)+1.*3.*sin(t)+0.}
\psline[linewidth=2.pt,linecolor=ttqqqq](3.,0.)(6.,0.)
\psline[linewidth=2.pt,linecolor=qqzzqq](6.,0.)(3.,3.)
\rput[tl](4.04,-0.45){$y=0$}
\begin{scriptsize}
\psdots[dotsize=4pt 0,dotstyle=*,linecolor=red](3.,0.)
\psdots[dotsize=4pt 0,dotstyle=*,linecolor=red](1.5,2.598076211353316)
\psdots[dotsize=4pt 0,dotstyle=*,linecolor=red](3.,3.)
\psdots[dotsize=4pt 0,dotstyle=*,linecolor=red](6.,0.)
\end{scriptsize}
\end{pspicture*}"""

NEW2 = r"""\begin{tikzpicture}[scale=0.7]
  \draw[->] (-2,0) -- (8,0) node[right] {$x$};
  \draw[->] (0,-2.4) -- (0,5) node[above] {$y$};
  \draw[thick, red] (3,0) arc[start angle=0, end angle=60, radius=3];
  \draw[thick, blue] (3,3) arc[start angle=90, end angle=120, radius=3];
  \draw[thick, red!40!black] (3,0) -- (6,0);
  \draw[thick, green!60!black] (6,0) -- (3,3);
  \node[red, right, font=\small] at (0.4,1.7) {$x^2{+}y^2{=}9$};
  \node[blue, above, font=\small] at (0.3,4.2) {$(x{-}3)^2{+}y^2{=}9$};
  \node[green!60!black, right, font=\small] at (4.2,2.6) {$y{=}{-}x{+}6$};
  \node[below, font=\small] at (4.5,0) {$y{=}0$};
  \fill[red] (3,0) circle (3pt);
  \fill[red] (1.5,2.598) circle (3pt);
  \fill[red] (3,3) circle (3pt);
  \fill[red] (6,0) circle (3pt);
  \foreach \x in {2,4,6} \draw (\x,2pt) -- (\x,-2pt) node[below] {\tiny$\x$};
  \foreach \y in {2,4} \draw (2pt,\y) -- (-2pt,\y) node[left] {\tiny$\y$};
\end{tikzpicture}"""

content = R(content, OLD2, NEW2, 'Fig2 arcs r=3')

# ================================================================
# FIGURE 3: Two arcs (r=5) + two lines — L.535-554
# ================================================================
OLD3 = r"""\newrgbcolor{qqzzqq}{0. 0.6 0.}
\newrgbcolor{ttqqqq}{0.2 0. 0.}
\psset{xunit=.75cm,yunit=.75cm,algebraic=true,dimen=middle,dotstyle=o,dotsize=5pt 0,linewidth=1.6pt,arrowsize=3pt 2,arrowinset=0.25}
\begin{pspicture*}(-0.7647503187928759,-1.768843956453707)(11.60382506969471,6.804083958318099)
\psaxes[labelFontSize=\scriptstyle,xAxis=true,yAxis=true,Dx=2.,Dy=2.,ticksize=-2pt 0,subticks=2]{->}(0,0)(-0.7647503187928759,-1.768843956453707)(11.60382506969471,6.804083958318099)
\rput[tl](1.0240030883605316,1.830476923793998){$\red{x^{2} + y^{2} = 25}$}
\rput[tl](0.1950685826065135,5.647938463450655){$\blue{(x - 5)^{2} + y^{2} = 25}$}
\rput[tl](7.808177595978942,3.31383340777487){$\qqzzqq{y = - x + 10}$}
\parametricplot[linewidth=2.pt,linecolor=red]{0.0}{1.0471975511965979}{1.*5.*cos(t)+0.*5.*sin(t)+0.|0.*5.*cos(t)+1.*5.*sin(t)+0.}
\psline[linewidth=2.pt,linecolor=ttqqqq](5.,0.)(10.,0.)
\psline[linewidth=2.pt,linecolor=qqzzqq](10.,0.)(5.,5.)
\rput[tl](7.4155244090428285,-0.329115604354625){$y=0$}
\parametricplot[linewidth=2.pt,linecolor=blue]{1.5707963267948966}{2.0943951023931957}{1.*5.*cos(t)+0.*5.*sin(t)+5.|0.*5.*cos(t)+1.*5.*sin(t)+0.}
\begin{scriptsize}
\psdots[dotsize=4pt 0,dotstyle=*,linecolor=red](5.,0.)
\psdots[dotsize=4pt 0,dotstyle=*,linecolor=red](2.5,4.330127018922194)
\psdots[dotsize=4pt 0,dotstyle=*,linecolor=red](10.,0.)
\psdots[dotsize=4pt 0,dotstyle=*,linecolor=darkgray](5.,5.)
\end{scriptsize}
\end{pspicture*}"""

NEW3 = r"""\begin{tikzpicture}[scale=0.42]
  \draw[->] (-1,0) -- (12,0) node[right] {$x$};
  \draw[->] (0,-1.8) -- (0,7) node[above] {$y$};
  \draw[thick, red] (5,0) arc[start angle=0, end angle=60, radius=5];
  \draw[thick, blue] (5,5) arc[start angle=90, end angle=120, radius=5];
  \draw[thick, red!40!black] (5,0) -- (10,0);
  \draw[thick, green!60!black] (10,0) -- (5,5);
  \node[red, right, font=\small] at (0.5,3.2) {$x^2{+}y^2{=}25$};
  \node[blue, above, font=\small] at (0.2,5.5) {$(x{-}5)^2{+}y^2{=}25$};
  \node[green!60!black, right, font=\small] at (7.5,3.2) {$y{=}{-}x{+}10$};
  \node[below, font=\small] at (7.5,0) {$y{=}0$};
  \fill[red] (5,0) circle (4pt);
  \fill[red] (2.5,4.33) circle (4pt);
  \fill[red] (10,0) circle (4pt);
  \fill[darkgray] (5,5) circle (4pt);
  \foreach \x in {2,4,6,8,10} \draw (\x,2pt) -- (\x,-2pt) node[below] {\tiny$\x$};
  \foreach \y in {2,4,6} \draw (2pt,\y) -- (-2pt,\y) node[left] {\tiny$\y$};
\end{tikzpicture}"""

content = R(content, OLD3, NEW3, 'Fig3 arcs r=5')

# ================================================================
# FIGURE 4: Rectangle [0,4]x[0,3] dotted fill — L.706-720
# ================================================================
OLD4 = r"""\psset{xunit=1.0cm,yunit=1.0cm,algebraic=true,dimen=middle,dotstyle=o,dotsize=5pt 0,linewidth=1.6pt,arrowsize=3pt 2,arrowinset=0.25}
\begin{pspicture*}(-1.88,-2.58)(5.94,4.32)
\psaxes[labelFontSize=\scriptstyle,xAxis=true,yAxis=true,Dx=1.,Dy=1.,ticksize=-2pt 0,subticks=2]{->}(0,0)(-1.88,-2.58)(5.94,4.32)
\pspolygon[linewidth=2.pt,linestyle=dashed,dash=1pt 1pt,hatchcolor=black,fillstyle=dots*,hatchangle=45.0,hatchsep=0.2](0.,0.)(0.,3.)(4.,3.)(4.,0.)
\psline[linewidth=2.pt](0.,0.)(0.,3.)
\psline[linewidth=2.pt](0.,3.)(4.,3.)
\psline[linewidth=2.pt](4.,3.)(4.,0.)
\psline[linewidth=2.pt](4.,0.)(0.,0.)
\begin{scriptsize}
\psdots[dotstyle=*](4.,0.)
\psdots[dotstyle=*](0.,3.)
\psdots[dotstyle=*](4.,3.)
\psdots[dotsize=4pt 0,dotstyle=*](0.,0.)
\end{scriptsize}
\end{pspicture}"""

NEW4 = r"""\begin{tikzpicture}[scale=0.8]
  \draw[->] (-1.9,0) -- (6,0) node[right] {$x$};
  \draw[->] (0,-2.6) -- (0,4.4) node[above] {$y$};
  \fill[gray!20] (0,0) rectangle (4,3);
  \draw[thick, dashed] (0,0) rectangle (4,3);
  \fill (4,0) circle (2.5pt); \fill (0,3) circle (2.5pt);
  \fill (4,3) circle (2.5pt); \fill (0,0) circle (2.5pt);
  \foreach \x in {1,2,3,4} \draw (\x,2pt) -- (\x,-2pt) node[below] {\small$\x$};
  \foreach \y in {1,2,3} \draw (2pt,\y) -- (-2pt,\y) node[left] {\small$\y$};
\end{tikzpicture}"""

content = R(content, OLD4, NEW4, 'Fig4 rectangle 4x3')

# ================================================================
# FIGURE 5: Area under y=e^x from 0 to 1 — L.735-743
# ================================================================
OLD5 = r"""\psset{xunit=1.0cm,yunit=1.0cm,algebraic=true,dimen=middle,dotstyle=o,dotsize=5pt 0,linewidth=1.6pt,arrowsize=3pt 2,arrowinset=0.25}
\begin{pspicture*}(-1.5,-1.66)(4.36,4.3)
\psaxes[labelFontSize=\scriptstyle,xAxis=true,yAxis=true,Dx=1.,Dy=1.,ticksize=-2pt 0,subticks=2]{->}(0,0)(-1.5,-1.66)(4.36,4.3)
\pscustom[linewidth=0.8pt,hatchcolor=black,fillstyle=hlines,hatchangle=25.0,hatchsep=0.2]{\psplot{0.}{1.}{0.0}\lineto(1.,2.718281828459045)\psplot{1.}{0.}{2.718281828459045^(x)}\lineto(0.,0.)\closepath}
\rput[tl](1.26,3.1){$\left(1, e \right)$}
\begin{scriptsize}
\psdots[dotsize=4pt 0,dotstyle=*,linecolor=darkgray](1.,2.718281828459045)
\end{scriptsize}
\end{pspicture*}"""

NEW5 = r"""\begin{tikzpicture}[scale=0.9]
  \fill[gray!20] (0,0) -- plot[domain=0:1, samples=50] (\x,{exp(\x)}) -- (1,0) -- cycle;
  \draw[thick] plot[domain=-0.2:1.6, samples=60] (\x,{exp(\x)});
  \draw[->] (-1.5,0) -- (4.5,0) node[right] {$x$};
  \draw[->] (0,-1.7) -- (0,4.4) node[above] {$y$};
  \fill[darkgray] (1,{exp(1)}) circle (2.5pt);
  \node[right, font=\small] at (1.1,{exp(1)}) {$(1,e)$};
  \draw (1,2pt) -- (1,-2pt) node[below] {\small$1$};
  \foreach \y in {1,2,3} \draw (2pt,\y) -- (-2pt,\y) node[left] {\small$\y$};
\end{tikzpicture}"""

content = R(content, OLD5, NEW5, 'Fig5 area under e^x')

# ================================================================
# FIGURE 6: Rectangle bxh with labels — L.781-791
# ================================================================
OLD6 = r"""\psset{xunit=1.0cm,yunit=1.0cm,algebraic=true,dimen=middle,dotstyle=o,dotsize=5pt 0,linewidth=1.6pt,arrowsize=3pt 2,arrowinset=0.25}
\begin{pspicture*}(-1.26,-1.7)(6.24,4.52)
\psaxes[labelFontSize=\scriptstyle,xAxis=true,yAxis=true,labels=none,Dx=1.,Dy=1.,ticksize=-2pt 0,subticks=2]{->}(0,0)(-1.26,-1.7)(6.24,4.52)
\pspolygon[linewidth=2.pt,hatchcolor=black,fillstyle=hlines,hatchangle=45.0,hatchsep=0.2](0.,0.)(4.,0.)(4.,3.)(0.,3.)
\psline[linewidth=2.pt](0.,0.)(4.,0.)
\psline[linewidth=2.pt](4.,0.)(4.,3.)
\psline[linewidth=2.pt](4.,3.)(0.,3.)
\psline[linewidth=2.pt](0.,3.)(0.,0.)
\rput[bl](4,-0.5){$b$}
\rput[bl](4.32,3){$h$}
\end{pspicture}"""

NEW6 = r"""\begin{tikzpicture}[scale=0.8]
  \draw[->] (-1.3,0) -- (6.3,0) node[right] {$x$};
  \draw[->] (0,-1.7) -- (0,4.6) node[above] {$y$};
  \fill[gray!20] (0,0) rectangle (4,3);
  \draw[thick] (0,0) rectangle (4,3);
  \node[below, font=\small] at (4,-0.5) {$b$};
  \node[right, font=\small] at (4.3,3) {$h$};
\end{tikzpicture}"""

content = R(content, OLD6, NEW6, 'Fig6 rectangle bxh')

# ================================================================
# FIGURE 7: Two regions — parabola+line pairs — L.894-911
# Left:  y=-x²-4x-1, y=x+5   (x∈[-2,0])
# Right: y=5x²-10x+5, y=x-1  (x∈[0,1])
# ================================================================
OLD7 = r"""\psset{xunit=1.0cm,yunit=1.0cm,algebraic=true,dimen=middle,dotstyle=o,dotsize=5pt 0,linewidth=1.6pt,arrowsize=3pt 2,arrowinset=0.25}
\begin{pspicture*}(-5,-2.)(4.18,5.72)
\multips(0,-2)(0,1.0){8}{\psline[linestyle=dashed,linecap=1,dash=1.5pt 1.5pt,linewidth=0.4pt,linecolor=lightgray]{c-c}(-3.72,0)(4.18,0)}
\multips(-3,0)(1.0,0){8}{\psline[linestyle=dashed,linecap=1,dash=1.5pt 1.5pt,linewidth=0.4pt,linecolor=lightgray]{c-c}(0,-2.)(0,5.72)}
\psaxes[labelFontSize=\scriptstyle,xAxis=true,yAxis=true,Dx=1.,Dy=1.,ticksize=-2pt 0,subticks=2]{->}(0,0)(-3.72,-2.)(4.18,5.72)
\pscustom[linewidth=0.8pt, linecolor=red]{\psplot{-2.}{0.}{-x^(2.0)-4.0*x-1.0}\lineto(0.,5.)\psplot{0.}{-2.}{x+5.0}\lineto(-2.,3.)\closepath}
\pscustom[linewidth=0.8pt, linecolor=red]{\psplot{0.}{1.}{x-1.0}\lineto(1.,0.)\psplot{1.}{0.}{5.0*x^(2.0)-10.0*x+5.0}\lineto(0.,-1.)\closepath}
\rput[tl](-4.5,1.62){$y= -x^{2} - 4x - 1$}
\rput[tl](0.46,3.){$y= 5 x^{2} - 10 x + 5$}
\rput[tl](-2.72,4.82){$y =  x + 5$}
\rput[tl](0.36,-0.44){$y =  x - 1$}
\begin{scriptsize}
\psdots[dotsize=4pt 0,dotstyle=*](0.,5.)
\psdots[dotsize=4pt 0,dotstyle=*](1.,0.)
\psdots[dotstyle=*](-2.,3.)
\psdots[dotstyle=*](0.,-1.)
\end{scriptsize}
\end{pspicture*}"""

NEW7 = r"""\begin{tikzpicture}[scale=0.8]
  \draw[->] (-5,0) -- (4.3,0) node[right] {$x$};
  \draw[->] (0,-2) -- (0,5.9) node[above] {$y$};
  \foreach \gx in {-4,-3,-2,-1,1,2,3,4} \draw[lightgray, dashed, thin] (\gx,-2) -- (\gx,5.9);
  \foreach \gy in {-1,1,2,3,4,5} \draw[lightgray, dashed, thin] (-5,\gy) -- (4.3,\gy);
  \fill[red!20]
    plot[domain=-2:0, samples=30] (\x,{-\x*\x-4*\x-1})
    -- (0,5)
    -- plot[domain=0:-2, samples=30] (\x,{\x+5})
    -- cycle;
  \fill[red!20]
    plot[domain=0:1, samples=20] (\x,{\x-1})
    -- plot[domain=1:0, samples=20] (\x,{5*\x*\x-10*\x+5})
    -- (0,-1)
    -- cycle;
  \draw[thick, red] plot[domain=-3.5:0.5, samples=80] (\x,{-\x*\x-4*\x-1});
  \draw[thick, red] plot[domain=-3:1, samples=60] (\x,{\x+5});
  \draw[thick, red] plot[domain=-0.1:1.5, samples=60] (\x,{5*\x*\x-10*\x+5});
  \draw[thick, red] plot[domain=-0.5:1.5, samples=40] (\x,{\x-1});
  \node[left, font=\tiny] at (-4.5,1.7) {$y{=}{-}x^2{-}4x{-}1$};
  \node[right, font=\tiny] at (0.3,4.5) {$y{=}5x^2{-}10x{+}5$};
  \node[above, font=\tiny] at (-2.5,3.8) {$y{=}x{+}5$};
  \node[below, font=\tiny] at (0.8,-0.5) {$y{=}x{-}1$};
  \foreach \x in {-4,-3,-2,-1,1,2,3} \draw (\x,2pt) -- (\x,-2pt) node[below, font=\tiny] {$\x$};
  \foreach \y in {-1,1,2,3,4,5} \draw (2pt,\y) -- (-2pt,\y) node[left, font=\tiny] {$\y$};
  \fill (0,5) circle (2.5pt); \fill (1,0) circle (2.5pt);
  \fill (-2,3) circle (2.5pt); \fill (0,-1) circle (2.5pt);
\end{tikzpicture}"""

content = R(content, OLD7, NEW7, 'Fig7 two regions par+line')

# ================================================================
# FIGURE 8: Two regions — L.921-939
# Left:  y=-(x+3)²+1, y=x+4   (x∈[-3,0])
# Right: y=(x-2)², y=4x-8      (x∈[0,2])
# ================================================================
OLD8 = r"""\newrgbcolor{ccqqqq}{0.8 0. 0.}
\psset{xunit=1.0cm,yunit=1.0cm,algebraic=true,dimen=middle,dotstyle=o,dotsize=5pt 0,linewidth=1.6pt,arrowsize=3pt 2,arrowinset=0.25}
\begin{pspicture*}(-6.369882993197273,-9.280107693158559)(6.342466279519943,5.598471500470104)
\multips(0,-9)(0,2.0){8}{\psline[linestyle=dashed,linecap=1,dash=1.5pt 1.5pt,linewidth=0.4pt,linecolor=lightgray]{c-c}(-6.369882993197273,0)(6.342466279519943,0)}
\multips(-6,0)(2.0,0){7}{\psline[linestyle=dashed,linecap=1,dash=1.5pt 1.5pt,linewidth=0.4pt,linecolor=lightgray]{c-c}(0,-9.280107693158559)(0,5.598471500470104)}
\psaxes[labelFontSize=\scriptstyle,xAxis=true,yAxis=true,Dx=2.,Dy=2.,ticksize=-2pt 0,subticks=2]{->}(0,0)(-6.369882993197273,-9.280107693158559)(6.342466279519943,5.598471500470104)
\pscustom[linewidth=0.8pt,linecolor=ccqqqq]{\psplot{-3.}{0.}{-(x+3.0)^(2.0)+1.0}\lineto(0.,4.)\psplot{0.}{-3.}{4.0+x}\lineto(-3.,1.)\closepath}
\pscustom[linewidth=0.8pt,linecolor=ccqqqq]{\psplot{0.}{2.}{-8.0+4.0*x}\lineto(2.,0.)\psplot{2.}{0.}{(x-2.0)^(2.0)}\lineto(0.,-8.)\closepath}
\rput[tl](-4.716707527238532,3.6602657817598563){$\ccqqqq{-x + y = 4}$}
\rput[tl](1.4114429069188705,-2.5533937282229946){$\ccqqqq{-4x + y = -8}$}
\rput[tl](1.2119217299928156,2.57715082130413){$\ccqqqq{\left(x - 2 \right)^{2}}$}
\rput[tl](-5.543295260217903,-1.840818096344227){$\ccqqqq{-\left(x + 3 \right)^{2} + 1}$}
\begin{scriptsize}
\psdots[dotstyle=*,linecolor=ccqqqq](-3.,1.)
\psdots[dotstyle=*,linecolor=ccqqqq](0.,4.)
\psdots[dotsize=4pt 0,dotstyle=*,linecolor=ccqqqq](0.,-8.)
\psdots[dotstyle=*,linecolor=ccqqqq](2.,0.)
\end{scriptsize}
\end{pspicture*}"""

NEW8 = r"""\begin{tikzpicture}[scale=0.55]
  \draw[->] (-6.4,0) -- (6.4,0) node[right] {$x$};
  \draw[->] (0,-9.3) -- (0,5.7) node[above] {$y$};
  \foreach \gx in {-6,-4,-2,2,4,6} \draw[lightgray, dashed, thin] (\gx,-9.3) -- (\gx,5.7);
  \foreach \gy in {-8,-6,-4,-2,2,4} \draw[lightgray, dashed, thin] (-6.4,\gy) -- (6.4,\gy);
  \fill[red!20]
    plot[domain=-3:0, samples=30] (\x,{-(\x+3)*(\x+3)+1})
    -- (0,4)
    -- plot[domain=0:-3, samples=30] (\x,{\x+4})
    -- cycle;
  \fill[red!20]
    plot[domain=0:2, samples=20] (\x,{4*\x-8})
    -- plot[domain=2:0, samples=20] (\x,{(\x-2)*(\x-2)})
    -- (0,-8)
    -- cycle;
  \draw[thick, red] plot[domain=-4.5:0.2, samples=60] (\x,{-(\x+3)*(\x+3)+1});
  \draw[thick, red] plot[domain=-4:1, samples=60] (\x,{\x+4});
  \draw[thick, red] plot[domain=-0.5:2.5, samples=40] (\x,{(\x-2)*(\x-2)});
  \draw[thick, red] plot[domain=-0.3:3.5, samples=40] (\x,{4*\x-8});
  \node[left, font=\tiny] at (-4.7,-1.5) {$y{=}{-}(x{+}3)^2{+}1$};
  \node[right, font=\tiny] at (-3.5,3.7) {$y{=}x{+}4$};
  \node[right, font=\tiny] at (1.2,2.5) {$y{=}(x{-}2)^2$};
  \node[right, font=\tiny] at (1.2,-3) {$y{=}4x{-}8$};
  \foreach \x in {-6,-4,-2,2,4,6} \draw (\x,2pt) -- (\x,-2pt) node[below, font=\tiny] {$\x$};
  \foreach \y in {-8,-6,-4,-2,2,4} \draw (2pt,\y) -- (-2pt,\y) node[left, font=\tiny] {$\y$};
  \fill[red] (-3,1) circle (3pt); \fill[red] (0,4) circle (3pt);
  \fill[red] (0,-8) circle (3pt); \fill[red] (2,0) circle (3pt);
\end{tikzpicture}"""

content = R(content, OLD8, NEW8, 'Fig8 two regions par+line (large)')

# ================================================================
# FIGURE 9: Two regions — L.948-966
# Left:  y=2(x+2)², y=-4-2x   (x∈[-2,0])
# Right: y=-(x-2)², y=-4x+8   (x∈[0,2])
# ================================================================
OLD9 = r"""\newrgbcolor{ccqqqq}{0.8 0. 0.}
\psset{xunit=1.0cm,yunit=1.0cm,algebraic=true,dimen=middle,dotstyle=o,dotsize=5pt 0,linewidth=1.6pt,arrowsize=3pt 2,arrowinset=0.25}
\begin{pspicture*}(-5.630768994361358,-4.610292739805597)(4.7720311331921845,8.688525005674933)
\multips(0,-4)(0,2.0){7}{\psline[linestyle=dashed,linecap=1,dash=1.5pt 1.5pt,linewidth=0.4pt,linecolor=lightgray]{c-c}(-5.630768994361358,0)(4.7720311331921845,0)}
\multips(-5,0)(2.0,0){6}{\psline[linestyle=dashed,linecap=1,dash=1.5pt 1.5pt,linewidth=0.4pt,linecolor=lightgray]{c-c}(0,-4.610292739805597)(0,8.688525005674933)}
\psaxes[labelFontSize=\scriptstyle,xAxis=true,yAxis=true,Dx=2.,Dy=2.,ticksize=-2pt 0,subticks=2]{->}(0,0)(-5.630768994361358,-4.610292739805597)(4.7720311331921845,8.688525005674933)
\pscustom[linewidth=0.8pt,linecolor=ccqqqq]{\psplot{-2.}{0.}{-4.0-2.0*x}\lineto(0.,8.)\psplot{0.}{-2.}{2.0*(x+2.0)^(2.0)}\lineto(-2.,0.)\closepath}
\pscustom[linewidth=0.8pt,linecolor=ccqqqq]{\psplot{0.}{2.}{-(x-2.0)^(2.0)}\lineto(2.,0.)\psplot{2.}{0.}{-4.0*x+8.0}\lineto(0.,-4.)\closepath}
\rput[tl](-2.75,3.2775447195481844){$\ccqqqq{2 \; \left(x + 2 \right)^{2}}$}
\rput[tl](1.5,-0.9521652224241329){$\ccqqqq{-\left(x - 2 \right)^{2}}$}
\rput[tl](-3.75,-1.2951146771786453){$\ccqqqq{2x + y = -4}$}
\rput[tl](1.5,4.039654619002656){$\ccqqqq{4x + y = 8}$}
\begin{scriptsize}
\psdots[dotsize=4pt 0,dotstyle=*,linecolor=ccqqqq](-2.,0.)
\psdots[dotsize=4pt 0,dotstyle=*,linecolor=ccqqqq](0.,-4.)
\psdots[dotsize=4pt 0,dotstyle=*,linecolor=ccqqqq](0.,8.)
\psdots[dotsize=4pt 0,dotstyle=*,linecolor=ccqqqq](2.,0.)
\end{scriptsize}
\end{pspicture*}"""

NEW9 = r"""\begin{tikzpicture}[scale=0.45]
  \draw[->] (-5.7,0) -- (4.9,0) node[right] {$x$};
  \draw[->] (0,-4.7) -- (0,8.8) node[above] {$y$};
  \foreach \gx in {-4,-2,2,4} \draw[lightgray, dashed, thin] (\gx,-4.7) -- (\gx,8.8);
  \foreach \gy in {-4,-2,2,4,6,8} \draw[lightgray, dashed, thin] (-5.7,\gy) -- (4.9,\gy);
  \fill[red!20]
    plot[domain=-2:0, samples=20] (\x,{-4-2*\x})
    -- (0,8)
    -- plot[domain=0:-2, samples=20] (\x,{2*(\x+2)*(\x+2)})
    -- cycle;
  \fill[red!20]
    plot[domain=0:2, samples=20] (\x,{-(\x-2)*(\x-2)})
    -- plot[domain=2:0, samples=20] (\x,{-4*\x+8})
    -- (0,-4)
    -- cycle;
  \draw[thick, red] plot[domain=-3.5:0.2, samples=60] (\x,{-4-2*\x});
  \draw[thick, red] plot[domain=-3.5:0.2, samples=60] (\x,{2*(\x+2)*(\x+2)});
  \draw[thick, red] plot[domain=-0.5:2.5, samples=40] (\x,{-(\x-2)*(\x-2)});
  \draw[thick, red] plot[domain=-0.5:3, samples=40] (\x,{-4*\x+8});
  \node[left, font=\tiny] at (-2.5,3) {$2(x{+}2)^2$};
  \node[right, font=\tiny] at (1,-1.5) {$-(x{-}2)^2$};
  \node[left, font=\tiny] at (-3,-1.5) {$2x{+}y{=}{-}4$};
  \node[right, font=\tiny] at (0.5,5.5) {$4x{+}y{=}8$};
  \foreach \x in {-4,-2,2,4} \draw (\x,2pt) -- (\x,-2pt) node[below, font=\tiny] {$\x$};
  \foreach \y in {-4,-2,2,4,6,8} \draw (2pt,\y) -- (-2pt,\y) node[left, font=\tiny] {$\y$};
  \fill[red] (-2,0) circle (3pt); \fill[red] (0,-4) circle (3pt);
  \fill[red] (0,8) circle (3pt); \fill[red] (2,0) circle (3pt);
\end{tikzpicture}"""

content = R(content, OLD9, NEW9, 'Fig9 two regions par+line v2')

# ================================================================
# FIGURE 10: Two regions — L.980-991
# Left:  y=2x+4, y=-2x²-4x    (x∈[-1,0])
# Right: y=3x,   y=-x²+4      (x∈[0,1])
# ================================================================
OLD10 = r"""\psset{xunit=1.8cm,yunit=1.8cm,algebraic=true,dimen=middle,dotstyle=o,dotsize=5pt 0,linewidth=2.pt,arrowsize=3pt 2,arrowinset=0.25}
\begin{pspicture*}(-2.693010288679664,-0.969888369565933)(3.5663649933592434,4.983875461089504)
\multips(0,0)(0,1.0){6}{\psline[linestyle=dashed,linecap=1,dash=1.5pt 1.5pt,linewidth=0.4pt,linecolor=lightgray]{c-c}(-2.693010288679664,0)(3.5663649933592434,0)}
\multips(-2,0)(1.0,0){7}{\psline[linestyle=dashed,linecap=1,dash=1.5pt 1.5pt,linewidth=0.4pt,linecolor=lightgray]{c-c}(0,-0.969888369565933)(0,4.983875461089504)}
\psaxes[labelFontSize=\scriptstyle,xAxis=true,yAxis=true,Dx=1.,Dy=1.,ticksize=-2pt 0,subticks=2]{->}(0,0)(-2.693010288679664,-0.969888369565933)(3.5663649933592434,4.983875461089504)
\pscustom[linewidth=1.6pt]{\psplot{-1.}{0.}{2.0*x+4.0}\lineto(0.,0.)\psplot{0.}{-1.}{-2.0*x^(2.0)-4.0*x}\lineto(-1.,2.)\closepath}
\pscustom[linewidth=1.6pt]{\psplot{0.}{1.}{3.0*x}\lineto(1.,3.)\psplot{1.}{0.}{-x^(2.0)+4.0}\lineto(0.,0.)\closepath}
\rput[tl](-2,3.546369745322887){$f\left(x \right)\, = \,2 \; x + 4$}
\rput[tl](-2.5,1.2033486180497397){$g\left(x \right)\, = \,-2 \; x^{2} - 4 \; x$}
\rput[tl](0.5215694221685272,4.4066093862540905){$h\left(x \right)\, = \,-x^{2} + 4$}
\rput[tl](0.7819051029766553,1.6561063238030047){$p\left(x \right)\, = \,3 \; x$}
\end{pspicture*}"""

NEW10 = r"""\begin{tikzpicture}[scale=0.95]
  \draw[->] (-2.7,0) -- (3.7,0) node[right] {$x$};
  \draw[->] (0,-1) -- (0,5.1) node[above] {$y$};
  \foreach \gx in {-2,-1,1,2,3} \draw[lightgray, dashed, thin] (\gx,-1) -- (\gx,5.1);
  \foreach \gy in {1,2,3,4} \draw[lightgray, dashed, thin] (-2.7,\gy) -- (3.7,\gy);
  \fill[gray!25]
    plot[domain=-1:0, samples=20] (\x,{2*\x+4})
    -- (0,0)
    -- plot[domain=0:-1, samples=20] (\x,{-2*\x*\x-4*\x})
    -- cycle;
  \fill[gray!25]
    plot[domain=0:1, samples=20] (\x,{3*\x})
    -- plot[domain=1:0, samples=20] (\x,{-\x*\x+4})
    -- (0,0)
    -- cycle;
  \draw[thick] plot[domain=-2:0.2, samples=60] (\x,{2*\x+4});
  \draw[thick] plot[domain=-2.5:0.2, samples=60] (\x,{-2*\x*\x-4*\x});
  \draw[thick] plot[domain=-0.5:2.5, samples=60] (\x,{-\x*\x+4});
  \draw[thick] plot[domain=-0.5:1.5, samples=30] (\x,{3*\x});
  \node[left, font=\small] at (-1.9,3.5) {$f{=}2x{+}4$};
  \node[left, font=\small] at (-2.5,1.2) {$g{=}{-}2x^2{-}4x$};
  \node[right, font=\small] at (0.6,4.5) {$h{=}{-}x^2{+}4$};
  \node[right, font=\small] at (0.8,1.6) {$p{=}3x$};
  \foreach \x in {-2,-1,1,2,3} \draw (\x,2pt) -- (\x,-2pt) node[below, font=\tiny] {$\x$};
  \foreach \y in {1,2,3,4} \draw (2pt,\y) -- (-2pt,\y) node[left, font=\tiny] {$\y$};
\end{tikzpicture}"""

content = R(content, OLD10, NEW10, 'Fig10 two regions f/g/h/p')

# ================================================================
# FIGURE 11: Two regions — L.1005-1016
# Left:  y=x+6, y=-x²-4x    (x∈[-2,0])
# Right: y=x,   y=-x²+6     (x∈[0,2])
# ================================================================
OLD11 = r"""\psset{xunit=1.45cm,yunit=1.45cm,algebraic=true,dimen=middle,dotstyle=o,dotsize=5pt 0,linewidth=2.pt,arrowsize=3pt 2,arrowinset=0.25}
\begin{pspicture*}(-4.445819300468519,-1.3719174041252018)(4.594173090925399,6.298825325380035)
\multips(0,-1)(0,1.0){8}{\psline[linestyle=dashed,linecap=1,dash=1.5pt 1.5pt,linewidth=0.4pt,linecolor=lightgray]{c-c}(-4.445819300468519,0)(4.594173090925399,0)}
\multips(-4,0)(1.0,0){10}{\psline[linestyle=dashed,linecap=1,dash=1.5pt 1.5pt,linewidth=0.4pt,linecolor=lightgray]{c-c}(0,-1.3719174041252018)(0,6.298825325380035)}
\psaxes[labelFontSize=\scriptstyle,xAxis=true,yAxis=true,Dx=1.,Dy=1.,ticksize=-2pt 0,subticks=2]{->}(0,0)(-4.445819300468519,-1.3719174041252018)(4.594173090925399,6.298825325380035)
\pscustom[linewidth=1.6pt]{\psplot{-2.}{0.}{x+6.0}\lineto(0.,0.)\psplot{0.}{-2.}{-x^(2.0)-4.0*x}\lineto(-2.,4.)\closepath}
\pscustom[linewidth=1.6pt]{\psplot{0.}{2.}{x}\lineto(2.,2.)\psplot{2.}{0.}{-x^(2.0)+6.0}\lineto(0.,0.)\closepath}
\rput[tl](-3.1207389825117553,5.680454510333547){$f\left(x \right)\, = \,x + 6$}
\rput[tl](-3.6360479950504967,2.1763532250701187){$g\left(x \right)\, = \,-x^{2} - 4 \; x$}
\rput[tl](1.3550878692533113,5.474330905318051){$h\left(x \right)\, = \,-x^{2} + 6$}
\rput[tl](1.3550878692533113,1.1015658560607478){$p\left(x \right)\, = \,x$}
\end{pspicture*}"""

NEW11 = r"""\begin{tikzpicture}[scale=0.85]
  \draw[->] (-4.5,0) -- (4.7,0) node[right] {$x$};
  \draw[->] (0,-1.4) -- (0,6.5) node[above] {$y$};
  \foreach \gx in {-4,-3,-2,-1,1,2,3,4} \draw[lightgray, dashed, thin] (\gx,-1.4) -- (\gx,6.5);
  \foreach \gy in {-1,1,2,3,4,5,6} \draw[lightgray, dashed, thin] (-4.5,\gy) -- (4.7,\gy);
  \fill[gray!25]
    plot[domain=-2:0, samples=20] (\x,{\x+6})
    -- (0,0)
    -- plot[domain=0:-2, samples=20] (\x,{-\x*\x-4*\x})
    -- cycle;
  \fill[gray!25]
    plot[domain=0:2, samples=20] (\x,{\x})
    -- plot[domain=2:0, samples=20] (\x,{-\x*\x+6})
    -- (0,0)
    -- cycle;
  \draw[thick] plot[domain=-3.5:0.3, samples=60] (\x,{\x+6});
  \draw[thick] plot[domain=-4.1:0.2, samples=60] (\x,{-\x*\x-4*\x});
  \draw[thick] plot[domain=-0.3:2.7, samples=60] (\x,{-\x*\x+6});
  \draw[thick] plot[domain=-0.5:2.5, samples=30] (\x,{\x});
  \node[above, font=\small] at (-2.5,5) {$f{=}x{+}6$};
  \node[left, font=\small] at (-3.6,2.2) {$g{=}{-}x^2{-}4x$};
  \node[right, font=\small] at (1.4,5.4) {$h{=}{-}x^2{+}6$};
  \node[right, font=\small] at (1.2,1.1) {$p{=}x$};
  \foreach \x in {-4,-3,-2,-1,1,2,3,4} \draw (\x,2pt) -- (\x,-2pt) node[below, font=\tiny] {$\x$};
  \foreach \y in {-1,1,2,3,4,5,6} \draw (2pt,\y) -- (-2pt,\y) node[left, font=\tiny] {$\y$};
\end{tikzpicture}"""

content = R(content, OLD11, NEW11, 'Fig11 two regions f/g/h/p v2')

# ================================================================
# WRITE & REPORT
# ================================================================
with open('inttriples.tex', 'w', encoding='utf-8') as f:
    f.write(content)

ok   = sum(1 for r in results if r.startswith('OK'))
miss = sum(1 for r in results if r.startswith('MISS'))
for r in results:
    print(r.encode('ascii', 'replace').decode('ascii'))
print(f'\n{ok} OK, {miss} missed')
