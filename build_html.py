# -*- coding: utf-8 -*-
import json
import os

base_dir = r"C:\Users\HP\.gemini\antigravity\scratch\wedding-invitation"
brain_dir = r"C:\Users\HP\.gemini\antigravity\brain\ef83a52c-d4e8-43ee-a994-00aba285c933"

with open(os.path.join(base_dir, "images.json"), "r", encoding="utf-8") as f:
    images = json.load(f)

envelope_b64 = images["envelope"]
seal_b64 = images["seal"]
couples_b64 = images["couples"]
details_b64 = images["details"]
couples_bg_b64 = images["couples_bg"]
couple_left_b64 = images["couple_left"]
couple_right_b64 = images["couple_right"]

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Wedding Invitation • Salmabee & Muhammed Ajnas | Rahmabee & Shahbaz Muhammed</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;800&family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Great+Vibes&family=Montserrat:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">

  <style>
    :root {{
      --burgundy-deep: #180205;
      --burgundy-rich: #480C17;
      --burgundy-card: #5E1220;
      --gold-primary: #D4AF37;
      --gold-light: #F4E29F;
      --gold-dark: #9A7720;
      --gold-gradient: linear-gradient(135deg, #FDF0CD 0%, #D4AF37 50%, #9A7720 100%);
      --gold-glow: rgba(212, 175, 55, 0.45);
      --parchment-bg: #FAF6EF;
      --ink-dark: #2A1C1D;
      --ink-muted: #6C5B5D;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      font-family: 'Cormorant Garamond', serif;
      background-color: var(--burgundy-deep);
      background-image: 
        radial-gradient(circle at 50% 20%, rgba(138, 26, 47, 0.45) 0%, transparent 65%),
        radial-gradient(circle at 50% 80%, rgba(24, 2, 5, 0.98) 0%, rgba(8, 1, 2, 1) 100%);
      color: var(--ink-dark);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      overflow-x: hidden;
      position: relative;
    }}

    /* Background Particles Canvas */
    #particlesCanvas {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 1;
    }}

    /* Discreet Corner Controls */
    .corner-controls {{
      position: fixed;
      top: 18px;
      right: 18px;
      z-index: 100;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .icon-btn {{
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: rgba(30, 4, 8, 0.78);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(212, 175, 55, 0.4);
      color: var(--gold-light);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 14px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.5);
      transition: all 0.3s ease;
    }}

    .icon-btn:hover {{
      background: rgba(212, 175, 55, 0.25);
      transform: scale(1.08);
      color: #fff;
    }}

    .icon-btn.music-active {{
      background: rgba(212, 175, 55, 0.35);
      border-color: #d4af37;
      box-shadow: 0 0 16px rgba(212, 175, 55, 0.7);
      animation: pulseMusic 2.4s ease-in-out infinite;
    }}
    @keyframes pulseMusic {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.08); }}
    }}

    /* Main Stage Container */
    .stage-wrapper {{
      position: relative;
      z-index: 10;
      width: min(94vw, 440px);
      height: min(94vh, 880px);
      perspective: 1800px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: auto;
    }}

    /* Card Base Styling */
    .invitation-card {{
      position: absolute;
      width: 100%;
      height: 100%;
      background: var(--parchment-bg);
      background-image: 
        radial-gradient(ellipse at center, #FFFCF7 0%, #F5EFE4 100%),
        repeating-linear-gradient(0deg, transparent, transparent 3px, rgba(0,0,0,0.01) 3px, rgba(0,0,0,0.01) 4px);
      border-radius: 12px;
      box-shadow: 
        0 25px 60px rgba(0, 0, 0, 0.8),
        0 0 0 1px rgba(212, 175, 55, 0.35),
        inset 0 0 40px rgba(180, 150, 110, 0.2);
      border: 6px solid #480C17;
      outline: 2px solid var(--gold-primary);
      outline-offset: -3px;
      overflow-y: auto;
      overflow-x: hidden;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 34px 20px 20px 20px;
      opacity: 0;
      pointer-events: none;
      transform: translateY(14px) scale(0.98);
      transition: opacity 1.8s cubic-bezier(0.25, 1, 0.5, 1), transform 1.8s cubic-bezier(0.25, 1, 0.5, 1);
    }}

    .invitation-card.active {{
      opacity: 1;
      pointer-events: auto;
      transform: translateY(0) scale(1);
    }}

    .invitation-card::-webkit-scrollbar {{
      width: 4px;
    }}
    .invitation-card::-webkit-scrollbar-track {{
      background: rgba(0,0,0,0.03);
    }}
    .invitation-card::-webkit-scrollbar-thumb {{
      background: var(--gold-primary);
      border-radius: 4px;
    }}

    /* =========================================================
       SCENE 1: ROYAL ENVELOPE UNFOLDS DIRECTLY OVER "YOU'RE CORDIALLY INVITED"
       (Zero Blank Card: Envelope flaps unfold slowly over the invitation)
       ========================================================= */
    .envelope-flaps-overlay {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border-radius: 8px;
      transform-style: preserve-3d;
      perspective: 1200px;
      pointer-events: auto;
      z-index: 45;
      cursor: pointer;
    }}

    .envelope-flaps-overlay.opened {{
      pointer-events: none;
    }}

    .flap {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-image: url("{envelope_b64}");
      background-size: 100% 100%;
      background-position: center;
      background-repeat: no-repeat;
      transition: transform 5.8s cubic-bezier(0.25, 1, 0.35, 1), opacity 1.6s ease 4.6s;
      backface-visibility: hidden;
      z-index: 10;
    }}

    .flap-top {{
      clip-path: polygon(0 0, 100% 0, 50.4% 46.2%);
      transform-origin: top center;
      z-index: 12;
      filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
    }}

    .flap-bottom {{
      clip-path: polygon(0 100%, 100% 100%, 50.4% 46.2%);
      transform-origin: bottom center;
      z-index: 11;
      filter: drop-shadow(0 -2px 4px rgba(0,0,0,0.3));
    }}

    .flap-left {{
      clip-path: polygon(0 0, 50.4% 46.2%, 0 100%);
      transform-origin: left center;
      z-index: 10;
      filter: drop-shadow(2px 0 4px rgba(0,0,0,0.3));
    }}

    .flap-right {{
      clip-path: polygon(100% 0, 100% 100%, 50.4% 46.2%);
      transform-origin: right center;
      z-index: 10;
      filter: drop-shadow(-2px 0 4px rgba(0,0,0,0.3));
    }}

    .envelope-flaps-overlay.opened .flap-top {{
      transform: rotateX(160deg);
      opacity: 0;
    }}
    .envelope-flaps-overlay.opened .flap-bottom {{
      transform: rotateX(-160deg);
      opacity: 0;
    }}
    .envelope-flaps-overlay.opened .flap-left {{
      transform: rotateY(-160deg);
      opacity: 0;
    }}
    .envelope-flaps-overlay.opened .flap-right {{
      transform: rotateY(160deg);
      opacity: 0;
    }}

    .wax-seal {{
      position: absolute;
      top: 46.2%;
      left: 50.4%;
      transform: translate(-50%, -50%);
      width: 96px;
      height: 96px;
      background-image: url("{seal_b64}");
      background-size: contain;
      background-repeat: no-repeat;
      background-position: center;
      z-index: 25;
      filter: drop-shadow(0 8px 18px rgba(0,0,0,0.5));
      transition: all 0.5s ease;
      cursor: pointer;
    }}

    .envelope-flaps-overlay.opened .wax-seal {{
      transform: translate(-50%, -50%) scale(1.3);
      opacity: 0;
      pointer-events: none;
      transition: transform 2.8s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 2.4s cubic-bezier(0.2, 0.8, 0.2, 1);
    }}

    /* =========================================================
       SCENE 2: YOU'RE CORDIALLY INVITED
       ========================================================= */
    .bismillah {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 17px;
      color: var(--gold-dark);
      letter-spacing: 2px;
      margin-top: 10px;
      margin-bottom: 25px;
      text-align: center;
      opacity: 0;
      transform: translateY(10px);
      transition: all 1.4s ease 0.5s;
    }}

    .active .bismillah {{
      opacity: 1;
      transform: translateY(0);
    }}

    .reveal-container {{
      text-align: center;
      margin: auto 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 14px;
    }}

    .fade-youre {{
      font-family: 'Cinzel', serif;
      font-size: 18px;
      letter-spacing: 8px;
      color: var(--burgundy-rich);
      opacity: 0;
      filter: blur(8px);
      transform: translateY(12px);
      transition: all 1.6s cubic-bezier(0.2, 0.8, 0.2, 1) 0.8s;
    }}

    .fade-cordially {{
      font-family: 'Cinzel', serif;
      font-size: 38px;
      font-weight: 700;
      letter-spacing: 5px;
      color: var(--burgundy-card);
      text-shadow: 0 1px 2px rgba(0,0,0,0.1);
      opacity: 0;
      filter: blur(10px);
      transform: scale(0.94) translateY(15px);
      transition: all 1.8s cubic-bezier(0.2, 0.8, 0.2, 1) 1.8s;
    }}

    .fade-cordially .dot-o {{
      position: relative;
      display: inline-block;
    }}
    .fade-cordially .dot-o::after {{
      content: "•";
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      font-size: 14px;
      color: var(--burgundy-card);
    }}

    .fade-invited {{
      font-family: 'Cinzel', serif;
      font-size: 22px;
      letter-spacing: 7px;
      color: var(--burgundy-rich);
      opacity: 0;
      filter: blur(8px);
      transform: translateY(12px);
      transition: all 1.8s cubic-bezier(0.2, 0.8, 0.2, 1) 2.8s;
    }}

    .fade-subtext {{
      font-family: 'Cormorant Garamond', serif;
      font-style: italic;
      font-size: 18px;
      color: var(--ink-muted);
      margin-top: 15px;
      max-width: 290px;
      line-height: 1.45;
      opacity: 0;
      transform: translateY(10px);
      transition: all 1.8s ease 3.8s;
    }}

    .active .fade-youre,
    .active .fade-cordially,
    .active .fade-invited,
    .active .fade-subtext {{
      opacity: 1;
      filter: blur(0px);
      transform: scale(1) translateY(0);
    }}

    .gold-divider {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      width: 80%;
      margin: 16px 0;
    }}

    .gold-divider::before, .gold-divider::after {{
      content: "";
      flex: 1;
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--gold-primary), transparent);
    }}

    .gold-divider svg {{
      width: 22px;
      height: 22px;
      fill: var(--gold-primary);
    }}

    .card-nav-row {{
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-top: auto;
      padding-top: 14px;
    }}

    .nav-link-btn {{
      background: transparent;
      border: 1px solid rgba(212, 175, 55, 0.4);
      color: var(--burgundy-rich);
      padding: 8px 16px;
      border-radius: 20px;
      font-family: 'Montserrat', sans-serif;
      font-size: 10px;
      font-weight: 600;
      letter-spacing: 1px;
      text-transform: uppercase;
      cursor: pointer;
      transition: all 0.3s ease;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}

    .nav-link-btn:hover {{
      background: rgba(72, 12, 23, 0.08);
      border-color: var(--gold-dark);
    }}

    .gold-btn {{
      background: var(--gold-gradient);
      color: #380811;
      border: 1px solid #AA7C11;
      padding: 10px 22px;
      border-radius: 25px;
      font-family: 'Montserrat', sans-serif;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(154, 119, 32, 0.35);
      transition: all 0.3s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      margin-left: auto;
    }}

    .gold-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(154, 119, 32, 0.5);
      filter: brightness(1.05);
    }}

    /* =========================================================
       SCENE 3: WE'RE GETTING MARRIED - TWIN COUPLES
       ========================================================= */
    .title-banner {{
      font-family: 'Cinzel', serif;
      font-size: 13px;
      letter-spacing: 4px;
      text-transform: uppercase;
      color: var(--burgundy-card);
      font-weight: 600;
      margin-top: 4px;
      margin-bottom: 2px;
    }}

    .subtitle-banner {{
      font-family: 'Cormorant Garamond', serif;
      font-style: italic;
      font-size: 15px;
      color: var(--ink-muted);
      margin-bottom: 10px;
    }}

    .twins-badge {{
      background: rgba(72, 12, 23, 0.07);
      border: 1px dashed var(--gold-primary);
      padding: 4px 14px;
      border-radius: 20px;
      font-family: 'Montserrat', sans-serif;
      font-size: 10px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: var(--burgundy-rich);
      font-weight: 600;
      margin-bottom: 12px;
    }}

    .scene-body-content {{
      width: 100%;
      margin: auto 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      flex-grow: 1;
    }}

    .couples-stack {{
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin: auto 0;
    }}

    .couple-card {{
      background: rgba(255, 255, 255, 0.65);
      border: 1px solid rgba(212, 175, 55, 0.35);
      border-radius: 12px;
      padding: 12px 10px;
      text-align: center;
      position: relative;
      box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    }}

    .couple-role {{
      font-family: 'Montserrat', sans-serif;
      font-size: 9px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--gold-dark);
      font-weight: 600;
      margin-bottom: 2px;
    }}

    .bride-name {{
      font-family: 'Great Vibes', cursive;
      font-size: 32px;
      color: var(--burgundy-card);
      line-height: 1.1;
      text-shadow: 0 1px 1px rgba(0,0,0,0.05);
    }}

    .ampersand {{
      font-family: 'Cormorant Garamond', serif;
      font-style: italic;
      font-size: 18px;
      color: var(--gold-primary);
      margin: 1px 0;
    }}

    .groom-name {{
      font-family: 'Cinzel', serif;
      font-size: 15px;
      font-weight: 700;
      letter-spacing: 2px;
      color: var(--ink-dark);
      margin-top: 1px;
    }}

    .couple-sub {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 12px;
      color: var(--ink-muted);
      margin-top: 3px;
    }}

    /* =========================================================
       SLOW CALLIGRAPHY HANDWRITING REVEAL ANIMATION
       ========================================================= */
    .write-wrap {{
      position: relative;
      display: inline-block;
      text-align: center;
      margin: 1px auto;
    }}

    .write-text {{
      display: inline-block;
      white-space: nowrap;
      clip-path: inset(0 100% 0 0);
      opacity: 0;
    }}

    .pen-nib {{
      position: absolute;
      top: 50%;
      width: 6px;
      height: 6px;
      background: radial-gradient(circle, #FFF5D6 0%, #D4AF37 70%, #9B7811 100%);
      border-radius: 50%;
      box-shadow: 0 0 10px 2px rgba(212, 175, 55, 0.85);
      pointer-events: none;
      opacity: 0;
      transform: translate(-50%, -50%);
    }}

    @keyframes writeReveal {{
      0% {{
        clip-path: inset(0 100% 0 0);
        opacity: 0.15;
      }}
      5% {{
        opacity: 1;
      }}
      100% {{
        clip-path: inset(0 0% 0 0);
        opacity: 1;
      }}
    }}

    @keyframes penNibGlide {{
      0% {{
        left: 0%;
        opacity: 0;
      }}
      4% {{
        opacity: 1;
      }}
      94% {{
        left: 100%;
        opacity: 1;
      }}
      100% {{
        left: 100%;
        opacity: 0;
      }}
    }}

    @keyframes softFadeScale {{
      0% {{
        opacity: 0;
        transform: scale(0.88);
      }}
      100% {{
        opacity: 1;
        transform: scale(1);
      }}
    }}

    /* Active triggers for Couple 1 (Salmabee & Muhammed Ajnas) */
    #scene-couples.active .bride-write-1 .write-text {{
      animation: writeReveal 2.6s cubic-bezier(0.35, 0, 0.25, 1) 0.6s forwards;
    }}
    #scene-couples.active .bride-write-1 .pen-nib {{
      animation: penNibGlide 2.6s cubic-bezier(0.35, 0, 0.25, 1) 0.6s forwards;
    }}

    #scene-couples.active .ampersand-1 {{
      opacity: 0;
      animation: softFadeScale 1.0s ease 3.0s forwards;
    }}

    #scene-couples.active .groom-write-1 .write-text {{
      animation: writeReveal 2.0s cubic-bezier(0.35, 0, 0.25, 1) 3.3s forwards;
    }}
    #scene-couples.active .groom-write-1 .pen-nib {{
      animation: penNibGlide 2.0s cubic-bezier(0.35, 0, 0.25, 1) 3.3s forwards;
    }}

    #scene-couples.active .sub-1 {{
      opacity: 0;
      animation: softFadeScale 1.2s ease 4.2s forwards;
    }}

    /* Active triggers for Couple 2 (Rahmabee & Shahbaz Muhammed) */
    #scene-couples.active .bride-write-2 .write-text {{
      animation: writeReveal 2.6s cubic-bezier(0.35, 0, 0.25, 1) 5.2s forwards;
    }}
    #scene-couples.active .bride-write-2 .pen-nib {{
      animation: penNibGlide 2.6s cubic-bezier(0.35, 0, 0.25, 1) 5.2s forwards;
    }}

    #scene-couples.active .ampersand-2 {{
      opacity: 0;
      animation: softFadeScale 1.0s ease 7.6s forwards;
    }}

    #scene-couples.active .groom-write-2 .write-text {{
      animation: writeReveal 2.0s cubic-bezier(0.35, 0, 0.25, 1) 7.9s forwards;
    }}
    #scene-couples.active .groom-write-2 .pen-nib {{
      animation: penNibGlide 2.0s cubic-bezier(0.35, 0, 0.25, 1) 7.9s forwards;
    }}

    #scene-couples.active .sub-2 {{
      opacity: 0;
      animation: softFadeScale 1.2s ease 8.8s forwards;
    }}

    /* =========================================================
       SCENE 4: STANDARDIZED FULL-IMAGE COUPLES PORTRAIT
       (Both couples move from two sides into exact place; no blinking lights)
       ========================================================= */
    #scene-portrait {{
      padding: 0 !important;
      overflow: hidden !important;
      position: relative;
      background: #FAF6EF;
      border: 6px solid #480C17;
      outline: 2px solid var(--gold-primary);
      outline-offset: -3px;
    }}

    .full-artwork-container {{
      position: relative;
      width: 100%;
      height: 100%;
      overflow: hidden;
    }}

    /* Base background layer (Flowers + Golden Names) */
    .couples-bg-layer {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center top;
      display: block;
      z-index: 1;
    }}

    /* Left Bride & Groom (Salmabee & Muhammed Ajnas) moves from left side */
    .couple-left-layer {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center top;
      display: block;
      pointer-events: none;
      z-index: 3;
      transform: translateX(-24%);
      opacity: 0;
      transition: transform 2.2s cubic-bezier(0.16, 1, 0.3, 1), opacity 1.6s ease;
      will-change: transform, opacity;
    }}

    /* Right Bride & Groom (Rahmabee & Shahbaz Muhammed) moves from right side */
    .couple-right-layer {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center top;
      display: block;
      pointer-events: none;
      z-index: 3;
      transform: translateX(24%);
      opacity: 0;
      transition: transform 2.2s cubic-bezier(0.16, 1, 0.3, 1), opacity 1.6s ease;
      will-change: transform, opacity;
    }}

    /* When Scene 4 opens: Both couples glide in from the two sides to their exact place! */
    .active .couple-left-layer {{
      transform: translateX(0);
      opacity: 1;
    }}

    .active .couple-right-layer {{
      transform: translateX(0);
      opacity: 1;
    }}

    .portrait-nav-overlay {{
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      padding: 30px 18px 16px 18px;
      background: linear-gradient(to top, rgba(24, 2, 5, 0.88) 0%, rgba(24, 2, 5, 0.6) 65%, transparent 100%);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      z-index: 20;
    }}

    .portrait-nav-overlay .nav-link-btn {{
      color: var(--gold-light);
      border-color: rgba(212, 175, 55, 0.5);
      background: rgba(30, 4, 8, 0.5);
      backdrop-filter: blur(4px);
    }}

    .portrait-nav-overlay .nav-link-btn:hover {{
      background: rgba(212, 175, 55, 0.2);
      color: #FFF;
    }}

    .portrait-nav-overlay .gold-btn {{
      box-shadow: 0 4px 18px rgba(0,0,0,0.5);
    }}

    /* =========================================================
       SCENE 5: CEREMONY DETAILS (FROM IMAGE 5)
       ========================================================= */
    .card-top-header {{
      font-family: 'Cinzel', serif;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 2.2px;
      color: var(--burgundy-card);
      text-align: center;
      margin-top: 10px;
      margin-bottom: 10px;
    }}

    .parents-section {{
      text-align: center;
      margin-bottom: 12px;
    }}

    .parents-names {{
      font-family: 'Playfair Display', serif;
      font-size: 18px;
      font-weight: 700;
      color: var(--ink-dark);
      letter-spacing: 0.4px;
    }}

    .residence-line {{
      font-family: 'Montserrat', sans-serif;
      font-size: 11px;
      color: var(--ink-muted);
      margin-top: 4px;
    }}

    .invite-text {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 15px;
      font-style: italic;
      color: var(--ink-dark);
      text-align: center;
      line-height: 1.45;
      margin: 10px auto 18px auto;
      max-width: 340px;
    }}

    .couples-detail-grid {{
      width: 100%;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-top: 6px;
      margin-bottom: 22px;
    }}

    .couple-detail-box {{
      background: rgba(255, 255, 255, 0.8);
      border: 1.5px solid rgba(212, 175, 55, 0.45);
      border-radius: 12px;
      padding: 22px 10px;
      text-align: center;
      box-shadow: 0 6px 18px rgba(0,0,0,0.07);
      display: flex;
      flex-direction: column;
      justify-content: center;
    }}

    .quran-blessing {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 13.5px;
      font-style: italic;
      color: var(--gold-dark);
      text-align: center;
      line-height: 1.4;
      margin: 10px auto 20px auto;
      max-width: 320px;
      padding: 10px 14px;
      border-top: 1px solid rgba(212, 175, 55, 0.3);
      border-bottom: 1px solid rgba(212, 175, 55, 0.3);
    }}

    .insha-allah-header {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 22px;
      color: var(--gold-dark);
      letter-spacing: 2.5px;
      text-align: center;
      margin-top: 14px;
      margin-bottom: 4px;
    }}

    .insha-allah-sub {{
      font-family: 'Cinzel', serif;
      font-size: 14.5px;
      font-weight: 700;
      color: var(--burgundy-card);
      letter-spacing: 2.5px;
      text-align: center;
      margin-bottom: 18px;
    }}

    .c-union-tag {{
      font-family: 'Montserrat', sans-serif;
      font-size: 8px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: var(--gold-dark);
      font-weight: 600;
      margin-bottom: 4px;
    }}

    .c-bride {{
      font-family: 'Great Vibes', cursive;
      font-size: 28px;
      color: var(--burgundy-card);
      line-height: 1.1;
    }}

    .c-with {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 11px;
      font-style: italic;
      color: var(--ink-muted);
    }}

    .c-groom {{
      font-family: 'Cinzel', serif;
      font-size: 13.5px;
      font-weight: 700;
      color: var(--ink-dark);
      margin: 1px 0;
    }}

    .c-parentage {{
      font-family: 'Montserrat', sans-serif;
      font-size: 9px;
      color: var(--ink-muted);
      line-height: 1.3;
      margin-top: 2px;
    }}

    .insha-allah {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 13px;
      font-weight: 600;
      color: var(--gold-dark);
      letter-spacing: 1px;
      text-align: center;
      margin: 2px 0 6px 0;
    }}

    .event-info-cards {{
      width: 100%;
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 8px;
      margin-bottom: 26px;
    }}

    .info-card {{
      background: #480C17;
      color: #fff;
      border-radius: 12px;
      padding: 18px 6px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 10px rgba(0,0,0,0.15);
      border: 1px solid rgba(212, 175, 55, 0.3);
    }}

    .info-card .icon {{
      font-size: 15px;
      margin-bottom: 2px;
    }}

    .info-card .label {{
      font-family: 'Montserrat', sans-serif;
      font-size: 8px;
      letter-spacing: 1px;
      text-transform: uppercase;
      color: var(--gold-light);
    }}

    .info-card .main-val {{
      font-family: 'Cinzel', serif;
      font-size: 13px;
      font-weight: 700;
      color: #fff;
      margin: 2px 0;
    }}

    .info-card .sub-val {{
      font-family: 'Montserrat', sans-serif;
      font-size: 7.5px;
      color: #E2D3D5;
    }}

    .countdown-wrap {{
      width: 100%;
      background: rgba(72, 12, 23, 0.05);
      border: 1.5px solid rgba(212, 175, 55, 0.38);
      border-radius: 14px;
      padding: 16px 14px;
      text-align: center;
      margin-bottom: 24px;
    }}

    .countdown-label {{
      font-family: 'Montserrat', sans-serif;
      font-size: 8.5px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: var(--gold-dark);
      font-weight: 600;
      margin-bottom: 3px;
    }}

    .timer-units {{
      display: flex;
      justify-content: center;
      gap: 10px;
    }}

    .timer-unit {{
      display: flex;
      flex-direction: column;
      align-items: center;
    }}

    .timer-unit .num {{
      font-family: 'Cinzel', serif;
      font-size: 20px;
      font-weight: 700;
      color: var(--burgundy-card);
    }}

    .timer-unit .unit {{
      font-family: 'Montserrat', sans-serif;
      font-size: 7.5px;
      text-transform: uppercase;
      color: var(--ink-muted);
    }}

    .compliments-note {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 13.5px;
      font-style: italic;
      color: var(--ink-muted);
      text-align: center;
      border-top: 1px solid rgba(212, 175, 55, 0.3);
      padding-top: 14px;
      margin-bottom: 20px;
      width: 100%;
      line-height: 1.5;
    }}

    .action-row {{
      display: flex;
      gap: 10px;
      width: 100%;
      margin-bottom: 16px;
    }}

    .action-btn {{
      flex: 1;
      padding: 10px 12px;
      border-radius: 6px;
      border: 1px solid var(--gold-primary);
      background: #FFF;
      color: var(--burgundy-rich);
      font-family: 'Montserrat', sans-serif;
      font-size: 9.5px;
      font-weight: 600;
      letter-spacing: 0.5px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      text-decoration: none;
      transition: all 0.3s ease;
    }}

    .action-btn:hover {{
      background: var(--burgundy-rich);
      color: #fff;
    }}

    /* =========================================================
       SCENE 6: VENUE, ADDRESS & ACCURATE GOOGLE MAP DIRECTIONS
       ========================================================= */
    .venue-title {{
      font-family: 'Cinzel', serif;
      font-size: 17px;
      font-weight: 700;
      color: var(--burgundy-card);
      letter-spacing: 2px;
      text-align: center;
      margin-bottom: 2px;
    }}

    .venue-sub {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 13.5px;
      color: var(--ink-muted);
      margin-bottom: 8px;
    }}

    .address-card {{
      width: 100%;
      background: rgba(255, 255, 255, 0.7);
      border: 1px solid rgba(212, 175, 55, 0.4);
      border-radius: 8px;
      padding: 10px;
      text-align: center;
      margin-bottom: 8px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }}

    .residence-name {{
      font-family: 'Playfair Display', serif;
      font-size: 15px;
      font-weight: 700;
      color: var(--burgundy-rich);
    }}

    .full-address {{
      font-family: 'Montserrat', sans-serif;
      font-size: 10.5px;
      color: var(--ink-dark);
      margin-top: 3px;
      line-height: 1.4;
    }}

    .phone-contact {{
      font-family: 'Montserrat', sans-serif;
      font-size: 11px;
      font-weight: 600;
      color: var(--burgundy-card);
      margin-top: 4px;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      text-decoration: none;
    }}

    /* Direct Google Maps Embed Container - Fills screen fully */
    #scene-map {{
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
      padding: 30px 18px 16px 18px;
    }}

    .gmap-frame-box {{
      width: 100%;
      flex: 1;
      min-height: 280px;
      border-radius: 10px;
      border: 2px solid var(--gold-primary);
      margin-top: 4px;
      margin-bottom: 12px;
      overflow: hidden;
      box-shadow: 0 4px 16px rgba(0,0,0,0.15);
      position: relative;
    }}

    .gmap-frame-box iframe {{
      width: 100%;
      height: 100%;
      border: 0;
      display: block;
    }}

    /* Clean Focused Directions Buttons (WhatsApp & Call Host REMOVED) */
    .directions-btn-grid {{
      width: 100%;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin-bottom: 6px;
    }}

    .dir-action-btn {{
      padding: 9px 8px;
      border-radius: 6px;
      border: 1px solid var(--gold-primary);
      background: #480C17;
      color: #FFF;
      font-family: 'Montserrat', sans-serif;
      font-size: 10px;
      font-weight: 600;
      letter-spacing: 0.5px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
      text-decoration: none;
      transition: all 0.25s ease;
      box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    }}

    .dir-action-btn:hover {{
      background: #651423;
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    }}

    .dir-action-btn.primary-directions {{
      background: var(--gold-gradient);
      color: #380811;
      border-color: #AA7C11;
      font-weight: 700;
    }}

    .dir-action-btn.primary-directions:hover {{
      filter: brightness(1.06);
    }}

    .toast {{
      position: fixed;
      top: 20px;
      left: 50%;
      transform: translateX(-50%) translateY(-20px);
      background: #480C17;
      color: #FFF;
      border: 1px solid var(--gold-primary);
      padding: 8px 18px;
      border-radius: 20px;
      font-family: 'Montserrat', sans-serif;
      font-size: 12px;
      letter-spacing: 0.5px;
      z-index: 200;
      opacity: 0;
      pointer-events: none;
      transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }}

    .toast.show {{
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }}

    .lightbox-modal {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(18, 2, 5, 0.94);
      backdrop-filter: blur(8px);
      z-index: 300;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}

    .lightbox-modal.open {{
      display: flex;
    }}

    .lightbox-content {{
      max-width: 90vw;
      max-height: 85vh;
      border: 3px solid var(--gold-primary);
      border-radius: 12px;
      box-shadow: 0 15px 50px rgba(0,0,0,0.8);
      position: relative;
    }}

    .lightbox-content img {{
      max-width: 100%;
      max-height: 80vh;
      display: block;
      border-radius: 8px;
    }}

    .lightbox-close {{
      position: absolute;
      top: -16px;
      right: -16px;
      background: var(--gold-gradient);
      border: 1px solid #AA7C11;
      color: #2A040B;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      font-size: 16px;
      font-weight: bold;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 4px 10px rgba(0,0,0,0.4);
    }}
    /* =========================================================
       STORY SEGMENTED PROGRESS HEADER BAR (Instagram / WhatsApp Model)
       ========================================================= */
    .story-header-bar {{
      position: absolute;
      top: 10px;
      left: 12px;
      right: 12px;
      display: flex;
      align-items: center;
      gap: 5px;
      z-index: 80;
      padding: 4px 6px;
      border-radius: 8px;
      background: rgba(24, 2, 5, 0.25);
      backdrop-filter: blur(4px);
      -webkit-backdrop-filter: blur(4px);
      box-shadow: 0 2px 8px rgba(0,0,0,0.25);
    }}

    .story-dash {{
      flex: 1;
      height: 4px;
      background: rgba(255, 255, 255, 0.42);
      border-radius: 3px;
      overflow: hidden;
      position: relative;
      cursor: pointer;
      box-shadow: 0 1px 2px rgba(0,0,0,0.2);
      transition: transform 0.15s ease;
    }}

    .story-dash:hover {{
      transform: scaleY(1.5);
    }}

    .story-dash-fill {{
      width: 0%;
      height: 100%;
      border-radius: 3px;
      background: linear-gradient(90deg, #D4AF37 0%, #F5DE98 60%, #FFF5D6 100%);
      box-shadow: 0 0 6px rgba(212, 175, 55, 0.7);
      transition: width 0.08s linear;
    }}

    .story-dash.completed .story-dash-fill {{
      width: 100% !important;
      transition: none !important;
    }}

    .story-dash.pending .story-dash-fill {{
      width: 0% !important;
      transition: none !important;
    }}

    /* =========================================================
       STANDARDIZED MOBILE SCREEN VIEW (Full Screen Edge-to-Edge)
       ========================================================= */
    @media (max-width: 850px), (max-device-width: 850px), (hover: none) and (pointer: coarse) {{
      html, body {{
        width: 100vw;
        height: 100vh;
        height: 100dvh;
        min-height: 100dvh;
        padding: 0;
        margin: 0;
        overflow: hidden;
        background: #480C17;
      }}

      .stage-wrapper {{
        width: 100vw;
        height: 100vh;
        height: 100dvh;
        max-width: 100vw;
        max-height: 100dvh;
        margin: 0;
        padding: 0;
        border-radius: 0;
        box-shadow: none;
      }}

      .invitation-card {{
        width: 100vw;
        height: 100vh;
        height: 100dvh;
        max-width: 100vw;
        max-height: 100dvh;
        border-radius: 0;
        border: 3px solid #5E1220;
        outline: 1.5px solid #d4af37;
        outline-offset: -3px;
        box-shadow: none;
        box-sizing: border-box;
        padding: 28px 12px 10px 12px;
      }}

      .story-header-bar {{
        top: 10px;
        left: 10px;
        right: 48px;
        width: calc(100% - 58px);
      }}

      .corner-controls {{
        top: 6px;
        right: 8px;
        z-index: 120;
      }}

      .icon-btn {{
        width: 30px;
        height: 30px;
        font-size: 11px;
      }}

      /* Universal Mobile Bottom Navigation Bar (Guaranteed visible, never cut off) */
      .card-nav-row {{
        width: 100%;
        padding-top: 4px;
        padding-bottom: max(6px, env(safe-area-inset-bottom));
        margin-top: auto;
        flex-shrink: 0;
        gap: 8px;
      }}

      .nav-link-btn {{
        padding: 6px 14px;
        font-size: 9px;
        letter-spacing: 0.8px;
      }}

      .gold-btn {{
        padding: 7px 16px;
        font-size: 9px;
        letter-spacing: 1px;
      }}

      /* =========================================================
         SCENE 1: ENVELOPE & CORDIALLY INVITED MOBILE FIT
         ========================================================= */
      #scene-invited {{
        padding: 26px 12px 10px 12px;
      }}
      .invited-title {{
        font-size: 16px;
        letter-spacing: 3px;
      }}
      .bismillah-text {{
        font-size: 15px;
      }}
      .invited-desc {{
        font-size: 11px;
        line-height: 1.35;
      }}

      /* =========================================================
         SCENE 2: WE'RE GETTING MARRIED (TWIN COUPLES) MOBILE FIT
         ========================================================= */
      #scene-couples {{
        padding-top: 24px;
        padding-bottom: 8px;
      }}
      .title-banner {{
        font-size: 11px;
        letter-spacing: 2.5px;
        margin-top: 2px;
        margin-bottom: 1px;
      }}
      .subtitle-banner {{
        font-size: 12px;
        margin-bottom: 4px;
      }}
      .twins-badge {{
        font-size: 8.5px;
        letter-spacing: 1px;
        padding: 2px 10px;
        margin-bottom: 6px;
      }}
      .couples-stack {{
        gap: 5px;
        margin: auto 0;
        width: 100%;
      }}
      .couple-card {{
        padding: 6px 8px;
        border-radius: 8px;
      }}
      .couple-role {{
        font-size: 8px;
        letter-spacing: 1.5px;
        margin-bottom: 1px;
      }}
      .bride-name {{
        font-size: 24px;
        line-height: 1.05;
      }}
      .ampersand {{
        font-size: 13px;
        margin: 0;
      }}
      .groom-name {{
        font-size: 12px;
        letter-spacing: 1.5px;
        margin-top: 1px;
      }}
      .couple-sub {{
        font-size: 10px;
        margin-top: 1px;
      }}

      /* =========================================================
         SCENE 3: PORTRAIT ARTWORK MOBILE FIT
         ========================================================= */
      #scene-portrait {{
        padding: 26px 12px 10px 12px;
      }}
      .portrait-parchment-frame {{
        max-height: calc(100dvh - 90px);
      }}

      /* =========================================================
         SCENE 4: CEREMONY DETAILS (BALANCED & CENTERED)
         ========================================================= */
      #scene-details {{
        padding: 24px 12px 10px 12px;
      }}
      #scene-details .scene-body-content {{
        margin: auto 0;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      }}
      .card-top-header {{
        font-size: 10px;
        letter-spacing: 2px;
        margin-bottom: 5px;
        color: var(--burgundy-card);
      }}
      .parents-section {{
        margin-bottom: 8px;
        text-align: center;
      }}
      .parents-names {{
        font-size: 14.5px;
        font-weight: 700;
        color: var(--burgundy-card);
        font-family: 'Cinzel', serif;
      }}
      .residence-line {{
        font-size: 10.5px;
        color: var(--ink-muted);
        margin-top: 2px;
      }}
      .invite-text {{
        font-size: 12.5px;
        margin: 6px auto 12px auto;
        line-height: 1.4;
        max-width: 320px;
        text-align: center;
      }}
      .couples-detail-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px;
        width: 100%;
        margin: 4px 0 12px 0;
      }}
      .couple-detail-box {{
        padding: 12px 6px;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.85);
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        border: 1.5px solid rgba(212, 175, 55, 0.45);
        text-align: center;
      }}
      .c-union-tag {{
        font-size: 7.5px;
        letter-spacing: 1.5px;
        margin-bottom: 2px;
      }}
      .c-bride {{
        font-size: 22px;
        line-height: 1.1;
        color: var(--burgundy-card);
      }}
      .c-with {{
        font-size: 10px;
        font-style: italic;
      }}
      .c-groom {{
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1px;
        margin: 1px 0;
      }}
      .c-parentage {{
        font-size: 9px;
        line-height: 1.2;
        color: var(--ink-muted);
        margin-top: 2px;
      }}
      .quran-blessing {{
        font-size: 11px;
        line-height: 1.35;
        margin: 8px auto 4px auto;
        padding: 6px 12px;
        text-align: center;
        border-top: 1px solid rgba(212, 175, 55, 0.35);
        border-bottom: 1px solid rgba(212, 175, 55, 0.35);
        max-width: 320px;
      }}

      /* =========================================================
         SCENE 5: SCHEDULE & COUNTDOWN (BALANCED & CENTERED)
         ========================================================= */
      #scene-schedule {{
        padding: 24px 12px 10px 12px;
      }}
      #scene-schedule .scene-body-content {{
        margin: auto 0;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      }}
      .insha-allah-header {{
        font-size: 20px;
        margin-bottom: 2px;
        color: var(--gold-dark);
      }}
      .insha-allah-sub {{
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 12px;
        color: var(--burgundy-card);
      }}
      .event-info-cards {{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 6px;
        width: 100%;
        margin-bottom: 12px;
      }}
      .info-card {{
        padding: 12px 4px;
        border-radius: 10px;
        background: #480C17;
        color: #fff;
        border: 1px solid rgba(212, 175, 55, 0.3);
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
      }}
      .info-card .icon {{
        font-size: 16px;
        margin-bottom: 2px;
      }}
      .info-card .label {{
        font-size: 7.5px;
        letter-spacing: 1px;
        color: var(--gold-light);
      }}
      .info-card .main-val {{
        font-size: 13px;
        margin: 2px 0;
        font-weight: 700;
        color: #fff;
      }}
      .info-card .sub-val {{
        font-size: 7.5px;
        line-height: 1.15;
        color: #E2D3D5;
      }}
      .countdown-wrap {{
        width: 100%;
        background: rgba(72, 12, 23, 0.05);
        border: 1.5px solid rgba(212, 175, 55, 0.38);
        border-radius: 12px;
        padding: 10px 8px;
        margin-bottom: 12px;
        text-align: center;
      }}
      .countdown-label {{
        font-size: 8.5px;
        letter-spacing: 1.5px;
        margin-bottom: 3px;
        color: var(--gold-dark);
        font-weight: 600;
      }}
      .timer-units {{
        display: flex;
        justify-content: center;
        gap: 8px;
      }}
      .timer-unit .num {{
        font-size: 17px;
        font-weight: 700;
        color: var(--burgundy-card);
      }}
      .timer-unit .unit {{
        font-size: 8px;
        color: var(--ink-muted);
      }}
      .compliments-note {{
        font-size: 10.5px;
        line-height: 1.35;
        margin-top: 4px;
        text-align: center;
        color: var(--ink-muted);
      }}

      /* =========================================================
         SCENE 6: VENUE & ROUTE MAP MOBILE FIT
         ========================================================= */
      #scene-map {{
        padding: 26px 12px 8px 12px;
      }}
      .venue-title {{
        font-size: 12px;
        letter-spacing: 2px;
      }}
      .venue-sub {{
        font-size: 10.5px;
        margin-bottom: 4px;
      }}
      .gmap-frame-box {{
        flex: 1;
        min-height: 180px;
        margin-bottom: 6px;
      }}
    }}
  </style>
