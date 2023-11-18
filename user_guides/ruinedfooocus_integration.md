# RuinedFooocus

[RuinedFooocus](https://github.com/runew0lf/RuinedFooocus) is a great Fooocus fork, which as One Button Prompt built in. I highly recommend this fork.

One Button Prompt can be found under the One Button tab:

![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/23e54b29-ed3b-48ad-bcf5-9d407d62759d)


## Main differences
There is currently not way to generate directly. You need to add the prompts to the prompt field first.

The __Create Random Prompt__ adds the prompt to the prompt field. 

The __Add To Prompt__ adds an additional prompt to the prompt field. In RuinedFooocus you can string multiple prompts together with ---

There is a kind of workaround, which is via wildcards.

## One Button Prompt Wildcard integration

There is logic, to use One Button Prompt via wildcards in RuinedFooocus.

These are the OneButtonPrompt style wildcards that can be used:

`__onebuttonprompt__` --> Executes a random one button prompt with all standard settings. Usefull for iterating through many images at once. It will not react to the settings on the One Button tab.

`__onebuttonsubject__` --> Executes a tiny one button prompt, just the subject, no other frills, images types or other stuff. Great for using with styles! Or even random styles.

`__onebuttonhumanoid__, __onebuttonmale__, __onebuttonfemale__`, same as above, but for all humans, males or females

`__onebuttonanimal__, __onebuttonlandscape__, __onebuttonobject__, __onebuttonconcept__`, same as above, but for those specific types.

All __onebutton wildcards work with subject override, it can be typed like this:
`__onebuttonprompt:keanu reeves__`
or
`__onebuttonanimal:cute dog__`

### Example of `__onebuttonprompt__` wildcard
![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/cbd59c11-b27c-4ba3-b46f-f1ef45cfad69)

### Example of `__onebuttonmale:Keanu Reeves__' wildcard
![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/fa492e0e-c442-4096-9a9a-ea78e8d9935a)
