/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../static/templates/**/*.{html,js}",
            "../blog/templates/**/*.{html,js}",
            "../home/templates/**/*.{html,js}",
  ],
  theme: {
    extend: {
      fontSize: {
        '2xs': '0.625rem', // 10px
        '3xs': '0.5rem', // 8px
        '4xs': '0.375rem', // 6px
        '5xs': '0.25rem', // 4px
      },
      fontFamily: {
        haus: ['At Hauss', 'sans-serif'],
        lato: ['Lato', 'sans-serif']
      },
      keyframes: {
        slideInLeft: {
          '0%': { transform: 'translateX(-100%)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' },
        },
        slideInRight: {
          '0%': { transform: 'translateX(100%)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' },
        },
        slideInUp: {
          '0%': { transform: 'translateY(-100%)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        slideInDown: {
          '0%': { transform: 'translateY(100%)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        pulseFocus: {
          '0%, 100%': { transform: 'scale(1)', zIndex: '0' },
          '25%': { transform: 'scale(1.5)', zIndex: '10' },
          '50%': { transform: 'scale(1)', zIndex: '1' },
        },
        shakeX: {
          '0%, 100%': { transform: 'translateX(0)' },
          '25%': { transform: 'translateX(-4px)' },
          '75%': { transform: 'translateX(4px)' },
        },
      },
      animation: {
        slideInLeft: 'slideInLeft 1s ease-out forwards',
        slideInRight: 'slideInRight 1s ease-out forwards',
        slideInUp: 'slideInUp 1s ease-out forwards',
        slideInDown: 'slideInDown 1s ease-out forwards',
        // pulseFocus1: 'pulseFocus 8s infinite ease-in-out',
        // pulseFocus2: 'pulseFocus 8s infinite ease-in-out 2s',
        // pulseFocus3: 'pulseFocus 8s infinite ease-in-out 4s',
        // pulseFocus4: 'pulseFocus 8s infinite ease-in-out 6s',
        pulseFocus: 'pulseFocus 5s ease-in-out infinite',
        shakeX: 'shakeX 1s ease-in-out infinite',
      },
    },
  },
  plugins: [require('daisyui'),],
}
