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
        .gallery-intro {
          max-width: 760px;
          margin-bottom: 1.6rem;
          color: #555;
        }
        .gallery-event {
          margin-top: 2rem;
        }
        .gallery-event-header {
          display: flex;
          justify-content: space-between;
          gap: 1rem;
          align-items: flex-end;
          margin-bottom: 1rem;
        }
        .gallery-event h3 {
          margin: 0 !important;
          font-size: 1.35rem !important;
          font-weight: 650 !important;
        }
        .gallery-event-date {
          margin: 0 !important;
          color: #777;
          font-size: 0.88rem !important;
          white-space: nowrap;
        }
        .gallery-feature {
          overflow: hidden;
          border-radius: 8px;
          margin-bottom: 16px;
          box-shadow: 0 6px 18px rgba(0,0,0,0.10);
          background: white;
        }
        .gallery-feature img {
          width: 100%;
          height: auto;
          display: block;
        }
        .gallery-feature-caption {
          padding: 10px 12px 12px;
          color: #555;
          font-size: 0.9rem;
          background: white;
        }
        .gallery-grid {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
          gap: 18px;
          margin-top: 0;
          align-items: start;
        }
        .gallery-item {
          overflow: hidden;
          border-radius: 8px;
          box-shadow: 0 2px 10px rgba(0,0,0,0.09);
          transition: transform 0.3s ease, box-shadow 0.3s ease;
          background: #f5f5f5;
        }
        .gallery-item:hover {
          transform: translateY(-4px);
          box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        }
        .gallery-item img {
          width: 100%;
          height: auto;
          display: block;
        }
        .gallery-item.large {
          grid-column: span 2;
        }
        .gallery-item.wide {
          grid-column: span 2;
        }
        .gallery-item.tall {
          grid-column: span 1;
        }
        .gallery-item.small {
          grid-column: span 1;
        }
        .gallery-caption {
          padding: 10px 12px 12px;
          background: white;
          font-size: 0.86rem;
          color: #555;
          text-align: left;
        }
        @media (max-width: 768px) {
          .gallery-event-header {
            display: block;
          }
          .gallery-event-date {
            margin-top: 4px !important;
            white-space: normal;
          }
          .gallery-grid {
            grid-template-columns: 1fr;
          }
          .gallery-item,
          .gallery-item.large,
          .gallery-item.wide,
          .gallery-item.tall,
          .gallery-item.small {
            grid-column: auto;
            grid-row: auto;
          }
        }
        </style>

        <p class="gallery-intro">Snapshots from lab activities, conferences, and team moments throughout the years.</p>

        <div class="gallery-event">
          <div class="gallery-event-header">
            <h3>CRC 2026</h3>
            <p class="gallery-event-date">ASCE CI CRC Conference - 2026</p>
          </div>

          <div class="gallery-feature">
            <img src="CRC%202026/web/crc2026-hero.jpg" alt="DIREC Lab members at CRC 2026">
            <div class="gallery-feature-caption">DIREC Lab at CRC 2026</div>
          </div>

          <div class="gallery-grid">
            <div class="gallery-item large">
              <img src="CRC%202026/web/crc2026-01.jpg" alt="CRC 2026 conference session" loading="lazy">
              <div class="gallery-caption">Conference sessions</div>
            </div>
            <div class="gallery-item wide">
              <img src="CRC%202026/web/crc2026-02.jpg" alt="CRC 2026 presentation moment" loading="lazy">
              <div class="gallery-caption">Presentation moments</div>
            </div>
            <div class="gallery-item small">
              <img src="CRC%202026/web/crc2026-03.jpg" alt="CRC 2026 team conversation" loading="lazy">
              <div class="gallery-caption">Around the venue</div>
            </div>
            <div class="gallery-item tall">
              <img src="CRC%202026/web/crc2026-04.jpg" alt="CRC 2026 portrait moment" loading="lazy">
              <div class="gallery-caption">Between sessions</div>
            </div>
            <div class="gallery-item wide">
              <img src="CRC%202026/web/crc2026-05.jpg" alt="CRC 2026 conference activity" loading="lazy">
              <div class="gallery-caption">CRC 2026</div>
            </div>
            <div class="gallery-item small">
              <img src="CRC%202026/web/crc2026-06.jpg" alt="Taste of Texas reception at CRC 2026" loading="lazy">
              <div class="gallery-caption">Taste of Texas reception</div>
            </div>
            <div class="gallery-item small">
              <img src="CRC%202026/web/crc2026-07.jpg" alt="Reception moment at CRC 2026" loading="lazy">
              <div class="gallery-caption">Reception moments</div>
            </div>
            <div class="gallery-item large">
              <img src="CRC%202026/web/crc2026-08.jpg" alt="CRC 2026 group photo" loading="lazy">
              <div class="gallery-caption">Team time</div>
            </div>
            <div class="gallery-item wide">
              <img src="CRC%202026/web/crc2026-11.jpg" alt="CRC 2026 conference activity" loading="lazy">
              <div class="gallery-caption">Conference week</div>
            </div>
          </div>
        </div>
    design:
      columns: '1'
---
