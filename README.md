# Dataset

### 数据问题:
基本所有之前处理的数据中,有的歌词有双引号,用pandas读取会强行读取闭合的双引号,将多行读取成一行,导致数据少十多行.

### df_all_01.csv:删除了双引号,只有歌词,会正常读取


- 最终数据：df_all_pinyin_clear.csv，删除了脏句，删除了重复4次以上的歌词。  
  包含：
  lyrics:歌词  
  isBad：是否脏句（脏句已经删除，全部为0,不为脏句）  
  pinyin_neg1-5：倒数第1-5个字的拼音  

- 分词后数据（仅歌词）（来自Zili Wang）: lyrics_only_fenci.txt  

