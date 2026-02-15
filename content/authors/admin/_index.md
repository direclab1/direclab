---
# Display name
title: H. David Jeong

# Full Name (for SEO)
first_name: H. David
last_name: Jeong

# Is this the primary user of the site?
superuser: true

# Role/position
role: Professor & Associate Department Head

# Organizations/Affiliations
organizations:
  - name: Department of Construction Science
    url: ''
  - name: Texas A&M University
    url: 'https://www.tamu.edu'

# Short bio (displayed in user profile at end of posts)
bio: My research focuses on applying data analytics and artificial intelligence to construction management, natural language processing, civil integrated management, and infrastructure asset management.

# Social/Academic Networking
social:
  - icon: envelope
    icon_pack: fas
    link: 'mailto:djeong@tamu.edu'
  - icon: google-scholar
    icon_pack: ai
    link: https://scholar.google.com/citations?user=djeong
  - icon: building
    icon_pack: fas
    link: https://construction.arch.tamu.edu/

# Enter email to display Gravatar (if Gravatar enabled in Config)
email: 'djeong@tamu.edu'

# Highlight the author in author lists? (true/false)
highlight_name: true

# Organizational groups that you belong to (for People widget)
user_groups:
  - Director

# Disable the "Latest" publications section
show_related: false
---

Dr. H. David Jeong is a Professor and Associate Department Head in the Department of Construction Science at Texas A&M University. His research focuses on applying data analytics and artificial intelligence to construction management, natural language processing, civil integrated management, and infrastructure asset management.

<style>
/* Hide Latest section with CSS */
.page-body .stream-item,
.page-body .pub-list-item,
.page-body ul.ul-edu,
.page-body ul.ul-interests {
  display: none !important;
}
/* Hide Latest heading */
.page-body h2:has(+ .stream-item),
.page-body h2:has(+ .pub-list-item) {
  display: none !important;
}
/* Adjust font size and spacing for content */
.article-style p {
  font-size: 0.9rem !important;
  line-height: 1.8 !important;
  margin-bottom: 1.2rem !important;
}
.article-style ul {
  font-size: 0.9rem !important;
  line-height: 1.8 !important;
  margin-bottom: 1.2rem !important;
}
.article-style li {
  margin-bottom: 0.6rem !important;
}
/* Reposition only Dr. Jeong's avatar within the circular crop */
#profile .avatar[alt="H. David Jeong"] {
  object-fit: cover;
  object-position: center 26%;
}
</style>

<script>
// Remove Latest section only
(function() {
  function removeLatest() {
    // Only remove h2 elements that contain "Latest" text
    document.querySelectorAll('h2').forEach(function(h2) {
      if (h2.textContent.trim().toLowerCase().includes('latest')) {
        let elem = h2.nextElementSibling;
        h2.remove();
        while (elem) {
          let next = elem.nextElementSibling;
          if (elem.tagName === 'H2') break;
          elem.remove();
          elem = next;
        }
      }
    });

    // Remove publication lists
    document.querySelectorAll('.stream-item, .pub-list-item').forEach(function(el) {
      el.remove();
    });
  }

  // Run immediately
  removeLatest();

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', removeLatest);
  }

  // Run after a short delay
  setTimeout(removeLatest, 100);
  setTimeout(removeLatest, 500);
  setTimeout(removeLatest, 1000);

  // Use MutationObserver to catch dynamically added content
  var observer = new MutationObserver(removeLatest);
  observer.observe(document.body, { childList: true, subtree: true });
})();
</script>

**Contact Information**

- Phone: (979) 458-9380
- Email: djeong@tamu.edu
- Office: Francis Hall, Room 321B, Texas A&M University, College Station, TX 77843-3137

**Education**

- **Ph.D.**, Purdue University, West Lafayette, Indiana, May 2005. Major: Civil Engineering, Concentration: Construction Engineering & Management
- **M.S.**, Purdue University, West Lafayette, Indiana, December 2001. Major: Civil Engineering, Concentration: Construction Engineering & Management
- **B.S.**, Seoul National University, Seoul, South Korea, February 1994. Major: Agricultural Engineering (Civil Engineering Emphasis)
- **Certificate:** Applied Management Principles Program (Mini-MBA), Krannert Graduate School of Management, Purdue University, West Lafayette, Indiana, August 2003

**Professional Experience**

- Texas A&M University, College Station, Texas: Associate Department Head, Department of Construction Science, January 2022 - Present
- Texas A&M University, College Station, Texas: Professor, Department of Construction Science, September 2018 - Present
- Texas A&M University, College Station, Texas: Ph.D. Program Coordinator, Department of Construction Science, September 2021 - August 2024
- Texas A&M University, College Station, Texas: Professor (Courtesy Appointment), Department of Multidisciplinary Engineering, September 2019 - Present
- Texas A&M University, College Station, Texas: Research Scientist, Texas A&M Transportation Institute (TTI), September 2018 - Present
- Iowa State University, Ames, Iowa: Professor, Department of Civil, Construction and Environmental Engineering, August 2018
- Iowa State University, Ames, Iowa: Associate Professor, Department of Civil, Construction and Environmental Engineering, August 2012 - July 2018
- Oklahoma State University, Stillwater, Oklahoma: Associate/Assistant Professor, School of Civil and Environmental Engineering, August 2005 - August 2012
- Purdue University, West Lafayette, Indiana: Graduate Research/Teaching Assistant, School of Civil Engineering, January 2001 - May 2005
- Daewoo Engineering & Construction Co., Seoul, South Korea: Assistant General Manager (Cost Engineer), January 1999 - April 2000
- Daewoo Engineering & Construction Co., Seoul, South Korea: Project Engineer, Korean High Speed Railway Project, June 1994 - December 1998

