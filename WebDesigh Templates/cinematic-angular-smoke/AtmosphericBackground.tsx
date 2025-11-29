import React, { useRef, useEffect } from 'react';

interface AtmosphericBackgroundProps {
  children?: React.ReactNode;
  videoSrc?: string;
  noiseTextureSrc?: string;
}

const AtmosphericBackground: React.FC<AtmosphericBackgroundProps> = ({
  children,
  videoSrc = '/videos/smoke-loop.mp4',
  noiseTextureSrc = '/textures/noise.png',
}) => {
  const videoRef = useRef<HTMLVideoElement>(null);

  useEffect(() => {
    // Ensure video plays (some browsers require user interaction)
    const video = videoRef.current;
    if (video) {
      video.play().catch((error) => {
        console.warn('Video autoplay failed:', error);
      });
    }
  }, []);

  return (
    <div className="relative w-full h-full min-h-screen overflow-hidden bg-bg-void">
      {/* Base Background Color */}
      <div className="absolute inset-0 bg-bg-void" />

      {/* Fog Noise Texture Layer */}
      <div
        className="absolute inset-0 pointer-events-none opacity-[0.05]"
        style={{
          backgroundImage: `url('${noiseTextureSrc}')`,
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          backgroundRepeat: 'no-repeat',
          mixBlendMode: 'overlay',
        }}
        aria-hidden="true"
      />

      {/* Fluid/Smoke Video Loop */}
      <video
        ref={videoRef}
        className="absolute inset-0 w-full h-full object-cover mix-blend-screen pointer-events-none"
        src={videoSrc}
        autoPlay
        loop
        muted
        playsInline
        preload="auto"
        aria-hidden="true"
      >
        Your browser does not support the video tag.
      </video>

      {/* Content Layer */}
      <div className="relative z-10">
        {children}
      </div>
    </div>
  );
};

export default AtmosphericBackground;

