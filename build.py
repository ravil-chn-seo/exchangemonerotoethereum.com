from pathlib import Path
from html import escape
import json, shutil

ROOT = Path(__file__).parent
SRC = ROOT / 'src'
OUT = ROOT / 'dist'

DOMAIN = 'exchangemonerotoethereum.com'
SITE = f'https://{DOMAIN}/'
CN = 'https://changenow.io/currencies/monero/ethereum'
CN_REL = 'sponsored nofollow noopener noreferrer'  # Variant B: independent site with affiliate links
REVIEWED = 'November 3, 2026'
ISO_DATE = '2026-11-03'

TITLE = 'Best Ways to Exchange Monero to Ethereum (XMR to ETH)'
DESCRIPTION = 'Compare five XMR to ETH exchange services. See why ChangeNOW is our best overall choice and learn how to exchange Monero for Ethereum step by step.'
OG_DESCRIPTION = 'Compare XMR to ETH exchange services and learn why ChangeNOW is our best overall choice.'
OG_IMAGE = f'{SITE}assets/xmr-to-eth-guide.webp'


def e(text):
    return escape(text, quote=True)


def cn_link(label, loc, cls='btn btn-dark'):
    return (f'<a class="{cls}" href="{CN}" target="_blank" rel="{CN_REL}" data-cta="{loc}">'
            f'<span>{e(label)}</span></a>')


# ---------------------------------------------------------------- content

fact_strip = [
    ('1,000+', 'digital assets on ChangeNOW'),
    ('1M+', 'supported exchange pairs'),
    ('110', 'blockchains supported'),
    ('98%', 'Triumph Rate within a 0.5% deviation or better'),
]

comparison_head = ['Rank', 'Service', 'Best for', 'XMR → ETH', 'Rate options',
                   'Account for standard swap', 'Support', 'Score']
comparison_rows = [
    ['1', 'ChangeNOW', 'Best overall', 'Available', 'Fixed and floating', 'Not required', '24/7', '9.4/10'],
    ['2', 'SimpleSwap', 'Broad coin coverage', 'Available', 'Fixed and floating', 'Not required', '24/7', '9.0/10'],
    ['3', 'StealthEX', 'Simple wallet-to-wallet flow', 'Available', 'Fixed and floating where offered', 'Not required', 'Customer support available', '8.7/10'],
    ['4', 'ChangeHero', 'Straightforward four-step exchange', 'Available', 'Best Rate and Fixed Rate', 'Not required', '24/7', '8.4/10'],
    ['5', 'Exolix', 'Minimal pair interface', 'Available', 'Check the live offer', 'Not required', '24/7 assistance stated', '8.1/10'],
]

why_cards = [
    ('Direct XMR to ETH route', 'Monero and Ethereum can be selected as the source and destination assets without using an order book or making an intermediate trade manually.'),
    ('Fixed and floating rates', 'Floating mode follows current market conditions. Fixed mode is intended to preserve the agreed output under the conditions shown for the exchange.'),
    ('Upfront estimate', 'The estimated ETH output and included costs are shown before the user sends the XMR deposit.'),
    ('Broad coverage', 'ChangeNOW lists more than 1,000 digital assets, more than one million exchange pairs and support across 110 blockchains.'),
    ('No upper swap limit', 'ChangeNOW does not publish a maximum amount for standard crypto-to-crypto swaps. The live minimum still depends on the pair, liquidity and network costs.'),
    ('24/7 support', 'Support is available around the clock, including assistance with complex transaction issues.'),
]

