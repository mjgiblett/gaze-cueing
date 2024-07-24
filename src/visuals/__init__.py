"""
Contains non-interactive visual elements and fonts. 

Classes
-------
Element
    Base class for all visual and GUI elements.
FixationCross
    Class for creating and displaying a fixation cross.
Image
    Class for handling and displaying images.
MultilineText
    Class representing multiple lines of text.
Text
    Class representing a single line of text.

Variables
---------
fonts : dict 
    Dictionary containing system font styles and properties.
    
Functions
---------
init_fonts() -> None
    Initialises fonts. Should be called immediantly after pygame initialisation.
"""

from .element import Element
from .fixation_cross import FixationCross
from .fonts import fonts, init_fonts
from .image import Image
from .multiline_text import MultilineText
from .text import Text

__all__ = [
    "Element",
    "FixationCross",
    "Image",
    "MultilineText",
    "Text",
    "fonts",
    "init_fonts",
]
