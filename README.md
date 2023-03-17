# beamer

## 新しいまとめ作成方法
以下コマンドを実行することで, テンプレートフォルダが作成される
```
python3 prepare_new_paper.py -d [FOLDER NAME]
```
 - `main.tex`: メインファイル. この中で他のソースファイルを読み込む
 - `abstract/introduction/conclusion.tex`: このセクションはどの論文にもあるので, 自動生成される
 - `prior_knowledge.tex`: [コンフル](https://tier4.atlassian.net/wiki/spaces/EMBIV/pages/2674852113)にまとめられた前提知識ページのリンクを貼るファイル
 - `symbols_terms.tex`: 論文中の表記法や簡単な用語の定義をまとめるファイル
 - `figure/`: 資料で使用する図はこのフォルダに格納する
 - `figure/supplementary_figure.pptm`: 図をjpg化するマクロを備えたパワポファイル. 基本的にこのファイル経由で図を作成することを推奨


## よく使う標準のコマンド
- `\input{xxx.tex}`: 他のファイルをインポートする. このコマンドを書いた部分がインポートしたファイルとそのまま置き換わると考えてOK. 主に `main.tex` で使用する.
- `\begin{itemize} \item xxx \end{itemize}`: 箇条書き
- `\begin{frame}{TITLE} xxx \end{frame}`: スライド作成
- `\begin{block}{TITLE} xxx \end{block}`: TITLE を題名として, 四角で囲める
- `\begin{definition}{TITLE} xxx \end{definition}`: blockの色違い. 定義を入れる場合はこれを使用する
- `\begin{lemma}{TITLE} xxx \end{lemma}`: blockの色違い. 補題を入れる場合はこれを使用する
- `\begin{theorem}{TITLE} xxx \end{theorem}`: blockの色違い. 定理を入れる場合はこれを使用する
- カラム. スライドを左右に分けたい時に使用する
    ```
    \begin{columns}
        \begin{column}{0.5\textwidth}
            xxx
        \end{column}
        \begin{column}{0.5\textwidth}
            xxx
        \end{column}
    \end{columns}
    ```

## カスタムコマンド
高速化や利便性のために, いくつかのカスタムコマンドが定義されている
- `\summary[2]`: 1pサマリをスライドとして追加する. このコマンドでは, `one_page_summary.jpg` が表示されるので, この命名を守る必要がある.
  - 引数1: y軸方向の位置調整. ミリ単位
  - 引数2: x軸方向の位置調整. ミリ単位
- `\notes[1]`: 注釈を入れる時に使用する
- `\hlink[2]`: 文書内のハイパーリンクを追加する
  - 引数1: ラベル名. `\begin{frame}[label=xxx]`でラベル名を付けられる
  - 引数2: ハイパーリンクを入れたい文字列
- `\ourl[2]`: 外部リンクを追加
  - 引数1: サイトのリンク
  - 引数2: ハイパーリンクを入れたい文字列
- `\desc[2]`: シンボルの説明を1行で入れたい時に使用する
  - 引数1: 説明したいシンボルや用語
  - 引数2: 意味
- `\full[1]`: スライド内に1つの要素だけ入れたい時にこれで囲む
- `\fitimage[2]`: 文章の下に画像を入れて, 画像サイズを自動調整するコマンド
  - 引数1: 文章など
  - 引数2: 入れたい画像ファイル名



## Tips
- `BIT`と入力することで, 高速で itemize できる


## Reference
- [Latex & vscode](https://qiita.com/rainbartown/items/d7718f12d71e688f3573)
- [Latex日本語コンパイル](https://gist.github.com/Ikuyadeu/204d06fffd912f441b383eb02463e29b)
- [Beamer読本](https://ayapin-film.sakura.ne.jp/LaTeX/Slides/Beamer-tutorial.pdf)
- [Beamer & Tikz](https://tasusu.github.io/tikz.html)