reviews = [
    {
        'id': 'review-changenow', 'rank': 1, 'award': '#1 · Best Overall', 'name': 'ChangeNOW', 'featured': True,
        'paras': [
            'ChangeNOW is our top XMR-to-ETH choice for users who want a direct exchange with a clear estimate and a choice between fixed and floating rates. The standard flow does not require account registration: select XMR and ETH, enter an Ethereum address, review the estimate and send the Monero deposit.',
            'The service stands out for the combination of route coverage and execution options. It supports more than 1,000 assets, more than one million pairs and 110 blockchains. ChangeNOW also publishes a 98% Triumph Rate, meaning swaps over the measured period were completed at a better rate than estimated or within a deviation of less than 0.5%.',
            'Users should still treat the displayed amount as an estimate when choosing a floating rate. Monero confirmation time, market movement and liquidity can change the result. Fixed mode is the better fit when output certainty matters more than following the live market.',
        ],
        'facts': [('Rate modes', 'Fixed and floating'), ('Account', 'Not required for a standard swap'),
                  ('Asset coverage', '1,000+ digital assets'), ('Upper swap limit', 'None published'),
                  ('Support', '24/7'), ('Our score', '9.4/10')],
        'best': 'Most users who want a balanced mix of simplicity, rate choice, broad coverage and support.',
        'consider': 'The average exchange time is not a guarantee for a specific XMR-to-ETH transaction.',
        'cta': 'Exchange XMR to ETH on ChangeNOW',
    },
    {
        'id': 'review-simpleswap', 'rank': 2, 'award': '#2 · Best for Broad Coin Coverage', 'name': 'SimpleSwap',
        'paras': [
            'SimpleSwap is a strong alternative for users who value a large catalogue of supported assets. Its official information describes a self-custodial multi-source swap aggregator with more than 2,800 cryptocurrencies and 3.2 million trading pairs. The service displayed a direct XMR-to-ETH page during our review.',
            'The interface provides fixed and floating rate options and does not require users to create an account for a standard swap. Its broad coverage makes SimpleSwap particularly useful when a user expects to exchange less common assets before or after the XMR-to-ETH transaction.',
            'ChangeNOW ranks higher in this comparison because we found its combination of exchange flow, published operational metrics, broad blockchain coverage and support evidence stronger for this specific route. A live quote comparison may still favor either provider at a particular moment.',
        ],
        'facts': [('Rate modes', 'Fixed and floating'), ('Account', 'Not required for a standard swap'),
                  ('Asset coverage', '2,800+ cryptocurrencies stated'), ('Support', '24/7'), ('Our score', '9.0/10')],
        'best': 'Users who prioritize the widest possible asset catalogue.',
        'consider': 'Always compare the final ETH estimate for the same XMR amount immediately before exchanging.',
    },
    {
        'id': 'review-stealthex', 'rank': 3, 'award': '#3 · Best for a Minimal Wallet-to-Wallet Flow', 'name': 'StealthEX',
        'paras': [
            'StealthEX offers a dedicated Monero-to-Ethereum route and a straightforward exchange process: choose the currencies, enter the receiving wallet address, send the deposit and wait for the payout. Its pair page states that fixed and floating options may be available and that no account is required for a standard exchange.',
            'The service emphasizes wallet-to-wallet swaps and lists more than 2,000 coins and tokens. This makes it a credible alternative for users who want a simple interface with relatively broad coin support.',
            'It ranks below ChangeNOW and SimpleSwap because its public pair page makes several broad marketing claims that users should verify against the live offer and current terms. We give more weight to a clearly presented estimate, documented service metrics and a balanced explanation of transaction conditions.',
        ],
        'facts': [('XMR → ETH route', 'Available during review'), ('Rate modes', 'Fixed and floating where offered'),
                  ('Account', 'Not required for a standard swap'), ('Asset coverage', '2,000+ coins and tokens stated'),
                  ('Our score', '8.7/10')],
        'best': 'Users who want a minimal pair-focused interface.',
        'consider': 'Do not rely on general privacy or speed claims; read the live exchange terms for the specific transaction.',
    },
    {
        'id': 'review-changehero', 'rank': 4, 'award': '#4 · Best for a Guided Four-Step Swap', 'name': 'ChangeHero',
        'paras': [
            'ChangeHero displayed an active XMR-to-ETH route and organizes the exchange into four clear steps: enter the amount, provide the ETH address, confirm the transaction and receive the payout. It offers a Best Rate mode and a Fixed Rate mode and does not require an account for a standard exchange.',
            'The service states support for more than 300 cryptocurrencies and provides round-the-clock assistance. Its focused interface can work well for users who prefer a guided process over a feature-heavy platform.',
            'ChangeHero ranks fourth because its supported-asset catalogue is smaller than the leading services in this comparison. Its official page also states percentage-based fee ceilings for its two rate modes, but the most useful comparison remains the final ETH output offered for the same XMR amount.',
        ],
        'facts': [('Rate modes', 'Best Rate and Fixed Rate'), ('Account', 'Not required for a standard swap'),
                  ('Asset coverage', '300+ cryptocurrencies stated'), ('Support', '24/7'), ('Our score', '8.4/10')],
        'best': 'Users who prefer a guided four-step exchange.',
        'consider': 'Compare the final expected output rather than a headline fee percentage alone.',
    },
    {
        'id': 'review-exolix', 'rank': 5, 'award': '#5 · Best for a Simple Pair Page', 'name': 'Exolix',
        'paras': [
            'Exolix provides a dedicated XMR-to-ETH pair page with a minimal exchange interface. The route was listed as available during our review, and the service presents the expected amount before the user proceeds to the wallet and deposit stages.',
            'This uncluttered format may appeal to users who already understand cross-chain exchanges and do not need much guidance. Exolix also states that account creation is not required for its standard exchange flow.',
            'It ranks fifth because the public information available for a route-level comparison is less detailed than the documentation offered by the higher-ranked services. Users should confirm the rate type, minimum amount, expected processing time and support conditions in the live form before sending XMR.',
        ],
        'facts': [('XMR → ETH route', 'Available during review'), ('Account', 'Not required for a standard swap'),
                  ('Quote', 'Shown in the live exchange flow'), ('Our score', '8.1/10')],
        'best': 'Experienced users who want a minimal exchange page.',
        'consider': 'Verify all transaction conditions in the live form because public route-level details are limited.',
    },
]

criteria = [
    ('Pair availability', 20, 'Whether a direct XMR-to-ETH route was available during review'),
    ('Quote and cost transparency', 20, 'Whether the estimated ETH output and included costs were visible before deposit'),
    ('Exchange speed', 15, 'Published timing, clarity of conditions and dependence on network confirmations'),
    ('Ease of use', 15, 'Number of steps, form clarity and whether an account was required for a standard swap'),
    ('Rate options', 10, 'Availability and explanation of fixed and floating modes'),
    ('Limits and coverage', 10, 'Live minimum, maximum policy, asset catalogue and blockchain coverage'),
    ('Support and reputation', 10, 'Support availability, public documentation and review evidence'),
]

