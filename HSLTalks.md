---
title: HSLTalks – Official Pilot Proposal for Demo Day 17.6.2025
author: Hiroshi Doyu, [NinjaLABO](https://ninjalabo.ai)
date: \today
header-includes:
  - \usepackage[colorlinks=true,linkcolor=red,urlcolor=blue,citecolor=green]{hyperref}

---



#  HSLTalks – Official Pilot Proposal for Demo Day 17.6.2025

![](images/HSLTalks.png){height=100%}

## 1. Pilot Title and Summary

### **Title**

HSLTalks – Conversational Public Transport Assistant


### **Summary**

HSLTalks transforms [Espoo](https://www.espoo.fi/en)’s existing [digital signage displays (DSDs)](https://omatnaytot.hsl.fi/monitors) into interactive, [AI](https://openai.com/research)-powered mobility assistants. Users scan a [QR code](https://en.wikipedia.org/wiki/QR_code) to access a browser-based [chatbot](https://platform.openai.com/docs/guides/gpt) that responds to questions about routes, delays, or multimodal options — unlocking the full value of [HSL](https://www.hsl.fi/en)'s [Journey Planner](https://reittiopas.hsl.fi/) APIs.


## 2. Pilot Objectives
1. **Unlock HSL’s Underused APIs:** Enable access to [Digitransit](https://digitransit.fi/en/) data (e.g., routing, [GTFS-RT](https://developers.google.com/transit/gtfs-realtime), bike stations) through [natural language](https://en.wikipedia.org/wiki/Natural-language_user_interface) interaction.
2. **Integrate Open Data Sources:** Combine HSL API with [City of Espoo Open Data](https://www.espoo.fi/en/open-data) (e.g., weather, traffic, parking) for context-aware route suggestions.
3. **Interactive Digital Signage:** Repurpose DSDs into two-way interfaces using HTML + [iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe), requiring no hardware changes.


**Impact on Espoo’s 2030 Carbon Neutrality Goals:**
HSLTalks promotes eco-friendly travel by improving accessibility and awareness of transit alternatives (e.g., bike+metro, park-and-ride). Even small shifts away from car usage result in [CO2 savings](https://www.iea.org/topics/transport).

## 3. Target User Groups
- **Residents**: especially those who use the HSL app only to buy tickets.
- **Visitors**: unfamiliar with local options and language.
- **Seniors / Accessibility Users**: who benefit from large screens and voice interaction.

![](images/SCTalks.png){height=100%}

**Experience Improvements**:
- Voice/text interaction in Finnish, English, or other languages.
- No app installation — only a QR scan.
- Visual reply panel on DSD shows map + chat replies.
- Accessible design (large display, simple UI, voice support).

## 4. Pilot Location
- **Site:** [Tapiola Metro & Bus Terminal](https://www.hsl.fi/en/tapiola-metrostation)
- **Justification:** High-traffic hub with existing DSD infrastructure and diverse daily users.

## 5. Timeline
- **Aug–Sep 2025:** UI design + API integration ([FastHTML](https://medium.com/@pol.avec/ai-is-the-new-ui-generative-ui-with-fasthtml-e8cfcc98e5b5) prototype)
- **Oct–Nov 2025:** Deploy to 2–3 screens in Tapiola. Collect feedback.
- **Dec 2025:** Analyze KPIs, report results.

## 6. Technical Setup
- **Software:**
  - HSLTalks chatbot UI (HTML/JS)
  - [ChatGPT](https://platform.openai.com/docs)
  - [HSL Routing API](https://digitransit.fi/en/developers/apis/1-routing-api/), [Realtime APIs](https://digitransit.fi/en/developers/apis/2-routing-api/gtfs-realtime/)
  - [Espoo traffic + weather APIs](https://www.espoo.fi/en/open-data)
- **Hardware:**
  - Existing DSDs + smartphones (BYOD)
- **Integration:**
  - Display via browser + iframe
  - No SDK access required initially

## 7. Cost Breakdown (Total €10,000)
- **Development (chat/API integration):** €4,000
- **Deployment (DSD layout integration + testing):** €4,000
- **Infra/data/API:** Provided in-kind by [HSL](https://www.hsl.fi/en) and [City of Espoo](https://www.espoo.fi/en)
- **Cloud/API usage:**  €2,000

## 8. KPIs & Outcomes
- **Social:**
  - 200+ unique QR/chat users
  - \>80% satisfaction from short post-chat surveys
  - Voice & multilingual usage tracked

## 9. Scalability & Sustainability
- **Citywide:** Extend to Otaniemi, Leppävaara, Espoo Center
- **Regional:** Apply across the [HSL area](https://www.hsl.fi/en)
- **National:** Cities using [Digitransit](https://digitransit.fi/en/) APIs
- **Long-term:** Embed into [HSL App](https://www.hsl.fi/en/app) or national MaaS solutions

## 10. Risks and Mitigations
- **DSD Integration Risk** → Start with a simple iframe.
- **Low Usage** → displaying conversation examples.

## 11. Support Needed
- HTML injection rights or [CMS](https://en.wikipedia.org/wiki/Web_content_management_system) access to DSD
- Optional: Social post by Espoo/HSL to raise awareness

## 12. Demo (PoC)
- Live HTML prototype simulating HSL use case
- DSD shows chatbot, map, and journey result
- ~~Voice + multilingual queries~~
- Example: *Scan → Ask “How to reach Espoo City Hall?” → See reply + visualized route*

---

© 2025 [NinjaLABO](https://ninjalabo.ai) | Made in Finland
