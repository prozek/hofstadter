square = Import["~/hofstadter/8x849.csv", "Data"];
honeycomb = Import["~/hofstadter/3x349.csv", "Data"];

j = 1;

sqplt = Show[
  Table[ListPlot[
    Table[{j/50, square[[j, i]]}, {i, 1, Dimensions[square][[2]]}], 
    PlotMarkers -> {Automatic, Tiny}, PlotStyle -> Blue], {j, 1, 
    Dimensions[square][[1]]}], PlotRange -> {{0, 1}, {-4, 4}}, 
  AspectRatio -> 1, Frame -> True, 
  FrameLabel -> {"magnetic flux \[Phi]/\[Phi]0", "energy level /t"}, 
  PlotLabel -> "square lattice 8x8, 49 fluxes"]

hcplt = Show[
  Table[ListPlot[
    Table[{j/50, honeycomb[[j, i]]}, {i, 1, 
      Dimensions[honeycomb][[2]]}], PlotMarkers -> {Automatic, Tiny}, 
    PlotStyle -> Blue], {j, 1, Dimensions[honeycomb][[1]]}], 
  PlotRange -> {{0, 1}, {-4, 4}}, AspectRatio -> 1, Frame -> True, 
  FrameLabel -> {"magnetic flux \[Phi]/\[Phi]0", "energy level /t"}, 
  PlotLabel -> "honeycomb lattice 6x6, 49 fluxes"]

Export["~/hofstadter/hc.pdf", hcplt]
Export["~/hofstadter/sq.pdf", sqplt]
