---
title: Gallery
date: 2024-01-01

type: landing

sections:
  - block: markdown
    content:
      title: Gallery
      subtitle: Lab Activities and Events
      text: |
        <style>
        .home-section p {
          font-size: 0.9rem !important;
          line-height: 1.6 !important;
        }
        .crc-intro {
          max-width: 760px;
          margin-bottom: 1.6rem;
          color: #555;
        }
        .crc-event {
          margin-top: 2rem;
        }
        .crc-event-header {
          display: flex;
          justify-content: space-between;
          gap: 1rem;
          align-items: flex-end;
          margin-bottom: 1rem;
        }
        .crc-event h3 {
          margin: 0 !important;
          font-size: 1.35rem !important;
          font-weight: 650 !important;
        }
        .crc-event-date {
          margin: 0 !important;
          color: #777;
          font-size: 0.88rem !important;
          white-space: nowrap;
        }
        .crc-grid {
          display: grid;
          grid-template-columns: repeat(3, minmax(0, 1fr));
          gap: 18px;
          align-items: start;
        }
        .crc-card {
          border-radius: 8px;
          overflow: hidden;
          box-shadow: 0 2px 10px rgba(0,0,0,0.09);
          transition: transform 0.3s ease, box-shadow 0.3s ease;
          background: white;
        }
        .crc-card:hover {
          transform: translateY(-4px);
          box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        }
        .crc-card.feature {
          grid-column: 1 / -1;
        }
        .crc-card.wide {
          grid-column: span 2;
        }
        .crc-photo {
          width: 100%;
          background-color: #f7f7f7;
          background-position: center;
          background-repeat: no-repeat;
          background-size: contain;
        }
        .crc-photo.landscape {
          aspect-ratio: 3 / 2;
        }
        .crc-photo.portrait {
          aspect-ratio: 2 / 3;
        }
        .crc-photo.group {
          aspect-ratio: 4 / 3;
        }
        @media (max-width: 768px) {
          .crc-event-header {
            display: block;
          }
          .crc-event-date {
            margin-top: 4px !important;
            white-space: normal;
          }
          .crc-grid {
            grid-template-columns: 1fr;
          }
          .crc-card,
          .crc-card.feature,
          .crc-card.wide {
            grid-column: auto;
          }
        }
        </style>

        <p class="crc-intro">Snapshots from lab activities, conferences, and team moments throughout the years.</p>

        <div class="crc-event">
          <div class="crc-event-header">
            <h3>CRC 2026</h3>
            <p class="crc-event-date">ASCE CI CRC Conference - 2026</p>
          </div>

          <div class="crc-grid">
            <div class="crc-card feature">
              <div class="crc-photo landscape" role="img" aria-label="DIREC Lab members at CRC 2026" style="background-image: url('CRC%202026/web/crc2026-hero.jpg');"></div>
            </div>
            <div class="crc-card">
              <div class="crc-photo landscape" role="img" aria-label="CRC 2026 conference session" style="background-image: url('CRC%202026/web/crc2026-01.jpg');"></div>
            </div>
            <div class="crc-card">
              <div class="crc-photo landscape" role="img" aria-label="CRC 2026 presentation moment" style="background-image: url('CRC%202026/web/crc2026-02.jpg');"></div>
            </div>
            <div class="crc-card">
              <div class="crc-photo landscape" role="img" aria-label="CRC 2026 team conversation" style="background-image: url('CRC%202026/web/crc2026-03.jpg');"></div>
            </div>
            <div class="crc-card">
              <div class="crc-photo portrait" role="img" aria-label="CRC 2026 portrait moment" style="background-image: url('CRC%202026/web/crc2026-04.jpg');"></div>
            </div>
            <div class="crc-card wide">
              <div class="crc-photo landscape" role="img" aria-label="CRC 2026 conference activity" style="background-image: url('CRC%202026/web/crc2026-05.jpg');"></div>
            </div>
            <div class="crc-card">
              <div class="crc-photo landscape" role="img" aria-label="Taste of Texas reception at CRC 2026" style="background-image: url('CRC%202026/web/crc2026-06.jpg');"></div>
            </div>
            <div class="crc-card">
              <div class="crc-photo landscape" role="img" aria-label="Reception moment at CRC 2026" style="background-image: url('CRC%202026/web/crc2026-07.jpg');"></div>
            </div>
            <div class="crc-card wide">
              <div class="crc-photo landscape" role="img" aria-label="CRC 2026 group photo" style="background-image: url('CRC%202026/web/crc2026-08.jpg');"></div>
            </div>
            <div class="crc-card">
              <div class="crc-photo group" role="img" aria-label="CRC 2026 conference activity" style="background-image: url('CRC%202026/web/crc2026-11.jpg');"></div>
            </div>
          </div>
        </div>
    design:
      columns: '1'
---
