/** @type {import('tailwindcss').Config} */
const { iconsPlugin, getIconCollections } = require("@egoist/tailwindcss-icons")

module.exports = {
  darkMode: 'class',
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
  ],
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        'sea-buckthorn': {
          50: '#FEFAF4',
          100: '#FEF6E9',
          200: '#FCE8C8',
          300: '#FBDBA7',
          400: '#F7BF66',
          500: '#F4A424',
          600: '#DC9420',
          700: '#926216',
          800: '#6E4A10',
          900: '#49310B',
        },
        gray: {
          50:  '#f9fafb',
          100: '#f3f4f6',
          200: '#e5e7eb',
          300: '#d1d5db',
          400: '#9ca3af',
          500: '#6b7280',
          600: '#4b5563',
          700: '#374151',
          800: '#1f2937',
          900: '#111827',
          950: '#0a0d14',
        },
      },
      boxShadow: {
        'custom': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
        'custom-dark': '0 4px 6px -1px rgba(0, 0, 0, 0.5), 0 2px 4px -1px rgba(0, 0, 0, 0.25)',
      },
      width: {
        box: '500px'
      },
      height: {
        box: '500px'
      }
    }
  },
  variants: {},
  plugins: [
    iconsPlugin({
      collections: getIconCollections(["mingcute", "twemoji"]),
    }),
  ],
  safelist: ['i-mingcute-arrows-up-line', 'i-mingcute-arrows-down-line', 'bg-gray-200', 'bg-sea-buckthorn-500', 'bg-sea-buckthorn-100', 'text-gray-500']
}

