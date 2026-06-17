# TCD Origin 古文字数据库链接汇总

本文档整理了 TCD Origin 智能体可用的所有古文字数据库资源。

---

## 一、核心甲骨文数据集

| 名称 | 链接 | 说明 |
|------|------|------|
| **HUST-OBC** | https://github.com/Pengjie-W/HUST-OBC | 华中科技大学，140,053幅图像，9,411未破译字 |
| **HUST-OBC 论文** | https://arxiv.org/html/2401.15365 | Scientific Data 2024 正式发表 |
| **EVOBC 演化数据集** | https://arxiv.org/html/2401.12467v1 | 甲骨文跨时期演化数据集 |
| **PD-OBS 象形解析** | https://github.com/PKXX1943/PD-OBS | 复旦团队，47,157个汉字象形分析数据集 |
| **数字甲骨多模态** | 世界人工智能大会2024开源 | 全球首个甲骨文多模态数据集 |
| **76类甲骨文数据集** | https://wenku.csdn.net/doc/3qag07wtwv | 4万张高清拓片图像 |

---

## 二、甲骨文研究平台

| 名称 | 链接 | 说明 |
|------|------|------|
| **殷契文渊** | https://oradata.cloud/ | 安阳师范学院，甲骨文专业数据库 |
| **新甲骨文编** | https://www.gwz.fudan.edu.cn/ | 复旦大学古文字研究中心 |
| **殷契行止** | 腾讯SSV数字文化 | 全球首个甲骨文AI智能体 |
| **了不起的甲骨文** | 微信小程序 | 腾讯甲骨文公众体验平台 |

---

## 三、楔形文字数据库

| 名称 | 链接 | 说明 |
|------|------|------|
| **CDLI** | https://cdli.mpiwg-berlin.mpg.de/ | 楔形文字数字图书馆（德国马普所） |
| **British Museum Cuneiform** | https://www.britishmuseum.org/collection/departments/ancient-near-east/cuneiform-inscriptions | 大英博物馆藏 |

---

## 四、埃及圣书体数据库

| 名称 | 链接 | 说明 |
|------|------|------|
| **Egyptian Hieroglyphs DB** | https://www.britishmuseum.org/collection/egyptian-hieroglyphs | 大英博物馆 |
| **Unikemet** | https://unicode.org/reports/tr57/ | Unicode官方埃及象形文字数据库 |
| **EgMM-Corpus** | https://huggingface.co/datasets/Anwar12/EgMM-Corpus | 埃及文化多模态数据集 |

---

## 五、综合古文字数据集

| 名称 | 链接 | 说明 |
|------|------|------|
| **Chronicles-OCR** | https://github.com/VirtualLUOUCAS/Chronicles-OCR | 七字体跨时期数据集（甲骨/金文/篆/隶/楷/行/草） |
| **UniCalli** | https://huggingface.co/datasets/TSXu/UniCalli_dataset | 古文字书法生成数据集 |
| **甲骨文CNN识别** | https://gitcode.com/Universal-Tool/bf956 | CNN甲骨文识别开源项目 |
| **季羡林数据集** | https://iridescent-china.github.io/ | 古文字图像数据集 |

---

## 六、Unicode 古文字区块

| 名称 | 链接 |
|------|------|
| 甲骨文 Unicode | https://unicode-table.com/en/blocks/oracle-bone-script/ |
| 楔形文字 Unicode | https://unicode-table.com/en/blocks/cuneiform/ |
| 圣书体 Unicode | https://unicode-table.com/en/blocks/egyptian-hieroglyphs/ |

---

## 七、学术论文资源

| 名称 | 链接 | 说明 |
|------|------|------|
| Fudan OBC破译 | https://arxiv.org/abs/2508.10113 | 复旦团队SOTA破译框架，CVPR2025/ICCV2025 |
| HUST-OBC 论文 | https://doi.org/10.1038/s41597-024-03807-x | Scientific Data (Nature) 2024 |
| 古文字识别综述 | https://arxiv.org/abs/2103.12558 | arXiv古文字识别论文 |

---

## 八、中国古文字综合

| 名称 | 链接 | 说明 |
|------|------|------|
| 中国古文字数据库 | https://www.china-writing.com/ | 古文字综合检索 |
| 小学堂 | https://www.xiaoxue.tzu.edu.tw/ | 甲骨文、金文、小篆查询 |
| 故宫博物院 | https://www.dpm.org.cn/ | 古文字文物数据库 |

---

## 九、数据集引用规范

### HUST-OBC（必须引用）

```
Wang, P., Zhang, K., Wang, X., Han, S., Liu, Y., Wan, J., Guan, H., Kuang, Z., 
Jin, L., Bai, X. & Liu, Y. An open dataset for oracle bone character recognition 
and decipherment. Sci Data 11, 976 (2024). https://doi.org/10.1038/s41597-024-03807-x
```

### EVOBC

```
@article{evobc2024,
  title={An open dataset for the evolution of oracle bone characters},
  journal={arXiv},
  year={2024}
}
```

### PD-OBS

```
@article{pdobs2025,
  title={Pictographic Decipherment of Oracle Bone Script},
  journal={arXiv},
  year={2025}
}
```

---

**文档版本**：v1.0 | **更新日期**：2025年7月