compare_steps = [
    'Open each service within the same 10–15 minute window.',
    'Enter the same XMR amount on every service.',
    'Select the same rate type where possible.',
    'Record the estimated ETH output before sending funds.',
    'Check whether network and service costs are already included.',
    'Compare the live minimum and expected completion conditions.',
    'Recheck the wallet address and final estimate before choosing a provider.',
]

howto_steps = [
    ('Select Monero and Ethereum', 'Open the XMR-to-ETH exchange page. Choose Monero as the asset you send and Ethereum as the asset you receive. Enter the XMR amount. The form will display the live minimum and estimated ETH output.'),
    ('Choose a rate mode', 'Use floating mode if you want the exchange to follow current market conditions. Choose fixed mode when it is available and receiving the agreed amount matters more than tracking short-term market movement. Read the conditions shown in the live form.'),
    ('Enter your Ethereum address', 'Paste the destination ETH address from your own wallet. Compare the first and last characters with the original address. Confirm that the exchange form is sending native ETH on the Ethereum network. Do not enter a Monero address or select a wrapped ETH version on another network by mistake.'),
    ('Review, send XMR and track the exchange', 'Confirm the pair, amount, rate mode and ETH address. Send the required Monero amount to the generated deposit address. If the sending wallet asks for transaction details, follow the instructions shown in the live exchange form. Keep the exchange ID and follow the status until the native ETH payout reaches your wallet.'),
]

vs_head = ['Feature', 'Monero (XMR)', 'Ethereum (ETH)']
vs_rows = [
    ['Blockchain visibility', 'Privacy features conceal sender, recipient and amount data', 'Addresses, transfers and amounts are publicly visible on-chain'],
    ['Address type', 'Monero-compatible address', 'Ethereum-compatible 0x address'],
    ['Asset role in this exchange', 'Deposit asset', 'Payout asset'],
    ['Main user check', 'Correct XMR deposit amount and exchange instructions', 'Correct ETH address and Ethereum network'],
    ['Reversibility', 'Blockchain transfers are irreversible', 'Blockchain transfers are irreversible'],
]

rate_cards = [
    ('Exchange rate', 'The XMR-to-ETH rate shows how much Ethereum you can receive for a given amount of Monero. It changes with market prices, liquidity and the selected rate mode.'),
    ('Included costs', 'ChangeNOW states that all costs are built into the estimate shown before the swap, with no additional charge added after the exchange. Compare final ETH output rather than a headline fee alone.'),
    ('Processing time', 'ChangeNOW publishes an overall average exchange time of about one minute, but an XMR-to-ETH swap can take longer because it starts after the required Monero confirmations and depends on network and liquidity conditions.'),
]

safety_items = [
    'Confirm that XMR is the deposit asset and ETH is the payout asset.',
    'Use an Ethereum-compatible receiving wallet that you control.',
    'Confirm that the payout is native ETH on the Ethereum network.',
    'Copy the ETH address instead of typing it manually.',
    'Compare the first and last characters after pasting the address.',
    'Review the live minimum and estimated ETH output.',
    'Check whether you selected a fixed or floating rate.',
    'Send exactly the amount requested by the exchange form.',
    'Save the exchange ID until the ETH payout arrives.',
    'Consider a smaller test exchange when the transaction size justifies it.',
    'Contact support through the service’s official domain only.',
]

faq = [
    ('What is the best way to exchange Monero for Ethereum?',
     'ChangeNOW is our best overall choice for exchanging XMR to ETH. It offers a direct route, fixed and floating rate modes, an upfront estimate, no required account for a standard swap and 24/7 support. The best live quote can still change, so compare the final ETH output immediately before sending Monero.'),
    ('Can I exchange XMR to ETH without creating an account?',
     'Yes. ChangeNOW and the other services in this comparison state that account registration is not required for a standard XMR-to-ETH exchange. This does not mean a transaction can never be reviewed. Providers may apply risk-based checks under their terms, policies and legal obligations.'),
    ('How long does an XMR to ETH exchange take?',
     'The exact time depends on Monero confirmations, Ethereum processing, liquidity and network congestion. ChangeNOW publishes an overall average exchange time of about one minute, but XMR-to-ETH transactions can take longer. Delivery is usually expected within one hour, although this is not a guarantee for every swap.'),
    ('What is the minimum XMR to ETH exchange amount?',
     'The minimum is dynamic because it depends on network costs, liquidity and the live exchange conditions. ChangeNOW states that minimums can be as low as the equivalent of $2, but users should rely on the current minimum displayed in the XMR-to-ETH form.'),
    ('Are XMR to ETH exchanges anonymous?',
     'No provider can guarantee that the entire exchange is anonymous. Monero conceals transaction details within its own network, but the exchange service may retain operational records and apply risk-based controls. The ETH payout and subsequent activity are publicly visible on the Ethereum blockchain.'),
    ('What fees apply when converting Monero to Ethereum?',
     'Costs depend on network conditions, liquidity, the exchange amount and rate mode. ChangeNOW says its costs are included in the estimate shown before the swap. To compare providers fairly, enter the same XMR amount and compare the final estimated ETH output rather than looking only at a headline fee.'),
    ('Should I choose a fixed or floating XMR-to-ETH rate?',
     'Choose fixed mode when receiving the agreed output is the priority and the live conditions are acceptable. Choose floating mode when you prefer the transaction to follow the market during processing. A floating result can differ from the initial estimate, while fixed mode may show a different starting quote.'),
    ('What happens if I enter the wrong Ethereum address?',
     'The payout may be sent to the wrong destination and can be impossible to recover. Check that the wallet supports Ethereum, paste the address carefully and compare its first and last characters before starting the exchange. Contact support immediately if you notice an error, but recovery cannot be guaranteed.'),
    ('Which Ethereum network will I receive ETH on?',
     'Use the network displayed in the live exchange form. For this landing page, the intended destination is native ETH on the Ethereum network, not a wrapped or bridged ETH version on another chain. Confirm the selected asset and network before entering the receiving address.'),
    ('Can I cancel the exchange after sending Monero?',
     'Usually not. Once the Monero deposit has been broadcast and confirmed, the blockchain transfer cannot be reversed. Review the pair, amount, rate mode and receiving address before sending funds.'),
    ('Can I exchange Ethereum back to Monero later?',
     'Yes, when the reverse ETH-to-XMR route is available. You will need a Monero-compatible receiving address and enough native ETH to meet the current minimum and cover the sending network fee. Rates, liquidity and network conditions will be recalculated for the new transaction.'),
]

