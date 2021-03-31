"""
Text fields allow users to enter input
"""

from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ColorProperty
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoTextField',
    'CupertinoTextView',
    'CupertinoSearchBar'
]

Builder.load_string("""
<CupertinoTextField>:
    password_mask: '•'
    multiline: False
    cursor_width: '2sp'
    cursor_color: 0.25, 0.5, 0.95, 1
    font_name: 'San Francisco'
    
    canvas.after:
        Color:
            rgba: 0.95, 0.95, 0.95, 1
        Rectangle:
            size: self.width, 2
            pos: self.pos

<CupertinoTextView>:
    multiline: True
    password: False
    cursor_width: '2sp'
    cursor_color: 0.25, 0.5, 0.95, 1
    font_name: 'San Francisco'
    hint_text: ''

<CupertinoSearchBar>:
    orientation: 'horizontal'
    padding: 5, 0
    
    canvas.before:
        Color:
            rgba: self.background_color
        RoundedRectangle:
            radius: self.height/4,
            size: self.size
            pos: self.pos
    
    CupertinoSymbol:
        symbol: 'search'
        color: root.symbol_color
        size_hint_x: 0.05
    TextInput:
        id: textfield
        multiline: False
        password: False
        cursor_width: '2sp'
        cursor_color: 0.25, 0.5, 0.95, 1
        hint_text: 'Search'
        font_size: root.height/2.5
        font_name: 'San Francisco'
        background_color: 0, 0, 0, 0
        foreground_color: root.foreground_color
    CupertinoSymbolButton:
        symbol: 'xmark_circle_fill' if textfield.text else ' '
        symbol_color: root.symbol_color
        background_down: 0, 0, 0, 0
        on_release: textfield.text = ''
        size_hint_x: 0.05
""")


class CupertinoTextField(TextInput):
    """
    iOS style Text Field to be used for single-line input

    .. image:: ../_static/text_field.gif
    """

    hint_text = StringProperty('')
    """
    A :class:`~kivy.properties.StringProperty` defining the text of hint of
    :class:`~kivycupertino.uix.textfield.CupertinoTextField`
    """

    background_color = ColorProperty([0, 0, 0, 0])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.textfield.CupertinoTextField`
    """

    foreground_color = ColorProperty([0, 0, 0, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the text color of
    :class:`~kivycupertino.uix.textfield.CupertinoTextField`
    """


class CupertinoTextView(TextInput):
    """
    iOS style Text View for multiline input

    .. image:: ../_static/text_view.gif
    """

    background_color = ColorProperty([0, 0, 0, 0])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.textfield.CupertinoTextView`
    """

    foreground_color = ColorProperty([0, 0, 0, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the text color of
    :class:`~kivycupertino.uix.textfield.CupertinoTextView`
    """


class CupertinoSearchBar(BoxLayout):
    """
    iOS style search bar

    .. image:: ../_static/search_bar.gif
    """

    background_color = ColorProperty([0.85, 0.85, 0.85, 0.7])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.textfield.CupertinoSearchBar`
    """

    foreground_color = ColorProperty([0, 0, 0, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the text color of
    :class:`~kivycupertino.uix.textfield.CupertinoSearchBar`
    """

    symbol_color = ColorProperty([0.55, 0.55, 0.6, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of the symbols of
    :class:`~kivycupertino.uix.textfield.CupertinoSearchBar`
    """