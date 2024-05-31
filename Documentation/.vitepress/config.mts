import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Imgal Documentation",
  description: "Documentation for Imgal by KioydioLabs",
  head: [['link', { rel: 'icon', href: '/public/icon.jpg' }]],
  themeConfig: {
    search: {
      provider: 'local'
    },
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Website', link: 'https://imgal.kioydiolabs.org' }
    ],

    sidebar: [
      {
        items: [
          { text: 'Introduction', link: '/introduction' },
        ]
      },
      {
        text: 'Installing Prerequisites',
        link: '/prerequisites',
        collapsed: true,
        items: [
            { text: 'Windows', link: '/windows-prereq' },
            { text: 'Linux', link: '/linux-prereq' },
        ]
      },
      {
        text: 'Creating an image gallery',
        link: '/creating-an-image-gallery'
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/kioydiolabs/imgal' }
    ]
  }
})