**Research Interests**

- Applications of Data Analytics and Artificial Intelligence to Construction Management
- Natural Language Processing for Construction Data Analytics
- Civil Integrated Management (CIM)
- Digital Project Delivery / Integrated Project Delivery
- Data and Information Integration Models for Enhanced Decision Making
- Visualization of information and decisions
- Infrastructure Asset Management

**Honors and Awards**

- 2024: Best Scholarly Paper of the Year Award, Journal of Construction Engineering and Management, ASCE
- 2023: Faculty Aspiring Leadership Program Fellow, Texas A&M University
- 2023: Editor's Choice Paper for May 2023, Journal of Management in Engineering, ASCE
- 2023: Best Poster Award, AKC10-Construction Management, 102nd Transportation Research Board (TRB) Annual Meeting, January 8-12, 2023, Washington, D.C.
- 2020: Editor's Choice Paper for May 2020, Journal of Management in Engineering, ASCE
- 2019: Most Valuable Researcher of the Year Award, Construction Science, Texas A&M University
- 2019-Present: The James C. Smith CIAC Endowed Professorship, Texas A&M University
- 2018: Editor's Choice Paper for July 2018, Journal of Management in Engineering, ASCE
- 2017: Nominated for ASCE Arthur M. Wellington Prize by the ASCE Journal of Construction Engineering and Management
- 2017: Charles W. Schafer Award for Excellence in Teaching, Research, and Service, CCEE, Iowa State University
- 2016: Best Scholarly Paper Award, Journal of Construction Engineering and Management, ASCE
- 2016: Outstanding Leadership Award, Korean-American Construction Engineering and Project Management Association (KACEPMA)
- 2016: Joseph C. & Elizabeth A. Anderlik Faculty Award for Excellence in Undergraduate Teaching, CCEE, Iowa State University
- 2015: Distinguished Professor Award, Construction Industry Institute (CII)
- 2013: Outstanding Reviewer Award, Journal of Pipeline Systems Engineering - Management & Practice, ASCE
- 2013: Outstanding Reviewer Award, Journal of Construction Engineering and Management, ASCE
- 2013: ARTBA Young Executive Development Program Fellow, American Road and Transportation Builders Association (ARTBA)
- 2012: Williams Foundation Professorship, Oklahoma State University
- 2011: Nominated for Halliburton Outstanding Junior Faculty Award, Oklahoma State University
- 2010: Outstanding Researcher of the Year Award, Construction Industry Institute (CII)
- 2008: Institute of Industrial Engineers (IIE) Transactions Award, Best Application Paper in Operations Engineering
- 2007: Chi Epsilon Outstanding Teacher of the Year, School of Civil & Environmental Engineering, Oklahoma State University
- 1993: Outstanding Junior Scholarship, Seoul National University Alumni Foundation
- 1990: Admittance Scholarship, Seoul National University (awarded to top two new students in the department)

**Professional Activities**

American Society of Civil Engineers (ASCE)
- Member since 2005
- Chair, Digital Project Delivery Committee (2017-2022)
- Secretary, Digital Project Delivery Committee (2014-2016)
- Assistant Specialty Editor, Journal of Construction Engineering and Management (2010-present)
- Associate Editor, Journal of Pipeline Systems (2009-present)
- Construction Research Council member (2005–present)
- Utility Pipeline Asset Management Committee member (2005–2010)
- Water Infrastructure Security Enhancement Standards Committee (2004–2008)

Construction Industry Institute (CII)
- Academic Advisor for Power, Utilities, and Infrastructure Sector Committee (2019)
- Research Committee member (2007–2016)

Transportation Research Board (TRB)
- Construction Management Committee member (2017–present)
- Emerging Design and Construction Technologies Committee (2017–2020)
- Civil Integrated Management Sub-Committee member
- Information Systems in Construction Management Subcommittee member
- Utilities Committee member (2014-2016)

Korean-American Construction Engineering & Project Management Association (CEPMA)
- President (2015–2016)
- Vice President (2014–2015)
- Founding Member/Secretary (2013–2014)

Additional Memberships
- Korean Institute of Civil Engineering research advisory board (2012–present)
- North American Society of Trenchless Technology (2002–2012)
- Buried Asset Management Institute–International (2006–2011)

**Publications**

Kindly visit the <a href="/direclab/publication/">Publications page</a> to view all past publications by Dr. David Jeong.
