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
        .gallery-grid {
          display: grid;
          grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
          gap: 20px;
          margin-top: 2rem;
        }
        .gallery-item {
          position: relative;
          overflow: hidden;
          border-radius: 8px;
          box-shadow: 0 2px 8px rgba(0,0,0,0.1);
          transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .gallery-item:hover {
          transform: translateY(-5px);
          box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        }
        .gallery-item img {
          width: 100%;
          height: 250px;
          object-fit: cover;
          display: block;
        }
        .gallery-caption {
          padding: 12px;
          background: white;
          font-size: 0.9rem;
          color: #666;
          text-align: center;
        }
        </style>

        Explore our lab's activities, events, and team moments captured throughout the years.

        <div class="gallery-grid">
          <!-- Add gallery items here -->
          <!-- Example:
          <div class="gallery-item">
            <img src="event-1.jpg" alt="Lab Event 1">
            <div class="gallery-caption">Team Meeting - Fall 2024</div>
          </div>
          -->
        </div>
    design:
      columns: '1'
---
