/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './app/**/templates/*.html',
    // Add paths to other apps if necessary
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
}

