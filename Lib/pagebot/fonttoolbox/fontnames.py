#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     fontnames.py
#
#     Knowing the Postscript name of a font, it is not always easy
#     to guess the exact file name, which we need to open a font
#     as Font instance. This "hard-wired" link between the Postscript
#     name (as use by DrawBot and Sketch) to the filename.
#     This is a current dump generated by the commented script, that
#     may need updates later for other OS versions.
#     But for now it is an extra clue for findFont() where too look.
#     We just store the fileName, the path where to find fonts is still
#     guessed by getFontPathOfFont(fontName)

FONT_NAME_2_FILE_NAME = {
    #'.AlBayanPUA': 'AlBayan.ttc',
    #'.AlBayanPUA-Bold': 'AlBayan.ttc',
    #'.AlNilePUA': 'Al Nile.ttc',
    #'.AlNilePUA-Bold': 'Al Nile.ttc',
    #'.AlTarikhPUA': 'Al Tarikh.ttc',
    #'.AppleColorEmojiUI': 'Apple Color Emoji.ttc',
    #'.AppleSDGothicNeoI-Bold': 'AppleSDGothicNeo.ttc',
    #'.AppleSDGothicNeoI-ExtraBold': 'AppleSDGothicNeo.ttc',
    #'.AppleSDGothicNeoI-Heavy': 'AppleSDGothicNeo.ttc',
    #'.AppleSDGothicNeoI-Light': 'AppleSDGothicNeo.ttc',
    #'.AppleSDGothicNeoI-Medium': 'AppleSDGothicNeo.ttc',
    #'.AppleSDGothicNeoI-Regular': 'AppleSDGothicNeo.ttc',
    #'.AppleSDGothicNeoI-SemiBold': 'AppleSDGothicNeo.ttc',
    #'.AppleSDGothicNeoI-Thin': 'AppleSDGothicNeo.ttc',
    #'.AppleSDGothicNeoI-UltraLight': 'AppleSDGothicNeo.ttc',
    #'.ArialHebrewDeskInterface': 'ArialHB.ttc',
    #'.ArialHebrewDeskInterface-Bold': 'ArialHB.ttc',
    #'.ArialHebrewDeskInterface-Light': 'ArialHB.ttc',
    #'.BaghdadPUA': 'Baghdad.ttc',
    #'.BeirutPUA': 'Beirut.ttc',
    #'.DamascusPUA': 'Damascus.ttc',
    #'.DamascusPUABold': 'Damascus.ttc',
    #'.DamascusPUALight': 'Damascus.ttc',
    #'.DamascusPUAMedium': 'Damascus.ttc',
    #'.DamascusPUASemiBold': 'Damascus.ttc',
    #'.DecoTypeNaskhPUA': 'DecoTypeNaskh.ttc',
    #'.DiwanKufiPUA': 'Diwan Kufi.ttc',
    #'.FarahPUA': 'Farah.ttc',
    #'.GeezaProInterface': 'GeezaPro.ttc',
    #'.GeezaProInterface-Bold': 'GeezaPro.ttc',
    #'.GeezaProInterface-Light': 'GeezaPro.ttc',
    #'.GeezaProPUA-Bold': 'GeezaPro.ttc',
    #'.GeezaProPUA-Regular': 'GeezaPro.ttc',
    #'.HelveticaNeueDeskInterface-Bold': 'HelveticaNeueDeskInterface.ttc',
    #'.HelveticaNeueDeskInterface-BoldItalic': 'HelveticaNeueDeskInterface.ttc',
    #'.HelveticaNeueDeskInterface-Heavy': 'HelveticaNeueDeskInterface.ttc',
    #'.HelveticaNeueDeskInterface-Italic': 'HelveticaNeueDeskInterface.ttc',
    #'.HelveticaNeueDeskInterface-Light': 'HelveticaNeueDeskInterface.ttc',
    #'.HelveticaNeueDeskInterface-MediumItalicP4': 'HelveticaNeueDeskInterface.ttc',
    #'.HelveticaNeueDeskInterface-MediumP4': 'HelveticaNeueDeskInterface.ttc',
    #'.HelveticaNeueDeskInterface-Regular': 'HelveticaNeueDeskInterface.ttc',
    #'.HelveticaNeueDeskInterface-Thin': 'HelveticaNeueDeskInterface.ttc',
    #'.HelveticaNeueDeskInterface-UltraLightP2': 'HelveticaNeueDeskInterface.ttc',
    #'.HiraKakuInterface-W0': 'ヒラギノ角ゴシック W0.ttc',
    #'.HiraKakuInterface-W1': 'ヒラギノ角ゴシック W1.ttc',
    #'.HiraKakuInterface-W2': 'ヒラギノ角ゴシック W2.ttc',
    #'.HiraKakuInterface-W3': 'ヒラギノ角ゴシック W3.ttc',
    #'.HiraKakuInterface-W4': 'ヒラギノ角ゴシック W4.ttc',
    #'.HiraKakuInterface-W5': 'ヒラギノ角ゴシック W5.ttc',
    #'.HiraKakuInterface-W6': 'ヒラギノ角ゴシック W6.ttc',
    #'.HiraKakuInterface-W7': 'ヒラギノ角ゴシック W7.ttc',
    #'.HiraKakuInterface-W8': 'ヒラギノ角ゴシック W8.ttc',
    #'.HiraKakuInterface-W9': 'ヒラギノ角ゴシック W9.ttc',
    #'.HiraginoSansGBInterface-W3': 'Hiragino Sans GB W3.ttc',
    #'.HiraginoSansGBInterface-W6': 'Hiragino Sans GB W6.ttc',
    '.Keyboard': 'Keyboard.ttf',
    #'.KufiStandardGKPUA': 'KufiStandardGK.ttc',
    #'.LucidaGrandeUI': 'LucidaGrande.ttc',
    #'.LucidaGrandeUI-Bold': 'LucidaGrande.ttc',
    #'.MunaPUA': 'Muna.ttc',
    #'.MunaPUABlack': 'Muna.ttc',
    #'.MunaPUABold': 'Muna.ttc',
    #'.NadeemPUA': 'Nadeem.ttc',
    #'.PingFangHK-Light': 'PingFang.ttc',
    #'.PingFangHK-Medium': 'PingFang.ttc',
    #'.PingFangHK-Regular': 'PingFang.ttc',
    #'.PingFangHK-Semibold': 'PingFang.ttc',
    #'.PingFangHK-Thin': 'PingFang.ttc',
    #'.PingFangHK-Ultralight': 'PingFang.ttc',
    #'.PingFangSC-Light': 'PingFang.ttc',
    #'.PingFangSC-Medium': 'PingFang.ttc',
    #'.PingFangSC-Regular': 'PingFang.ttc',
    #'.PingFangSC-Semibold': 'PingFang.ttc',
    #'.PingFangSC-Thin': 'PingFang.ttc',
    #'.PingFangSC-Ultralight': 'PingFang.ttc',
    #'.PingFangTC-Light': 'PingFang.ttc',
    #'.PingFangTC-Medium': 'PingFang.ttc',
    #'.PingFangTC-Regular': 'PingFang.ttc',
    #'.PingFangTC-Semibold': 'PingFang.ttc',
    #'.PingFangTC-Thin': 'PingFang.ttc',
    #'.PingFangTC-Ultralight': 'PingFang.ttc',
    '.SFCompactDisplay-Black': 'SFCompactDisplay-Black.otf',
    '.SFCompactDisplay-Bold': 'SFCompactDisplay-Bold.otf',
    '.SFCompactDisplay-Heavy': 'SFCompactDisplay-Heavy.otf',
    '.SFCompactDisplay-Light': 'SFCompactDisplay-Light.otf',
    '.SFCompactDisplay-Medium': 'SFCompactDisplay-Medium.otf',
    '.SFCompactDisplay-Regular': 'SFCompactDisplay-Regular.otf',
    '.SFCompactDisplay-Semibold': 'SFCompactDisplay-Semibold.otf',
    '.SFCompactDisplay-Thin': 'SFCompactDisplay-Thin.otf',
    '.SFCompactDisplay-Ultralight': 'SFCompactDisplay-Ultralight.otf',
    '.SFCompactRounded-Black': 'SFCompactRounded-Black.otf',
    '.SFCompactRounded-Bold': 'SFCompactRounded-Bold.otf',
    '.SFCompactRounded-Heavy': 'SFCompactRounded-Heavy.otf',
    '.SFCompactRounded-Light': 'SFCompactRounded-Light.otf',
    '.SFCompactRounded-Medium': 'SFCompactRounded-Medium.otf',
    '.SFCompactRounded-Regular': 'SFCompactRounded-Regular.otf',
    '.SFCompactRounded-Semibold': 'SFCompactRounded-Semibold.otf',
    '.SFCompactRounded-Thin': 'SFCompactRounded-Thin.otf',
    '.SFCompactRounded-Ultralight': 'SFCompactRounded-Ultralight.otf',
    '.SFCompactText-Bold': 'SFCompactText-Bold.otf',
    '.SFCompactText-BoldItalic': 'SFCompactText-BoldItalic.otf',
    '.SFCompactText-Heavy': 'SFCompactText-Heavy.otf',
    '.SFCompactText-HeavyItalic': 'SFCompactText-HeavyItalic.otf',
    '.SFCompactText-Italic': 'SFCompactText-RegularItalic.otf',
    '.SFCompactText-Light': 'SFCompactText-Light.otf',
    '.SFCompactText-LightItalic': 'SFCompactText-LightItalic.otf',
    '.SFCompactText-Medium': 'SFCompactText-Medium.otf',
    '.SFCompactText-MediumItalic': 'SFCompactText-MediumItalic.otf',
    '.SFCompactText-Regular': 'SFCompactText-Regular.otf',
    '.SFCompactText-Semibold': 'SFCompactText-Semibold.otf',
    '.SFCompactText-SemiboldItalic': 'SFCompactText-SemiboldItalic.otf',
    '.SFNSDisplay': 'SFNSDisplay.ttf',
    '.SFNSDisplay-Black': 'SFNSDisplay.ttf',
    '.SFNSDisplay-Bold': 'SFNSDisplay.ttf',
    '.SFNSDisplay-Heavy': 'SFNSDisplay.ttf',
    '.SFNSDisplay-Light': 'SFNSDisplay.ttf',
    '.SFNSDisplay-Medium': 'SFNSDisplay.ttf',
    '.SFNSDisplay-Semibold': 'SFNSDisplay.ttf',
    '.SFNSDisplay-Thin': 'SFNSDisplay.ttf',
    '.SFNSDisplay-Ultralight': 'SFNSDisplay.ttf',
    '.SFNSDisplayCondensed-Black': 'SFNSDisplayCondensed-Black.otf',
    '.SFNSDisplayCondensed-Bold': 'SFNSDisplayCondensed-Bold.otf',
    '.SFNSDisplayCondensed-Heavy': 'SFNSDisplayCondensed-Heavy.otf',
    '.SFNSDisplayCondensed-Light': 'SFNSDisplayCondensed-Light.otf',
    '.SFNSDisplayCondensed-Medium': 'SFNSDisplayCondensed-Medium.otf',
    '.SFNSDisplayCondensed-Regular': 'SFNSDisplayCondensed-Regular.otf',
    '.SFNSDisplayCondensed-Semibold': 'SFNSDisplayCondensed-Semibold.otf',
    '.SFNSDisplayCondensed-Thin': 'SFNSDisplayCondensed-Thin.otf',
    '.SFNSDisplayCondensed-Ultralight': 'SFNSDisplayCondensed-Ultralight.otf',
    '.SFNSText': 'SFNSText.ttf',
    '.SFNSText-Bold': 'SFNSText.ttf',
    '.SFNSText-BoldItalic': 'SFNSTextItalic.ttf',
    '.SFNSText-Heavy': 'SFNSText.ttf',
    '.SFNSText-HeavyItalic': 'SFNSTextItalic.ttf',
    '.SFNSText-Italic': 'SFNSTextItalic.ttf',
    '.SFNSText-Light': 'SFNSText.ttf',
    '.SFNSText-LightItalic': 'SFNSTextItalic.ttf',
    '.SFNSText-Medium': 'SFNSText.ttf',
    '.SFNSText-MediumItalic': 'SFNSTextItalic.ttf',
    '.SFNSText-Semibold': 'SFNSText.ttf',
    '.SFNSText-SemiboldItalic': 'SFNSTextItalic.ttf',
    '.SFNSTextCondensed-Bold': 'SFNSTextCondensed-Bold.otf',
    '.SFNSTextCondensed-Heavy': 'SFNSTextCondensed-Heavy.otf',
    '.SFNSTextCondensed-Light': 'SFNSTextCondensed-Light.otf',
    '.SFNSTextCondensed-Medium': 'SFNSTextCondensed-Medium.otf',
    '.SFNSTextCondensed-Regular': 'SFNSTextCondensed-Regular.otf',
    '.SFNSTextCondensed-Semibold': 'SFNSTextCondensed-Semibold.otf',
    #'.SanaPUA': 'Sana.ttc',
    #'.SavoyeLetPlainCC': 'Savoye LET.ttc',
    #'AlBayan': 'AlBayan.ttc',
    #'AlBayan-Bold': 'AlBayan.ttc',
    #'AlNile': 'Al Nile.ttc',
    #'AlNile-Bold': 'Al Nile.ttc',
    #'AlTarikh': 'Al Tarikh.ttc',
    #'AmericanTypewriter': 'AmericanTypewriter.ttc',
    #'AmericanTypewriter-Bold': 'AmericanTypewriter.ttc',
    #'AmericanTypewriter-Condensed': 'AmericanTypewriter.ttc',
    #'AmericanTypewriter-CondensedBold': 'AmericanTypewriter.ttc',
    #'AmericanTypewriter-CondensedLight': 'AmericanTypewriter.ttc',
    #'AmericanTypewriter-Light': 'AmericanTypewriter.ttc',
    #'AmericanTypewriter-Semibold': 'AmericanTypewriter.ttc',
    'AndaleMono': 'Andale Mono.ttf',
    'Apple-Chancery': 'Apple Chancery.ttf',
    'AppleBraille': 'Apple Braille.ttf',
    'AppleBraille-Outline6Dot': 'Apple Braille Outline 6 Dot.ttf',
    'AppleBraille-Outline8Dot': 'Apple Braille Outline 8 Dot.ttf',
    'AppleBraille-Pinpoint6Dot': 'Apple Braille Pinpoint 6 Dot.ttf',
    'AppleBraille-Pinpoint8Dot': 'Apple Braille Pinpoint 8 Dot.ttf',
    #'AppleColorEmoji': 'Apple Color Emoji.ttc',
    'AppleGothic': 'AppleGothic.ttf',
    'AppleMyungjo': 'AppleMyungjo.ttf',
    #'AppleSDGothicNeo-Bold': 'AppleSDGothicNeo.ttc',
    #'AppleSDGothicNeo-ExtraBold': 'AppleSDGothicNeo.ttc',
    #'AppleSDGothicNeo-Heavy': 'AppleSDGothicNeo.ttc',
    #'AppleSDGothicNeo-Light': 'AppleSDGothicNeo.ttc',
    #'AppleSDGothicNeo-Medium': 'AppleSDGothicNeo.ttc',
    #'AppleSDGothicNeo-Regular': 'AppleSDGothicNeo.ttc',
    #'AppleSDGothicNeo-SemiBold': 'AppleSDGothicNeo.ttc',
    #'AppleSDGothicNeo-Thin': 'AppleSDGothicNeo.ttc',
    #'AppleSDGothicNeo-UltraLight': 'AppleSDGothicNeo.ttc',
    'AppleSymbols': 'Apple Symbols.ttf',
    #'AquaKana': 'AquaKana.ttc',
    #'AquaKana-Bold': 'AquaKana.ttc',
    'Arial-Black': 'Arial Black.ttf',
    'Arial-BoldItalicMT': 'Arial Bold Italic.ttf',
    'Arial-BoldMT': 'Arial Bold.ttf',
    'Arial-ItalicMT': 'Arial Italic.ttf',
    #'ArialHebrew': 'ArialHB.ttc',
    #'ArialHebrew-Bold': 'ArialHB.ttc',
    #'ArialHebrew-Light': 'ArialHB.ttc',
    #'ArialHebrewScholar': 'ArialHB.ttc',
    #'ArialHebrewScholar-Bold': 'ArialHB.ttc',
    #'ArialHebrewScholar-Light': 'ArialHB.ttc',
    'ArialMT': 'Arial.ttf',
    'ArialNarrow': 'Arial Narrow.ttf',
    'ArialNarrow-Bold': 'Arial Narrow Bold.ttf',
    'ArialNarrow-BoldItalic': 'Arial Narrow Bold Italic.ttf',
    'ArialNarrow-Italic': 'Arial Narrow Italic.ttf',
    'ArialRoundedMTBold': 'Arial Rounded Bold.ttf',
    'ArialUnicodeMS': 'Arial Unicode.ttf',
    #'Athelas-Bold': 'Athelas.ttc',
    #'Athelas-BoldItalic': 'Athelas.ttc',
    #'Athelas-Italic': 'Athelas.ttc',
    #'Athelas-Regular': 'Athelas.ttc',
    #'Avenir-Black': 'Avenir.ttc',
    #'Avenir-BlackOblique': 'Avenir.ttc',
    #'Avenir-Book': 'Avenir.ttc',
    #'Avenir-BookOblique': 'Avenir.ttc',
    #'Avenir-Heavy': 'Avenir.ttc',
    #'Avenir-HeavyOblique': 'Avenir.ttc',
    #'Avenir-Light': 'Avenir.ttc',
    #'Avenir-LightOblique': 'Avenir.ttc',
    #'Avenir-Medium': 'Avenir.ttc',
    #'Avenir-MediumOblique': 'Avenir.ttc',
    #'Avenir-Oblique': 'Avenir.ttc',
    #'Avenir-Roman': 'Avenir.ttc',
    #'AvenirNext-Bold': 'Avenir Next.ttc',
    #'AvenirNext-BoldItalic': 'Avenir Next.ttc',
    #'AvenirNext-DemiBold': 'Avenir Next.ttc',
    #'AvenirNext-DemiBoldItalic': 'Avenir Next.ttc',
    #'AvenirNext-Heavy': 'Avenir Next.ttc',
    #'AvenirNext-HeavyItalic': 'Avenir Next.ttc',
    #'AvenirNext-Italic': 'Avenir Next.ttc',
    #'AvenirNext-Medium': 'Avenir Next.ttc',
    #'AvenirNext-MediumItalic': 'Avenir Next.ttc',
    #'AvenirNext-Regular': 'Avenir Next.ttc',
    #'AvenirNext-UltraLight': 'Avenir Next.ttc',
    #'AvenirNext-UltraLightItalic': 'Avenir Next.ttc',
    #'AvenirNextCondensed-Bold': 'Avenir Next Condensed.ttc',
    #'AvenirNextCondensed-BoldItalic': 'Avenir Next Condensed.ttc',
    #'AvenirNextCondensed-DemiBold': 'Avenir Next Condensed.ttc',
    #'AvenirNextCondensed-DemiBoldItalic': 'Avenir Next Condensed.ttc',
    #'AvenirNextCondensed-Heavy': 'Avenir Next Condensed.ttc',
    #'AvenirNextCondensed-HeavyItalic': 'Avenir Next Condensed.ttc',
    #'AvenirNextCondensed-Italic': 'Avenir Next Condensed.ttc',
    #'AvenirNextCondensed-Medium': 'Avenir Next Condensed.ttc',
    #'AvenirNextCondensed-MediumItalic': 'Avenir Next Condensed.ttc',
    #'AvenirNextCondensed-Regular': 'Avenir Next Condensed.ttc',
    #'AvenirNextCondensed-UltraLight': 'Avenir Next Condensed.ttc',
    #'AvenirNextCondensed-UltraLightItalic': 'Avenir Next Condensed.ttc',
    'Ayuthaya': 'Ayuthaya.ttf',
    #'Baghdad': 'Baghdad.ttc',
    #'BanglaMN': 'Bangla MN.ttc',
    #'BanglaMN-Bold': 'Bangla MN.ttc',
    #'BanglaSangamMN': 'Bangla Sangam MN.ttc',
    #'BanglaSangamMN-Bold': 'Bangla Sangam MN.ttc',
    #'Baskerville': 'Baskerville.ttc',
    #'Baskerville-Bold': 'Baskerville.ttc',
    #'Baskerville-BoldItalic': 'Baskerville.ttc',
    #'Baskerville-Italic': 'Baskerville.ttc',
    #'Baskerville-SemiBold': 'Baskerville.ttc',
    #'Baskerville-SemiBoldItalic': 'Baskerville.ttc',
    'BebasNeueBold': '.37900.otf',
    #'Beirut': 'Beirut.ttc',
    'BigCaslon-Medium': 'BigCaslon.ttf',
    'BodoniOrnamentsITCTT': 'Bodoni Ornaments.ttf',
    #'BodoniSvtyTwoITCTT-Bold': 'Bodoni 72.ttc',
    #'BodoniSvtyTwoITCTT-Book': 'Bodoni 72.ttc',
    #'BodoniSvtyTwoITCTT-BookIta': 'Bodoni 72.ttc',
    #'BodoniSvtyTwoOSITCTT-Bold': 'Bodoni 72 OS.ttc',
    #'BodoniSvtyTwoOSITCTT-Book': 'Bodoni 72 OS.ttc',
    #'BodoniSvtyTwoOSITCTT-BookIt': 'Bodoni 72 OS.ttc',
    'BodoniSvtyTwoSCITCTT-Book': 'Bodoni 72 Smallcaps Book.ttf',
    'BradleyHandITCTT-Bold': 'Bradley Hand Bold.ttf',
    'Brandaris-Regular82': 'Brandaris-Regular82.otf',
    'Brandaris-Thin': 'Brandaris-Thin.otf',
    'BrushScriptMT': 'Brush Script.ttf',
    #'Chalkboard': 'Chalkboard.ttc',
    #'Chalkboard-Bold': 'Chalkboard.ttc',
    #'ChalkboardSE-Bold': 'ChalkboardSE.ttc',
    #'ChalkboardSE-Light': 'ChalkboardSE.ttc',
    #'ChalkboardSE-Regular': 'ChalkboardSE.ttc',
    'Chalkduster': 'Chalkduster.ttf',
    #'Charter-Black': 'Charter.ttc',
    #'Charter-BlackItalic': 'Charter.ttc',
    #'Charter-Bold': 'Charter.ttc',
    #'Charter-BoldItalic': 'Charter.ttc',
    #'Charter-Italic': 'Charter.ttc',
    #'Charter-Roman': 'Charter.ttc',
    #'Cochin': 'Cochin.ttc',
    #'Cochin-Bold': 'Cochin.ttc',
    #'Cochin-BoldItalic': 'Cochin.ttc',
    #'Cochin-Italic': 'Cochin.ttc',
    'ComicSansMS': 'Comic Sans MS.ttf',
    'ComicSansMS-Bold': 'Comic Sans MS Bold.ttf',
    #'Copperplate': 'Copperplate.ttc',
    #'Copperplate-Bold': 'Copperplate.ttc',
    #'Copperplate-Light': 'Copperplate.ttc',
    #'CorsivaHebrew': 'Corsiva.ttc',
    #'CorsivaHebrew-Bold': 'Corsiva.ttc',
    #'Courier': 'Courier.dfont',
    #'Courier-Bold': 'Courier.dfont',
    #'Courier-BoldOblique': 'Courier.dfont',
    #'Courier-Oblique': 'Courier.dfont',
    'CourierNewPS-BoldItalicMT': 'Courier New Bold Italic.ttf',
    'CourierNewPS-BoldMT': 'Courier New Bold.ttf',
    'CourierNewPS-ItalicMT': 'Courier New Italic.ttf',
    'CourierNewPSMT': 'Courier New.ttf',
    'DINAlternate-Bold': 'DIN Alternate Bold.ttf',
    'DINCondensed-Bold': 'DIN Condensed Bold.ttf',
    #'Damascus': 'Damascus.ttc',
    #'DamascusBold': 'Damascus.ttc',
    #'DamascusLight': 'Damascus.ttc',
    #'DamascusMedium': 'Damascus.ttc',
    #'DamascusSemiBold': 'Damascus.ttc',
    #'DecoTypeNaskh': 'DecoTypeNaskh.ttc',
    #'DevanagariMT': 'DevanagariMT.ttc',
    #'DevanagariMT-Bold': 'DevanagariMT.ttc',
    #'DevanagariSangamMN': 'Devanagari Sangam MN.ttc',
    #'DevanagariSangamMN-Bold': 'Devanagari Sangam MN.ttc',
    #'Didot': 'Didot.ttc',
    #'Didot-Bold': 'Didot.ttc',
    #'Didot-Italic': 'Didot.ttc',
    #'DiwanKufi': 'Diwan Kufi.ttc',
    'DiwanMishafi': 'Mishafi.ttf',
    'DiwanMishafiGold': 'Mishafi Gold.ttf',
    'DiwanThuluth': 'Diwan Thuluth.ttf',
    #'EuphemiaUCAS': 'EuphemiaCAS.ttc',
    #'EuphemiaUCAS-Bold': 'EuphemiaCAS.ttc',
    #'EuphemiaUCAS-Italic': 'EuphemiaCAS.ttc',
    'F5MultiLanguageFontTT-Bold': 'F5MultiLanguageFontTT-Bold.ttf',
    'F5MultiLanguageFontTT-Regular': 'F5MultiLanguageFontTT-Regular.ttf',
    'FCI-Logo-Regular': 'FCI-Logo-Regular.ttf',
    #'Farah': 'Farah.ttc',
    'Farisi': 'Farisi.ttf',
    #'Futura-Bold': 'Futura.ttc',
    #'Futura-CondensedExtraBold': 'Futura.ttc',
    #'Futura-CondensedMedium': 'Futura.ttc',
    #'Futura-Medium': 'Futura.ttc',
    #'Futura-MediumItalic': 'Futura.ttc',
    'GB18030Bitmap': 'NISC18030.ttf',
    #'GeezaPro': 'GeezaPro.ttc',
    #'GeezaPro-Bold': 'GeezaPro.ttc',
    #'Geneva': 'Geneva.dfont',
    'Georgia': 'Georgia.ttf',
    'Georgia-Bold': 'Georgia Bold.ttf',
    'Georgia-BoldItalic': 'Georgia Bold Italic.ttf',
    'Georgia-Italic': 'Georgia Italic.ttf',
    #'GillSans': 'GillSans.ttc',
    #'GillSans-Bold': 'GillSans.ttc',
    #'GillSans-BoldItalic': 'GillSans.ttc',
    #'GillSans-Italic': 'GillSans.ttc',
    #'GillSans-Light': 'GillSans.ttc',
    #'GillSans-LightItalic': 'GillSans.ttc',
    #'GillSans-SemiBold': 'GillSans.ttc',
    #'GillSans-SemiBoldItalic': 'GillSans.ttc',
    #'GillSans-UltraBold': 'GillSans.ttc',
    #'GujaratiMT': 'GujaratiMT.ttc',
    #'GujaratiMT-Bold': 'GujaratiMT.ttc',
    #'GujaratiSangamMN': 'Gujarati Sangam MN.ttc',
    #'GujaratiSangamMN-Bold': 'Gujarati Sangam MN.ttc',
    #'GurmukhiMN': 'Gurmukhi MN.ttc',
    #'GurmukhiMN-Bold': 'Gurmukhi MN.ttc',
    #'GurmukhiSangamMN': 'Gurmukhi Sangam MN.ttc',
    #'GurmukhiSangamMN-Bold': 'Gurmukhi Sangam MN.ttc',
    'HarnaschSans-SemiBold': 'HarnaschSans-SemiBold.ttf',
    #'Helvetica': 'Helvetica.dfont',
    #'Helvetica-Bold': 'Helvetica.dfont',
    #'Helvetica-BoldOblique': 'Helvetica.dfont',
    #'Helvetica-Light': 'Helvetica.dfont',
    #'Helvetica-LightOblique': 'Helvetica.dfont',
    #'Helvetica-Oblique': 'Helvetica.dfont',
    #'HelveticaNeue': 'HelveticaNeue.dfont',
    #'HelveticaNeue-Bold': 'HelveticaNeue.dfont',
    #'HelveticaNeue-BoldItalic': 'HelveticaNeue.dfont',
    #'HelveticaNeue-CondensedBlack': 'HelveticaNeue.dfont',
    #'HelveticaNeue-CondensedBold': 'HelveticaNeue.dfont',
    #'HelveticaNeue-Italic': 'HelveticaNeue.dfont',
    #'HelveticaNeue-Light': 'HelveticaNeue.dfont',
    #'HelveticaNeue-LightItalic': 'HelveticaNeue.dfont',
    #'HelveticaNeue-Medium': 'HelveticaNeue.dfont',
    #'HelveticaNeue-MediumItalic': 'HelveticaNeue.dfont',
    #'HelveticaNeue-Thin': 'HelveticaNeue.dfont',
    #'HelveticaNeue-ThinItalic': 'HelveticaNeue.dfont',
    #'HelveticaNeue-UltraLight': 'HelveticaNeue.dfont',
    #'HelveticaNeue-UltraLightItalic': 'HelveticaNeue.dfont',
    'Herculanum': 'Herculanum.ttf',
    #'HiraKakuPro-W3': 'ヒラギノ角ゴシック W3.ttc',
    #'HiraKakuPro-W6': 'ヒラギノ角ゴシック W6.ttc',
    #'HiraKakuProN-W3': 'ヒラギノ角ゴシック W3.ttc',
    #'HiraKakuProN-W6': 'ヒラギノ角ゴシック W6.ttc',
    #'HiraKakuStd-W8': 'ヒラギノ角ゴシック W8.ttc',
    #'HiraKakuStdN-W8': 'ヒラギノ角ゴシック W8.ttc',
    #'HiraMaruPro-W4': 'ヒラギノ丸ゴ ProN W4.ttc',
    #'HiraMaruProN-W4': 'ヒラギノ丸ゴ ProN W4.ttc',
    #'HiraMinPro-W3': 'ヒラギノ明朝 ProN W3.ttc',
    #'HiraMinPro-W6': 'ヒラギノ明朝 ProN W6.ttc',
    #'HiraMinProN-W3': 'ヒラギノ明朝 ProN W3.ttc',
    #'HiraMinProN-W6': 'ヒラギノ明朝 ProN W6.ttc',
    #'HiraginoSans-W0': 'ヒラギノ角ゴシック W0.ttc',
    #'HiraginoSans-W1': 'ヒラギノ角ゴシック W1.ttc',
    #'HiraginoSans-W2': 'ヒラギノ角ゴシック W2.ttc',
    #'HiraginoSans-W3': 'ヒラギノ角ゴシック W3.ttc',
    #'HiraginoSans-W4': 'ヒラギノ角ゴシック W4.ttc',
    #'HiraginoSans-W5': 'ヒラギノ角ゴシック W5.ttc',
    #'HiraginoSans-W6': 'ヒラギノ角ゴシック W6.ttc',
    #'HiraginoSans-W7': 'ヒラギノ角ゴシック W7.ttc',
    #'HiraginoSans-W8': 'ヒラギノ角ゴシック W8.ttc',
    #'HiraginoSans-W9': 'ヒラギノ角ゴシック W9.ttc',
    #'HiraginoSansGB-W3': 'Hiragino Sans GB W3.ttc',
    #'HiraginoSansGB-W6': 'Hiragino Sans GB W6.ttc',
    #'HoeflerText-Black': 'Hoefler Text.ttc',
    #'HoeflerText-BlackItalic': 'Hoefler Text.ttc',
    #'HoeflerText-Italic': 'Hoefler Text.ttc',
    'HoeflerText-Ornaments': 'Hoefler Text Ornaments.ttf',
    #'HoeflerText-Regular': 'Hoefler Text.ttc',
    #'ITFDevanagari-Bold': 'ITFDevanagari.ttc',
    #'ITFDevanagari-Book': 'ITFDevanagari.ttc',
    #'ITFDevanagari-Demi': 'ITFDevanagari.ttc',
    #'ITFDevanagari-Light': 'ITFDevanagari.ttc',
    #'ITFDevanagari-Medium': 'ITFDevanagari.ttc',
    #'ITFDevanagariMarathi-Bold': 'ITFDevanagari.ttc',
    #'ITFDevanagariMarathi-Book': 'ITFDevanagari.ttc',
    #'ITFDevanagariMarathi-Demi': 'ITFDevanagari.ttc',
    #'ITFDevanagariMarathi-Light': 'ITFDevanagari.ttc',
    #'ITFDevanagariMarathi-Medium': 'ITFDevanagari.ttc',
    'Impact': 'Impact.ttf',
    'InaiMathi': 'InaiMathi.ttf',
    'InspireTWDC-Medium': 'InspireTWDC-Medium.otf',
    #'IowanOldStyle-Black': 'Iowan Old Style.ttc',
    #'IowanOldStyle-BlackItalic': 'Iowan Old Style.ttc',
    #'IowanOldStyle-Bold': 'Iowan Old Style.ttc',
    #'IowanOldStyle-BoldItalic': 'Iowan Old Style.ttc',
    #'IowanOldStyle-Italic': 'Iowan Old Style.ttc',
    #'IowanOldStyle-Roman': 'Iowan Old Style.ttc',
    #'IowanOldStyle-Titling': 'Iowan Old Style.ttc',
    #'Kailasa': 'Kailasa.ttc',
    #'Kailasa-Bold': 'Kailasa.ttc',
    #'KannadaMN': 'Kannada MN.ttc',
    #'KannadaMN-Bold': 'Kannada MN.ttc',
    #'KannadaSangamMN': 'Kannada Sangam MN.ttc',
    #'KannadaSangamMN-Bold': 'Kannada Sangam MN.ttc',
    #'Kefa-Bold': 'Kefa.ttc',
    #'Kefa-Regular': 'Kefa.ttc',
    #'KhmerMN': 'Khmer MN.ttc',
    #'KhmerMN-Bold': 'Khmer MN.ttc',
    'KhmerSangamMN': 'Khmer Sangam MN.ttf',
    #'KohinoorBangla-Bold': 'KohinoorBangla.ttc',
    #'KohinoorBangla-Light': 'KohinoorBangla.ttc',
    #'KohinoorBangla-Medium': 'KohinoorBangla.ttc',
    #'KohinoorBangla-Regular': 'KohinoorBangla.ttc',
    #'KohinoorBangla-Semibold': 'KohinoorBangla.ttc',
    #'KohinoorDevanagari-Bold': 'Kohinoor.ttc',
    #'KohinoorDevanagari-Light': 'Kohinoor.ttc',
    #'KohinoorDevanagari-Medium': 'Kohinoor.ttc',
    #'KohinoorDevanagari-Regular': 'Kohinoor.ttc',
    #'KohinoorDevanagari-Semibold': 'Kohinoor.ttc',
    #'KohinoorTelugu-Bold': 'KohinoorTelugu.ttc',
    #'KohinoorTelugu-Light': 'KohinoorTelugu.ttc',
    #'KohinoorTelugu-Medium': 'KohinoorTelugu.ttc',
    #'KohinoorTelugu-Regular': 'KohinoorTelugu.ttc',
    #'KohinoorTelugu-Semibold': 'KohinoorTelugu.ttc',
    'Kokonor': 'Kokonor.ttf',
    'Krungthep': 'Krungthep.ttf',
    #'KufiStandardGK': 'KufiStandardGK.ttc',
    #'LaoMN': 'Lao MN.ttc',
    #'LaoMN-Bold': 'Lao MN.ttc',
    'LaoSangamMN': 'Lao Sangam MN.ttf',
    'LastResort': 'LastResort.ttf',
    #'LucidaGrande': 'LucidaGrande.ttc',
    #'LucidaGrande-Bold': 'LucidaGrande.ttc',
    'Luminari-Regular': 'Luminari.ttf',
    #'MalayalamMN': 'Malayalam MN.ttc',
    #'MalayalamMN-Bold': 'Malayalam MN.ttc',
    #'MalayalamSangamMN': 'Malayalam Sangam MN.ttc',
    #'MalayalamSangamMN-Bold': 'Malayalam Sangam MN.ttc',
    #'Marion-Bold': 'Marion.ttc',
    #'Marion-Italic': 'Marion.ttc',
    #'Marion-Regular': 'Marion.ttc',
    #'MarkerFelt-Thin': 'MarkerFelt.ttc',
    #'MarkerFelt-Wide': 'MarkerFelt.ttc',
    #'Menlo-Bold': 'Menlo.ttc',
    #'Menlo-BoldItalic': 'Menlo.ttc',
    #'Menlo-Italic': 'Menlo.ttc',
    #'Menlo-Regular': 'Menlo.ttc',
    'MicrosoftSansSerif': 'Microsoft Sans Serif.ttf',
    #'Monaco': 'Monaco.dfont',
    'MonotypeGurmukhi': 'Gurmukhi.ttf',
    'Montserrat-Black': '.37470.otf',
    'Montserrat-Medium': '.37462.otf',
    'Montserrat-SemiBold': '.37464.otf',
    #'Mshtakan': 'Mshtakan.ttc',
    #'MshtakanBold': 'Mshtakan.ttc',
    #'MshtakanBoldOblique': 'Mshtakan.ttc',
    #'MshtakanOblique': 'Mshtakan.ttc',
    #'Muna': 'Muna.ttc',
    #'MunaBlack': 'Muna.ttc',
    #'MunaBold': 'Muna.ttc',
    #'MyanmarMN': 'Myanmar MN.ttc',
    #'MyanmarMN-Bold': 'Myanmar MN.ttc',
    #'MyanmarSangamMN': 'Myanmar Sangam MN.ttc',
    #'MyanmarSangamMN-Bold': 'Myanmar Sangam MN.ttc',
    #'Nadeem': 'Nadeem.ttc',
    #'NewPeninimMT': 'NewPeninimMT.ttc',
    #'NewPeninimMT-Bold': 'NewPeninimMT.ttc',
    #'NewPeninimMT-BoldInclined': 'NewPeninimMT.ttc',
    #'NewPeninimMT-Inclined': 'NewPeninimMT.ttc',
    #'Noteworthy-Bold': 'Noteworthy.ttc',
    #'Noteworthy-Light': 'Noteworthy.ttc',
    #'Optima-Bold': 'Optima.ttc',
    #'Optima-BoldItalic': 'Optima.ttc',
    #'Optima-ExtraBlack': 'Optima.ttc',
    #'Optima-Italic': 'Optima.ttc',
    #'Optima-Regular': 'Optima.ttc',
    #'OriyaMN': 'Oriya MN.ttc',
    #'OriyaMN-Bold': 'Oriya MN.ttc',
    #'OriyaSangamMN': 'Oriya Sangam MN.ttc',
    #'OriyaSangamMN-Bold': 'Oriya Sangam MN.ttc',
    #'PTMono-Bold': 'PTMono.ttc',
    #'PTMono-Regular': 'PTMono.ttc',
    #'PTSans-Bold': 'PTSans.ttc',
    #'PTSans-BoldItalic': 'PTSans.ttc',
    #'PTSans-Caption': 'PTSans.ttc',
    #'PTSans-CaptionBold': 'PTSans.ttc',
    #'PTSans-Italic': 'PTSans.ttc',
    #'PTSans-Narrow': 'PTSans.ttc',
    #'PTSans-NarrowBold': 'PTSans.ttc',
    #'PTSans-Regular': 'PTSans.ttc',
    #'PTSerif-Bold': 'PTSerif.ttc',
    #'PTSerif-BoldItalic': 'PTSerif.ttc',
    #'PTSerif-Caption': 'PTSerifCaption.ttc',
    #'PTSerif-CaptionItalic': 'PTSerifCaption.ttc',
    #'PTSerif-Italic': 'PTSerif.ttc',
    #'PTSerif-Regular': 'PTSerif.ttc',
    #'Palatino-Bold': 'Palatino.ttc',
    #'Palatino-BoldItalic': 'Palatino.ttc',
    #'Palatino-Italic': 'Palatino.ttc',
    #'Palatino-Roman': 'Palatino.ttc',
    #'Papyrus': 'Papyrus.ttc',
    #'Papyrus-Condensed': 'Papyrus.ttc',
    #'Phosphate-Inline': 'Phosphate.ttc',
    #'Phosphate-Solid': 'Phosphate.ttc',
    #'PingFangHK-Light': 'PingFang.ttc',
    #'PingFangHK-Medium': 'PingFang.ttc',
    #'PingFangHK-Regular': 'PingFang.ttc',
    #'PingFangHK-Semibold': 'PingFang.ttc',
    #'PingFangHK-Thin': 'PingFang.ttc',
    #'PingFangHK-Ultralight': 'PingFang.ttc',
    #'PingFangSC-Light': 'PingFang.ttc',
    #'PingFangSC-Medium': 'PingFang.ttc',
    #'PingFangSC-Regular': 'PingFang.ttc',
    #'PingFangSC-Semibold': 'PingFang.ttc',
    #'PingFangSC-Thin': 'PingFang.ttc',
    #'PingFangSC-Ultralight': 'PingFang.ttc',
    #'PingFangTC-Light': 'PingFang.ttc',
    #'PingFangTC-Medium': 'PingFang.ttc',
    #'PingFangTC-Regular': 'PingFang.ttc',
    #'PingFangTC-Semibold': 'PingFang.ttc',
    #'PingFangTC-Thin': 'PingFang.ttc',
    #'PingFangTC-Ultralight': 'PingFang.ttc',
    'PlantagenetCherokee': 'PlantagenetCherokee.ttf',
    'Propcode-Regular': 'Propcode-Regular.otf',
    'ProximaNova-Regular': 'ProximaNova-Regular.otf',
    'Punch-Regular': 'Punch-Regular.otf',
    #'Raanana': 'Raanana.ttc',
    #'RaananaBold': 'Raanana.ttc',
    'SFUIDisplay-Black': 'SFDisplay-Black.otf',
    'SFUIDisplay-Bold': 'SFDisplay-Bold.otf',
    'SFUIDisplay-Heavy': 'SFDisplay-Heavy.otf',
    'SFUIDisplay-Light': 'SFDisplay-Light.otf',
    'SFUIDisplay-Medium': 'SFDisplay-Medium.otf',
    'SFUIDisplay-Regular': 'SFDisplay-Regular.otf',
    'SFUIDisplay-Semibold': 'SFDisplay-Semibold.otf',
    'SFUIDisplay-Thin': 'SFDisplay-Thin.otf',
    'SFUIDisplay-Ultralight': 'SFDisplay-Ultralight.otf',
    'SFUIText-Bold': 'SFText-Bold.otf',
    'SFUIText-BoldItalic': 'SFText-BoldItalic.otf',
    'SFUIText-Heavy': 'SFText-Heavy.otf',
    'SFUIText-HeavyItalic': 'SFText-HeavyItalic.otf',
    'SFUIText-Italic': 'SFText-RegularItalic.otf',
    'SFUIText-Light': 'SFText-Light.otf',
    'SFUIText-LightItalic': 'SFText-LightItalic.otf',
    'SFUIText-Medium': 'SFText-Medium.otf',
    'SFUIText-MediumItalic': 'SFText-MediumItalic.otf',
    'SFUIText-Regular': 'SFText-Regular.otf',
    'SFUIText-Semibold': 'SFText-Semibold.otf',
    'SFUIText-SemiboldItalic': 'SFText-SemiboldItalic.otf',
    #'STHeitiSC-Light': 'STHeiti Light.ttc',
    #'STHeitiSC-Medium': 'STHeiti Medium.ttc',
    #'STHeitiTC-Light': 'STHeiti Light.ttc',
    #'STHeitiTC-Medium': 'STHeiti Medium.ttc',
    'STIXGeneral-Bold': 'STIXGeneralBol.otf',
    'STIXGeneral-BoldItalic': 'STIXGeneralBolIta.otf',
    'STIXGeneral-Italic': 'STIXGeneralItalic.otf',
    'STIXGeneral-Regular': 'STIXGeneral.otf',
    'STIXIntegralsD-Bold': 'STIXIntDBol.otf',
    'STIXIntegralsD-Regular': 'STIXIntDReg.otf',
    'STIXIntegralsSm-Bold': 'STIXIntSmBol.otf',
    'STIXIntegralsSm-Regular': 'STIXIntSmReg.otf',
    'STIXIntegralsUp-Bold': 'STIXIntUpBol.otf',
    'STIXIntegralsUp-Regular': 'STIXIntUpReg.otf',
    'STIXIntegralsUpD-Bold': 'STIXIntUpDBol.otf',
    'STIXIntegralsUpD-Regular': 'STIXIntUpDReg.otf',
    'STIXIntegralsUpSm-Bold': 'STIXIntUpSmBol.otf',
    'STIXIntegralsUpSm-Regular': 'STIXIntUpSmReg.otf',
    'STIXNonUnicode-Bold': 'STIXNonUniBol.otf',
    'STIXNonUnicode-BoldItalic': 'STIXNonUniBolIta.otf',
    'STIXNonUnicode-Italic': 'STIXNonUniIta.otf',
    'STIXNonUnicode-Regular': 'STIXNonUni.otf',
    'STIXSizeFiveSym-Regular': 'STIXSizFiveSymReg.otf',
    'STIXSizeFourSym-Bold': 'STIXSizFourSymBol.otf',
    'STIXSizeFourSym-Regular': 'STIXSizFourSymReg.otf',
    'STIXSizeOneSym-Bold': 'STIXSizOneSymBol.otf',
    'STIXSizeOneSym-Regular': 'STIXSizOneSymReg.otf',
    'STIXSizeThreeSym-Bold': 'STIXSizThreeSymBol.otf',
    'STIXSizeThreeSym-Regular': 'STIXSizThreeSymReg.otf',
    'STIXSizeTwoSym-Bold': 'STIXSizTwoSymBol.otf',
    'STIXSizeTwoSym-Regular': 'STIXSizTwoSymReg.otf',
    'STIXVariants-Bold': 'STIXVarBol.otf',
    'STIXVariants-Regular': 'STIXVar.otf',
    #'STSong': 'Songti.ttc',
    #'STSongti-SC-Black': 'Songti.ttc',
    #'STSongti-SC-Bold': 'Songti.ttc',
    #'STSongti-SC-Light': 'Songti.ttc',
    #'STSongti-SC-Regular': 'Songti.ttc',
    #'STSongti-TC-Bold': 'Songti.ttc',
    #'STSongti-TC-Light': 'Songti.ttc',
    #'STSongti-TC-Regular': 'Songti.ttc',
    #'Sana': 'Sana.ttc',
    'Sathu': 'Sathu.ttf',
    #'SavoyeLetPlain': 'Savoye LET.ttc',
    #'Seravek': 'Seravek.ttc',
    #'Seravek-Bold': 'Seravek.ttc',
    #'Seravek-BoldItalic': 'Seravek.ttc',
    #'Seravek-ExtraLight': 'Seravek.ttc',
    #'Seravek-ExtraLightItalic': 'Seravek.ttc',
    #'Seravek-Italic': 'Seravek.ttc',
    #'Seravek-Light': 'Seravek.ttc',
    #'Seravek-LightItalic': 'Seravek.ttc',
    #'Seravek-Medium': 'Seravek.ttc',
    #'Seravek-MediumItalic': 'Seravek.ttc',
    #'ShreeDev0714': 'Shree714.ttc',
    #'ShreeDev0714-Bold': 'Shree714.ttc',
    #'ShreeDev0714-Bold-Italic': 'Shree714.ttc',
    #'ShreeDev0714-Italic': 'Shree714.ttc',
    #'SignPainter-HouseScript': 'SignPainter.ttc',
    #'SignPainter-HouseScriptSemibold': 'SignPainter.ttc',
    'Silom': 'Silom.ttf',
    #'SinhalaMN': 'Sinhala MN.ttc',
    #'SinhalaMN-Bold': 'Sinhala MN.ttc',
    #'SinhalaSangamMN': 'Sinhala Sangam MN.ttc',
    #'SinhalaSangamMN-Bold': 'Sinhala Sangam MN.ttc',
    'Skia-Regular': 'Skia.ttf',
    'Skia-Regular_Black': 'Skia.ttf',
    'Skia-Regular_Black-Condensed': 'Skia.ttf',
    'Skia-Regular_Black-Extended': 'Skia.ttf',
    'Skia-Regular_Bold': 'Skia.ttf',
    'Skia-Regular_Condensed': 'Skia.ttf',
    'Skia-Regular_Extended': 'Skia.ttf',
    'Skia-Regular_Light': 'Skia.ttf',
    'Skia-Regular_Light-Condensed': 'Skia.ttf',
    'Skia-Regular_Light-Extended': 'Skia.ttf',
    #'SnellRoundhand': 'SnellRoundhand.ttc',
    #'SnellRoundhand-Black': 'SnellRoundhand.ttc',
    #'SnellRoundhand-Bold': 'SnellRoundhand.ttc',
    'SourceSansPro-Bold': '.17267.otf',
    'SourceSansPro-Regular': '.17265.otf',
    'SourceSansPro-Semibold': '.17272.otf',
    #'SukhumvitSet-Bold': 'SukhumvitSet.ttc',
    #'SukhumvitSet-Light': 'SukhumvitSet.ttc',
    #'SukhumvitSet-Medium': 'SukhumvitSet.ttc',
    #'SukhumvitSet-SemiBold': 'SukhumvitSet.ttc',
    #'SukhumvitSet-Text': 'SukhumvitSet.ttc',
    #'SukhumvitSet-Thin': 'SukhumvitSet.ttc',
    #'Superclarendon-Black': 'SuperClarendon.ttc',
    #'Superclarendon-BlackItalic': 'SuperClarendon.ttc',
    #'Superclarendon-Bold': 'SuperClarendon.ttc',
    #'Superclarendon-BoldItalic': 'SuperClarendon.ttc',
    #'Superclarendon-Italic': 'SuperClarendon.ttc',
    #'Superclarendon-Light': 'SuperClarendon.ttc',
    #'Superclarendon-LightItalic': 'SuperClarendon.ttc',
    #'Superclarendon-Regular': 'SuperClarendon.ttc',
    'Symbol': 'Symbol.ttf',
    'TBGothic-Heavy': 'TBGothicH.otf',
    'TBGothic-SuperLight': 'TBGothicSL.otf',
    'TYPETRLogo-Circle64': 'TYPETR_Logo_Circle.otf',
    'TYPETRLogo-Inline': 'TYPETR_Logo_Inline.otf',
    'Tahoma': 'Tahoma.ttf',
    'Tahoma-Bold': 'Tahoma Bold.ttf',
    #'TamilMN': 'Tamil MN.ttc',
    #'TamilMN-Bold': 'Tamil MN.ttc',
    #'TamilSangamMN': 'Tamil Sangam MN.ttc',
    #'TamilSangamMN-Bold': 'Tamil Sangam MN.ttc',
    #'TeluguMN': 'Telugu MN.ttc',
    #'TeluguMN-Bold': 'Telugu MN.ttc',
    #'TeluguSangamMN': 'Telugu Sangam MN.ttc',
    #'TeluguSangamMN-Bold': 'Telugu Sangam MN.ttc',
    #'Thonburi': 'Thonburi.ttc',
    #'Thonburi-Bold': 'Thonburi.ttc',
    #'Thonburi-Light': 'Thonburi.ttc',
    #'Times-Bold': 'Times.dfont',
    #'Times-BoldItalic': 'Times.dfont',
    #'Times-Italic': 'Times.dfont',
    #'Times-Roman': 'Times.dfont',
    'TimesNewRomanPS-BoldItalicMT': 'Times New Roman Bold Italic.ttf',
    'TimesNewRomanPS-BoldMT': 'Times New Roman Bold.ttf',
    'TimesNewRomanPS-ItalicMT': 'Times New Roman Italic.ttf',
    'TimesNewRomanPSMT': 'Times New Roman.ttf',
    'Trattatello': 'Trattatello.ttf',
    'Trebuchet-BoldItalic': 'Trebuchet MS Bold Italic.ttf',
    'TrebuchetMS': 'Trebuchet MS.ttf',
    'TrebuchetMS-Bold': 'Trebuchet MS Bold.ttf',
    'TrebuchetMS-Italic': 'Trebuchet MS Italic.ttf',
    'UpgradeTry-Black': 'Upgrade_Try-Black.ttf',
    'UpgradeTry-BlackItalic': 'Upgrade_Try-Black_Italic.ttf',
    'UpgradeTry-Bold': 'Upgrade_Try-Bold.ttf',
    'UpgradeTry-BoldItalic': 'Upgrade_Try-Bold_Italic.ttf',
    'UpgradeTry-Book': 'Upgrade_Try-Book.ttf',
    'UpgradeTry-BookItalic': 'Upgrade_Try-Book_Italic.ttf',
    'UpgradeTry-ExtraBlack': 'Upgrade_Try-ExtraBlack.ttf',
    'UpgradeTry-ExtraBlackItalic': 'Upgrade_Try-ExtraBlack_Italic.ttf',
    'UpgradeTry-ExtraLight': 'Upgrade_Try-ExtraLight.ttf',
    'UpgradeTry-ExtraLightItalic': 'Upgrade_Try-ExtraLight_Italic.ttf',
    'UpgradeTry-Hairline': 'Upgrade_Try-Hairline.ttf',
    'UpgradeTry-HairlineItalic': 'Upgrade_Try-Hairline_Italic.ttf',
    'UpgradeTry-Italic': 'Upgrade_Try-Italic.ttf',
    'UpgradeTry-Light': 'Upgrade_Try-Light.ttf',
    'UpgradeTry-LightItalic': 'Upgrade_Try-Light_Italic.ttf',
    'UpgradeTry-Medium': 'Upgrade_Try-Medium.ttf',
    'UpgradeTry-MediumItalic': 'Upgrade_Try-Medium_Italic.ttf',
    'UpgradeTry-Regular': 'Upgrade_Try-Regular.ttf',
    'UpgradeTry-Semibold': 'Upgrade_Try-Semibold.ttf',
    'UpgradeTry-SemiboldItalic': 'Upgrade_Try-Semibold_Italic.ttf',
    'UpgradeTry-Semibook': 'Upgrade_Try-Semibook.ttf',
    'UpgradeTry-SemibookItalic': 'Upgrade_Try-Semibook_Italic.ttf',
    'UpgradeTry-Semilight': 'Upgrade_Try-Semilight.ttf',
    'UpgradeTry-SemilightItalic': 'Upgrade_Try-Semilight_Italic.ttf',
    'UpgradeTry-Semimedium': 'Upgrade_Try-Semimedium.ttf',
    'UpgradeTry-SemimediumItalic': 'Upgrade_Try-Semimedium_Italic.ttf',
    'UpgradeTry-Thin': 'Upgrade_Try-Thin.ttf',
    'UpgradeTry-ThinItalic': 'Upgrade_Try-Thin_Italic.ttf',
    'UpgradeTry-UltraBlack': 'Upgrade_Try-UltraBlack.ttf',
    'UpgradeTry-UltraBlackItalic': 'Upgrade_Try-UltraBlack_Italic.ttf',
    'Verdana': 'Verdana.ttf',
    'Verdana-Bold': 'Verdana Bold.ttf',
    'Verdana-BoldItalic': 'Verdana Bold Italic.ttf',
    'Verdana-Italic': 'Verdana Italic.ttf',
    #'Waseem': 'Waseem.ttc',
    #'WaseemLight': 'Waseem.ttc',
    'Webdings': 'Webdings.ttf',
    'Wingdings-Regular': 'Wingdings.ttf',
    'Wingdings2': 'Wingdings 2.ttf',
    'Wingdings3': 'Wingdings 3.ttf',
    'ZapfDingbatsITC': 'ZapfDingbats.ttf',
    'Zapfino': 'Zapfino.ttf',
}

if __name__ == '__main__':
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