nav = [('#comparison', 'Comparison'), ('#reviews', 'Reviews'), ('#methodology', 'Methodology'),
       ('#how-to', 'How to Exchange'), ('#faq', 'FAQ')]

# ---------------------------------------------------------------- JSON-LD

graph = {
    '@context': 'https://schema.org',
    '@graph': [
        {'@type': 'WebPage', '@id': f'{SITE}#webpage', 'url': SITE, 'name': TITLE, 'description': DESCRIPTION,
         'inLanguage': 'en-US', 'datePublished': ISO_DATE, 'dateModified': ISO_DATE,
         'breadcrumb': {'@id': f'{SITE}#breadcrumbs'}},
        {'@type': 'ItemList', '@id': f'{SITE}#ranking', 'name': 'Best services for exchanging Monero to Ethereum',
         'itemListOrder': 'https://schema.org/ItemListOrderAscending', 'numberOfItems': len(reviews),
         'itemListElement': [{'@type': 'ListItem', 'position': r['rank'], 'name': r['name'],
                              'url': f"{SITE}#{r['id']}"} for r in reviews]},
        {'@type': 'FAQPage', '@id': f'{SITE}#faq',
         'mainEntity': [{'@type': 'Question', 'name': q,
                         'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faq]},
        {'@type': 'BreadcrumbList', '@id': f'{SITE}#breadcrumbs',
         'itemListElement': [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE},
                             {'@type': 'ListItem', 'position': 2, 'name': 'XMR to ETH Exchange', 'item': SITE}]},
    ],
}
jsonld = json.dumps(graph, ensure_ascii=False).replace('<', '\\u003c')

# ---------------------------------------------------------------- HTML parts


def table_rows():
    out = []
    for r in comparison_rows:
        first = r[0] == '1'
        cells = [f'<td class="c-rank s1">{e(r[0])}</td>']
        svc = f'<strong>{e(r[1])}</strong>' + ('<span class="pick">Our pick</span>' if first else '')
        cells.append(f'<th scope="row" class="c-svc s2">{svc}</th>')
        for i, v in enumerate(r[2:], start=2):
            if i == len(r) - 1:
                pct = int(round(float(v.split('/')[0]) * 10))
                cells.append(f'<td class="c-score" style="--s:{pct}%">{e(v)}</td>')
            else:
                cells.append(f'<td>{e(v)}</td>')
        out.append(f'<tr class="{"top" if first else ""}">{"".join(cells)}</tr>')
    return '\n'.join(out)


def review_card(r):
    facts = ''.join(f'<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in r['facts'])
    paras = ''.join(f'<p>{e(p)}</p>' for p in r['paras'])
    cta = f'<div class="review-cta">{cn_link(r["cta"], "review")}</div>' if r.get('cta') else ''
    feat = ' featured' if r.get('featured') else ''
    return f'''<article class="review{feat}" id="{r['id']}">
  <div class="review-bar" aria-hidden="true"><i></i><i></i><i></i><span>review/{r['name'].lower()}.md</span></div>
  <div class="review-rank" aria-hidden="true">{r['rank']}</div>
  <div class="review-body">
    <p class="award">{e(r['award'])}</p>
    <h3>{e(r['name'])}</h3>
    {paras}
    <dl class="facts">{facts}</dl>
    <div class="review-notes">
      <div><h4>Best for</h4><p>{e(r['best'])}</p></div>
      <div><h4>Consideration</h4><p>{e(r['consider'])}</p></div>
    </div>
    {cta}
  </div>
</article>'''


def faq_items():
    out = []
    for i, (q, a) in enumerate(faq, start=1):
        out.append(f'''<div class="faq-item">
  <h3><button class="faq-q" type="button" id="faq-q{i}" aria-expanded="{'true' if i == 1 else 'false'}" aria-controls="faq-a{i}">{e(q)}</button></h3>
  <div class="faq-a" id="faq-a{i}" role="region" aria-labelledby="faq-q{i}"><p>{e(a)}</p></div>
</div>''')
    return '\n'.join(out)


weight_colors = ['#2EBD85', '#17201D', '#627EEA', '#FF6600', '#5E6673', '#9AA3AE', '#C5CCD3']
bar = ''.join(f'<span style="width:{w}%;background:{weight_colors[i]}" title="{e(n)} {w}%"></span>'
              for i, (n, w, _) in enumerate(criteria))
legend = ''.join(f'<li><i style="background:{weight_colors[i]}"></i><span>{e(n)}</span><b>{w}%</b></li>'
                 for i, (n, w, _) in enumerate(criteria))
crit_rows = ''.join(f'<tr><th scope="row">{e(n)}</th><td>{w}%</td><td>{e(d)}</td></tr>' for n, w, d in criteria)

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="{DESCRIPTION}">
<link rel="canonical" href="{SITE}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="theme-color" content="#07090B">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta property="og:type" content="website">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{OG_DESCRIPTION}">
<meta property="og:url" content="{SITE}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{TITLE}">
<meta name="twitter:description" content="{OG_DESCRIPTION}">
<meta name="twitter:image" content="{OG_IMAGE}">
<link rel="preload" href="/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts/fonts.css">
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">{jsonld}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="site-header">
  <div class="wrap header-in">
    <a class="logo" href="/" aria-label="XMR → ETH Guide, home"><span class="logo-mark" aria-hidden="true"></span>XMR → ETH Guide</a>
    <nav class="nav-desktop" aria-label="Primary">
      {''.join(f'<a href="{h}">{t}</a>' for h, t in nav)}
    </nav>
    <div class="header-actions">
      {cn_link('Exchange XMR to ETH', 'header', 'btn btn-dark btn-sm')}
      <details class="menu">
        <summary aria-label="Open menu"><span class="burger" aria-hidden="true"></span></summary>
        <nav aria-label="Mobile">{''.join(f'<a href="{h}">{t}</a>' for h, t in nav)}</nav>
      </details>
    </div>
  </div>
</header>

<main id="main">

<section class="hero" aria-labelledby="h1">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="label"><i aria-hidden="true"></i>Independently scored using a published methodology</p>
      <h1 id="h1">Best Ways to Exchange <span class="t-xmr">Monero</span> to <span class="t-eth">Ethereum</span> (XMR to ETH)</h1>
      <p class="lead"><a href="{CN}" target="_blank" rel="{CN_REL}" data-cta="hero">ChangeNOW is our best overall choice</a> for exchanging Monero to Ethereum. It combines a direct three-step swap flow with fixed and floating rate options, upfront pricing, broad asset coverage and 24/7 support. Among the five services reviewed, it offers the strongest overall balance of route availability, transparency, speed and ease of use.</p>
      <ul class="chips">
        <li>Best overall score: 9.4/10</li>
        <li>Fixed and floating rates</li>
        <li>No account required for a standard swap</li>
        <li>24/7 human support</li>
      </ul>
      <div class="hero-actions">
        {cn_link('Exchange XMR to ETH on ChangeNOW', 'hero', 'btn btn-dark btn-lg hero-cta')}
        <a class="btn btn-light btn-lg" href="#comparison">See the comparison</a>
      </div>
      <p class="micro">Last reviewed: {REVIEWED}. Pair availability, minimum amounts and estimates can change. Check the live exchange form before sending funds.</p>
    </div>
    <a class="xcard" href="{CN}" target="_blank" rel="{CN_REL}" data-cta="hero" aria-label="Open the live XMR to ETH exchange form on ChangeNOW">
      <span class="xbar" aria-hidden="true"><i></i><i></i><i></i><em>route / xmr-eth</em></span>
      <span class="xcard-title">XMR to ETH exchange</span>
      <span class="route" aria-hidden="true"><i class="node n-xmr">XMR</i><i class="wire"><b></b><b></b><b></b></i><i class="node n-eth">ETH</i></span>
      <span class="field">
        <span class="field-text"><small>You send</small><b>XMR — Monero</b></span>
        <span class="coin coin-xmr" aria-hidden="true">XMR</span>
      </span>
      <span class="swap-row"><span class="swap-icon" aria-hidden="true"></span><span>Live estimate available on ChangeNOW</span></span>
      <span class="field">
        <span class="field-text"><small>You receive</small><b>ETH — Ethereum</b></span>
        <span class="coin coin-eth" aria-hidden="true">ETH</span>
      </span>
      <span class="modes"><span>Floating rate</span><span class="dot" aria-hidden="true">·</span><span>Fixed rate available</span></span>
      <span class="btn btn-dark btn-block"><span>Check the live XMR/ETH rate</span></span>
      <span class="xcard-note">All costs are included in the estimate shown before the swap. Network and market conditions can affect the final result in floating-rate mode.</span>
    </a>
  </div>
</section>

<section class="strip-sec" aria-label="ChangeNOW key figures">
  <div class="wrap">
    <ul class="strip">
      {''.join(f'<li><b>{e(v)}</b><span>{e(l)}</span></li>' for v, l in fact_strip)}
    </ul>
    <p class="strip-note">ChangeNOW product figures. The Triumph Rate describes swaps completed at a better rate than estimated or with a deviation below 0.5%; it is not a promise that every swap will match its estimate.</p>
  </div>
</section>

<section class="sec" id="comparison" aria-labelledby="comparison-h">
  <div class="wrap">
    <div class="text-block">
      <h2 id="comparison-h">XMR to ETH Exchange Services Compared</h2>
      <p>We compared five services that displayed an available Monero-to-Ethereum route during our review. Each service was evaluated using the same weighted criteria: pair availability, quote transparency, exchange speed, ease of use, rate options, limits, coverage, support and public reputation.</p>
      <p>Quotes change continuously, so we do not publish a static XMR/ETH rate in this table. Open the live form and compare the amount of ETH offered for the same XMR input immediately before starting an exchange.</p>
    </div>
    <div class="table-card" data-track="comparison">
      <div class="table-scroll" tabindex="0" role="region" aria-label="XMR to ETH exchange services comparison table">
        <table class="cmp">
          <caption class="sr">XMR to ETH exchange services compared</caption>
          <thead><tr>{''.join(f'<th scope="col" class="{"s1" if i == 0 else "s2" if i == 1 else ""}">{e(h)}</th>' for i, h in enumerate(comparison_head))}</tr></thead>
          <tbody>
{table_rows()}
          </tbody>
        </table>
      </div>
    </div>
    <p class="table-note">“Account not required” does not mean that a transaction can never be reviewed. Exchange services may apply risk-based checks under their terms and policies. Availability and conditions can vary by transaction and jurisdiction.</p>
    <div class="verdict">
      <p><strong>Our verdict:</strong> ChangeNOW ranks first because it combines an available direct route, two rate modes, a clear three-step flow, no upper swap limit, broad multi-chain coverage and 24/7 support in one service.</p>
      {cn_link('Open ChangeNOW XMR to ETH Exchange', 'comparison', 'btn btn-green')}
    </div>
  </div>
</section>

<section class="sec sec-white" id="why-changenow" aria-labelledby="why-h">
  <div class="wrap why-grid">
    <div class="why-text">
      <h2 id="why-h">Why ChangeNOW Is Our Best Overall XMR to ETH Exchange</h2>
      <p>ChangeNOW earned the highest score in our comparison because it performs well across the full exchange journey rather than winning on a single feature. The XMR-to-ETH route is presented in a clear form, users can choose between fixed and floating rates when both are available, and the expected output is shown before the deposit is sent.</p>
      <p>A standard exchange does not require an account. The process has three main stages: select the pair and amount, enter the receiving Ethereum address, then send Monero to the generated deposit address. ChangeNOW states that all costs are built into the displayed rate, so there are no additional charges added after the swap.</p>
      <h3>What to consider</h3>
      <p>The one-minute figure published by ChangeNOW is an overall average, not a guaranteed completion time for every XMR-to-ETH transaction. Monero confirmations, Ethereum processing rules, liquidity and network congestion can extend the exchange. ChangeNOW says delivery is usually expected within one hour, but the live status page is the correct source for an active transaction.</p>
      {cn_link('Check the Current XMR to ETH Estimate', 'comparison')}
    </div>
    <div class="why-cards">
      {''.join(f'<div class="wcard"><span class="wnum" aria-hidden="true">{i}</span><h3>{e(t)}</h3><p>{e(b)}</p></div>' for i, (t, b) in enumerate(why_cards, start=1))}
    </div>
  </div>
</section>

<section class="sec" id="reviews" aria-labelledby="reviews-h">
  <div class="wrap">
    <div class="text-block">
      <h2 id="reviews-h">The 5 Best Services for Exchanging Monero to Ethereum</h2>
      <p>All five services below displayed an XMR-to-ETH route when this page was reviewed. Rankings reflect the weighted methodology published further down the page, not a claim that one service will offer the highest live quote at every moment.</p>
    </div>
    <div class="reviews">
      {''.join(review_card(r) for r in reviews)}
    </div>
  </div>
</section>

<section class="sec sec-tint" id="methodology" aria-labelledby="meth-h" data-track="methodology">
  <div class="wrap">
    <div class="meth-top">
      <div class="meth-text">
        <h2 id="meth-h">How We Compared XMR to ETH Exchange Services</h2>
        <p>We reviewed services that displayed a working Monero-to-Ethereum route on {REVIEWED}. Every service was assessed using the same seven criteria. We prioritized the complete user journey rather than selecting a winner from a single headline fee or marketing claim.</p>
        <p>Live crypto quotes change from minute to minute. A fair price check uses the same XMR input, the same rate type and a narrow time window. Because a static quote would become outdated quickly, this page explains how to repeat the comparison immediately before exchanging.</p>
      </div>
      <div class="weights" role="img" aria-label="Criteria weights: {'; '.join(f'{n} {w}%' for n, w, _ in criteria)}">
        <p class="weights-title">Scoring weights</p>
        <div class="bar" aria-hidden="true">{bar}</div>
        <ul class="legend" aria-hidden="true">{legend}</ul>
      </div>
    </div>
    <div class="table-card">
      <div class="table-scroll" tabindex="0" role="region" aria-label="Comparison criteria table">
        <table class="crit">
          <caption class="sr">Comparison criteria, weights and evaluation method</caption>
          <thead><tr><th scope="col">Criterion</th><th scope="col">Weight</th><th scope="col">How it was evaluated</th></tr></thead>
          <tbody>{crit_rows}</tbody>
        </table>
      </div>
    </div>
    <div class="meth-bottom">
      <div class="meth-col">
        <h3>How to compare live quotes yourself</h3>
        <ol class="num-list">{''.join(f'<li>{e(s)}</li>' for s in compare_steps)}</ol>
      </div>
      <div class="meth-col">
        <h3>Limitations</h3>
        <p>Our review used publicly available service information and route-level forms. We did not send a real deposit through every provider. A displayed estimate is not the same as a completed-transaction result, particularly in floating-rate mode.</p>
        <h3>Why ChangeNOW won</h3>
        <p>ChangeNOW achieved the strongest combined score. It did not need to be the top service in every individual category. Its first-place result came from offering the direct route, two rate modes, an upfront estimate, broad coverage, no published upper swap limit, a simple three-step process and 24/7 support in one product.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="how-to" aria-labelledby="how-h">
  <div class="wrap how-grid">
    <div class="how-main">
      <h2 id="how-h">How to Exchange Monero for Ethereum on ChangeNOW</h2>
      <p class="intro">The standard XMR-to-ETH flow has three main exchange stages, plus a final address and amount check before you start. You need a Monero wallet with enough XMR for the deposit and an Ethereum-compatible wallet address for receiving native ETH.</p>
      <ol class="timeline">
        {''.join(f'<li><span class="tl-num" aria-hidden="true">{i}</span><div><h3>{e(t)}</h3><p>{e(b)}</p></div></li>' for i, (t, b) in enumerate(howto_steps, start=1))}
      </ol>
      <p class="warn"><strong>Important:</strong> A crypto exchange cannot normally be cancelled after you send the deposit. Blockchain transfers are irreversible, so verify every field before sending XMR.</p>
    </div>
    <aside class="how-side" aria-label="Start the exchange">
      <div class="side-card">
        <h3>Ready to exchange?</h3>
        <p>Open the live ChangeNOW form to check the current minimum, estimate and rate modes.</p>
        {cn_link('Start XMR to ETH Exchange', 'how_to', 'btn btn-dark btn-block')}
      </div>
    </aside>
  </div>
</section>

<section class="sec sec-white" aria-labelledby="vs-h">
  <div class="wrap">
    <div class="text-block">
      <h2 id="vs-h">What Changes When You Exchange XMR for ETH?</h2>
      <p>Monero and Ethereum are separate assets on separate blockchains. Exchanging XMR for ETH is not a transfer between two addresses on the same network. The service receives Monero and sends native Ethereum to the destination address you provide.</p>
    </div>
    <div class="vs-grid">
      <div class="table-card">
        <div class="table-scroll" tabindex="0" role="region" aria-label="Monero versus Ethereum table">
          <table class="vs">
            <caption class="sr">Monero compared with Ethereum in an exchange</caption>
            <thead><tr><th scope="col">{vs_head[0]}</th><th scope="col"><span class="tick tick-xmr" aria-hidden="true"></span>{vs_head[1]}</th><th scope="col"><span class="tick tick-eth" aria-hidden="true"></span>{vs_head[2]}</th></tr></thead>
            <tbody>{''.join(f'<tr><th scope="row">{e(r[0])}</th><td>{e(r[1])}</td><td>{e(r[2])}</td></tr>' for r in vs_rows)}</tbody>
          </table>
        </div>
      </div>
      <div class="vs-note">
        <h3>Does exchanging XMR to ETH preserve Monero-level privacy?</h3>
        <p>No. Monero and Ethereum have different privacy models. Monero is designed to conceal transaction details within its network, while a standard Ethereum transfer is publicly visible. After the exchange, the ETH payout address, transferred amount and subsequent on-chain activity can be viewed through an Ethereum block explorer.</p>
        <p>The exchange service may also retain operational records and apply legal or risk-based controls under its policies. Do not describe an XMR-to-ETH exchange as anonymous or untraceable. The accurate statement is that the source asset uses Monero’s privacy-focused network, while the destination asset enters Ethereum’s transparent public ledger.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec" aria-labelledby="rates-h">
  <div class="wrap">
    <div class="text-block"><h2 id="rates-h">XMR to ETH Rates, Fees and Exchange Time</h2></div>
    <div class="rate-cards">
      {''.join(f'<div class="rcard"><h3>{e(t)}</h3><p>{e(b)}</p></div>' for t, b in rate_cards)}
    </div>
    <div class="rate-text">
      <div>
        <h3>Fixed rate or floating rate?</h3>
        <p>A floating rate follows the market while the exchange is processed, so the final ETH amount can differ from the initial estimate. A fixed rate is designed to preserve the agreed output when the exchange conditions are met. Fixed mode may use a different estimate because the provider takes on short-term rate risk.</p>
        <p>Choose based on your priority: potential market movement in floating mode or greater output certainty in fixed mode. Always read the live terms before sending XMR.</p>
      </div>
      <div>
        <h3>Is there a minimum or maximum amount?</h3>
        <p>The live minimum changes with the pair, network costs and liquidity. ChangeNOW says minimum amounts can be as low as the equivalent of $2, but the XMR-to-ETH form is the authoritative source for the current transaction. ChangeNOW does not publish an upper limit for standard crypto-to-crypto swaps.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-pad-sm" aria-labelledby="safety-h">
  <div class="wrap">
    <div class="safety">
      <h2 id="safety-h">XMR to ETH Safety Checklist</h2>
      <p class="safety-intro">Complete these checks before sending Monero. Most address and network mistakes cannot be reversed.</p>
      <ul class="checklist">{''.join(f'<li>{e(s)}</li>' for s in safety_items)}</ul>
      <p class="alert"><strong>Never</strong> send funds based on an address received through an unsolicited message, social-media reply or search advertisement. Start from the official exchange page and verify the domain.</p>
    </div>
  </div>
</section>

<section class="sec" id="faq" aria-labelledby="faq-h" data-track="faq">
  <div class="wrap faq-wrap">
    <h2 id="faq-h">Frequently Asked Questions</h2>
    <div class="faq">
{faq_items()}
    </div>
  </div>
</section>

<section class="sec-final" aria-labelledby="final-h">
  <div class="wrap">
    <div class="final">
      <div class="final-copy">
        <p class="label label-dark"><i aria-hidden="true"></i>Our #1 XMR to ETH choice</p>
        <h2 id="final-h">Exchange Monero to Ethereum with ChangeNOW</h2>
        <p>ChangeNOW ranks first in our comparison for its direct XMR-to-ETH route, fixed and floating rate options, upfront estimate, simple exchange flow and 24/7 support. Open the live form to check the current minimum and expected ETH output before sending funds.</p>
      </div>
      <div class="final-cta">
        {cn_link('Check the Live XMR to ETH Rate', 'final', 'btn btn-green btn-lg')}
        <p>Crypto prices and estimates can change. Verify the address, rate mode and expected output before confirming the exchange.</p>
      </div>
    </div>
  </div>
</section>

</main>

<footer class="site-footer">
  <div class="wrap foot-grid">
    <div>
      <p class="foot-h">About</p>
      <p><strong>XMR → ETH Guide</strong><br>A focused comparison resource for users researching how to exchange Monero for Ethereum.</p>
    </div>
    <div>
      <p class="foot-h">Page links</p>
      <ul class="foot-links">
        <li><a href="#comparison">Comparison</a></li>
        <li><a href="#reviews">Reviews</a></li>
        <li><a href="#methodology">Methodology</a></li>
        <li><a href="#how-to">How to Exchange</a></li>
        <li><a href="#faq">FAQ</a></li>
      </ul>
    </div>
    <div>
      <p class="foot-h">Disclosures</p>
      <p>Rankings are based on the published methodology and information available on the review date. Availability, estimates, limits and service terms can change.</p>
      <p>Cryptocurrency transactions involve price, network, liquidity and operational risks. This page provides general information and is not financial, investment, legal or tax advice. Blockchain transfers are irreversible. Verify all transaction details independently.</p>
      <p><strong>Affiliate disclosure:</strong> We may earn a commission when you use links on this page. This does not change the price you pay. Rankings are based on the methodology and data described above.</p>
    </div>
  </div>
  <div class="wrap copy">© 2026 XMR → ETH Guide. All rights reserved.</div>
</footer>

<div class="sticky-cta" id="sticky-cta" aria-hidden="true">
  <span>Best overall: ChangeNOW</span>
  <a class="btn btn-green btn-sm" href="{CN}" target="_blank" rel="{CN_REL}" data-cta="mobile_sticky" tabindex="-1"><span>Exchange XMR to ETH</span></a>
</div>

<script src="/assets/app.js" defer></script>
</body>
</html>
'''

kickers = {
    'comparison-h': '01 / comparison', 'why-h': '02 / verdict', 'reviews-h': '03 / ranking',
    'meth-h': '04 / methodology', 'how-h': '05 / execution', 'vs-h': '06 / chains',
    'rates-h': '07 / rates', 'safety-h': '08 / safety', 'faq-h': '09 / faq',
}
for hid, label in kickers.items():
    tag = f'<h2 id="{hid}">'
    assert tag in html, hid
    html = html.replace(tag, f'<p class="kicker" aria-hidden="true">{label}</p>{tag}', 1)

# ---------------------------------------------------------------- write

OUT.mkdir(exist_ok=True)
(OUT / 'assets').mkdir(exist_ok=True)
(OUT / 'fonts').mkdir(exist_ok=True)
for f in ('style.css', 'app.js'):
    shutil.copy2(SRC / f, OUT / 'assets' / f)
shutil.copy2(SRC / 'assets' / 'xmr-to-eth-guide.webp', OUT / 'assets' / 'xmr-to-eth-guide.webp')
for f in (SRC / 'fonts').iterdir():
    shutil.copy2(f, OUT / 'fonts' / f.name)
(OUT / 'index.html').write_text(html)
(OUT / 'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#17201D"/><path d="M18 24h28M40 16l8 8-8 8M46 40H18M24 32l-8 8 8 8" fill="none" stroke="#2EBD85" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>\n')
(OUT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n')
(OUT / 'sitemap.xml').write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    f'  <url>\n    <loc>{SITE}</loc>\n    <lastmod>{ISO_DATE}</lastmod>\n  </url>\n</urlset>\n')
print('built', OUT / 'index.html', len(html), 'bytes')
