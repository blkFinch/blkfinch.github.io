---
title: Ruby Flatten Vs. Flat Map
date: 2023-10-30
tags: 
aliases: 
feed: hide
published: true
---
Flatten will flatten all elements into a single array- flat map will only flatten one level, and retain nested arrays

>#flatten flattens everything by default (retuning an array with no arrays as members), where #flat_map does not (if you pass it a multi-level array, it will retain the structure of it).

```ruby
[1, [2,3],[[4,5]] ].flat_map {|i| i}
=> [1,2,3,[4,5]]
[1, [2,3],[[4,5]] ].map{|i| i}.flatten
=> [1,2,3,4,5]
```
