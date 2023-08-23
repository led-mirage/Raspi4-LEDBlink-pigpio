# ラズパイ pigpioでLチカ

## はじめに

私はずっとWindowsの世界で生きてきたので、Linux系のOSには馴染みがありません。また電子回路も素人なので、間違った記載があるかもしれません。あらかじめご了承ください。

## プログラム概要

なんの変哲もないLチカサンプルです。PWM制御でLEDの明るさを抑えています。

GPIO制御用にはpigpioライブラリを使用しています。最初、RPi.GPIOを使用して作ったのですが、チラツキが発生したので使用するライブラリをpigpioに変更したところ、チラツキが抑えられていい感じになりました。

ソフトウェアでPWM制御を行っているRPi.GPIOに対して、ハードウェアで制御を行っているpigpioの方が高精度な動作を実現しているものだと思われます。たぶん。

## 機能

- プログラムを実行すると１秒間隔でLEDが点滅します
- PWM制御でLEDの明るさを変更しています
- Ctrl+Cで停止します

## 機材

- Raspberry Pi 4 Model B 4GB
- 抵抗入りLED
- ブレッドボード
- ジャンプワイヤー２本

## 配線

- GPIO26 (Pin#37) -> LEDアノード
- GND (Pin#39) -> LEDカソード

## 実行の様子

https://github.com/led-mirage/Raspi4-LEDBlink-pigpio/assets/139528700/8a2206b7-bbbd-48aa-adac-f86a6b4228e9

## 実行環境

- Raspberry Pi 4 Model B 4GB
- Raspberry Pi OS 64bit bullseye
- Python 3.9.17
- pigpio 1.78

## 開発環境

- Thonny 4.0.1（ラズパイプリインストール）
- pyenv 2.3.24

## 事前準備（pigpioのインストール）

pigpio を利用するにはあらかじめ pigpio をインストールし、デーモンを起動しておく必要があります。また、Python用のライブラリもインストールする必要があります。Python用のライブラリは `sudo apt python3-pigpio` でもインストールできますが、pyenv を使っている環境では下記のように別途インストールしてください。

### インストール

```bash
sudo apt update
sudo apt install pigpio
```

### デーモン起動

```bash
sudo pigpiod
```

### Python用のライブラリのインストール

```bash
pip install pigpio
```

### 【メモ】OS起動時にデーモンを自動起動させたい場合

OS起動時にデーモンを自動起動させたい場合は、次のようして pigpiod デーモンを有効にします。

```bash
sudo systemctl enable pigpiod
```

こうすることで次回起動時に pigpiod が起動されますが、すぐに起動したい場合は、続けて次のコマンドを実行します。

```bash
sudo systemctl start pigpiod
```

#### ！自動起動がうまくいかない場合

私の環境だけかもしれませんがラズパイのOSが32bitの場合、動作が安定しない現象が発生しました。

具体的には、本来はLEDがゆっくり点滅するプログラムのはずが、異常に早く点滅するようになりました。プログラム中のsleepも効いていない感じです。原因はわかりませんが、明らかにおかしい感じです。

そういった場合は、`/etc/rc.local` ファイルに以下の行を追加することでも pigpiod を自動起動できます。

```bash
/usr/bin/pigpiod
```

追加する場所は、ファイル末尾の `exit 0` の直前でOKです。

ただし最近は、このやり方は推奨されていないみたいです。

## プログラムの実行

### クローン

ラズパイのターミナルを開き、プログラムをクローンしたいディレクトリに移動し、次のコマンドを実行します。

```bash
git clone https://github.com/led-mirage/Raspi4-LEDBlink-pigpio.git
```

### 実行

pigpiodデーモンを起動後、以下のコマンドを実行するとプログラムが開始しLEDが点滅し始めます。

```bash
python led.py
```

### 停止

ターミナルで「Ctrl + C」を押すとプログラムが停止します。

お疲れ様でした。

## バージョン履歴

### 1.0 (2023/08/14)
- ファーストリリース
