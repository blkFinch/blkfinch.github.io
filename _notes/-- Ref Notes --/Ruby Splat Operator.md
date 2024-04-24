---
title: Ruby Splat Operator
date: 2023-10-17
tags:
  - programming
aliases: 
feed: hide
published: true
---

## Splat Constructs or Destructs an Array
It can deconstruct an array ex:
```ruby
x, y, z = *[1,2,3] 
puts x # => 1 
puts y # => 2 
puts z # => 3
```

or it can wrap a value in brackets.

This is useful extracting or merging arrays. 
```ruby
arr = [1,2,3,4,5]
first, *rest = arr

puts first
# => 1
puts rest
# => [2,3,4,5]

#you could also wrap the first element with the splat
puts *first
# => [1]
```

it can deconstruct an array which makes it useful for merging
```ruby
arr = [x,y]
nums = [1,2, *arr,4]

puts nums
# => [1,2,x,y,4]
```
### Double Splat Constructs or Deconstructs a Hash

Same as above but for hashes:
```ruby
x = {x: 1, y: 2}
y = { z: 1, **x }
puts y
# {:z=>1, :x=>1, :y=>2}
```

___
### References

[betterprogramming](https://betterprogramming.pub/single-and-double-splat-operators-in-ruby-55dbe771ace6)