# cemu-freepie

> Configurable FreePIE script for cemu

This is a python script for [FreePIE](http://andersmalmgren.github.io/FreePIE/) and 
[Cemu](http://cemu.info/). It allows to emulate [vJoy](https://github.com/shauleiz/vJoy) 
inputs using completely custom configuration files per game.

Configuration files allow custom key-bindings and are automagically loaded depending on 
which game is currently running in [Cemu](http://cemu.info/).

__Please make sure to read the [requirements](#requirements)__!

## Background
The goal of this project is to provide a universal script, which allows to play any game 
without loading or editing a different script for each game. This lowers the need to 
create multiple copies of the same code and also separates configuration from code.

Also this script provides the convenience of locking the mouse cursor into place, 
and allowing to do so on a different spot __per game__.

## Requirements

- [FreePIE](http://andersmalmgren.github.io/FreePIE/): To run the script.
- [vJoy](https://github.com/shauleiz/vJoy): To emulate a controller.
- [Cemu](http://cemu.info/): Duh!

## Installation
### Releases

You can just download the [cemu.py](https://github.com/rampage128/cemu-freepie/blob/master/cemu.py) or clone this repository [From source](#from-source)

### From source

1. Clone the repository wherever you like  
   ```
   git clone https://github.com/rampage128/cemu-freepie.git
   ```
2. Get your [favourite Text editor](https://notepad-plus-plus.org/)
3. __Profit!__

## Usage

1. [Install](#installation) the script
2. Edit or create a configuration file with the title-id of your game (shown in the Cemu title).
3. Open the [cemu.py](https://github.com/rampage128/cemu-freepie/blob/master/cemu.py) in [FreePIE](http://andersmalmgren.github.io/FreePIE/)
4. Change the variable `config_dir` in [cemu.py](https://github.com/rampage128/cemu-freepie/blob/master/cemu.py) to the path your configuration files are located.
5. Start Cemu and load the game.
6. Run the script in [FreePIE](http://andersmalmgren.github.io/FreePIE/)
7. Toggle the controls by pressing `F1` on your keyboard

### Editing configuration files

In order to change the key-bindings to your liking, you can edit or create configuration files.

Each configuration file has the name of the games title-id. The title-id will be shown in your
Cemu window's title bar. This is also how the script detects which game is currently running.

Configuration files need two sections.

The `[settings]` section contains global settings:

| Key          | Type        | Possible values           | Description                                           |
| ------------ | ----------- | ------------------------- | ----------------------------------------------------- |
| `trap_mouse` | boolean     | `False`, `True`, `0`, `1` | Decides if the mouse cursor should be locked in place |
| `mouse_x`    | int         | Any integer value         | x coordinate, where the mouse cursor should be locked |
| `mouse_y`    | int         | Any integer value         | y coordinate, where the mouse cursor should be locked |

The `[controller]` section contains the key-bindings for the controller. The values get parsed
as real python expressions. This means you can use actual script code in the entries!

- Available buttons are: `A`, `B`, `X`, `Y`, `L`, `R`, `ZL`, `ZR`, `+`, `-`, `LP`, `RP`, `DU`, `DD`, `DL`, `DR`
- Available axes are: `LX`, `LY`, `RX`, `RY`

Buttons require a boolean or int value. Axes require a value between vJoys axis maximum and the inversion 
of that value. In order to make this easier in the config file, there is several helper methods:

- `keys2Axis(boolean max, boolean min)`: Calculates an axis value based on two key-presses.
- `delta2Axis(int delta, float sensitivity)`: Calculates an axis value based on a delta value, 
  divided by given sensitivity.

Besides these helpers, all other FreePIE objects are available. Here is an example to bind `W` `A` `S` `D`
to the left and the mouse to the right joystick:
```
[controller]
...
LX = keys2Axis(keyboard.getKeyDown(Key.D), keyboard.getKeyDown(Key.A))
LY = keys2Axis(keyboard.getKeyDown(Key.W), keyboard.getKeyDown(Key.S))
RX = delta2Axis(mouse.deltaX, 10)
RY = delta2Axis(-mouse.deltaY, 10)
...
```

For more information, please check out one of the [example configuration files](https://github.com/rampage128/cemu-freepie/).

## Known issues

- Unfortunately the path to the configuration files has to be changed in the script
  (Only dynamic solution would be, if FreePIE would provide the path of the current 
  script as variable; so I doubt this will be fixable anytime soon.)
- Error handling of missing configuration files or entries is really bad
  (This can be improved!)

## Contribute

Feel free to [open an issue](https://github.com/rampage128/cemu-freepie/issues) or submit a PR

Also, if you like this or other of my projects, please feel free to support me using the Link below.

[![Buy me a beer](https://img.shields.io/badge/buy%20me%20a%20beer-PayPal-green.svg)](https://www.paypal.me/FrederikWolter/1)

## Dependencies

- [FreePIE](http://andersmalmgren.github.io/FreePIE/): To run the script.
- [vJoy](https://github.com/shauleiz/vJoy): To emulate a controller.
- [Cemu](http://cemu.info/): Duh!