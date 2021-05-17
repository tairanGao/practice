---
attachments: [Clipboard_2021-04-29-15-48-17.png]
tags: [KMP, 九章]
title: Implement strStr()
created: '2021-04-29T19:35:05.254Z'
modified: '2021-04-29T20:50:08.934Z'
---

# [Implement strStr()](https://www.lintcode.com/problem/13/description?_from=ladder&fromId=1)


- KMP Algorithm: Knuth–Morris–Pratt algorithm *字符串匹配算法*
- Wrost case complexity is O(n)
- [视频讲解1](https://www.youtube.com/watch?v=dgPabAsTFa8)
- [视频讲解2](https://www.youtube.com/watch?v=3IFxpozBs2I)

1. calculate **Prefix Table**:
for example "a, b, a, b, c"
there are 5 prefixes:
  a
  ab
  aba
  abab
  ababc

对于这5个 找到他们的最长公共前后缀 

-> a b a b
最长前缀 aba, 最长后缀 bab-> 3个字母不一样 所以缩成2个
前缀 ab 后缀 ab 一样 所以 

-1  -> 
 0  -> a
 0  -> ab
 1  -> aba
 2  -> abab
 0  -> ababc
![](@attachment/Clipboard_2021-04-29-15-48-17.png)






