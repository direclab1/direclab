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
          position: relative;
          overflow: hidden;
          border-radius: 8px;
          margin-bottom: 16px;
          box-shadow: 0 8px 24px rgba(0,0,0,0.12);
          background: #f5f5f5;
        }
        .gallery-feature img {
          width: 100%;
          height: min(58vh, 520px);
          min-height: 320px;
          object-fit: cover;
          display: block;
        }
        .gallery-feature-caption {
          position: absolute;
          left: 0;
          right: 0;
          bottom: 0;
          padding: 32px 18px 16px;
          color: white;
          font-size: 0.95rem;
          background: linear-gradient(to top, rgba(0,0,0,0.64), rgba(0,0,0,0));
        }
        .gallery-grid {
          display: grid;
          grid-template-columns: repeat(6, 1fr);
          grid-auto-rows: 150px;
          gap: 14px;
          margin-top: 0;
        }
        .gallery-item {
          position: relative;
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
          height: 100%;
          object-fit: cover;
          display: block;
        }
        .gallery-item.large {
          grid-column: span 3;
          grid-row: span 2;
        }
        .gallery-item.wide {
          grid-column: span 3;
        }
        .gallery-item.tall {
          grid-column: span 2;
          grid-row: span 2;
        }
        .gallery-item.small {
          grid-column: span 2;
        }
        .gallery-caption {
          position: absolute;
          left: 0;
          right: 0;
          bottom: 0;
          padding: 28px 12px 10px;
          background: linear-gradient(to top, rgba(0,0,0,0.58), rgba(0,0,0,0));
          font-size: 0.86rem;
          color: white;
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
          .gallery-feature img {
            height: 320px;
            min-height: 0;
          }
          .gallery-grid {
            grid-template-columns: 1fr;
            grid-auto-rows: auto;
          }
          .gallery-item,
          .gallery-item.large,
          .gallery-item.wide,
          .gallery-item.tall,
          .gallery-item.small {
            grid-column: auto;
            grid-row: auto;
          }
          .gallery-item img {
            height: auto;
            aspect-ratio: 4 / 3;
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
            <div class="gallery-item small">
              <img src="CRC%202026/web/crc2026-09.jpg" alt="CRC 2026 casual group photo" loading="lazy">
              <div class="gallery-caption">More from CRC</div>
            </div>
            <div class="gallery-item tall">
              <img src="CRC%202026/web/crc2026-10.jpg" alt="CRC 2026 portrait photo" loading="lazy">
              <div class="gallery-caption">A quick pause</div>
            </div>
            <div class="gallery-item wide">
              <img src="CRC%202026/web/crc2026-11.jpg" alt="CRC 2026 conference activity" loading="lazy">
              <div class="gallery-caption">Conference week</div>
            </div>
            <div class="gallery-item wide">
              <img src="CRC%202026/web/crc2026-12.jpg" alt="CRC 2026 casual team photo" loading="lazy">
              <div class="gallery-caption">Closing out CRC</div>
            </div>
          </div>
        </div>
    design:
      columns: '1'
---
