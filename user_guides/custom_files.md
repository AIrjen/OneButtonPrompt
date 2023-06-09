# Custom files
In the /userfiles/ directory it is possible to include personal additions and overwrites. This is the place to include LoRA's and textual inversions. You can also maintain your own artist lists.

These are the things that are possible:
- Adding style LoRA's and textual inversions
- Maintaining own personal favorite artists lists
- Adding on to, or replacing One Button Prompt main lists
- Adding custom lists
- filling an antilist, that removes values during prompt generation

In the /userfiles/ directory, there are already samples placed to help. These are ignored.

Files created here will not be overwritten during upgrading of One Button Prompt.

## Adding style LoRA's and textual inversions

Filename: __styles_ti_lora.csv__

Fill this one with style textual inversions and LoRA's. They will then randomly be used in prompt generation and placed at the end of the prompt.
You need to have the appropiate TI or LoRA installed for this to work.

Example values:
> style-sylvamagic
> 
> <lora:LowRA:0.6>
> 
> <lora:add_detail:1>

##  Maintaining own personal favorite artists lists
Filename: __personal_artists_xyz.csv__   (replace xyz with the name of your choice)

Add any number of files formed as personal_artists_xyz.csv. 
  
These will show up in the artists selection in One Button Prompt.

For example, you can create a personal_artists_portrait.csv and a personal_artists_favorites.csv. Both will then show up as options.
 
Example values:
> Alena Aenami
>
> Victo Ngai
>
> Victor Nizovtsev
  
This is how it will then show up in the WebUI:
![image](https://github.com/AIrjen/OneButtonPrompt/assets/130234949/ce100d74-8a0a-4927-8b90-fab9cb8f2e48)


## Adding on to, or replacing One Button Prompt main lists
Filename: __listname_addon.csv__  (replace listname with the name of the corresponding csv file in /csvfiles/ directory)

Filename: __listname_replace.csv__  (replace listname with the name of the corresponding csv file in /csvfiles/ directory)

Addon files will be automatically added to the existing csv files in the ./csvfiles/ directory. So you can add your own personal stuff. They need to be named the same, such as vehicles_addon.csv

Replace files will automatically replace the existing csv files in the ./csvfiles/ directory during prompt generation. This way, you can run of your own custom lists if you need. They need to be named the same, such as vehicles_replace.csv
  
## Adding custom lists
Filename: __custom_input_prefix.csv__

Filename: __custom_input_mid.csv__

Filename: __custom_input_suffix.csv__

Add anything in these files, and they will show up in the front of the prompt, in the middle, or at the end. This adds some additional flexiblity, if you want more freedom or maybe some certain keywords to show up. They will be randomly used in the prompt generation.

These are added for flexibility.

## filling an antilist, that removes values during prompt generation
Filename: __antilist.csv__

Any value in this csv file will be removed from any list/csv file used during prompt generation.
For example, if you don't want "film grain" to show up, add this to the antilist.csv

Example values:
> film grain
> 
> purple
> 
> cat

## loading subject from a file with a special wildcard
In the user_files folder, you can place a file called custom_subjects.csv . If you use this -subjectfromfile- wildcard, it will select a random value from this file. Suggested use is on the Overwrite Subject field.
