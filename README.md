# EventGeneration
We will learn two aspects of event generation,
- *MC instructions* on how to produce events using MadGraph, Pythia, Delphes etc in general and using unique Model UFO files.
-  Producing gridpacks to NanoAOD samples which includes CMS detector simulation will be added later. <br>

This is a work involving many people over a past few years in CMS multilepton group. I'm documenting them with my own analysis requirement and with some basic usage tips of these event generation softwares based on my experience.

**Contact Person:** Arnab Laha (arnab.laha@cern.ch)

## Resources
- How to produce gridpack: https://twiki.cern.ch/twiki/bin/viewauth/CMS/QuickGuideMadGraph5aMCatNLO
- Basic MadGraph usage   : https://twiki.cern.ch/twiki/bin/view/CMSPublic/MadgraphTutorial

## About the VLL UFO file
Ask me for the VLL model UFO file ```VLL.zip ``` (this is private). In addition, some relevant information provided by the authors about this model file are -
```- PARTICLES: tau’ -> lp (lp~ being its antiparticle), nu’ -> vlp (vlp~ being its antiparticle) 
- MASSES: The masses of these particles (“MLP" (mass of tau’) and “ MVLP” (mass of nu’)) are by default set to 100 GeV, 
  which can be changed during the runtime in “Block mass” of the “param_card.dat”.
  
- WIDTHS: Also Widths ("WLP" and "WVLP" for widths of tau’ and nu’ respectively) are by default set to 1 GeV, 
  which could also be changed during the runtime.
  
- SWITCHING BETWEEN SINGLET & DOUBLET MODELS: By default, the UFO file is set to “singlet model”. This can also
  be changed to “doublet model” (during runtime) by changing the "Weak Isospin" of tau’ (called “Tl”) in “Block Isospin” 
  of “param_card.dat” from “0.0” (singlet) to “-0.5”(doublet).
  ```
<br>
More Update later

