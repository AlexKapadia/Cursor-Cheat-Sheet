import React from 'react';

interface RazorCardProps {
  children: React.ReactNode;
  className?: string;
  onClick?: () => void;
  as?: keyof JSX.IntrinsicElements;
}

const RazorCard: React.FC<RazorCardProps> = ({
  children,
  className = '',
  onClick,
  as: Component = 'div',
}) => {
  return (
    <Component
      className={`
        relative
        p-6
        border border-[rgba(255,255,255,0.1)]
        bg-transparent
        transition-all duration-[1200ms] ease-[cubic-bezier(0.2,0.8,0.2,1)]
        hover:border-accent-primary
        hover:bg-[rgba(255,255,255,0.05)]
        ${onClick ? 'cursor-pointer' : ''}
        ${className}
      `}
      onClick={onClick}
      style={{
        borderRadius: '0px', // Enforce "Razor" geometry
      }}
    >
      {children}
    </Component>
  );
};

export default RazorCard;

