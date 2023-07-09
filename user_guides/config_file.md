# Be in control with config.csv

After you start up One Button Prompt for the first time, it will create a config.csv file in the /userfiles/ folder.

In this file, you can not only set what to generate, but you can even set the randomness of certain parts of the generation process.

To update the UI, you might need to restart WebUI.

###  On resetting/restoring the file

If you made a mistake, or wish to fully restore the config.csv file in the /userfiles/ folder, simply remove it. It will be recreated by One Button Prompt.

## Setting main generation options

In the following part, you can set parts of subjects the generations on and off. Turning off all subjects within a group, turns the main group off.

Example, if you don't want fictional characters or celebrities in the generation process, turn off subject_fictional and subject_nonfictional.



    # objects;
    subject_object;on
    subject_vehicle;on
    subject_food;on
    subject_space;on
    subject_building;on
    subject_flora;on
    # animals;
    subject_animal;on
    # humanoids;
    subject_manwoman;on
    subject_manwomanrelation;on
    subject_fictional;on
    subject_nonfictional;on
    subject_humanoid;on
    subject_job;on
    subject_firstnames;on
    # landscape;
    subject_landscape;on
    # concept;
    subject_event;on
    subject_concept;on
    subject_poemline;on
    subject_songline;on

## Other generation options

These options apply to the default prompt generation mode only. Here you can set the random chance of something appearing in the prompt, or even turn things on and off.

The config you see is the default config of One Button Prompt.

You can overwrite these, so for example, if you always want a pose to be generated change  __posechance;uncommon__ to  __posechance;always__

You can use the following random chances, in order of increasing appearing chance:

- always
- common
- normal
- uncommon
- rare
- legendary
- unique
- extraordinary
- novel
- never



  
      # other main lists, in order of appearance;
      # setting the random chance, for normal generation;
      # these can be, in order of most appearing to least appearing;
      # always, common, normal, uncommon, rare, legendary, unique, extraordinary, novel, never;
      custominputprefixrepeats;2
      custominputprefixchance;uncommon
      imagetypechance;normal
      imagetypequalitychance;rare
      # some prefixes that happen rarely;
      minilocationadditionchance;unique
      artmovementprefixchance;unique
      minivomitprefix1chance;rare
      minivomitprefix2chance;unique
      # shot size generation;
      shotsizechance;uncommon
      # subject specific stuff;
      subjectdescriptor1chance;common
      subjectdescriptor2chance;uncommon
      subjectbodytypechance;normal
      subjectculturechance;normal
      subjectconceptsuffixchance;unique
      # subjectlandscape specific stuff;
      subjectlandscapeinsideshotchance;unique
      subjectlandscapeaddonlocationchance;normal
      subjectlandscapeaddonlocationdescriptorchance;rare
      subjectlandscapeaddonlocationculturechance;rare
      # all additions;
      objectadditionsrepeats;2
      objectadditionschance;uncommon
      humanadditionchance;rare
      overalladditionchance;extraordinary
      # humanoid other stuff;
      emojichance;legendary
      joboractivitychance;normal
      # things in the middle of the prompt;
      custominputmidrepeats;2
      custominputmidchance;uncommon
      minivomitmidchance;unique
      # humanoid main stuff;
      outfitchance;normal
      posechance;uncommon
      hairchance;normal
      accessorychance;normal
      humanoidinsideshotchance;legendary
      humanoidbackgroundchance;uncommon
      # minilocation stuff;
      landscapeminilocationchance;uncommon
      generalminilocationchance;rare
      # general stuff add the end of the prompt;
      timperiodchance;normal
      focuschance;normal
      directionchance;normal
      moodchance;normal
      minivomitsuffixchance;unique
      artmovementchance;normal
      lightingchance;normal
      photoadditionchance;common
      lenschance;normal
      colorschemechance;normal
      vomit1chance;uncommon
      vomit2chance;uncommon
      greatworkchance;novel
      poemlinechance;novel
      songlinechance;novel
      quality1chance;uncommon
      quality2chance;uncommon
      # custom style list (lora and tis);
      customstyle1chance;uncommon
      customstyle2chance;uncommon
      # suffix custom list;
      custominputsuffixrepeats;2
      custominputsuffixchance;uncommon
      # artists stuff;
      artistsatbackchance;uncommon
