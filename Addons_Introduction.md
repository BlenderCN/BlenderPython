Add-ons are scripts with extra 'boilerplate' and 'interface' code added. The extra code is for giving Blender a way to automatically load the add-on and have it load in the right places (menus) or appear in the right context (in edit mode for example).

Blender now has [great docs showing best practices](http://www.blender.org/api/blender_python_api_current/info_tutorial_addon.html) for approaching add-on code. The page also links to additional Python tutorials that cover the level of Python that you will need to be able to write stable add-ons. Even if your goal is to only write Blender add-ons, learning Python as fully as possible will never be a waste of time.

That tutorial shows how to register addons / operators and how to define and remove user defined keyboard shortcuts. I think most of that code is not obvious until you see working examples, and you experiment with dummy add-ons. Just like with the Operators programming page on this wiki I'll suggest you read more closely the content of Blender's `/addons` folder. If you've followed the above tutorial then seeing real add-ons with already working code will quickly reinforce the concepts.

### When not to code an add-on

- Not all scripts need to have full blown add-on code straight away. Sometimes you'll write a script for a specific task and never use it again or only use it 2 years later. Infrequently used scripts like that don't need add-on code (if you can get away with it). 
