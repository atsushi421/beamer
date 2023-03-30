# beamer

## 環境構築
Windows, WSL2, vscode の使用を推奨. ([WLS2インストール・設定方法](https://www.kagoya.jp/howto/it-glossary/develop/wsl2_linux/)).

1. WSL2 に latex をインストールする: `sudo apt -y update & sudo apt -y install texlive-lang-japanese`
2. `git clone https://github.com/atsushi421/beamer.git`
3. beamer/template.tex の2行目の `\beamerDir` コマンドのパスを自分の環境に合わせて設定
   - 設定するパスは wsl から見たパスにする
4. vscodeに以下の拡張機能を入れる
   - LaTeX Workshop
   - Batch Replacer


## 新しいまとめ作成方法
以下コマンドを実行することで, テンプレートフォルダが作成される. その後は適宜新規 .tex ファイルをディレクトリ内に作成し, その .tex ファイルを `main.tex` から読み込むだけで良い
```
python3 prepare_new_paper.py -d [FOLDER NAME]
```

### テンプレートフォルダ構成
 - `main.tex`: メインファイル. この中で他のソースファイルを読み込む
 - `abstract/introduction/conclusion.tex`: このセクションはどの論文にもあるので, 自動生成される
 - `prior_knowledge.tex`: [コンフル](https://tier4.atlassian.net/wiki/spaces/EMBIV/pages/2674852113)にまとめられた前提知識ページのリンクを貼るファイル
 - `symbols_terms.tex`: 論文中の表記法や簡単な用語の定義をまとめるファイル
 - `figure/`: 資料で使用する図はこのフォルダに格納する
 - `figure/supplementary_figure.pptm`: 図をjpg化するマクロを備えたパワポファイル. 基本的にこのファイル経由で図を作成することを推奨


## ビルド方法
`Ctrl + Alt + B` でビルド可能．setting.json を編集すれば save 時に自動ビルドも可能


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
高速化や利便性のために, いくつかのカスタムコマンドが定義されている．[]内の数字は引数の数
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


## スニペット
スニペットを使うことで, 構文入力を高速でできる．vscodeのLaTeX-Workshopで標準に用意されているスニペットは [このページ](https://github.com/James-Yu/LaTeX-Workshop/wiki/Snippets#environments) 参照.
これ以外にも，beamer/.vscode/内で以下のカスタムスニペットを定義している．
- todo


## その他Tips
- 一括置換:
  - 拡張機能 Batch Replacer によって, ファイルに書かれた置換コマンドを一括で実行できる
  - 置換コマンドが書かれたファイルのサンプルは beamer/batch_replace.txt である
  - batch_replace.txt をアクティブにし, `Ctrl + Shift + p` -> `Batch Replace` を選択することで, 全ての .tex ファイルが一括置換される
  - うまく使えば高速化に繋がるので, 使ってみてほしい
  - [公式ドキュメント](https://github.com/angelo-mollame/batch-replacer)
- パワポの画像保存マクロ:
  - テンプレートフォルダの figure/ にある `supplementary_figure.pptm` は選択されたオブジェクトを .jpg で同一ディレクトリに保存するマクロを備えている
  - 図にしたい部分をグループ化して選択し, `Alt + 3` を押すとマクロが実行され, 画像名を入力するウィンドウが出てくる
  - そのウィンドウに入力した名前で, figure/ に .jpg 画像が保存される


## 参考資料
- [Latex & vscode](https://qiita.com/rainbartown/items/d7718f12d71e688f3573)
- [VSCode と WSL2 で LaTeX 執筆環境を作ろう](https://zenn.dev/minatoneko/articles/b4038eb6524199#latex-workshop-%E3%81%AE%E8%A8%AD%E5%AE%9A)
- [Latex日本語コンパイル](https://gist.github.com/Ikuyadeu/204d06fffd912f441b383eb02463e29b)
- [Beamer読本](https://ayapin-film.sakura.ne.jp/LaTeX/Slides/Beamer-tutorial.pdf)
- [Beamer & Tikz](https://tasusu.github.io/tikz.html)
