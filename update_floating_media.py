import re

with open("index.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# ---------------------------------------------------------------------------
# 1. NEW CSS FOR SECTION 4: FEATURED VIDEO & FLOATING MEDIA STREAM (LEFT TO RIGHT)
# ---------------------------------------------------------------------------
new_field_css = """/* ==========================================================================
   SECTION 4: FEATURED VIDEO & IMMERSIVE FLOATING MEDIA STREAM (LEFT TO RIGHT)
   ========================================================================== */
#tested-in-field {
  position: relative;
  background-color: var(--soft-grey);
  padding: 6rem 0 5rem;
  overflow: hidden;
}

#tested-in-field .section-header-wrap {
  max-width: 1100px;
  margin: 0 auto 3rem;
  padding: 0 6vw;
  text-align: center;
}

/* Featured Video Container & Player */
.featured-video-container {
  max-width: 1240px;
  margin: 0 auto 4rem;
  padding: 0 4vw;
}

.featured-video-card {
  background: #111317;
  border-radius: 16px;
  overflow: hidden;
  display: grid;
  grid-template-columns: 1.35fr 1fr;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.18);
}

.video-player-box {
  background: #000;
  position: relative;
  min-height: 380px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.video-player-box video {
  width: 100%;
  height: 100%;
  max-height: 480px;
  object-fit: cover;
  display: block;
}

.video-info-box {
  padding: 2.5rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: var(--white);
  background: #15181e;
}

.video-tag-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: var(--orange-dim);
  color: var(--orange);
  border: 1px solid rgba(245, 138, 31, 0.3);
  border-radius: 999px;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  padding: 5px 14px;
  margin-bottom: 1rem;
  width: fit-content;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.video-title {
  font-family: var(--font-display);
  font-size: clamp(1.4rem, 2.2vw, 1.9rem);
  font-weight: 700;
  color: var(--white);
  margin-bottom: 0.8rem;
  line-height: 1.2;
  text-transform: uppercase;
}

.video-desc {
  color: var(--txt-secondary);
  font-size: 0.92rem;
  line-height: 1.6;
  margin-bottom: 1.8rem;
}

.video-specs-inline {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 1.4rem;
}

.vspec-item {
  display: flex;
  flex-direction: column;
}

.vspec-val {
  font-family: var(--font-mono);
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--white);
}

.vspec-lbl {
  font-size: 0.68rem;
  color: var(--txt-secondary);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-top: 2px;
}

/* ==========================================================================
   FLOATING MEDIA STREAM (FLOWING CONTINUOUSLY FROM LEFT TO RIGHT)
   ========================================================================== */
.floating-stream-section-header {
  text-align: center;
  max-width: 900px;
  margin: 0 auto 1.5rem;
  padding: 0 4vw;
}

.stream-eyebrow {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--orange);
  letter-spacing: 0.12em;
  font-weight: 600;
  text-transform: uppercase;
  margin-bottom: 0.4rem;
}

.stream-title {
  font-family: var(--font-display);
  font-size: clamp(1.8rem, 3vw, 2.5rem);
  font-weight: 700;
  color: var(--txt-dark);
  text-transform: uppercase;
  margin-bottom: 0.5rem;
}

.stream-subtitle {
  color: var(--txt-dark-sub);
  font-size: 0.95rem;
  line-height: 1.5;
}

.media-marquee-container {
  position: relative;
  width: 100vw;
  margin-left: calc(-50vw + 50%);
  margin-right: calc(-50vw + 50%);
  overflow: hidden;
  padding: 2.2rem 0 3.2rem;
  mask-image: linear-gradient(to right, transparent 0%, black 8%, black 92%, transparent 100%);
  -webkit-mask-image: linear-gradient(to right, transparent 0%, black 8%, black 92%, transparent 100%);
}

.media-marquee-track {
  display: flex;
  gap: 26px;
  width: max-content;
  /* Animates from -50% to 0% = FLOATS CONTINUOUSLY FROM LEFT TO RIGHT */
  animation: floatStreamLeftToRight 50s linear infinite;
  will-change: transform;
}

.media-marquee-container:hover .media-marquee-track {
  animation-play-state: paused;
}

/* Left-to-Right Floating Keyframe */
@keyframes floatStreamLeftToRight {
  0% {
    transform: translateX(-50%);
  }
  100% {
    transform: translateX(0%);
  }
}

/* Subtle Organic Floating Bobbing Animation */
@keyframes cardFloatBob {
  0% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-12px);
  }
  100% {
    transform: translateY(0px);
  }
}

/* Individual Floating Media Cards */
.zoom-media-card {
  flex: 0 0 340px;
  width: 340px;
  height: 385px;
  background: var(--white);
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 14px 35px rgba(0, 0, 0, 0.07);
  display: flex;
  flex-direction: column;
  cursor: pointer;
  animation: cardFloatBob 5.5s ease-in-out infinite;
  transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.35s ease, border-color 0.35s ease;
  user-select: none;
}

/* Staggered Floating Offsets for Organic Waves */
.zoom-media-card:nth-child(2n) {
  animation-delay: -1.8s;
  animation-duration: 6.2s;
}

.zoom-media-card:nth-child(3n) {
  animation-delay: -3.4s;
  animation-duration: 5.8s;
}

.zoom-media-card:nth-child(4n) {
  animation-delay: -4.6s;
  animation-duration: 6.8s;
}

.zoom-media-card:hover {
  transform: translateY(-16px) scale(1.03) !important;
  border-color: var(--orange);
  box-shadow: 0 24px 50px rgba(245, 138, 31, 0.22);
}

.zoom-media-frame {
  position: relative;
  height: 220px;
  width: 100%;
  overflow: hidden;
  background: #090a0c;
}

.zoom-media-frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.6s var(--transition-smooth);
}

.zoom-media-card:hover .zoom-media-frame img {
  transform: scale(1.1);
}

.zoom-media-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  z-index: 5;
  background: rgba(17, 17, 17, 0.88);
  backdrop-filter: blur(8px);
  color: var(--white);
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 6px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  border: 1px solid rgba(255, 255, 255, 0.14);
}

.zoom-click-hint {
  position: absolute;
  inset: 0;
  background: rgba(17, 17, 17, 0.45);
  backdrop-filter: blur(2px);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  color: var(--white);
  font-family: var(--font-heading);
  font-size: 0.84rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 6;
}

.zoom-media-card:hover .zoom-click-hint {
  opacity: 1;
}

.zoom-card-body {
  padding: 16px 20px;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background: var(--white);
}

.zoom-card-title {
  font-family: var(--font-heading);
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--txt-dark);
  text-transform: uppercase;
  line-height: 1.25;
  margin-bottom: 6px;
}

.zoom-card-desc {
  font-size: 0.82rem;
  color: var(--txt-dark-sub);
  line-height: 1.5;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

.zoom-card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--orange);
  font-weight: 600;
  text-transform: uppercase;
  padding-top: 10px;
  margin-top: 8px;
  border-top: 1px solid var(--soft-grey-border);
}
"""

# Insert new_field_css right above /* ALL IMAGES & CAD DIMENSIONS LABELED GALLERY GRID */
if "/* ALL IMAGES & CAD DIMENSIONS LABELED GALLERY GRID */" in html:
    html = html.replace(
        "/* ALL IMAGES & CAD DIMENSIONS LABELED GALLERY GRID */",
        new_field_css + "\n/* ALL IMAGES & CAD DIMENSIONS LABELED GALLERY GRID */"
    )
    print("Section 4 CSS injected successfully!")
else:
    print("Warning: anchor for Section 4 CSS not found, appending to styles")
    html = html.replace("</style>", new_field_css + "\n</style>")

# ---------------------------------------------------------------------------
# 2. NEW HTML FOR SECTION 4: IMMACULATE ALIGNMENT & DUAL-SET FLOATING STREAM
# ---------------------------------------------------------------------------
items_markup = """
        <!-- Item 1: Real Field Video -->
        <div class="zoom-media-card" onclick="openMediaLightbox('video', 'field-trial-video.mp4', 'Agrosteed Stredo HS-2T Field Trenching Demonstration', 'Watch the heavy-duty backhoe attachment in deep trenching action on farmland.')">
          <div class="zoom-media-frame">
            <img src="product.jpeg" alt="Field Video Thumbnail" loading="lazy">
            <div class="zoom-media-badge">Video • Field Trial</div>
            <div class="zoom-click-hint">▶ Click to Play Video</div>
          </div>
          <div class="zoom-card-body">
            <div>
              <h4 class="zoom-card-title">Stredo Field Trenching Video</h4>
              <p class="zoom-card-desc">Live footage of high-torque canal and plantation excavation.</p>
            </div>
            <div class="zoom-card-footer">
              <span>● Field Trial MP4</span>
              <span>2.85M Depth</span>
            </div>
          </div>
        </div>

        <!-- Item 2: Real Farm Rear Hitch -->
        <div class="zoom-media-card" onclick="openMediaLightbox('image', 'WhatsApp Image 2026-10-24 at 2.22.52 PM.jpeg', 'Agrosteed Stredo Tractor Rear Hitch Mount', 'Heavy-duty 3-point tractor connection subframe with ergonomic hydraulic control levers.')">
          <div class="zoom-media-frame">
            <img src="WhatsApp Image 2026-10-24 at 2.22.52 PM.jpeg" alt="Rear Hitch Mount" loading="lazy">
            <div class="zoom-media-badge">Field Photo • Subframe</div>
            <div class="zoom-click-hint">🔍 Click to Zoom</div>
          </div>
          <div class="zoom-card-body">
            <div>
              <h4 class="zoom-card-title">Rear Mount & Valve Bank</h4>
              <p class="zoom-card-desc">Ergonomic joystick control console and high-pressure hydraulic block.</p>
            </div>
            <div class="zoom-card-footer">
              <span>● 3-Point Hitch</span>
              <span>210 BAR</span>
            </div>
          </div>
        </div>

        <!-- Item 3: Canal Digging -->
        <div class="zoom-media-card" onclick="openMediaLightbox('image', 'WhatsApp Image 2026-10-24 at 2.23.00 PM.jpeg', 'Plantation Canal Excavation', 'Agrosteed Stredo clearing wide irrigation canals through heavy clay soil.')">
          <div class="zoom-media-frame">
            <img src="WhatsApp Image 2026-10-24 at 2.23.00 PM.jpeg" alt="Canal Trench Excavation" loading="lazy">
            <div class="zoom-media-badge">Field Trial • Farmland</div>
            <div class="zoom-click-hint">🔍 Click to Zoom</div>
          </div>
          <div class="zoom-card-body">
            <div>
              <h4 class="zoom-card-title">Canal Irrigation Digging</h4>
              <p class="zoom-card-desc">Deep soil penetration in wet agricultural conditions.</p>
            </div>
            <div class="zoom-card-footer">
              <span>● Irrigation Trench</span>
              <span>450mm Cut</span>
            </div>
          </div>
        </div>

        <!-- Item 4: Boom Articulation Arc -->
        <div class="zoom-media-card" onclick="openMediaLightbox('image', 'WhatsApp Image 2026-10-24 at 2.23.01 PM.jpeg', 'High Boom Elevation Clearance', 'Curved boom profile lifting spoil well above high canal embankments.')">
          <div class="zoom-media-frame">
            <img src="WhatsApp Image 2026-10-24 at 2.23.01 PM.jpeg" alt="Boom Elevation Arc" loading="lazy">
            <div class="zoom-media-badge">Hydraulics • Articulation</div>
            <div class="zoom-click-hint">🔍 Click to Zoom</div>
          </div>
          <div class="zoom-card-body">
            <div>
              <h4 class="zoom-card-title">Arched Boom Lift Height</h4>
              <p class="zoom-card-desc">Superior 3.42m operating elevation clearance over trench rims.</p>
            </div>
            <div class="zoom-card-footer">
              <span>● 155° Boom Arc</span>
              <span>3.42M Height</span>
            </div>
          </div>
        </div>

        <!-- Item 5: Model 4 CAD Side Elevation Blueprint -->
        <div class="zoom-media-card" onclick="openMediaLightbox('image', 'MODEL4.jpeg', 'Model 4: Side Elevation CAD Blueprint', 'Exact dimensions: 2.85m depth, 3.85m reach radius from slew pivot.')">
          <div class="zoom-media-frame">
            <img src="MODEL4.jpeg" alt="Model 4 CAD Blueprint" loading="lazy">
            <div class="zoom-media-badge">CAD Blueprint • Model 4</div>
            <div class="zoom-click-hint">🔍 Click to Zoom</div>
          </div>
          <div class="zoom-card-body">
            <div>
              <h4 class="zoom-card-title">Model 4: Side Elevation Reach</h4>
              <p class="zoom-card-desc">Factory CAD drawing detailing 2.85m digging depth and 3.85m horizontal reach.</p>
            </div>
            <div class="zoom-card-footer">
              <span>● CAD Blueprint</span>
              <span>3.85M Reach</span>
            </div>
          </div>
        </div>

        <!-- Item 6: Plantation Full Reach -->
        <div class="zoom-media-card" onclick="openMediaLightbox('image', 'WhatsApp Image 2026-10-24 at 2.23.05 PM.jpeg', 'Full Reach Plantation Trenching', 'Operating between coconut tree trunks with high precision.')">
          <div class="zoom-media-frame">
            <img src="WhatsApp Image 2026-10-24 at 2.23.05 PM.jpeg" alt="Plantation Trenching" loading="lazy">
            <div class="zoom-media-badge">Field Trial • Orchard</div>
            <div class="zoom-click-hint">🔍 Click to Zoom</div>
          </div>
          <div class="zoom-card-body">
            <div>
              <h4 class="zoom-card-title">Orchard Trench Excavation</h4>
              <p class="zoom-card-desc">Demonstrating compact radius between plantation tree lines.</p>
            </div>
            <div class="zoom-card-footer">
              <span>● Compact Slew</span>
              <span>Zero Roll</span>
            </div>
          </div>
        </div>

        <!-- Item 7: Dual Outrigger Anchor -->
        <div class="zoom-media-card" onclick="openMediaLightbox('image', 'product2.jpeg', 'Dual Hydraulic Stabilizers Deployed', 'Heavy outriggers deployed on soft farm soil providing solid anchor stability.')">
          <div class="zoom-media-frame">
            <img src="product2.jpeg" alt="Stabilizers Deployed" loading="lazy">
            <div class="zoom-media-badge">Field Photo • Stance</div>
            <div class="zoom-click-hint">🔍 Click to Zoom</div>
          </div>
          <div class="zoom-card-body">
            <div>
              <h4 class="zoom-card-title">Dual Outrigger Stance</h4>
              <p class="zoom-card-desc">2.2m wide-stance pads locking the tractor firmly to the terrain.</p>
            </div>
            <div class="zoom-card-footer">
              <span>● 2.2M Stance</span>
              <span>Lock Valves</span>
            </div>
          </div>
        </div>

        <!-- Item 8: Model 5 CAD Stabilizer Blueprint -->
        <div class="zoom-media-card" onclick="openMediaLightbox('image', 'MODEL5.jpeg', 'Model 5: Stabilizer Stance Blueprint', 'Plan view detailing 2.2m outrigger spread and independent hydraulic leveling.')">
          <div class="zoom-media-frame">
            <img src="MODEL5.jpeg" alt="Model 5 CAD Blueprint" loading="lazy">
            <div class="zoom-media-badge">CAD Blueprint • Model 5</div>
            <div class="zoom-click-hint">🔍 Click to Zoom</div>
          </div>
          <div class="zoom-card-body">
            <div>
              <h4 class="zoom-card-title">Model 5: Outrigger Stance (2.2m)</h4>
              <p class="zoom-card-desc">Engineering plan view showing full stabilizer deployment geometry.</p>
            </div>
            <div class="zoom-card-footer">
              <span>● CAD Blueprint</span>
              <span>2,200mm Span</span>
            </div>
          </div>
        </div>

        <!-- Item 9: Heavy Soil Extraction Crowd -->
        <div class="zoom-media-card" onclick="openMediaLightbox('image', 'WhatsApp Image 2026-10-24 at 2.23.03 PM.jpeg', 'High Breakout Soil Extraction', 'Induction-hardened hydraulic cylinders powering heavy bucket breakout in rocky trenches.')">
          <div class="zoom-media-frame">
            <img src="WhatsApp Image 2026-10-24 at 2.23.03 PM.jpeg" alt="Breakout Soil Extraction" loading="lazy">
            <div class="zoom-media-badge">Field Trial • Hard Dig</div>
            <div class="zoom-click-hint">🔍 Click to Zoom</div>
          </div>
          <div class="zoom-card-body">
            <div>
              <h4 class="zoom-card-title">Rocky Soil Breakout</h4>
              <p class="zoom-card-desc">2,150 kgf crowd force breaking through dense, compact earth.</p>
            </div>
            <div class="zoom-card-footer">
              <span>● Breakout Force</span>
              <span>2,150 kgf</span>
            </div>
          </div>
        </div>

        <!-- Item 10: Model 6 Isometric CAD Assembly -->
        <div class="zoom-media-card" onclick="openMediaLightbox('image', 'MODEL6.jpeg', 'Model 6: Isometric Mechanical Assembly', 'Complete axonometric mechanical weldment drawing.')">
          <div class="zoom-media-frame">
            <img src="MODEL6.jpeg" alt="Model 6 CAD Blueprint" loading="lazy">
            <div class="zoom-media-badge">CAD Blueprint • Model 6</div>
            <div class="zoom-click-hint">🔍 Click to Zoom</div>
          </div>
          <div class="zoom-card-body">
            <div>
              <h4 class="zoom-card-title">Model 6: Isometric Assembly</h4>
              <p class="zoom-card-desc">Complete 3D axonometric technical drawing illustrating structural weldments.</p>
            </div>
            <div class="zoom-card-footer">
              <span>● CAD Blueprint</span>
              <span>Hardox 450</span>
            </div>
          </div>
        </div>
"""

new_marquee_block = f"""
  <!-- FLOATING MEDIA STREAM (FLOWING CONTINUOUSLY FROM LEFT TO RIGHT) -->
  <div class="floating-stream-section-header">
    <span class="stream-eyebrow">CONTINUOUS FIELD &amp; BLUEPRINT STREAM</span>
    <h3 class="stream-title">FLOATING DEMONSTRATION STREAM</h3>
    <p class="stream-subtitle">
      Hover any card to pause and zoom. Live attachments operating across Indian agricultural soil and factory CAD drawings.
    </p>
  </div>

  <div class="media-marquee-container" aria-label="Auto-running media stream floating from left to right">
    <div class="media-marquee-track">
      <!-- SET A -->
{items_markup}
      <!-- SET B (DUPLICATE FOR SEAMLESS 100% INFINITE LOOP) -->
{items_markup}
    </div>
  </div>
"""

# Replace the old media marquee block in Section 4
old_marquee_pattern = re.compile(
    r'<!-- AUTO-RUNNING RIGHT-TO-LEFT SCROLL & ZOOM MARQUEE FOR ALL MEDIA -->[\s\S]*?</div>\s*</div>\s*(?=\s*<!-- ALL LABELED ASSETS SHOWCASE -->)',
    re.MULTILINE
)

if not old_marquee_pattern.search(html):
    print("Warning: Could not find exact old_marquee_pattern, searching for media-marquee-container")
    container_pattern = re.compile(
        r'<div class="media-marquee-container"[\s\S]*?</div>\s*</div>\s*(?=\s*<!-- ALL LABELED ASSETS SHOWCASE -->)',
        re.MULTILINE
    )
    if container_pattern.search(html):
        html = container_pattern.sub(new_marquee_block + "\n", html)
        print("Replaced media-marquee-container with new floating left-to-right stream!")
    else:
        print("Error: Could not locate media marquee in Section 4 HTML")
else:
    html = old_marquee_pattern.sub(new_marquee_block + "\n", html)
    print("Successfully replaced with new floating left-to-right stream!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html written successfully! Length:", len(html))
