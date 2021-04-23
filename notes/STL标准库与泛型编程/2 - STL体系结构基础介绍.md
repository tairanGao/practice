---
attachments: [Clipboard_2021-04-22-22-06-46.png, Clipboard_2021-04-22-22-12-31.png, Clipboard_2021-04-22-22-25-03.png, Clipboard_2021-04-22-22-29-37.png, Clipboard_2021-04-22-22-33-08.png]
tags: [C++, STL]
title: 2 - STL体系结构基础介绍
created: '2021-04-23T02:04:07.821Z'
modified: '2021-04-23T02:34:53.549Z'
---

# [2 - STL体系结构基础介绍](https://www.youtube.com/watch?v=VC51-1vldRE&list=PLTcwR9j5y6W2Bf4S-qi0HBQlHXQVFoJrP&index=2)


## STL 六大部件

- Containers
- Allocators
- Algorithms
- Iterators
- Adapters 
- Functors / Functor Adapters

![](@attachment/Clipboard_2021-04-22-22-06-46.png)

## Example
![](@attachment/Clipboard_2021-04-22-22-12-31.png)


## 容器：
![](@attachment/Clipboard_2021-04-22-22-25-03.png)
- 元素不一定是连续空间
- 所有的容器需要Follow **前闭后开[)** 原则
  - begin ->  第一个元素
  - end ->    最后一个元素的下一个
  - *(c.end()) 星号在这里是解指针

  ![](@attachment/Clipboard_2021-04-22-22-29-37.png)
- iterator 是一个泛化的指针

- C++ 11之后可以的Range based for loop:
![](@attachment/Clipboard_2021-04-22-22-33-08.png)




