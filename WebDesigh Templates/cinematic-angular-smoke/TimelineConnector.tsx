import React, { useEffect, useRef, useState } from 'react';

interface TimelineConnectorProps {
  targetId: string;
  startY?: number; // Starting Y position (default: 0)
  endY?: number; // Ending Y position (default: 100%)
  className?: string;
}

const TimelineConnector: React.FC<TimelineConnectorProps> = ({
  targetId,
  startY = 0,
  endY = 100,
  className = '',
}) => {
  const svgRef = useRef<SVGSVGElement>(null);
  const pathRef = useRef<SVGPathElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);
  const [pathLength, setPathLength] = useState(0);
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const path = pathRef.current;
    const container = containerRef.current;
    if (!path || !container) return;

    // Calculate path length
    const length = path.getTotalLength();
    setPathLength(length);
    path.style.strokeDasharray = `${length}`;
    path.style.strokeDashoffset = `${length}`; // Start fully hidden

    // Intersection Observer for scroll-triggered animation
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setIsVisible(true);
            animatePath(path, length);
          }
        });
      },
      {
        threshold: 0.1, // Trigger when 10% visible
        rootMargin: '0px',
      }
    );

    if (container) {
      observer.observe(container);
    }

    return () => {
      observer.disconnect();
    };
  }, []);

  const animatePath = (path: SVGPathElement, length: number) => {
    const startTime = performance.now();
    const duration = 1200; // 1.2s - matches "Liquid Time"

    const animate = (currentTime: number) => {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);

      // Cubic bezier easing: (0.2, 0.8, 0.2, 1)
      const ease = (t: number) => {
        return t < 0.5
          ? 4 * t * t * t
          : 1 - Math.pow(-2 * t + 2, 3) / 2;
      };

      const easedProgress = ease(progress);
      const drawLength = length * easedProgress;
      path.style.strokeDashoffset = `${length - drawLength}`;

      if (progress < 1) {
        requestAnimationFrame(animate);
      }
    };

    requestAnimationFrame(animate);
  };

  return (
    <div
      ref={containerRef}
      className={`relative w-full h-full ${className}`}
      style={{ position: 'relative' }}
    >
      <svg
        ref={svgRef}
        className="absolute inset-0 w-full h-full pointer-events-none"
        viewBox="0 0 100 100"
        preserveAspectRatio="none"
      >
        <path
          ref={pathRef}
          d={`M 50 ${startY} L 50 ${endY}`}
          stroke="var(--accent-primary)"
          strokeWidth="1"
          fill="none"
          vectorEffect="non-scaling-stroke"
        />
      </svg>
    </div>
  );
};

export default TimelineConnector;

