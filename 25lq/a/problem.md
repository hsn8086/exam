# MaiMaiDX
xwl喜欢在周一上午没课的时候坐七路车去市区打Mai,因为这个时候大家都在上学或者上班,不用排队.

但是今天却格外冷清,既然没人xwl就打算刷11.4514%完成度,但是这时候却发愁了,要怎么打才能打出11.4514%呢?

## 完成度计算

MaiMaiDX是音乐游戏,敲击音符后按误差时间的不同分成`Prefect` `Great` `Good` `Miss`四挡.

以下是分数对照表:
| 档次 | 分数 |
|------|------|
| Prefect | 500 |
| Great | 400 |
| Good | 200 |
| Miss | 0 |

全曲分数是: `score = 500 * 音符数量`

完成度是: `Acc = 累计分数 / 全曲分数` (向下取整)

## 任务
xwl想以`系ぎて`作为刷分的歌曲,全曲一共1400个音符,请帮他计算出有多少种达成的可能.

## 输出格式
本题目为填空题,仅需回答可能的数量