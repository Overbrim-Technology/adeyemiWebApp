/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./static/templates/**/*.{html,js}",
            "./blog/templates/**/*.{html,js}",
  ],
  theme: {
    extend: {
      fontFamily: {
        haus: ['At Hauss', 'sans-serif'],
        lato: ['Lato', 'sans-serif']
      },
    },
  },
  plugins: [require('daisyui'),],
}