</head>
<body>

  <!-- Floating Particles Canvas -->
  <canvas id="particlesCanvas"></canvas>

    <!-- Discreet Corner Controls (Default Active Music) -->
  <div class="corner-controls">
    <button id="audioBtn" class="icon-btn music-active" title="Background Music: Bi Saraha by Abeer Nehme (Playing)">
      <span id="audioIcon">\U0001f50a</span>
    </button>
  </div>

  <!-- Default Background Music: Bi Saraha (Abeer Nehme) -->
  <audio id="bgMusic" autoplay loop preload="auto" playsinline webkit-playsinline>
    <source src="audio/bi_saraha.m4a" type="audio/mp4">
    <source src="audio/bi_saraha.mp3" type="audio/mpeg">
  </audio>

  <!-- Toast Notification -->
  <div id="toast" class="toast">Address copied to clipboard!</div>

  <!-- Main Presentation Stage -->
  <div class="stage-wrapper">

    <!-- Story Segmented Header Bar (Instagram / WhatsApp Model) -->
    <div class="story-header-bar" id="storyHeaderBar">
      <div class="story-dash" onclick="restartPresentation()" title="1. Cordially Invited"><div class="story-dash-fill"></div></div>
      <div class="story-dash" onclick="userGoToStep(2)" title="2. We're Getting Married"><div class="story-dash-fill"></div></div>
      <div class="story-dash" onclick="userGoToStep(3)" title="3. Twin Couples Artwork"><div class="story-dash-fill"></div></div>
      <div class="story-dash" onclick="userGoToStep(4)" title="4. Ceremony Details"><div class="story-dash-fill"></div></div>
      <div class="story-dash" onclick="userGoToStep(5)" title="5. Event Schedule"><div class="story-dash-fill"></div></div>
      <div class="story-dash" onclick="userGoToStep(6)" title="6. Venue & Route Map"><div class="story-dash-fill"></div></div>
    </div>

    <!-- =========================================================
         SCENE 1: ROYAL ENVELOPE OPENING SLOWLY DIRECTLY INTO "YOU'RE CORDIALLY INVITED"
         (Zero Blank Card: Envelope flaps unfold slowly over the invitation)
         ========================================================= -->
    <div id="scene-invited" class="invitation-card active">

      <!-- The 4 Flaps Unfolding Outward in 3D directly over the card -->
      <div class="envelope-flaps-overlay" id="envelopeBox" title="Click to Open Invitation">
        <div class="flap flap-top"></div>
        <div class="flap flap-bottom"></div>
        <div class="flap flap-left"></div>
        <div class="flap flap-right"></div>
        <div class="wax-seal" id="waxSeal" title="Click to Open Invitation"></div>
      </div>
      <div class="bismillah">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>
      
      <div class="reveal-container">
        <div class="fade-youre">YOU'RE</div>
        <div class="fade-cordially">C<span class="dot-o">O</span>RDIALLY</div>
        <div class="fade-invited">INVITED</div>
        
        <div class="gold-divider">
          <svg viewBox="0 0 24 24"><path d="M12 2L14.4 9.6L22 12L14.4 14.4L12 22L9.6 14.4L2 12L9.6 9.6L12 2Z"/></svg>
        </div>

        <p class="fade-subtext">
          to celebrate the joyous union and wedding ceremony of our beloved children
        </p>
      </div>

      <div class="card-nav-row">
        <button class="nav-link-btn" onclick="restartPresentation()">‹ Replay</button>
        <button class="gold-btn" onclick="userGoToStep(2)">Announcement ➔</button>
      </div>
    </div>

    <!-- =========================================================
         SCENE 3: WE'RE GETTING MARRIED (TWIN BRIDES & GROOMS)
         ========================================================= -->
    <div id="scene-couples" class="invitation-card">
      <div class="title-banner">WE'RE GETTING MARRIED</div>
      <div class="subtitle-banner">Two Sisters • Two Love Stories • One Auspicious Day</div>
      <div class="twins-badge">✨ Twin Wedding Celebration ✨</div>

      <div class="couples-stack">
        <!-- Couple 1 -->
        <div class="couple-card">
          <div class="couple-role">The First Union</div>
          <div class="write-wrap bride-write-1">
            <span class="bride-name write-text">Salmabee</span>
            <span class="pen-nib"></span>
          </div>
          <div class="ampersand ampersand-1">&</div>
          <div class="write-wrap groom-write-1">
            <span class="groom-name write-text">MUHAMMED AJNAS</span>
            <span class="pen-nib"></span>
          </div>
          <div class="couple-sub sub-1">(Daughter of Abdul Rahman & Zeenath Rahman)</div>
        </div>

        <div class="gold-divider" style="margin: 2px 0;">
          <svg viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
        </div>

        <!-- Couple 2 -->
        <div class="couple-card">
          <div class="couple-role">The Second Union</div>
          <div class="write-wrap bride-write-2">
            <span class="bride-name write-text">Rahmabee</span>
            <span class="pen-nib"></span>
          </div>
          <div class="ampersand ampersand-2">&</div>
          <div class="write-wrap groom-write-2">
            <span class="groom-name write-text">SHAHBAZ MUHAMMED</span>
            <span class="pen-nib"></span>
          </div>
          <div class="couple-sub sub-2">(Daughter of Abdul Rahman & Zeenath Rahman)</div>
        </div>
      </div>

      <div class="card-nav-row">
        <button class="nav-link-btn" onclick="userGoToStep(1)">‹ Back</button>
        <button class="gold-btn" onclick="userGoToStep(3)">View Portrait ➔</button>
      </div>
    </div>

    <!-- =========================================================
         SCENE 4: STANDARDIZED FULL-IMAGE COUPLES PORTRAIT
         ========================================================= -->
    <div id="scene-portrait" class="invitation-card">
        <div class="full-artwork-container">
          <!-- Pristine Background: Floral Crest & Golden Names & Canvas -->
          <img class="couples-bg-layer" src="{couples_bg_b64}" alt="Twin Wedding Floral Crest and Golden Calligraphy" />

          <!-- Left Bride & Groom (Salmabee & Muhammed Ajnas) moves from left side to exact place -->
          <img class="couple-left-layer" src="{couple_left_b64}" alt="Salmabee & Muhammed Ajnas" />

          <!-- Right Bride & Groom (Rahmabee & Shahbaz Muhammed) moves from right side to exact place -->
          <img class="couple-right-layer" src="{couple_right_b64}" alt="Rahmabee & Shahbaz Muhammed" />

          <!-- Translucent Bottom Navigation Overlay -->
          <div class="portrait-nav-overlay">
          <button class="nav-link-btn" onclick="userGoToStep(2)">‹ Back</button>
          <button class="gold-btn" onclick="userGoToStep(4)">Ceremony Details ➔</button>
        </div>
      </div>
    </div>

    <!-- =========================================================
         SCENE 4: CEREMONY DETAILS: TWIN UNIONS
         (Host Parents & Twin Marriages)
         ========================================================= -->
    <div id="scene-details" class="invitation-card">
      <div class="scene-body-content">
        <div class="card-top-header">WITH GRATEFUL HEART & GREAT HAPPINESS</div>

        <div class="parents-section">
          <div class="parents-names">Mr. Abdul Rahman & Mrs. Zeenath Rahman</div>
          <div class="residence-line">Puthukkudy, P.O. Vakayad, Naduvannur • Ph: 7034490662</div>
        </div>

        <p class="invite-text">
          We cordially invite you with family to share the happiness of the Wedding ceremony of our children:
        </p>

        <div class="couples-detail-grid">
          <div class="couple-detail-box">
            <div class="c-union-tag">THE FIRST UNION</div>
            <div class="c-bride">Salmabee</div>
            <div class="c-with">with</div>
            <div class="c-groom">MUHAMMED AJNAS</div>
            <div class="c-parentage">S/o. Abdul Rahiman & Fousiya<br>Mundakutty, Pathirikkara</div>
          </div>

          <div class="couple-detail-box">
            <div class="c-union-tag">THE SECOND UNION</div>
            <div class="c-bride">Rahmabee</div>
            <div class="c-with">with</div>
            <div class="c-groom">SHAHBAZ MUHAMMED</div>
            <div class="c-parentage">S/o. Muhammed & Shabana<br>Kunnathkandi, Kadiyangad</div>
          </div>
        </div>

        <div class="quran-blessing">
          “And He placed between you affection and mercy.”
          <div style="font-size: 11px; font-style: normal; letter-spacing: 1px; color: var(--burgundy-card); margin-top: 3px;">— SURAH AR-RUM 30:21 —</div>
        </div>
      </div>

      <div class="card-nav-row" style="margin-top: auto;">
        <button class="nav-link-btn" onclick="userGoToStep(3)">‹ Back</button>
        <button class="gold-btn" onclick="userGoToStep(5)">Event Schedule ➔</button>
      </div>
    </div>

    <!-- =========================================================
         SCENE 5: CEREMONY SCHEDULE & AUSPICIOUS DAY
         (Date, Residence, Time, Live Countdown & Calendar)
         ========================================================= -->
    <div id="scene-schedule" class="invitation-card">
      <div class="scene-body-content">
        <div class="insha-allah-header">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>
        <div class="insha-allah-sub">In Sha Allah</div>

        <!-- 3 Key Event Highlights Matching Physical Invitation -->
        <div class="event-info-cards">
          <div class="info-card">
            <div class="icon">📅</div>
            <div class="label">SATURDAY</div>
            <div class="main-val">07</div>
            <div class="sub-val">NOVEMBER<br>2026</div>
          </div>

          <div class="info-card">
            <div class="icon">📍</div>
            <div class="label">VENUE</div>
            <div class="main-val" style="font-size: 10px; line-height: 1.2;">AT OUR<br>RESIDENCE</div>
            <div class="sub-val">Vakayad<br>Naduvannur</div>
          </div>

          <div class="info-card">
            <div class="icon">⏰</div>
            <div class="label">TIME</div>
            <div class="main-val" style="font-size: 11px; line-height: 1.2;">BETWEEN<br>5 - 9 PM</div>
            <div class="sub-val">EVENING<br>CEREMONY</div>
          </div>
        </div>

        <!-- Live Countdown -->
        <div class="countdown-wrap">
          <div class="countdown-label">✦ Countdown to the Auspicious Day ✦</div>
          <div class="timer-units">
            <div class="timer-unit"><span class="num" id="t-days">00</span><span class="unit">Days</span></div>
            <div class="timer-unit"><span class="num" id="t-hours">00</span><span class="unit">Hours</span></div>
            <div class="timer-unit"><span class="num" id="t-mins">00</span><span class="unit">Mins</span></div>
            <div class="timer-unit"><span class="num" id="t-secs">00</span><span class="unit">Secs</span></div>
          </div>
        </div>

        <div class="compliments-note">
          With best compliments from:<br>
          <strong>Shajeem, Anzeela Shajeem, Rizwan, Haizam & Ayana</strong>
        </div>
      </div>

      <div class="card-nav-row" style="margin-top: auto;">
        <button class="nav-link-btn" onclick="userGoToStep(4)">‹ Back</button>
        <button class="gold-btn" onclick="userGoToStep(6)">Route Map ➔</button>
      </div>
    </div>

    <!-- =========================================================
       SCENE 6: VENUE, ADDRESS & ACCURATE GOOGLE MAP DIRECTIONS
       (Wish on WhatsApp & Call Host buttons REMOVED)
       ========================================================= -->
    <div id="scene-map" class="invitation-card">
      <div class="venue-title">VENUE & ROUTE MAP</div>
      <div class="venue-sub">We look forward to welcoming you with warmth and joy</div>

      <div class="address-card">
        <div class="residence-name">Abdul Rahman Residence (Puthukkudy)</div>
        <div class="full-address">
          Puthukkudy, P.O. Vakayad, Naduvannur<br>
          Kozhikode District, Kerala, India - 673614
        </div>
        <div class="phone-contact">
          📞 Ph: +91 7034490662
        </div>
      </div>

      <!-- Accurate Direct Google Maps Direction Embed -->
      <div class="gmap-frame-box">
        <iframe 
          title="Google Maps Direction to Abdul Rahman Residence, Vakayad, Naduvannur"
          src="https://maps.google.com/maps?q=Vakayad,+Naduvannur,+Kozhikode,+Kerala&t=&z=14&ie=UTF8&iwloc=&output=embed"
          allowfullscreen="" 
          loading="lazy">
        </iframe>
      </div>

      <!-- Focused Directions Buttons -->
      <div class="directions-btn-grid">
        <a class="dir-action-btn primary-directions" target="_blank" href="https://www.google.com/maps/dir/?api=1&destination=Vakayad,+Naduvannur,+Kerala">
          🗺️ Get Directions
        </a>
        <button class="dir-action-btn" onclick="copyAddress()">
          📋 Copy Address
        </button>
      </div>

      <div class="card-nav-row">
        <button class="nav-link-btn" onclick="userGoToStep(5)">‹ Back</button>
        <button class="gold-btn" onclick="restartPresentation()">✉️ Replay from Beginning</button>
      </div>
    </div>

  </div>

  <!-- Lightbox Modal -->
  <div class="lightbox-modal" id="lightboxModal" onclick="closeLightbox()">
    <div class="lightbox-content" onclick="event.stopPropagation()">
      <div class="lightbox-close" onclick="closeLightbox()">✕</div>
      <img src="{couples_b64}" alt="Twin Brides & Grooms - Salmabee & Muhammed Ajnas and Rahmabee & Shahbaz Muhammed" />
    </div>
  </div>

  <!-- Interactive Scripts -->
  <script>
    let currentStep = 1;
    let envelopeOpened = false;
    let autoPlayEnabled = true;
    let autoPlayTimer = null;

    const cards = [
      document.getElementById('scene-invited'),
      document.getElementById('scene-couples'),
      document.getElementById('scene-portrait'),
      document.getElementById('scene-details'),
      document.getElementById('scene-schedule'),
      document.getElementById('scene-map')
    ];

    /* Standard, peaceful pacing for each scene */
    const stepDurations = {{
      1: 13000, // 2.2s pause + 5.8s slow 3D unfold + 5.0s reading "You're Cordially Invited"
      2: 12500, // We're Getting Married (slow calligraphy writing animation)
      3: 8500,  // Full Artwork Card
      4: 8500,  // Ceremony Details (Twin Unions)
      5: 9000   // Ceremony Schedule & Live Countdown
    }};

    const storyDashes = document.querySelectorAll('.story-dash');
    let storyProgressRaf = null;
    let storyStartTime = 0;
    let storyPausedElapsed = 0;

    function updateStoryProgress(step) {{
      if (storyProgressRaf) cancelAnimationFrame(storyProgressRaf);
      storyPausedElapsed = 0;

      storyDashes.forEach((dash, idx) => {{
        const fill = dash.querySelector('.story-dash-fill');
        dash.classList.remove('active', 'completed', 'pending');

        if (idx + 1 < step) {{
          dash.classList.add('completed');
          fill.style.width = '100%';
        }} else if (idx + 1 > step) {{
          dash.classList.add('pending');
          fill.style.width = '0%';
        }} else {{
          dash.classList.add('active');
          fill.style.width = '0%';
          startDashAnimation(dash, fill, step);
        }}
      }});
    }}

    function startDashAnimation(dash, fill, step) {{
      const duration = stepDurations[step] || 8500;
      if (step === 6) {{
        fill.style.width = '100%';
        return;
      }}

      storyStartTime = performance.now() - storyPausedElapsed;

      function frame(now) {{
        if (!autoPlayEnabled) return;
        const elapsed = now - storyStartTime;
        const pct = Math.min(100, (elapsed / duration) * 100);
        fill.style.width = pct + '%';

        if (pct < 100) {{
          storyProgressRaf = requestAnimationFrame(frame);
        }} else {{
          goToStep(step + 1);
        }}
      }}
      storyProgressRaf = requestAnimationFrame(frame);
    }}

    function goToStep(step) {{
      if (step < 1 || step > 6) return;
      currentStep = step;

      cards.forEach((card, idx) => {{
        if (idx + 1 === step) {{
          card.classList.add('active');
        }} else {{
          card.classList.remove('active');
        }}
      }});

      window.scrollTo({{ top: 0, behavior: 'smooth' }});

      updateStoryProgress(step);
    }}

    function scheduleNextStep() {{
      if (autoPlayTimer) clearTimeout(autoPlayTimer);
      if (!autoPlayEnabled) return;

      const duration = stepDurations[currentStep];
      if (duration && currentStep < 6) {{
        autoPlayTimer = setTimeout(() => {{
          goToStep(currentStep + 1);
        }}, duration);
      }}
    }}

    function userGoToStep(step) {{
      goToStep(step);
    }}

    function nextStep() {{
      if (currentStep < 6) goToStep(currentStep + 1);
    }}

    function prevStep() {{
      if (currentStep > 1) goToStep(currentStep - 1);
    }}

    const autoPlayBtn = document.getElementById('autoPlayBtn');
    const autoPlayIcon = document.getElementById('autoPlayIcon');

    if (autoPlayBtn) {{
      autoPlayBtn.addEventListener('click', () => {{
        autoPlayEnabled = !autoPlayEnabled;
        if (autoPlayEnabled) {{
          if (autoPlayIcon) autoPlayIcon.innerText = '\u23f8';
          const activeDash = document.querySelector('.story-dash.active');
          if (activeDash) {{
            const fill = activeDash.querySelector('.story-dash-fill');
            startDashAnimation(activeDash, fill, currentStep);
          }}
          showToast('Auto-play enabled');
        }} else {{
          if (autoPlayIcon) autoPlayIcon.innerText = '\u25b6';
          if (storyProgressRaf) cancelAnimationFrame(storyProgressRaf);
          storyPausedElapsed = performance.now() - storyStartTime;
          showToast('Auto-play paused');
        }}
      }});
    }}

    // ==========================================
    // MAJESTIC SLOW 4-SIDE FLAP OPENING (3.8s)
    // ==========================================
    const envelopeBox = document.getElementById('envelopeBox');
    const waxSeal = document.getElementById('waxSeal');

    let envelopeTimeout = null;
    function openInvitation() {{
      if (envelopeOpened) return;
      envelopeOpened = true;

      playBackgroundSong();

      envelopeBox.classList.add('opened');
      // The 4 flaps unfold slowly in 3D over 3.8s directly revealing "YOU'RE CORDIALLY INVITED" underneath!
    }}

    waxSeal.addEventListener('click', openInvitation);
    envelopeBox.addEventListener('click', openInvitation);

    function restartPresentation() {{
      if (storyProgressRaf) cancelAnimationFrame(storyProgressRaf);
      if (autoPlayTimer) clearTimeout(autoPlayTimer);
      autoPlayEnabled = true;

      // Reset flaps and wax seal instantly without transition delay
      const flaps = document.querySelectorAll('.flap');
      flaps.forEach(f => f.style.transition = 'none');
      if (waxSeal) waxSeal.style.transition = 'none';

      envelopeOpened = false;
      envelopeBox.classList.remove('opened');

      // Force DOM reflow to apply closed state instantly
      void envelopeBox.offsetHeight;

      // Restore smooth 3D unfolding transitions
      flaps.forEach(f => f.style.transition = '');
      if (waxSeal) waxSeal.style.transition = '';

      // Navigate to Step 1 ("YOU'RE CORDIALLY INVITED" with closed envelope on top)
      goToStep(1);

      // Begin slow majestic 3D unfold after 1.8s peaceful pause
      setTimeout(() => {{
        if (!envelopeOpened && currentStep === 1) {{
          openInvitation();
        }}
      }}, 2200);
    }}

    // Direct opening flow on page load
    window.addEventListener('DOMContentLoaded', () => {{
      const urlParams = new URLSearchParams(window.location.search);
      const stepParam = parseInt(urlParams.get('step'));
      const openedParam = urlParams.get('opened');
      if (openedParam === '1') {{
        envelopeOpened = true;
        envelopeBox.classList.add('opened');
      }}
      if (stepParam && stepParam >= 1 && stepParam <= 6) {{
        if (stepParam > 1) {{
          envelopeOpened = true;
          envelopeBox.classList.add('opened');
        }}
        goToStep(stepParam);
      }} else {{
        updateStoryProgress(1);
        setTimeout(() => {{
          if (!envelopeOpened) {{
            openInvitation();
          }}
        }}, 2200);
      }}
    }});

    // ==========================================
    // FLOATING PARTICLES CANVAS
    // ==========================================
    const pCanvas = document.getElementById('particlesCanvas');
    const pCtx = pCanvas.getContext('2d');
    let particles = [];

    function resizeParticlesCanvas() {{
      pCanvas.width = window.innerWidth;
      pCanvas.height = window.innerHeight;
    }}
    window.addEventListener('resize', resizeParticlesCanvas);
    resizeParticlesCanvas();

    class Particle {{
      constructor() {{
        this.reset();
      }}
      reset() {{
        this.x = Math.random() * pCanvas.width;
        this.y = Math.random() * -50;
        this.size = Math.random() * 3.5 + 1.5;
        this.speedY = Math.random() * 0.7 + 0.3;
        this.speedX = Math.sin(Math.random() * Math.PI * 2) * 0.4;
        this.opacity = Math.random() * 0.5 + 0.2;
        this.rotation = Math.random() * 360;
        this.rotSpeed = (Math.random() - 0.5) * 1.2;
        this.isPetal = Math.random() > 0.6;
      }}
      update() {{
        this.y += this.speedY;
        this.x += this.speedX + Math.sin(this.y * 0.02) * 0.4;
        this.rotation += this.rotSpeed;
        if (this.y > pCanvas.height + 20) {{
          this.reset();
        }}
      }}
      draw() {{
        pCtx.save();
        pCtx.translate(this.x, this.y);
        pCtx.rotate((this.rotation * Math.PI) / 180);
        pCtx.globalAlpha = this.opacity;

        if (this.isPetal) {{
          pCtx.fillStyle = '#C2185B';
          pCtx.beginPath();
          pCtx.ellipse(0, 0, this.size * 1.4, this.size, 0, 0, Math.PI * 2);
          pCtx.fill();
        }} else {{
          pCtx.fillStyle = '#FFD700';
          pCtx.shadowColor = '#FFD700';
          pCtx.shadowBlur = 5;
          pCtx.beginPath();
          pCtx.arc(0, 0, this.size * 0.5, 0, Math.PI * 2);
          pCtx.fill();
        }}
        pCtx.restore();
      }}
    }}

    for (let i = 0; i < 26; i++) {{
      const p = new Particle();
      p.y = Math.random() * pCanvas.height;
      particles.push(p);
    }}

    function animateParticles() {{
      pCtx.clearRect(0, 0, pCanvas.width, pCanvas.height);
      particles.forEach(p => {{
        p.update();
        p.draw();
      }});
      requestAnimationFrame(animateParticles);
    }}
    animateParticles();

    // ==========================================
    // ==// ==========================================
    // DEFAULT BACKGROUND MUSIC SYSTEM: "BI SARAHA" (بصراحة)
    // ==========================================
    const bgMusic = document.getElementById('bgMusic');
    const audioBtn = document.getElementById('audioBtn');
    const audioIcon = document.getElementById('audioIcon');
    let isMusicPlaying = true; // Enabled and playing by default

    function playBackgroundSong() {{
      if (!bgMusic) return;
      bgMusic.volume = 0.70;
      const playPromise = bgMusic.play();
      if (playPromise !== undefined) {{
        playPromise.then(() => {{
          isMusicPlaying = true;
          if (audioIcon) audioIcon.innerText = '\U0001f50a';
          if (audioBtn) audioBtn.classList.add('music-active');
        }}).catch((err) => {{
          console.log('Autoplay waiting for first touch/interaction:', err);
        }});
      }}
    }}

    // 1. Immediately attempt default playback on load
    playBackgroundSong();

    // 2. Immediate gesture listener to guarantee default play on first screen touch/tap
    const unlockDefaultAudio = () => {{
      if (bgMusic) {{
        bgMusic.volume = 0.70;
        bgMusic.play().then(() => {{
          isMusicPlaying = true;
          if (audioIcon) audioIcon.innerText = '\U0001f50a';
          if (audioBtn) audioBtn.classList.add('music-active');
        }}).catch(() => {{}});
      }}
    }};

    ['click', 'touchstart', 'touchend', 'pointerdown'].forEach((evt) => {{
      document.addEventListener(evt, unlockDefaultAudio, {{ once: true, passive: true }});
      window.addEventListener(evt, unlockDefaultAudio, {{ once: true, passive: true }});
    }});

    function toggleBackgroundSong() {{
      if (!bgMusic) return;
      if (isMusicPlaying) {{
        bgMusic.pause();
        isMusicPlaying = false;
        if (audioIcon) audioIcon.innerText = '\U0001f507';
        if (audioBtn) audioBtn.classList.remove('music-active');
      }} else {{
        bgMusic.volume = 0.70;
        bgMusic.play().then(() => {{
          isMusicPlaying = true;
          if (audioIcon) audioIcon.innerText = '\U0001f50a';
          if (audioBtn) audioBtn.classList.add('music-active');
        }}).catch((e) => console.warn('Audio play error:', e));
      }}
    }}

    if (audioBtn) {{
      audioBtn.addEventListener('click', (e) => {{
        e.stopPropagation();
        toggleBackgroundSong();
      }});
    }}

    // ==========================================
    // LIVE WEDDING COUNTDOWN TIMER
    // ==========================================
    const weddingDate = new Date('2026-11-07T17:00:00+05:30').getTime();

    function updateCountdown() {{
      const now = new Date().getTime();
      const diff = weddingDate - now;

      if (diff > 0) {{
        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        const secs = Math.floor((diff % (1000 * 60)) / 1000);

        document.getElementById('t-days').innerText = String(days).padStart(2, '0');
        document.getElementById('t-hours').innerText = String(hours).padStart(2, '0');
        document.getElementById('t-mins').innerText = String(mins).padStart(2, '0');
        document.getElementById('t-secs').innerText = String(secs).padStart(2, '0');
      }} else {{
        document.getElementById('t-days').innerText = '00';
        document.getElementById('t-hours').innerText = '00';
        document.getElementById('t-mins').innerText = '00';
        document.getElementById('t-secs').innerText = '00';
      }}
    }}
    setInterval(updateCountdown, 1000);
    updateCountdown();

    function showToast(msg) {{
      const t = document.getElementById('toast');
      t.innerText = msg;
      t.classList.add('show');
      setTimeout(() => {{
        t.classList.remove('show');
      }}, 2600);
    }}

    function copyAddress() {{
      const address = "Puthukkudy, P.O. Vakayad, Naduvannur, Kozhikode District, Kerala - 673614. Contact: 7034490662";
      navigator.clipboard.writeText(address).then(() => {{
        showToast('Address copied to clipboard!');
      }}).catch(() => {{
        showToast('Address: Puthukkudy, Vakayad, Naduvannur');
      }});
    }}

    function downloadICal() {{
      const icsData = [
        'BEGIN:VCALENDAR',
        'VERSION:2.0',
        'PRODID:-//Twin Wedding Invitation//EN',
        'CALSCALE:GREGORIAN',
        'METHOD:PUBLISH',
        'BEGIN:VEVENT',
        'SUMMARY:Wedding Ceremony of Salmabee & Muhammed Ajnas and Rahmabee & Shahbaz Muhammed',
        'DESCRIPTION:We cordially invite you with family to share the happiness of the Wedding ceremony of our children: Salmabee with Muhammed Ajnas and Rahmabee with Shahbaz Muhammed. Hosted by Mr. Abdul Rahman & Mrs. Zeenath Rahman.',
        'LOCATION:Puthukkudy, P.O. Vakayad, Naduvannur, Kozhikode, Kerala 673614',
        'DTSTART:20261107T113000Z',
        'DTEND:20261107T153000Z',
        'STATUS:CONFIRMED',
        'END:VEVENT',
        'END:VCALENDAR'
      ].join('\\r\\n');

      const blob = new Blob([icsData], {{ type: 'text/calendar;charset=utf-8' }});
      const link = document.createElement('a');
      link.href = window.URL.createObjectURL(blob);
      link.setAttribute('download', 'Wedding_Salmabee_Rahmabee.ics');
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      showToast('Calendar event downloaded!');
    }}

    function openLightbox() {{
      document.getElementById('lightboxModal').classList.add('open');
    }}
    function closeLightbox() {{
      document.getElementById('lightboxModal').classList.remove('open');
    }}

    // ==========================================
    // MOBILE TAP & GESTURE NAVIGATION
    // (Tap right to advance, tap left to go back, swipe left/right supported)
    // ==========================================
    let touchStartX = 0;
    let touchStartY = 0;
    let touchStartTime = 0;

    document.addEventListener('touchstart', (e) => {{
      if (e.touches.length > 0) {{
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
        touchStartTime = performance.now();
      }}
    }}, {{ passive: true }});

    document.addEventListener('touchend', (e) => {{
      if (e.changedTouches.length === 0) return;
      const endX = e.changedTouches[0].clientX;
      const endY = e.changedTouches[0].clientY;
      const deltaX = endX - touchStartX;
      const deltaY = endY - touchStartY;
      const elapsedTime = performance.now() - touchStartTime;

      // 1. Check for horizontal swipe gesture (> 45px movement)
      if (Math.abs(deltaX) > 45 && Math.abs(deltaX) > Math.abs(deltaY) * 1.2) {{
        if (deltaX < 0) {{
          nextStep(); // Swiped left -> Next page
        }} else {{
          prevStep(); // Swiped right -> Previous page
        }}
        return;
      }}

      // 2. Check for screen tap (< 18px movement within 380ms)
      if (Math.abs(deltaX) < 18 && Math.abs(deltaY) < 18 && elapsedTime < 380) {{
        // If tapping on interactive elements (buttons, links, map, controls), ignore screen tap
        const interactiveTarget = e.target.closest('button, a, .icon-btn, .story-dash, iframe, input, select');
        if (interactiveTarget) return;

        // If on Scene 1 and envelope is not yet opened, tap opens envelope
        if (currentStep === 1 && !envelopeOpened) {{
          openInvitation();
          return;
        }}

        // Tap left 30% of screen: Go to previous page
        if (endX < window.innerWidth * 0.32) {{
          prevStep();
        }} else {{
          // Tap main / right area (68% of screen): Move to next page!
          nextStep();
        }}
      }}
    }}, false);

    // Also support mouse click on stage for desktop preview
    const stageWrapper = document.querySelector('.stage-wrapper');
    if (stageWrapper) {{
      stageWrapper.addEventListener('click', (e) => {{
        // If clicking on interactive elements, let the button handle it
        if (e.target.closest('button, a, .icon-btn, .story-dash, iframe, input, select, #waxSeal, .envelope-flaps-overlay')) {{
          return;
        }}
        if (currentStep === 1 && !envelopeOpened) {{
          openInvitation();
          return;
        }}
        const rect = stageWrapper.getBoundingClientRect();
        const clickX = e.clientX - rect.left;
        if (clickX < rect.width * 0.32) {{
          prevStep();
        }} else {{
          nextStep();
        }}
      }});
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === ' ') nextStep();
      if (e.key === 'ArrowLeft') prevStep();
    }});
  </script>
</body>
</html>
'''

output_scratch = os.path.join(base_dir, "index.html")
with open(output_scratch, "w", encoding="utf-8") as f:
    f.write(html_content)

output_scratch_alias = os.path.join(base_dir, "wedding_invitation.html")
with open(output_scratch_alias, "w", encoding="utf-8") as f:
    f.write(html_content)

output_brain = os.path.join(brain_dir, "wedding_invitation.html")
with open(output_brain, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Updated directions and removed section successfully:")
print("1. Scratch index.html:", os.path.exists(output_scratch), "Size:", os.path.getsize(output_scratch))
print("2. Brain wedding_invitation.html:", os.path.exists(output_brain), "Size:", os.path.getsize(output_brain))
