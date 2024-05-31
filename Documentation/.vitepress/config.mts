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
    footer: {
      message: 'Released under the BSD 3-Clause License',
      copyright: 'KIOYDIOLABS © 2024'
    },
    logo: '/public/icon.jpg',
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Website', link: 'https://imgal.kioydiolabs.org' },
      {
        text: 'Resources',
        items: [
          {
            text: 'Demo Galleries',
            link: '/demo'
          },
          {
            text: 'Download Imgal',
            link: 'https://github.com/kioydiolabs/imgal/releases/latest/download/imgal_allPlatforms.zip'
          }
        ]
      }
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