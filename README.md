# Gate Delay Plot. PY

## Best to use in

ICS subject(Introduction to Computer System)
in KMITL university

**week 5**: including Lecture, Exercise

## Requirements

- Matplotlib installed

## Features

### plot

- plot() - plot all column & name (using step line)
- plot(*keys) - plot by key you select
- print_str() - print plot by string
- print_str(*keys) - print plot by string on key you select

### add

- add_and(a, b) - get key a, b then "bool and" save in dict for plot
- add_or(a, b) - get key a, b then "bool or"
- add_not(a) - get key a then "bool not"
- add_nand(a, b)
- add_nor(a, b)
- add_xor(a, b)
- add_delay(dict, delay) - when use same result but delay (buffer)

### other

- get_dict() - get dict that store name & 0/1 list
- get_init_dict() - get dict that from create object
- get_str() - similar print_str() but return instead

## Example

### print_str()

    A |_----_______|
    B |___---______|
    C |----___-----|
    D |-_-----_____|
    F |---___------|
    G |---__-------|

### Matplotlib
