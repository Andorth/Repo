





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-lLo2nlsdl+bHLu6PGvC2j3wfP45RnK4wKQLiPnCDcuXfU38AiD+JCdMywnF3WbJC1jaxe3lAI6AM4uJuMFBLEw==" rel="stylesheet" href="https://assets-cdn.github.com/assets/frameworks-08fc49d3bd2694c870ea23d0906f3610.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-cCRQcUhsfTkVe8C6yNZ+YkM1twPic6GqxfFEAxxsidOjoGB9Cidedo4iFY6JmOdTj4PrQsextq7Qnz5wmCnuvg==" rel="stylesheet" href="https://assets-cdn.github.com/assets/github-24c709db2b749fbf737913ce1668b00f.css" />
  
  
  <link crossorigin="anonymous" media="all" integrity="sha512-PcJMPDRp7jbbEAmTk9kaL2kRQqg69QZ26WsZf07xsPyaipKsi3wVG0805PZNYXxotPDAliKKFvNSQPhD8fp1FQ==" rel="stylesheet" href="https://assets-cdn.github.com/assets/site-50c740d9290419d070dd6213a7cd03b5.css" />
  
  

  <meta name="viewport" content="width=device-width">
  
  <title>script.speedtest/default.py at master · FusionwareIT/script.speedtest · GitHub</title>
    <meta name="description" content="Kodi speedtest.net addon, uses speedtest-cli. Contribute to FusionwareIT/script.speedtest development by creating an account on GitHub.">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta property="og:image" content="https://avatars2.githubusercontent.com/u/16002092?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="FusionwareIT/script.speedtest" /><meta property="og:url" content="https://github.com/FusionwareIT/script.speedtest" /><meta property="og:description" content="Kodi speedtest.net addon, uses speedtest-cli. Contribute to FusionwareIT/script.speedtest development by creating an account on GitHub." />

  <link rel="assets" href="https://assets-cdn.github.com/">
  
  <meta name="pjax-timeout" content="1000">
  
  <meta name="request-id" content="0A7B:0E01:23ED3CE:428A2ED:5C070851" data-pjax-transient>


  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

      <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="0A7B:0E01:23ED3CE:428A2ED:5C070851" /><meta name="octolytics-dimension-region_edge" content="iad" /><meta name="octolytics-dimension-region_render" content="iad" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">


<meta class="js-ga-set" name="dimension1" content="Logged Out">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="NmVmMjdjNDcyZDA2OTYzOTExZDJhNzdmNWI3OWQwNTYxYTE4NzVmOGMzNTU1OTMyYTEwMzU5NjA2ZGI3NTZlN3x7InJlbW90ZV9hZGRyZXNzIjoiMTM5LjQ3LjEwNC4xMTMiLCJyZXF1ZXN0X2lkIjoiMEE3QjowRTAxOjIzRUQzQ0U6NDI4QTJFRDo1QzA3MDg1MSIsInRpbWVzdGFtcCI6MTU0Mzk2NDc1OSwiaG9zdCI6ImdpdGh1Yi5jb20ifQ==">

    <meta name="enabled-features" content="DASHBOARD_V2_LAYOUT_OPT_IN,EXPLORE_DISCOVER_REPOSITORIES,UNIVERSE_BANNER,MARKETPLACE_PLAN_RESTRICTION_EDITOR">

  <meta name="html-safe-nonce" content="d5f3339f0348206edbd81dbf0c0ddac5d6c66f27">

  <meta http-equiv="x-pjax-version" content="1d5936c2f3ef15f45dc57ab6ea3ac38c">
  

      <link href="https://github.com/FusionwareIT/script.speedtest/commits/master.atom" rel="alternate" title="Recent Commits to script.speedtest:master" type="application/atom+xml">

  <meta name="go-import" content="github.com/FusionwareIT/script.speedtest git https://github.com/FusionwareIT/script.speedtest.git">

  <meta name="octolytics-dimension-user_id" content="16002092" /><meta name="octolytics-dimension-user_login" content="FusionwareIT" /><meta name="octolytics-dimension-repository_id" content="81059842" /><meta name="octolytics-dimension-repository_nwo" content="FusionwareIT/script.speedtest" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="81059842" /><meta name="octolytics-dimension-repository_network_root_nwo" content="FusionwareIT/script.speedtest" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/FusionwareIT/script.speedtest/blob/master/default.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">


  <meta name="u2f-support" content="true">

  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-out env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="px-2 py-4 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    


        
<header class="Header header-logged-out  position-relative f4 py-3" role="banner">
  <div class="container-lg d-flex px-3">
    <div class="d-flex flex-justify-between flex-items-center">
        <a class="mr-4" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark; experiment:site_header_dropdowns; group:dropdowns">
          <svg height="32" class="octicon octicon-mark-github text-white" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
        </a>
    </div>

    <div class="HeaderMenu HeaderMenu--logged-out d-flex flex-justify-between flex-items-center flex-auto">
      <div class="d-none">
        <button class="btn-link js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
          <svg height="24" class="octicon octicon-x text-gray" viewBox="0 0 12 16" version="1.1" width="18" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
        </button>
      </div>

        <nav class="mt-0" aria-label="Global">
          <ul class="d-flex list-style-none">
              <li class=" mr-3 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap  d-inline-block">
                    Why GitHub?
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-relative">
                      <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>
                  <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 mt-0  p-4 left-n4 position-absolute">
                    <a href="/features" class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Features">Features <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                    <ul class="list-style-none f5 pb-3">
                      <li class="edge-item-fix"><a href="/features/code-review/" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code review">Code review</a></li>
                      <li class="edge-item-fix"><a href="/features/project-management/" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Project management">Project management</a></li>
                      <li class="edge-item-fix"><a href="/features/integrations" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Integrations">Integrations</a></li>
                      <li class="edge-item-fix"><a href="/features#team-management" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Team management">Team management</a></li>
                      <li class="edge-item-fix"><a href="/features#social-coding" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Social coding">Social coding</a></li>
                      <li class="edge-item-fix"><a href="/features#documentation" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Documentation">Documentation</a></li>
                      <li class="edge-item-fix"><a href="/features#code-hosting" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code hosting">Code hosting</a></li>
                    </ul>

                    <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
                      <li class="edge-item-fix"><a href="/case-studies" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Case studies">Case Studies <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                      <li class="edge-item-fix"><a href="/security" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Security">Security <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                    </ul>
                  </div>
                </details>
              </li>
              <li class=" mr-3 mr-lg-3">
                <a href="/business" class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Business">Business</a>
              </li>

              <li class=" mr-3 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap  d-inline-block">
                    Explore
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-relative">
                      <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>

                  <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-0 mt-0  p-4 left-n4 position-absolute">
                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="/explore" class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Features">Explore GitHub <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                    </ul>

                    <h4 class="text-gray-light text-normal text-mono f5 mb-2  border-top pt-3">Learn &amp; contribute</h4>
                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="/topics" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Topics">Topics</a></li>
                      <li class="edge-item-fix"><a href="/collections" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Collections">Collections</a></li>
                      <li class="edge-item-fix"><a href="/trending" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Trending">Trending</a></li>
                      <li class="edge-item-fix"><a href="https://lab.github.com/" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Learning lab">Learning Lab</a></li>
                      <li class="edge-item-fix"><a href="https://opensource.guide" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Open source guides">Open source guides</a></li>
                    </ul>

                    <h4 class="text-gray-light text-normal text-mono f5 mb-2  border-top pt-3">Connect with others</h4>
                    <ul class="list-style-none mb-0">
                      <li class="edge-item-fix"><a href="/events" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Events">Events</a></li>
                      <li class="edge-item-fix"><a href="https://github.community" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Community forum">Community forum</a></li>
                      <li class="edge-item-fix"><a href="https://education.github.com" class="py-2 pb-0 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to GitHub Education">GitHub Education</a></li>
                    </ul>
                  </div>
                </details>
              </li>

              <li class=" mr-3 mr-lg-3">
                <a href="/marketplace" class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Marketplace">Marketplace</a>
              </li>

              <li class=" mr-3 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap  d-inline-block">
                    Pricing
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-relative">
                       <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>

                  <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-4 mt-0  p-4 left-n4 position-absolute">
                    <a href="/pricing" class="pb-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Pricing">Plans <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="/pricing/developer" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Developers">Developer</a></li>
                      <li class="edge-item-fix"><a href="/pricing/team" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Team">Team</a></li>
                      <li class="edge-item-fix"><a href="/pricing/business-cloud" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Business Cloud">Business Cloud</a></li>
                      <li class="edge-item-fix"><a href="/pricing/enterprise" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Enterprise">Enterprise</a></li>
                    </ul>

                    <ul class="list-style-none mb-0  border-top pt-3">
                      <li class="edge-item-fix"><a href="/pricing#feature-comparison" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Compare features">Compare plans <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                      <li class="edge-item-fix"><a href="/nonprofit" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Nonprofits">Nonprofit <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                      <li class="edge-item-fix"><a href="https://education.github.com/discount_requests/new" class="py-2 pb-0 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover"  data-ga-click="(Logged out) Header, go to Education">Education <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                    </ul>
                  </div>
                </details>
              </li>
          </ul>
        </nav>

      <div class="d-flex flex-items-center px-0 text-center text-left">
          <div class="d-lg-flex mr-3">
            <div class="header-search scoped-search site-scoped-search js-site-search position-relative js-jump-to"
  role="combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="false"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" data-scope-type="Repository" data-scope-id="81059842" data-scoped-search-url="/FusionwareIT/script.speedtest/search" data-unscoped-search-url="/search" action="/FusionwareIT/script.speedtest/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control header-search-wrapper header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search"
          data-unscoped-placeholder="Search GitHub"
          data-scoped-placeholder="Search"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations#csrf-token=3XBe8NRN1bMEDzcAJ3PKaVlcKdqKixOWFbNe66olZUZEuNw5EBkqw/V3SgiK0SmQvQeYhJVpTBfeeFpBz/0l6g=="
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://assets-cdn.github.com/images/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


</ul>

            </div>
      </label>
</form>  </div>
</div>

          </div>

        <a class="HeaderMenu-link no-underline mr-3" href="/login?return_to=%2FFusionwareIT%2Fscript.speedtest%2Fblob%2Fmaster%2Fdefault.py" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign&nbsp;in</a>
          <a class="HeaderMenu-link d-inline-block no-underline border border-gray-dark rounded-1 px-2 py-1" href="/join" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign&nbsp;up</a>
      </div>
    </div>
  </div>
</header>

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">

</div>



  <div role="main" class="application-main " data-commit-hovercards-enabled>
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <div id="js-repo-pjax-container" data-pjax-container >
      





  



  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav  ">
    <div class="repohead-details-container clearfix container">

      <ul class="pagehead-actions">
  <li>
      <a href="/login?return_to=%2FFusionwareIT%2Fscript.speedtest"
    class="btn btn-sm btn-with-count tooltipped tooltipped-s"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
    Watch
  </a>
  <a class="social-count" href="/FusionwareIT/script.speedtest/watchers"
     aria-label="1 user is watching this repository">
    1
  </a>

  </li>

  <li>
      <a href="/login?return_to=%2FFusionwareIT%2Fscript.speedtest"
    class="btn btn-sm btn-with-count tooltipped tooltipped-s"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
    Star
  </a>

    <a class="social-count js-social-count" href="/FusionwareIT/script.speedtest/stargazers"
      aria-label="0 users starred this repository">
      0
    </a>

  </li>

  <li>
      <a href="/login?return_to=%2FFusionwareIT%2Fscript.speedtest"
        class="btn btn-sm btn-with-count tooltipped tooltipped-s"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <svg class="octicon octicon-repo-forked v-align-text-bottom" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
        Fork
      </a>

    <a href="/FusionwareIT/script.speedtest/network/members" class="social-count"
       aria-label="0 users forked this repository">
      0
    </a>
  </li>
</ul>

      <h1 class="public ">
  <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" data-hovercard-type="organization" data-hovercard-url="/orgs/FusionwareIT/hovercard" href="/FusionwareIT">FusionwareIT</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/FusionwareIT/script.speedtest">script.speedtest</a></strong>

</h1>

    </div>
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax container"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
    aria-label="Repository"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /FusionwareIT/script.speedtest" href="/FusionwareIT/script.speedtest">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /FusionwareIT/script.speedtest/issues" href="/FusionwareIT/script.speedtest/issues">
        <svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /FusionwareIT/script.speedtest/pulls" href="/FusionwareIT/script.speedtest/pulls">
      <svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>


    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /FusionwareIT/script.speedtest/projects" href="/FusionwareIT/script.speedtest/projects">
      <svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>


  <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse alerts security /FusionwareIT/script.speedtest/pulse" href="/FusionwareIT/script.speedtest/pulse">
    <svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Insights
</a>

</nav>


  </div>

<div class="container new-discussion-timeline experiment-repo-nav  ">
  <div class="repository-content ">

    

  
    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/FusionwareIT/script.speedtest/blob/80fe817b4a6be4134b109476bcc782db228b477f/default.py">Permalink</a>

    <!-- blob contrib key: blob_contributors:v21:fded7c9525d7f7928b824a0a0358de06 -->

        <div class="signup-prompt-bg rounded-1">
      <div class="signup-prompt p-4 text-center mb-4 rounded-1">
        <div class="position-relative">
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/site/dismiss_signup_prompt" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="WExLFSu1KBQq88iK3PI4bbBakkk2QO8aFpls0+2O7aByOl/6HzJxjhMZWJQF02P0+JgaQqmPz9X3qzJHcNha4A==" />
            <button type="submit" class="position-absolute top-0 right-0 btn-link link-gray" data-ga-click="(Logged out) Sign up prompt, clicked Dismiss, text:dismiss">
              Dismiss
            </button>
</form>          <h3 class="pt-2">Join GitHub today</h3>
          <p class="col-6 mx-auto">GitHub is home to over 28 million developers working together to host and review code, manage projects, and build software together.</p>
          <a class="btn btn-primary" href="/join?source=prompt-blob-show" data-ga-click="(Logged out) Sign up prompt, clicked Sign up, text:sign-up">Sign up</a>
        </div>
      </div>
    </div>


    <div class="file-navigation">
      
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" aria-expanded="false" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg class="octicon octicon-x js-menu-close" role="img" aria-label="Close" viewBox="0 0 12 16" version="1.1" width="12" height="16"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <tab-container>
      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs" role="tablist">
          <ul>
            <li class="select-menu-tab">
              <button type="button" class="select-menu-tab-nav" data-filter-placeholder="Filter branches/tags" role="tab" aria-selected="true">Branches</button>
            </li>
            <li class="select-menu-tab">
              <button type="button" class="select-menu-tab-nav" data-filter-placeholder="Find a tag…" role="tab">Tags</button>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list" role="tabpanel">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/FusionwareIT/script.speedtest/blob/master/default.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list" role="tabpanel" hidden>
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/FusionwareIT/script.speedtest/tree/0.2/default.py"
              data-name="0.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="0.2">
                0.2
              </span>
            </a>
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>
      </tab-container>
    </div>
  </div>
</div>

      <div class="BtnGroup float-right">
        <a href="/FusionwareIT/script.speedtest/find/master"
              class="js-pjax-capture-input btn btn-sm BtnGroup-item"
              data-pjax
              data-hotkey="t">
          Find file
        </a>
        <clipboard-copy for="blob-path" class="btn btn-sm BtnGroup-item">
          Copy path
        </clipboard-copy>
      </div>
      <div id="blob-path" class="breadcrumb">
        <span class="repo-root js-repo-root"><span class="js-path-segment"><a data-pjax="true" href="/FusionwareIT/script.speedtest"><span>script.speedtest</span></a></span></span><span class="separator">/</span><strong class="final-path">default.py</strong>
      </div>
    </div>


    
  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/FusionwareIT/script.speedtest/commit/80fe817b4a6be4134b109476bcc782db228b477f" data-pjax>
          80fe817
        </a>
        <relative-time datetime="2017-02-06T19:07:48Z">Feb 6, 2017</relative-time>
      </span>
      <div>
        <a rel="contributor" data-skip-pjax="true" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=14877267" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/alepsrt"><img class="avatar" src="https://avatars3.githubusercontent.com/u/14877267?s=40&amp;v=4" width="20" height="20" alt="@alepsrt" /></a>
        <a class="user-mention" rel="contributor" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=14877267" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/alepsrt">alepsrt</a>
          <a data-pjax="true" title="version 0.2" class="message" href="/FusionwareIT/script.speedtest/commit/80fe817b4a6be4134b109476bcc782db228b477f">version 0.2</a>
      </div>

    <div class="commit-tease-contributors">
      
<details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark float-left mr-2" id="blob_contributors_box">
  <summary class="btn-link" aria-haspopup="dialog"  >
    
    <span><strong>1</strong> contributor</span>
  </summary>
  <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast " aria-label="Users who have contributed to this file">
    <div class="Box-header">
      <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <h3 class="Box-title">Users who have contributed to this file</h3>
    </div>
    
        <ul class="list-style-none overflow-auto">
            <li class="Box-row">
              <a class="link-gray-dark no-underline" href="/alepsrt">
                <img class="avatar mr-2" alt="" src="https://avatars3.githubusercontent.com/u/14877267?s=40&amp;v=4" width="20" height="20" />
                alepsrt
</a>            </li>
        </ul>

  </details-dialog>
</details>
      
    </div>
  </div>



    <div class="file ">
      <div class="file-header">
  <div class="file-actions">


    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/FusionwareIT/script.speedtest/raw/master/default.py">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/FusionwareIT/script.speedtest/blame/master/default.py">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/FusionwareIT/script.speedtest/commits/master/default.py">History</a>
    </div>

        <a class="btn-octicon tooltipped tooltipped-nw"
           href="https://desktop.github.com"
           aria-label="Open this file in GitHub Desktop"
           data-ga-click="Repository, open with desktop, type:windows">
            <svg class="octicon octicon-device-desktop" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z"/></svg>
        </a>

        <button type="button" class="btn-octicon disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
        </button>
        <button type="button" class="btn-octicon btn-octicon-danger disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
        </button>
  </div>

  <div class="file-info">
      900 lines (899 sloc)
      <span class="file-info-divider"></span>
    34.6 KB
  </div>
</div>

      

  <div itemprop="text" class="blob-wrapper data type-python ">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>!/usr/bin/env python</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>##################################################################################################</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>										Original Was modified from this and debranded from the arnu box </span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>                                ** Kodi SpeedTest.net Interface **                                </span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>   Adapted by:		Josh.5 (jsunnex@gmail.com)</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>   Date:		17 Sep, 2015</span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> </span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>   Credits:</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>          - Matt Martz (https://github.com/sivel/speedtest-cli) for his work on the original speedtest-cli</span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>   Reference documentation:</span></td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>          - https://pypi.python.org/pypi/speedtest-cli/</span></td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>   Copyright 2012-2014 Matt Martz</span></td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>   All Rights Reserved.</span></td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>          Licensed under the Apache License, Version 2.0 (the &quot;License&quot;); you may</span></td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>          not use this file except in compliance with the License. You may obtain</span></td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>          a copy of the License at</span></td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>               http://www.apache.org/licenses/LICENSE-2.0</span></td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>          Unless required by applicable law or agreed to in writing, software</span></td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>          distributed under the License is distributed on an &quot;AS IS&quot; BASIS, WITHOUT</span></td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>          WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the</span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>          License for the specific language governing permissions and limitations</span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>          under the License.</span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>###################################################################################################</span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">64</span> <span class="pl-k">-</span> <span class="pl-c1">64</span>: i11iIiiIii</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">65</span> <span class="pl-k">-</span> <span class="pl-c1">65</span>: O0 <span class="pl-k">/</span> iIii1I11I1II1 <span class="pl-k">%</span> OoooooooOO <span class="pl-k">-</span> i1IIi</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> xbmc</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> xbmcgui</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> xbmcaddon</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line"><span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">import</span> xml . etree . cElementTree <span class="pl-k">as</span> <span class="pl-c1">ET</span></td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">from</span> xml . dom <span class="pl-k">import</span> minidom <span class="pl-k">as</span> <span class="pl-c1">DOM</span></td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line"><span class="pl-k">except</span> <span class="pl-c1">ImportError</span> :</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">import</span> xml . etree . ElementTree <span class="pl-k">as</span> <span class="pl-c1">ET</span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">except</span> <span class="pl-c1">ImportError</span> :</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">from</span> xml . dom <span class="pl-k">import</span> minidom <span class="pl-k">as</span> <span class="pl-c1">DOM</span></td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">ET</span> <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">73</span> <span class="pl-k">-</span> <span class="pl-c1">73</span>: II111iiii</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">22</span> <span class="pl-k">-</span> <span class="pl-c1">22</span>: I1IiiI <span class="pl-k">*</span> Oo0Ooo <span class="pl-k">/</span> OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo <span class="pl-k">/</span> I1ii11iIi11i</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">I1IiI <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>script.speedtest<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">o0OOO <span class="pl-k">=</span> xbmcaddon . Addon ( I1IiI )</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">iIiiiI <span class="pl-k">=</span> o0OOO . getAddonInfo ( <span class="pl-s"><span class="pl-pds">&#39;</span>id<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">Iii1ii1II11i <span class="pl-k">=</span> o0OOO . getAddonInfo ( <span class="pl-s"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">iI111iI <span class="pl-k">=</span> o0OOO . getAddonInfo ( <span class="pl-s"><span class="pl-pds">&#39;</span>icon<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">IiII <span class="pl-k">=</span> o0OOO . getAddonInfo ( <span class="pl-s"><span class="pl-pds">&#39;</span>version<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">iI1Ii11111iIi <span class="pl-k">=</span> xbmc . translatePath ( <span class="pl-s"><span class="pl-pds">&quot;</span>special://profile/addon_data/<span class="pl-c1">%s</span>/<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> I1IiI )</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">i1i1II <span class="pl-k">=</span> o0OOO . getAddonInfo ( <span class="pl-s"><span class="pl-pds">&quot;</span>path<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">96</span> <span class="pl-k">-</span> <span class="pl-c1">96</span>: o0OO0 <span class="pl-k">-</span> Oo0ooO0oo0oO . I1i1iI1i <span class="pl-k">-</span> o00ooo0 <span class="pl-k">/</span> o00 <span class="pl-k">*</span> Oo0oO0ooo</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">56</span> <span class="pl-k">-</span> <span class="pl-c1">56</span>: ooO00oOoo <span class="pl-k">-</span> O0OOo</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">II1Iiii1111i <span class="pl-k">=</span> <span class="pl-c1">10</span></td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">i1IIi11111i <span class="pl-k">=</span> <span class="pl-c1">92</span></td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">74</span> <span class="pl-k">-</span> <span class="pl-c1">74</span>: o00 <span class="pl-k">*</span> Oo0oO0ooo</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">oo00o0Oo0oo <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">20</span> <span class="pl-k">-</span> <span class="pl-c1">20</span>: O0OOo <span class="pl-k">*</span> II111iiii</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">65</span> <span class="pl-k">-</span> <span class="pl-c1">65</span>: o0oOOo0O0Ooo <span class="pl-k">*</span> iIii1I11I1II1 <span class="pl-k">*</span> O0OOo</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">18</span> <span class="pl-k">-</span> <span class="pl-c1">18</span>: iIii1I11I1II1 <span class="pl-k">/</span> I1i1iI1i <span class="pl-k">+</span> o0OO0 <span class="pl-k">/</span> Oo0Ooo <span class="pl-k">-</span> II111iiii <span class="pl-k">-</span> I1i1iI1i</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">1</span> <span class="pl-k">-</span> <span class="pl-c1">1</span>: I1i1iI1i <span class="pl-k">-</span> Oo0ooO0oo0oO <span class="pl-k">%</span> O0 <span class="pl-k">+</span> I1IiiI <span class="pl-k">-</span> o00 <span class="pl-k">/</span> I1i1iI1i</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">31</span> <span class="pl-k">-</span> <span class="pl-c1">31</span>: OoO0O00 <span class="pl-k">+</span> II111iiii</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> os</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> re</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> sys</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> math</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> signal</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> socket</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> timeit</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> threading</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">13</span> <span class="pl-k">-</span> <span class="pl-c1">13</span>: Oo0ooO0oo0oO <span class="pl-k">*</span> o0OO0 <span class="pl-k">*</span> I1IiiI</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">__version__</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>0.3.2<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">55</span> <span class="pl-k">-</span> <span class="pl-c1">55</span>: II111iiii</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">43</span> <span class="pl-k">-</span> <span class="pl-c1">43</span>: OoOoOO00 <span class="pl-k">-</span> i1IIi <span class="pl-k">+</span> ooO00oOoo <span class="pl-k">+</span> o00ooo0</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">iII111ii <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>speedtest-cli/<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> <span class="pl-c1">__version__</span></td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">i1iIIi1 <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">ii11iIi1I <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">6</span> <span class="pl-k">-</span> <span class="pl-c1">6</span>: OoOoOO00 <span class="pl-k">*</span> o00</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">67</span> <span class="pl-k">-</span> <span class="pl-c1">67</span>: O0OOo <span class="pl-k">-</span> o0OO0 <span class="pl-k">*</span> o0oOOo0O0Ooo <span class="pl-k">%</span> o0oOOo0O0Ooo <span class="pl-k">%</span> I1i1iI1i <span class="pl-k">*</span> OoOoOO00</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">i1IIiiiii <span class="pl-k">=</span> socket . socket</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">55</span> <span class="pl-k">-</span> <span class="pl-c1">55</span>: i1IIi</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line"><span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">import</span> xml . etree . cElementTree <span class="pl-k">as</span> <span class="pl-c1">ET</span></td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">from</span> xml . dom <span class="pl-k">import</span> minidom <span class="pl-k">as</span> <span class="pl-c1">DOM</span></td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line"><span class="pl-k">except</span> <span class="pl-c1">ImportError</span> :</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">import</span> xml . etree . ElementTree <span class="pl-k">as</span> <span class="pl-c1">ET</span></td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">except</span> <span class="pl-c1">ImportError</span> :</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">from</span> xml . dom <span class="pl-k">import</span> minidom <span class="pl-k">as</span> <span class="pl-c1">DOM</span></td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">ET</span> <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">70</span> <span class="pl-k">-</span> <span class="pl-c1">70</span>: OoO0O00 . OoO0O00 <span class="pl-k">-</span> OoO0O00 <span class="pl-k">/</span> I1ii11iIi11i <span class="pl-k">*</span> Oo0ooO0oo0oO</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">86</span> <span class="pl-k">-</span> <span class="pl-c1">86</span>: i11iIiiIii <span class="pl-k">+</span> o00ooo0 <span class="pl-k">+</span> O0OOo <span class="pl-k">*</span> I1i1iI1i <span class="pl-k">+</span> o0oOOo0O0Ooo</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line"><span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">from</span> urllib2 <span class="pl-k">import</span> urlopen , Request , HTTPError , URLError</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line"><span class="pl-k">except</span> <span class="pl-c1">ImportError</span> :</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">from</span> urllib . request <span class="pl-k">import</span> urlopen , Request , HTTPError , URLError</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">61</span> <span class="pl-k">-</span> <span class="pl-c1">61</span>: OoO0O00 <span class="pl-k">/</span> i11iIiiIii</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line"><span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">from</span> httplib <span class="pl-k">import</span> HTTPConnection , HTTPSConnection</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line"><span class="pl-k">except</span> <span class="pl-c1">ImportError</span> :</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">from</span> http . client <span class="pl-k">import</span> HTTPConnection , HTTPSConnection</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">34</span> <span class="pl-k">-</span> <span class="pl-c1">34</span>: OoooooooOO <span class="pl-k">+</span> iIii1I11I1II1 <span class="pl-k">+</span> i11iIiiIii <span class="pl-k">-</span> I1ii11iIi11i <span class="pl-k">+</span> i11iIiiIii</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line"><span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">from</span> Queue <span class="pl-k">import</span> Queue</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line"><span class="pl-k">except</span> <span class="pl-c1">ImportError</span> :</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">from</span> queue <span class="pl-k">import</span> Queue</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">65</span> <span class="pl-k">-</span> <span class="pl-c1">65</span>: OoOoOO00</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line"><span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">from</span> urlparse <span class="pl-k">import</span> urlparse</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line"><span class="pl-k">except</span> <span class="pl-c1">ImportError</span> :</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">from</span> urllib . parse <span class="pl-k">import</span> urlparse</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">6</span> <span class="pl-k">-</span> <span class="pl-c1">6</span>: I1IiiI <span class="pl-k">/</span> Oo0Ooo <span class="pl-k">%</span> o00ooo0</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line"><span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">from</span> urlparse <span class="pl-k">import</span> parse_qs</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line"><span class="pl-k">except</span> <span class="pl-c1">ImportError</span> :</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">from</span> urllib . parse <span class="pl-k">import</span> parse_qs</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">except</span> <span class="pl-c1">ImportError</span> :</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">from</span> cgi <span class="pl-k">import</span> parse_qs</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">84</span> <span class="pl-k">-</span> <span class="pl-c1">84</span>: i11iIiiIii . o0oOOo0O0Ooo</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line"><span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">from</span> hashlib <span class="pl-k">import</span> md5</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line"><span class="pl-k">except</span> <span class="pl-c1">ImportError</span> :</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">from</span> md5 <span class="pl-k">import</span> md5</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">100</span> <span class="pl-k">-</span> <span class="pl-c1">100</span>: o00ooo0 <span class="pl-k">-</span> o00ooo0 <span class="pl-k">-</span> ooO00oOoo</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line"><span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">from</span> argparse <span class="pl-k">import</span> ArgumentParser <span class="pl-k">as</span> ArgParser</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line"><span class="pl-k">except</span> <span class="pl-c1">ImportError</span> :</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">from</span> optparse <span class="pl-k">import</span> OptionParser <span class="pl-k">as</span> ArgParser</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">20</span> <span class="pl-k">-</span> <span class="pl-c1">20</span>: OoooooooOO</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line"><span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">import</span> builtins</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line"><span class="pl-k">except</span> <span class="pl-c1">ImportError</span> :</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">def</span> <span class="pl-en">Ii11iI1i</span> ( <span class="pl-k">*</span> <span class="pl-smi">args</span> , <span class="pl-k">**</span> <span class="pl-smi">kwargs</span> ) :</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">  Ooo <span class="pl-k">=</span> kwargs . pop ( <span class="pl-s"><span class="pl-pds">&quot;</span>file<span class="pl-pds">&quot;</span></span> , sys . stdout )</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">68</span> <span class="pl-k">-</span> <span class="pl-c1">68</span>: I1i1iI1i <span class="pl-k">+</span> Oo0ooO0oo0oO . iIii1I11I1II1 <span class="pl-k">-</span> Oo0oO0ooo <span class="pl-k">%</span> iIii1I11I1II1 <span class="pl-k">-</span> O0OOo</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">79</span> <span class="pl-k">-</span> <span class="pl-c1">79</span>: Oo0Ooo <span class="pl-k">+</span> I1IiiI <span class="pl-k">-</span> o00</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">83</span> <span class="pl-k">-</span> <span class="pl-c1">83</span>: O0OOo</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">64</span> <span class="pl-k">-</span> <span class="pl-c1">64</span>: OoO0O00 <span class="pl-k">%</span> O0OOo <span class="pl-k">%</span> o00 <span class="pl-k">/</span> OoOoOO00 <span class="pl-k">-</span> OoO0O00</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> Ooo <span class="pl-k">is</span> <span class="pl-c1">None</span> :</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">74</span> <span class="pl-k">-</span> <span class="pl-c1">74</span>: o00 <span class="pl-k">*</span> O0</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">oOOo0oo</span> ( <span class="pl-smi">data</span> ) :</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">isinstance</span> ( data , <span class="pl-v">basestring</span> ) :</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">    data <span class="pl-k">=</span> <span class="pl-c1">str</span> ( data )</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">   Ooo . write ( data )</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">80</span> <span class="pl-k">-</span> <span class="pl-c1">80</span>: I1i1iI1i <span class="pl-k">*</span> i11iIiiIii <span class="pl-k">/</span> ooO00oOoo</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">  I11II1i <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">IIIII</span> <span class="pl-k">=</span> kwargs . pop ( <span class="pl-s"><span class="pl-pds">&quot;</span>sep<span class="pl-pds">&quot;</span></span> , <span class="pl-c1">None</span> )</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">IIIII</span> <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span> :</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">isinstance</span> ( <span class="pl-c1">IIIII</span> , <span class="pl-v">unicode</span> ) :</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">    I11II1i <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">elif</span> <span class="pl-k">not</span> <span class="pl-c1">isinstance</span> ( <span class="pl-c1">IIIII</span> , <span class="pl-c1">str</span> ) :</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">raise</span> <span class="pl-c1">TypeError</span> ( <span class="pl-s"><span class="pl-pds">&quot;</span>sep must be None or a string<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">  ooooooO0oo <span class="pl-k">=</span> kwargs . pop ( <span class="pl-s"><span class="pl-pds">&quot;</span>end<span class="pl-pds">&quot;</span></span> , <span class="pl-c1">None</span> )</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> ooooooO0oo <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span> :</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">isinstance</span> ( ooooooO0oo , <span class="pl-v">unicode</span> ) :</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">    I11II1i <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">elif</span> <span class="pl-k">not</span> <span class="pl-c1">isinstance</span> ( ooooooO0oo , <span class="pl-c1">str</span> ) :</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">raise</span> <span class="pl-c1">TypeError</span> ( <span class="pl-s"><span class="pl-pds">&quot;</span>end must be None or a string<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> kwargs :</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">raise</span> <span class="pl-c1">TypeError</span> ( <span class="pl-s"><span class="pl-pds">&quot;</span>invalid keyword arguments to print()<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-k">not</span> I11II1i :</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">for</span> IIiiiiiiIi1I1 <span class="pl-k">in</span> args :</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">isinstance</span> ( IIiiiiiiIi1I1 , <span class="pl-v">unicode</span> ) :</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">     I11II1i <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">     <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> I11II1i :</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">   I1IIIii <span class="pl-k">=</span> <span class="pl-v">unicode</span> ( <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">   oOoOooOo0o0 <span class="pl-k">=</span> <span class="pl-v">unicode</span> ( <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">else</span> :</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">   I1IIIii <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">   oOoOooOo0o0 <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span> <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">IIIII</span> <span class="pl-k">is</span> <span class="pl-c1">None</span> :</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">   <span class="pl-c1">IIIII</span> <span class="pl-k">=</span> oOoOooOo0o0</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> ooooooO0oo <span class="pl-k">is</span> <span class="pl-c1">None</span> :</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">   ooooooO0oo <span class="pl-k">=</span> I1IIIii</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">for</span> <span class="pl-c1">OOOO</span> , IIiiiiiiIi1I1 <span class="pl-k">in</span> <span class="pl-c1">enumerate</span> ( args ) :</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">OOOO</span> :</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">    oOOo0oo ( <span class="pl-c1">IIIII</span> )</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">   oOOo0oo ( IIiiiiiiIi1I1 )</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">  oOOo0oo ( ooooooO0oo )</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line"><span class="pl-k">else</span> :</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line"> Ii11iI1i <span class="pl-k">=</span> <span class="pl-c1">getattr</span> ( builtins , <span class="pl-s"><span class="pl-pds">&#39;</span>print<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">del</span> builtins</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">87</span> <span class="pl-k">-</span> <span class="pl-c1">87</span>: o0OO0 <span class="pl-k">/</span> I1i1iI1i <span class="pl-k">-</span> i1IIi <span class="pl-k">*</span> Oo0ooO0oo0oO <span class="pl-k">/</span> OoooooooOO . O0</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">1</span> <span class="pl-k">-</span> <span class="pl-c1">1</span>: II111iiii <span class="pl-k">-</span> I1i1iI1i <span class="pl-k">/</span> I1i1iI1i</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">I1II1III11iii</span> ( <span class="pl-c1">Exception</span> ) :</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">75</span> <span class="pl-k">-</span> <span class="pl-c1">75</span>: iIii1I11I1II1 <span class="pl-k">/</span> Oo0ooO0oo0oO <span class="pl-k">%</span> o0oOOo0O0Ooo <span class="pl-k">*</span> OoOoOO00</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">9</span> <span class="pl-k">-</span> <span class="pl-c1">9</span>: OoO0O00</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">33</span> <span class="pl-k">-</span> <span class="pl-c1">33</span>: O0OOo . o00</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">58</span> <span class="pl-k">-</span> <span class="pl-c1">58</span>: Oo0ooO0oo0oO <span class="pl-k">*</span> i11iIiiIii <span class="pl-k">/</span> OoOoOO00 <span class="pl-k">%</span> ooO00oOoo <span class="pl-k">-</span> I1ii11iIi11i <span class="pl-k">/</span> o0OO0</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">50</span> <span class="pl-k">-</span> <span class="pl-c1">50</span>: I1IiiI</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">34</span> <span class="pl-k">-</span> <span class="pl-c1">34</span>: I1IiiI <span class="pl-k">*</span> II111iiii <span class="pl-k">%</span> o00 <span class="pl-k">*</span> OoOoOO00 <span class="pl-k">-</span> I1IiiI</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">II1III</span> ( <span class="pl-k">*</span> <span class="pl-smi">args</span> , <span class="pl-k">**</span> <span class="pl-smi">kwargs</span> ) :</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">19</span> <span class="pl-k">-</span> <span class="pl-c1">19</span>: o0OO0 <span class="pl-k">%</span> i1IIi <span class="pl-k">%</span> o0oOOo0O0Ooo</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">93</span> <span class="pl-k">-</span> <span class="pl-c1">93</span>: iIii1I11I1II1 <span class="pl-k">%</span> o0OO0 <span class="pl-k">*</span> i1IIi</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">global</span> i1iIIi1</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line"> Ii11Ii1I <span class="pl-k">=</span> i1IIiiiii ( <span class="pl-k">*</span> args , <span class="pl-k">**</span> kwargs )</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line"> Ii11Ii1I . bind ( ( i1iIIi1 , <span class="pl-c1">0</span> ) )</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">return</span> Ii11Ii1I</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">72</span> <span class="pl-k">-</span> <span class="pl-c1">72</span>: o00 <span class="pl-k">/</span> i1IIi <span class="pl-k">*</span> Oo0Ooo <span class="pl-k">-</span> ooO00oOoo</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">51</span> <span class="pl-k">-</span> <span class="pl-c1">51</span>: II111iiii <span class="pl-k">*</span> OoO0O00 <span class="pl-k">%</span> o0oOOo0O0Ooo <span class="pl-k">*</span> II111iiii <span class="pl-k">%</span> I1ii11iIi11i <span class="pl-k">/</span> O0OOo</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">iIIIIii1</span> ( <span class="pl-smi">origin</span> , <span class="pl-smi">destination</span> ) :</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">58</span> <span class="pl-k">-</span> <span class="pl-c1">58</span>: i11iIiiIii <span class="pl-k">%</span> I1i1iI1i</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">71</span> <span class="pl-k">-</span> <span class="pl-c1">71</span>: Oo0ooO0oo0oO <span class="pl-k">+</span> O0OOo <span class="pl-k">%</span> i11iIiiIii <span class="pl-k">+</span> I1ii11iIi11i <span class="pl-k">-</span> Oo0oO0ooo</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line"> oO0OOoO0 , I111Ii111 <span class="pl-k">=</span> origin</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line"> i111IiI1I , O0iII <span class="pl-k">=</span> destination</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line"> o0 <span class="pl-k">=</span> <span class="pl-c1">6371</span></td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">62</span> <span class="pl-k">-</span> <span class="pl-c1">62</span>: iIii1I11I1II1 <span class="pl-k">*</span> OoOoOO00</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line"> i1 <span class="pl-k">=</span> math . radians ( i111IiI1I <span class="pl-k">-</span> oO0OOoO0 )</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line"> <span class="pl-c1">OOO</span> <span class="pl-k">=</span> math . radians ( O0iII <span class="pl-k">-</span> I111Ii111 )</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line"> Oo0oOOo <span class="pl-k">=</span> ( math . sin ( i1 <span class="pl-k">/</span> <span class="pl-c1">2</span> ) <span class="pl-k">*</span> math . sin ( i1 <span class="pl-k">/</span> <span class="pl-c1">2</span> ) <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line"> math . cos ( math . radians ( oO0OOoO0 ) ) <span class="pl-k">*</span></td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line"> math . cos ( math . radians ( i111IiI1I ) ) <span class="pl-k">*</span> math . sin ( <span class="pl-c1">OOO</span> <span class="pl-k">/</span> <span class="pl-c1">2</span> ) <span class="pl-k">*</span></td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line"> math . sin ( <span class="pl-c1">OOO</span> <span class="pl-k">/</span> <span class="pl-c1">2</span> ) )</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line"> Oo0OoO00oOO0o <span class="pl-k">=</span> <span class="pl-c1">2</span> <span class="pl-k">*</span> math . atan2 ( math . sqrt ( Oo0oOOo ) , math . sqrt ( <span class="pl-c1">1</span> <span class="pl-k">-</span> Oo0oOOo ) )</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line"> <span class="pl-c1">OOO00O</span> <span class="pl-k">=</span> o0 <span class="pl-k">*</span> Oo0OoO00oOO0o</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">84</span> <span class="pl-k">-</span> <span class="pl-c1">84</span>: o0OO0 <span class="pl-k">*</span> OoO0O00 <span class="pl-k">/</span> I1i1iI1i <span class="pl-k">-</span> O0</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">return</span> <span class="pl-c1">OOO00O</span></td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">30</span> <span class="pl-k">-</span> <span class="pl-c1">30</span>: iIii1I11I1II1 <span class="pl-k">/</span> O0OOo <span class="pl-k">-</span> ooO00oOoo <span class="pl-k">-</span> II111iiii <span class="pl-k">%</span> o00</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">49</span> <span class="pl-k">-</span> <span class="pl-c1">49</span>: I1IiiI <span class="pl-k">%</span> O0OOo . O0OOo . I1i1iI1i <span class="pl-k">*</span> O0OOo</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">O0oOO0</span> ( <span class="pl-smi">url</span> , <span class="pl-smi">data</span> <span class="pl-k">=</span> <span class="pl-c1">None</span> , <span class="pl-smi">headers</span> <span class="pl-k">=</span> { } ) :</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">68</span> <span class="pl-k">-</span> <span class="pl-c1">68</span>: ooO00oOoo <span class="pl-k">%</span> i1IIi . Oo0oO0ooo . I1ii11iIi11i</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">92</span> <span class="pl-k">-</span> <span class="pl-c1">92</span>: o00 . ooO00oOoo</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">31</span> <span class="pl-k">-</span> <span class="pl-c1">31</span>: ooO00oOoo . OoOoOO00 <span class="pl-k">/</span> O0</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">89</span> <span class="pl-k">-</span> <span class="pl-c1">89</span>: OoOoOO00</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">68</span> <span class="pl-k">-</span> <span class="pl-c1">68</span>: OoO0O00 <span class="pl-k">*</span> OoooooooOO <span class="pl-k">%</span> O0 <span class="pl-k">+</span> OoO0O00 <span class="pl-k">+</span> O0OOo</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">4</span> <span class="pl-k">-</span> <span class="pl-c1">4</span>: O0OOo <span class="pl-k">+</span> O0 <span class="pl-k">*</span> Oo0ooO0oo0oO</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line"> headers [ <span class="pl-s"><span class="pl-pds">&#39;</span>User-Agent<span class="pl-pds">&#39;</span></span> ] <span class="pl-k">=</span> iII111ii</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">return</span> Request ( url , <span class="pl-v">data</span> <span class="pl-k">=</span> data , <span class="pl-v">headers</span> <span class="pl-k">=</span> headers )</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">55</span> <span class="pl-k">-</span> <span class="pl-c1">55</span>: Oo0Ooo <span class="pl-k">+</span> iIii1I11I1II1 <span class="pl-k">/</span> OoOoOO00 <span class="pl-k">*</span> o0OO0 <span class="pl-k">-</span> i11iIiiIii <span class="pl-k">-</span> o00ooo0</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">25</span> <span class="pl-k">-</span> <span class="pl-c1">25</span>: I1ii11iIi11i</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">Ii1i</span> ( <span class="pl-smi">request</span> ) :</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">15</span> <span class="pl-k">-</span> <span class="pl-c1">15</span>: Oo0oO0ooo . iIii1I11I1II1 . OoooooooOO <span class="pl-k">/</span> i11iIiiIii <span class="pl-k">-</span> o00ooo0 . i1IIi</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">33</span> <span class="pl-k">-</span> <span class="pl-c1">33</span>: I1i1iI1i . o0oOOo0O0Ooo</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">75</span> <span class="pl-k">-</span> <span class="pl-c1">75</span>: o0oOOo0O0Ooo <span class="pl-k">%</span> o0oOOo0O0Ooo . ooO00oOoo</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">5</span> <span class="pl-k">-</span> <span class="pl-c1">5</span>: o0oOOo0O0Ooo <span class="pl-k">*</span> O0OOo <span class="pl-k">+</span> OoOoOO00 . Oo0ooO0oo0oO <span class="pl-k">+</span> OoOoOO00</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">91</span> <span class="pl-k">-</span> <span class="pl-c1">91</span>: O0</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">  oOOo0 <span class="pl-k">=</span> urlopen ( request )</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">return</span> oOOo0</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">except</span> ( HTTPError , URLError , socket . error ) :</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">54</span> <span class="pl-k">-</span> <span class="pl-c1">54</span>: O0 <span class="pl-k">-</span> Oo0oO0ooo <span class="pl-k">%</span> Oo0ooO0oo0oO</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">77</span> <span class="pl-k">-</span> <span class="pl-c1">77</span>: OoOoOO00 <span class="pl-k">/</span> I1IiiI <span class="pl-k">/</span> OoO0O00 <span class="pl-k">+</span> OoO0O00 . Oo0ooO0oo0oO</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">ii1ii11IIIiiI</span> ( <span class="pl-e">threading</span> . <span class="pl-e">Thread</span> ) :</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">67</span> <span class="pl-k">-</span> <span class="pl-c1">67</span>: I1i1iI1i <span class="pl-k">*</span> o0OO0 <span class="pl-k">*</span> I1ii11iIi11i <span class="pl-k">+</span> Oo0ooO0oo0oO <span class="pl-k">/</span> i1IIi</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">11</span> <span class="pl-k">-</span> <span class="pl-c1">11</span>: o00ooo0 <span class="pl-k">+</span> o00 <span class="pl-k">-</span> O0OOo <span class="pl-k">*</span> o0OO0 <span class="pl-k">%</span> i11iIiiIii <span class="pl-k">-</span> ooO00oOoo</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">def</span> <span class="pl-c1">__init__</span> ( <span class="pl-smi"><span class="pl-smi">self</span></span> , <span class="pl-smi">url</span> , <span class="pl-smi">start</span> ) :</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">self</span> . url <span class="pl-k">=</span> url</td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">self</span> . result <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">self</span> . starttime <span class="pl-k">=</span> start</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">  threading . Thread . <span class="pl-c1">__init__</span> ( <span class="pl-c1">self</span> )</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">83</span> <span class="pl-k">-</span> <span class="pl-c1">83</span>: I1i1iI1i <span class="pl-k">/</span> I1IiiI</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">def</span> <span class="pl-en">run</span> ( <span class="pl-smi"><span class="pl-smi">self</span></span> ) :</td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">self</span> . result <span class="pl-k">=</span> [ <span class="pl-c1">0</span> ]</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> ( timeit . default_timer ( ) <span class="pl-k">-</span> <span class="pl-c1">self</span> . starttime ) <span class="pl-k">&lt;=</span> <span class="pl-c1">10</span> :</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">    iIIiIi1iIII1 <span class="pl-k">=</span> O0oOO0 ( <span class="pl-c1">self</span> . url )</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">    OooOOOOo <span class="pl-k">=</span> urlopen ( iIIiIi1iIII1 )</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">while</span> <span class="pl-c1">1</span> <span class="pl-k">and</span> <span class="pl-k">not</span> ii11iIi1I . isSet ( ) :</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">     <span class="pl-c1">self</span> . result . append ( <span class="pl-c1">len</span> ( OooOOOOo . read ( <span class="pl-c1">10240</span> ) ) )</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">     <span class="pl-k">if</span> <span class="pl-c1">self</span> . result [ <span class="pl-k">-</span> <span class="pl-c1">1</span> ] <span class="pl-k">==</span> <span class="pl-c1">0</span> :</td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">    OooOOOOo . close ( )</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">except</span> <span class="pl-c1">IOError</span> :</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">76</span> <span class="pl-k">-</span> <span class="pl-c1">76</span>: OoO0O00</td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">29</span> <span class="pl-k">-</span> <span class="pl-c1">29</span>: Oo0ooO0oo0oO <span class="pl-k">+</span> Oo0Ooo . i11iIiiIii <span class="pl-k">-</span> i1IIi <span class="pl-k">/</span> iIii1I11I1II1</td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">i1iI11i1ii11</span> ( <span class="pl-smi">files</span> , <span class="pl-smi">quiet</span> <span class="pl-k">=</span> <span class="pl-c1">False</span> ) :</td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">58</span> <span class="pl-k">-</span> <span class="pl-c1">58</span>: OoO0O00 <span class="pl-k">%</span> i11iIiiIii . o00 <span class="pl-k">/</span> o0OO0</td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">84</span> <span class="pl-k">-</span> <span class="pl-c1">84</span>: o00 . I1ii11iIi11i <span class="pl-k">/</span> Oo0Ooo <span class="pl-k">-</span> I1IiiI <span class="pl-k">/</span> OoooooooOO <span class="pl-k">/</span> o0oOOo0O0Ooo</td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line"> II111iiiI1Ii <span class="pl-k">=</span> timeit . default_timer ( )</td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">78</span> <span class="pl-k">-</span> <span class="pl-c1">78</span>: o00ooo0 <span class="pl-k">%</span> ooO00oOoo <span class="pl-k">+</span> I1ii11iIi11i</td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">def</span> <span class="pl-en">OOooOoooOoOo</span> ( <span class="pl-smi">q</span> , <span class="pl-smi">files</span> ) :</td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">for</span> <span class="pl-v">file</span> <span class="pl-k">in</span> files :</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">   o0OOOO00O0Oo <span class="pl-k">=</span> ii1ii11IIIiiI ( <span class="pl-v">file</span> , II111iiiI1Ii )</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">   o0OOOO00O0Oo . start ( )</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">   q . put ( o0OOOO00O0Oo , <span class="pl-c1">True</span> )</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-k">not</span> quiet <span class="pl-k">and</span> <span class="pl-k">not</span> ii11iIi1I . isSet ( ) :</td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">    sys . stdout . write ( <span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">    sys . stdout . flush ( )</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">48</span> <span class="pl-k">-</span> <span class="pl-c1">48</span>: O0</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line"> I1IiiIIIi <span class="pl-k">=</span> [ ]</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">41</span> <span class="pl-k">-</span> <span class="pl-c1">41</span>: o00ooo0 <span class="pl-k">-</span> O0 <span class="pl-k">-</span> O0</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">def</span> <span class="pl-en">oO00OOoO00</span> ( <span class="pl-smi">q</span> , <span class="pl-smi">total_files</span> ) :</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">while</span> <span class="pl-c1">len</span> ( I1IiiIIIi ) <span class="pl-k">&lt;</span> total_files :</td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">   o0OOOO00O0Oo <span class="pl-k">=</span> q . get ( <span class="pl-c1">True</span> )</td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">while</span> o0OOOO00O0Oo . isAlive ( ) :</td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">    o0OOOO00O0Oo . join ( <span class="pl-v">timeout</span> <span class="pl-k">=</span> <span class="pl-c1">0.1</span> )</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">   I1IiiIIIi . append ( <span class="pl-c1">sum</span> ( o0OOOO00O0Oo . result ) )</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">del</span> o0OOOO00O0Oo</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">40</span> <span class="pl-k">-</span> <span class="pl-c1">40</span>: I1IiiI <span class="pl-k">*</span> o00ooo0 <span class="pl-k">+</span> Oo0ooO0oo0oO <span class="pl-k">%</span> o00</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line"> OOOOOoo0 <span class="pl-k">=</span> Queue ( <span class="pl-c1">6</span> )</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line"> ii1 <span class="pl-k">=</span> threading . Thread ( <span class="pl-v">target</span> <span class="pl-k">=</span> OOooOoooOoOo , <span class="pl-v">args</span> <span class="pl-k">=</span> ( OOOOOoo0 , files ) )</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line"> I1iI1iIi111i <span class="pl-k">=</span> threading . Thread ( <span class="pl-v">target</span> <span class="pl-k">=</span> oO00OOoO00 , <span class="pl-v">args</span> <span class="pl-k">=</span> ( OOOOOoo0 , <span class="pl-c1">len</span> ( files ) ) )</td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line"> II111iiiI1Ii <span class="pl-k">=</span> timeit . default_timer ( )</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line"> ii1 . start ( )</td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line"> I1iI1iIi111i . start ( )</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">while</span> ii1 . isAlive ( ) :</td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">  ii1 . join ( <span class="pl-v">timeout</span> <span class="pl-k">=</span> <span class="pl-c1">0.1</span> )</td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">while</span> I1iI1iIi111i . isAlive ( ) :</td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">  I1iI1iIi111i . join ( <span class="pl-v">timeout</span> <span class="pl-k">=</span> <span class="pl-c1">0.1</span> )</td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">return</span> ( <span class="pl-c1">sum</span> ( I1IiiIIIi ) <span class="pl-k">/</span> ( timeit . default_timer ( ) <span class="pl-k">-</span> II111iiiI1Ii ) )</td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">44</span> <span class="pl-k">-</span> <span class="pl-c1">44</span>: i1IIi <span class="pl-k">%</span> II111iiii <span class="pl-k">+</span> I1i1iI1i</td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">45</span> <span class="pl-k">-</span> <span class="pl-c1">45</span>: o00 <span class="pl-k">/</span> o00 <span class="pl-k">+</span> ooO00oOoo <span class="pl-k">+</span> O0OOo</td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">iI111i</span> ( <span class="pl-e">threading</span> . <span class="pl-e">Thread</span> ) :</td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">26</span> <span class="pl-k">-</span> <span class="pl-c1">26</span>: I1ii11iIi11i <span class="pl-k">*</span> o00 . II111iiii <span class="pl-k">*</span> o00ooo0</td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">28</span> <span class="pl-k">-</span> <span class="pl-c1">28</span>: OoO0O00 . i1IIi <span class="pl-k">*</span> I1IiiI <span class="pl-k">+</span> O0 . i1IIi <span class="pl-k">-</span> O0OOo</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">def</span> <span class="pl-c1">__init__</span> ( <span class="pl-smi"><span class="pl-smi">self</span></span> , <span class="pl-smi">url</span> , <span class="pl-smi">start</span> , <span class="pl-smi">size</span> ) :</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">self</span> . url <span class="pl-k">=</span> url</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">  i1I1ii11i1Iii <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">  I1IiiiiI <span class="pl-k">=</span> i1I1ii11i1Iii <span class="pl-k">*</span> ( <span class="pl-c1">int</span> ( <span class="pl-c1">round</span> ( <span class="pl-c1">int</span> ( size ) <span class="pl-k">/</span> <span class="pl-c1">36.0</span> ) ) )</td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">self</span> . data <span class="pl-k">=</span> ( <span class="pl-s"><span class="pl-pds">&#39;</span>content1=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> I1IiiiiI [ <span class="pl-c1">0</span> : <span class="pl-c1">int</span> ( size ) <span class="pl-k">-</span> <span class="pl-c1">9</span> ] ) . encode ( )</td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">del</span> I1IiiiiI</td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">self</span> . result <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">self</span> . starttime <span class="pl-k">=</span> start</td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">  threading . Thread . <span class="pl-c1">__init__</span> ( <span class="pl-c1">self</span> )</td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">80</span> <span class="pl-k">-</span> <span class="pl-c1">80</span>: ooO00oOoo . i11iIiiIii <span class="pl-k">-</span> o0oOOo0O0Ooo</td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">def</span> <span class="pl-en">run</span> ( <span class="pl-smi"><span class="pl-smi">self</span></span> ) :</td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> ( ( timeit . default_timer ( ) <span class="pl-k">-</span> <span class="pl-c1">self</span> . starttime ) <span class="pl-k">&lt;=</span> <span class="pl-c1">10</span> <span class="pl-k">and</span></td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">not</span> ii11iIi1I . isSet ( ) ) :</td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">    iIIiIi1iIII1 <span class="pl-k">=</span> O0oOO0 ( <span class="pl-c1">self</span> . url , <span class="pl-v">data</span> <span class="pl-k">=</span> <span class="pl-c1">self</span> . data )</td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line">    OooOOOOo <span class="pl-k">=</span> urlopen ( iIIiIi1iIII1 )</td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">    OooOOOOo . read ( <span class="pl-c1">11</span> )</td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line">    OooOOOOo . close ( )</td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span> . result <span class="pl-k">=</span> <span class="pl-c1">len</span> ( <span class="pl-c1">self</span> . data )</td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">else</span> :</td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span> . result <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">except</span> <span class="pl-c1">IOError</span> :</td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line">   <span class="pl-c1">self</span> . result <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">25</span> <span class="pl-k">-</span> <span class="pl-c1">25</span>: OoO0O00</td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">62</span> <span class="pl-k">-</span> <span class="pl-c1">62</span>: Oo0ooO0oo0oO <span class="pl-k">+</span> O0</td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">oO0OOOO0</span> ( <span class="pl-smi">url</span> , <span class="pl-smi">sizes</span> , <span class="pl-smi">quiet</span> <span class="pl-k">=</span> <span class="pl-c1">False</span> ) :</td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">26</span> <span class="pl-k">-</span> <span class="pl-c1">26</span>: o00ooo0</td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">35</span> <span class="pl-k">-</span> <span class="pl-c1">35</span>: o00ooo0 <span class="pl-k">-</span> I1IiiI <span class="pl-k">%</span> o0oOOo0O0Ooo . OoooooooOO <span class="pl-k">%</span> o00ooo0</td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line"> II111iiiI1Ii <span class="pl-k">=</span> timeit . default_timer ( )</td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">47</span> <span class="pl-k">-</span> <span class="pl-c1">47</span>: o00 <span class="pl-k">-</span> o00ooo0 . II111iiii <span class="pl-k">+</span> OoooooooOO . i11iIiiIii</td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">def</span> <span class="pl-en">OOooOoooOoOo</span> ( <span class="pl-smi">q</span> , <span class="pl-smi">sizes</span> ) :</td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">for</span> OOo0oO00ooO00 <span class="pl-k">in</span> sizes :</td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">   o0OOOO00O0Oo <span class="pl-k">=</span> iI111i ( url , II111iiiI1Ii , OOo0oO00ooO00 )</td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">   o0OOOO00O0Oo . start ( )</td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line">   q . put ( o0OOOO00O0Oo , <span class="pl-c1">True</span> )</td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-k">not</span> quiet <span class="pl-k">and</span> <span class="pl-k">not</span> ii11iIi1I . isSet ( ) :</td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">    sys . stdout . write ( <span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">    sys . stdout . flush ( )</td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">90</span> <span class="pl-k">-</span> <span class="pl-c1">90</span>: OoOoOO00 <span class="pl-k">*</span> ooO00oOoo <span class="pl-k">+</span> o0oOOo0O0Ooo</td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line"> I1IiiIIIi <span class="pl-k">=</span> [ ]</td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">81</span> <span class="pl-k">-</span> <span class="pl-c1">81</span>: o0OO0 . o0oOOo0O0Ooo <span class="pl-k">%</span> O0 <span class="pl-k">/</span> I1IiiI <span class="pl-k">-</span> o0OO0</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">def</span> <span class="pl-en">oO00OOoO00</span> ( <span class="pl-smi">q</span> , <span class="pl-smi">total_sizes</span> ) :</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">while</span> <span class="pl-c1">len</span> ( I1IiiIIIi ) <span class="pl-k">&lt;</span> total_sizes :</td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line">   o0OOOO00O0Oo <span class="pl-k">=</span> q . get ( <span class="pl-c1">True</span> )</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">while</span> o0OOOO00O0Oo . isAlive ( ) :</td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">    o0OOOO00O0Oo . join ( <span class="pl-v">timeout</span> <span class="pl-k">=</span> <span class="pl-c1">0.1</span> )</td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line">   I1IiiIIIi . append ( o0OOOO00O0Oo . result )</td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">del</span> o0OOOO00O0Oo</td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">43</span> <span class="pl-k">-</span> <span class="pl-c1">43</span>: i11iIiiIii <span class="pl-k">+</span> Oo0Ooo <span class="pl-k">*</span> II111iiii <span class="pl-k">*</span> ooO00oOoo <span class="pl-k">*</span> O0</td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line"> OOOOOoo0 <span class="pl-k">=</span> Queue ( <span class="pl-c1">6</span> )</td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line"> ii1 <span class="pl-k">=</span> threading . Thread ( <span class="pl-v">target</span> <span class="pl-k">=</span> OOooOoooOoOo , <span class="pl-v">args</span> <span class="pl-k">=</span> ( OOOOOoo0 , sizes ) )</td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line"> I1iI1iIi111i <span class="pl-k">=</span> threading . Thread ( <span class="pl-v">target</span> <span class="pl-k">=</span> oO00OOoO00 , <span class="pl-v">args</span> <span class="pl-k">=</span> ( OOOOOoo0 , <span class="pl-c1">len</span> ( sizes ) ) )</td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line"> II111iiiI1Ii <span class="pl-k">=</span> timeit . default_timer ( )</td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line"> ii1 . start ( )</td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line"> I1iI1iIi111i . start ( )</td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">while</span> ii1 . isAlive ( ) :</td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">  ii1 . join ( <span class="pl-v">timeout</span> <span class="pl-k">=</span> <span class="pl-c1">0.1</span> )</td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">while</span> I1iI1iIi111i . isAlive ( ) :</td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line">  I1iI1iIi111i . join ( <span class="pl-v">timeout</span> <span class="pl-k">=</span> <span class="pl-c1">0.1</span> )</td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">return</span> ( <span class="pl-c1">sum</span> ( I1IiiIIIi ) <span class="pl-k">/</span> ( timeit . default_timer ( ) <span class="pl-k">-</span> II111iiiI1Ii ) )</td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">64</span> <span class="pl-k">-</span> <span class="pl-c1">64</span>: Oo0ooO0oo0oO <span class="pl-k">%</span> iIii1I11I1II1 <span class="pl-k">*</span> o0OO0</td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">79</span> <span class="pl-k">-</span> <span class="pl-c1">79</span>: O0</td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">oOO00O</span> ( <span class="pl-smi">dom</span> , <span class="pl-smi">tagName</span> ) :</td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line"> OOOoo0OO <span class="pl-k">=</span> dom . getElementsByTagName ( tagName ) [ <span class="pl-c1">0</span> ]</td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">57</span> <span class="pl-k">-</span> <span class="pl-c1">57</span>: OoO0O00 <span class="pl-k">/</span> O0OOo</td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">29</span> <span class="pl-k">-</span> <span class="pl-c1">29</span>: iIii1I11I1II1 <span class="pl-k">+</span> OoOoOO00 <span class="pl-k">*</span> OoO0O00 <span class="pl-k">*</span> Oo0ooO0oo0oO . I1IiiI <span class="pl-k">*</span> I1IiiI</td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">7</span> <span class="pl-k">-</span> <span class="pl-c1">7</span>: Oo0oO0ooo <span class="pl-k">*</span> ooO00oOoo <span class="pl-k">%</span> o00ooo0 <span class="pl-k">-</span> o0oOOo0O0Ooo</td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">13</span> <span class="pl-k">-</span> <span class="pl-c1">13</span>: o00ooo0 . i11iIiiIii</td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">56</span> <span class="pl-k">-</span> <span class="pl-c1">56</span>: I1ii11iIi11i <span class="pl-k">%</span> O0 <span class="pl-k">-</span> I1IiiI</td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">100</span> <span class="pl-k">-</span> <span class="pl-c1">100</span>: o00ooo0 <span class="pl-k">-</span> O0 <span class="pl-k">%</span> o0OO0 <span class="pl-k">*</span> Oo0ooO0oo0oO <span class="pl-k">+</span> I1IiiI</td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">return</span> <span class="pl-c1">dict</span> ( <span class="pl-c1">list</span> ( OOOoo0OO . attributes . items ( ) ) )</td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">88</span> <span class="pl-k">-</span> <span class="pl-c1">88</span>: OoooooooOO <span class="pl-k">-</span> OoO0O00 <span class="pl-k">*</span> O0 <span class="pl-k">*</span> OoooooooOO . OoooooooOO</td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">33</span> <span class="pl-k">-</span> <span class="pl-c1">33</span>: ooO00oOoo <span class="pl-k">+</span> o00 <span class="pl-k">*</span> o0OO0 <span class="pl-k">/</span> iIii1I11I1II1 <span class="pl-k">-</span> I1IiiI</td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">O0oO</span> ( ) :</td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">73</span> <span class="pl-k">-</span> <span class="pl-c1">73</span>: I1ii11iIi11i <span class="pl-k">*</span> i11iIiiIii <span class="pl-k">%</span> o0OO0 . I1ii11iIi11i</td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">66</span> <span class="pl-k">-</span> <span class="pl-c1">66</span>: o0OO0 <span class="pl-k">+</span> o0OO0 <span class="pl-k">+</span> O0OOo <span class="pl-k">/</span> o00 <span class="pl-k">+</span> Oo0ooO0oo0oO</td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">30</span> <span class="pl-k">-</span> <span class="pl-c1">30</span>: O0</td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">44</span> <span class="pl-k">-</span> <span class="pl-c1">44</span>: o0OO0 <span class="pl-k">/</span> I1i1iI1i <span class="pl-k">/</span> I1i1iI1i</td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line"> iIIiIi1iIII1 <span class="pl-k">=</span> O0oOO0 ( <span class="pl-s"><span class="pl-pds">&#39;</span>https://www.speedtest.net/speedtest-config.php<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line"> oOOo0 <span class="pl-k">=</span> Ii1i ( iIIiIi1iIII1 )</td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> oOOo0 <span class="pl-k">is</span> <span class="pl-c1">False</span> :</td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line">  Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Could not retrieve speedtest.net configuration<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line">  sys . <span class="pl-c1">exit</span> ( <span class="pl-c1">1</span> )</td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line"> OOOiiiiI <span class="pl-k">=</span> [ ]</td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">while</span> <span class="pl-c1">1</span> :</td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line">  OOOiiiiI . append ( oOOo0 . read ( <span class="pl-c1">10240</span> ) )</td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">len</span> ( OOOiiiiI [ <span class="pl-k">-</span> <span class="pl-c1">1</span> ] ) <span class="pl-k">==</span> <span class="pl-c1">0</span> :</td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">int</span> ( oOOo0 . code ) <span class="pl-k">!=</span> <span class="pl-c1">200</span> :</td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">return</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line"> oOOo0 . close ( )</td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line">   oooOo0OOOoo0 <span class="pl-k">=</span> <span class="pl-c1">ET</span> . fromstring ( <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span> . encode ( ) . join ( OOOiiiiI ) )</td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line">   OOoO <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>client<span class="pl-pds">&#39;</span></span> : oooOo0OOOoo0 . find ( <span class="pl-s"><span class="pl-pds">&#39;</span>client<span class="pl-pds">&#39;</span></span> ) . attrib ,</td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>times<span class="pl-pds">&#39;</span></span> : oooOo0OOOoo0 . find ( <span class="pl-s"><span class="pl-pds">&#39;</span>times<span class="pl-pds">&#39;</span></span> ) . attrib ,</td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>download<span class="pl-pds">&#39;</span></span> : oooOo0OOOoo0 . find ( <span class="pl-s"><span class="pl-pds">&#39;</span>download<span class="pl-pds">&#39;</span></span> ) . attrib ,</td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>upload<span class="pl-pds">&#39;</span></span> : oooOo0OOOoo0 . find ( <span class="pl-s"><span class="pl-pds">&#39;</span>upload<span class="pl-pds">&#39;</span></span> ) . attrib }</td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">except</span> <span class="pl-c1">Exception</span> , <span class="pl-c1">OO0O000</span> :</td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line">   xbmc . log ( <span class="pl-s"><span class="pl-pds">&#39;</span>Exception for ET: <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span> ( <span class="pl-c1">OO0O000</span> ) , <span class="pl-v">level</span> <span class="pl-k">=</span> xbmc . <span class="pl-c1">LOGDEBUG</span> )</td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line">   oooOo0OOOoo0 <span class="pl-k">=</span> <span class="pl-c1">DOM</span> . parseString ( <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span> . join ( OOOiiiiI ) )</td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line">   OOoO <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>client<span class="pl-pds">&#39;</span></span> : oOO00O ( oooOo0OOOoo0 , <span class="pl-s"><span class="pl-pds">&#39;</span>client<span class="pl-pds">&#39;</span></span> ) ,</td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>times<span class="pl-pds">&#39;</span></span> : oOO00O ( oooOo0OOOoo0 , <span class="pl-s"><span class="pl-pds">&#39;</span>times<span class="pl-pds">&#39;</span></span> ) ,</td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>download<span class="pl-pds">&#39;</span></span> : oOO00O ( oooOo0OOOoo0 , <span class="pl-s"><span class="pl-pds">&#39;</span>download<span class="pl-pds">&#39;</span></span> ) ,</td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>upload<span class="pl-pds">&#39;</span></span> : oOO00O ( oooOo0OOOoo0 , <span class="pl-s"><span class="pl-pds">&#39;</span>upload<span class="pl-pds">&#39;</span></span> ) }</td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">except</span> <span class="pl-c1">SyntaxError</span> :</td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line">  Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Failed to parse speedtest.net configuration<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line">  sys . <span class="pl-c1">exit</span> ( <span class="pl-c1">1</span> )</td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">del</span> oooOo0OOOoo0</td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">del</span> OOOiiiiI</td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">return</span> OOoO</td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">37</span> <span class="pl-k">-</span> <span class="pl-c1">37</span>: OoooooooOO <span class="pl-k">-</span> O0 <span class="pl-k">-</span> o0oOOo0O0Ooo</td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">77</span> <span class="pl-k">-</span> <span class="pl-c1">77</span>: Oo0ooO0oo0oO <span class="pl-k">*</span> iIii1I11I1II1</td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">oO00oOOoooO</span> ( <span class="pl-smi">client</span> , <span class="pl-smi">all</span> <span class="pl-k">=</span> <span class="pl-c1">False</span> ) :</td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">46</span> <span class="pl-k">-</span> <span class="pl-c1">46</span>: I1IiiI <span class="pl-k">-</span> OoooooooOO <span class="pl-k">-</span> I1i1iI1i <span class="pl-k">*</span> II111iiii</td>
      </tr>
      <tr>
        <td id="L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="LC433" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">34</span> <span class="pl-k">-</span> <span class="pl-c1">34</span>: I1i1iI1i <span class="pl-k">-</span> o00 <span class="pl-k">/</span> Oo0ooO0oo0oO <span class="pl-k">+</span> I1ii11iIi11i <span class="pl-k">*</span> o00ooo0</td>
      </tr>
      <tr>
        <td id="L434" class="blob-num js-line-number" data-line-number="434"></td>
        <td id="LC434" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">73</span> <span class="pl-k">-</span> <span class="pl-c1">73</span>: OoOoOO00 . o00ooo0 <span class="pl-k">*</span> I1ii11iIi11i <span class="pl-k">%</span> I1ii11iIi11i <span class="pl-k">%</span> OoooooooOO</td>
      </tr>
      <tr>
        <td id="L435" class="blob-num js-line-number" data-line-number="435"></td>
        <td id="LC435" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">63</span> <span class="pl-k">-</span> <span class="pl-c1">63</span>: iIii1I11I1II1 <span class="pl-k">*</span> i11iIiiIii <span class="pl-k">%</span> iIii1I11I1II1 <span class="pl-k">*</span> i11iIiiIii</td>
      </tr>
      <tr>
        <td id="L436" class="blob-num js-line-number" data-line-number="436"></td>
        <td id="LC436" class="blob-code blob-code-inner js-file-line"> iI1111iiii <span class="pl-k">=</span> [</td>
      </tr>
      <tr>
        <td id="L437" class="blob-num js-line-number" data-line-number="437"></td>
        <td id="LC437" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>https://www.speedtest.net/speedtest-servers-static.php<span class="pl-pds">&#39;</span></span> ,</td>
      </tr>
      <tr>
        <td id="L438" class="blob-num js-line-number" data-line-number="438"></td>
        <td id="LC438" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>http://c.speedtest.net/speedtest-servers-static.php<span class="pl-pds">&#39;</span></span> ,</td>
      </tr>
      <tr>
        <td id="L439" class="blob-num js-line-number" data-line-number="439"></td>
        <td id="LC439" class="blob-code blob-code-inner js-file-line"> ]</td>
      </tr>
      <tr>
        <td id="L440" class="blob-num js-line-number" data-line-number="440"></td>
        <td id="LC440" class="blob-code blob-code-inner js-file-line"> Oo0OO <span class="pl-k">=</span> { }</td>
      </tr>
      <tr>
        <td id="L441" class="blob-num js-line-number" data-line-number="441"></td>
        <td id="LC441" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">for</span> O0OooOo0o <span class="pl-k">in</span> iI1111iiii :</td>
      </tr>
      <tr>
        <td id="L442" class="blob-num js-line-number" data-line-number="442"></td>
        <td id="LC442" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L443" class="blob-num js-line-number" data-line-number="443"></td>
        <td id="LC443" class="blob-code blob-code-inner js-file-line">   iIIiIi1iIII1 <span class="pl-k">=</span> O0oOO0 ( O0OooOo0o )</td>
      </tr>
      <tr>
        <td id="L444" class="blob-num js-line-number" data-line-number="444"></td>
        <td id="LC444" class="blob-code blob-code-inner js-file-line">   oOOo0 <span class="pl-k">=</span> Ii1i ( iIIiIi1iIII1 )</td>
      </tr>
      <tr>
        <td id="L445" class="blob-num js-line-number" data-line-number="445"></td>
        <td id="LC445" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> oOOo0 <span class="pl-k">is</span> <span class="pl-c1">False</span> :</td>
      </tr>
      <tr>
        <td id="L446" class="blob-num js-line-number" data-line-number="446"></td>
        <td id="LC446" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">raise</span> I1II1III11iii</td>
      </tr>
      <tr>
        <td id="L447" class="blob-num js-line-number" data-line-number="447"></td>
        <td id="LC447" class="blob-code blob-code-inner js-file-line">   iiI11ii1I1 <span class="pl-k">=</span> [ ]</td>
      </tr>
      <tr>
        <td id="L448" class="blob-num js-line-number" data-line-number="448"></td>
        <td id="LC448" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">while</span> <span class="pl-c1">1</span> :</td>
      </tr>
      <tr>
        <td id="L449" class="blob-num js-line-number" data-line-number="449"></td>
        <td id="LC449" class="blob-code blob-code-inner js-file-line">    iiI11ii1I1 . append ( oOOo0 . read ( <span class="pl-c1">10240</span> ) )</td>
      </tr>
      <tr>
        <td id="L450" class="blob-num js-line-number" data-line-number="450"></td>
        <td id="LC450" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">len</span> ( iiI11ii1I1 [ <span class="pl-k">-</span> <span class="pl-c1">1</span> ] ) <span class="pl-k">==</span> <span class="pl-c1">0</span> :</td>
      </tr>
      <tr>
        <td id="L451" class="blob-num js-line-number" data-line-number="451"></td>
        <td id="LC451" class="blob-code blob-code-inner js-file-line">     <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L452" class="blob-num js-line-number" data-line-number="452"></td>
        <td id="LC452" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">int</span> ( oOOo0 . code ) <span class="pl-k">!=</span> <span class="pl-c1">200</span> :</td>
      </tr>
      <tr>
        <td id="L453" class="blob-num js-line-number" data-line-number="453"></td>
        <td id="LC453" class="blob-code blob-code-inner js-file-line">    oOOo0 . close ( )</td>
      </tr>
      <tr>
        <td id="L454" class="blob-num js-line-number" data-line-number="454"></td>
        <td id="LC454" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">raise</span> I1II1III11iii</td>
      </tr>
      <tr>
        <td id="L455" class="blob-num js-line-number" data-line-number="455"></td>
        <td id="LC455" class="blob-code blob-code-inner js-file-line">   oOOo0 . close ( )</td>
      </tr>
      <tr>
        <td id="L456" class="blob-num js-line-number" data-line-number="456"></td>
        <td id="LC456" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L457" class="blob-num js-line-number" data-line-number="457"></td>
        <td id="LC457" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L458" class="blob-num js-line-number" data-line-number="458"></td>
        <td id="LC458" class="blob-code blob-code-inner js-file-line">     oooOo0OOOoo0 <span class="pl-k">=</span> <span class="pl-c1">ET</span> . fromstring ( <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span> . encode ( ) . join ( iiI11ii1I1 ) )</td>
      </tr>
      <tr>
        <td id="L459" class="blob-num js-line-number" data-line-number="459"></td>
        <td id="LC459" class="blob-code blob-code-inner js-file-line">     Ooo0OOoOoO0 <span class="pl-k">=</span> oooOo0OOOoo0 . getiterator ( <span class="pl-s"><span class="pl-pds">&#39;</span>server<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L460" class="blob-num js-line-number" data-line-number="460"></td>
        <td id="LC460" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">except</span> <span class="pl-c1">Exception</span> , <span class="pl-c1">OO0O000</span> :</td>
      </tr>
      <tr>
        <td id="L461" class="blob-num js-line-number" data-line-number="461"></td>
        <td id="LC461" class="blob-code blob-code-inner js-file-line">     xbmc . log ( <span class="pl-s"><span class="pl-pds">&#39;</span>Exception for ET: <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span> ( <span class="pl-c1">OO0O000</span> ) , <span class="pl-v">level</span> <span class="pl-k">=</span> xbmc . <span class="pl-c1">LOGDEBUG</span> )</td>
      </tr>
      <tr>
        <td id="L462" class="blob-num js-line-number" data-line-number="462"></td>
        <td id="LC462" class="blob-code blob-code-inner js-file-line">     oooOo0OOOoo0 <span class="pl-k">=</span> <span class="pl-c1">DOM</span> . parseString ( <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span> . join ( iiI11ii1I1 ) )</td>
      </tr>
      <tr>
        <td id="L463" class="blob-num js-line-number" data-line-number="463"></td>
        <td id="LC463" class="blob-code blob-code-inner js-file-line">     Ooo0OOoOoO0 <span class="pl-k">=</span> oooOo0OOOoo0 . getElementsByTagName ( <span class="pl-s"><span class="pl-pds">&#39;</span>server<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L464" class="blob-num js-line-number" data-line-number="464"></td>
        <td id="LC464" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">except</span> <span class="pl-c1">SyntaxError</span> :</td>
      </tr>
      <tr>
        <td id="L465" class="blob-num js-line-number" data-line-number="465"></td>
        <td id="LC465" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">raise</span> I1II1III11iii</td>
      </tr>
      <tr>
        <td id="L466" class="blob-num js-line-number" data-line-number="466"></td>
        <td id="LC466" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">for</span> oOo0OOoO0 <span class="pl-k">in</span> Ooo0OOoOoO0 :</td>
      </tr>
      <tr>
        <td id="L467" class="blob-num js-line-number" data-line-number="467"></td>
        <td id="LC467" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L468" class="blob-num js-line-number" data-line-number="468"></td>
        <td id="LC468" class="blob-code blob-code-inner js-file-line">     <span class="pl-c1">II</span> <span class="pl-k">=</span> oOo0OOoO0 . attrib</td>
      </tr>
      <tr>
        <td id="L469" class="blob-num js-line-number" data-line-number="469"></td>
        <td id="LC469" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">except</span> <span class="pl-c1">AttributeError</span> :</td>
      </tr>
      <tr>
        <td id="L470" class="blob-num js-line-number" data-line-number="470"></td>
        <td id="LC470" class="blob-code blob-code-inner js-file-line">     <span class="pl-c1">II</span> <span class="pl-k">=</span> <span class="pl-c1">dict</span> ( <span class="pl-c1">list</span> ( oOo0OOoO0 . attributes . items ( ) ) )</td>
      </tr>
      <tr>
        <td id="L471" class="blob-num js-line-number" data-line-number="471"></td>
        <td id="LC471" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">OOO00O</span> <span class="pl-k">=</span> iIIIIii1 ( [ <span class="pl-c1">float</span> ( client [ <span class="pl-s"><span class="pl-pds">&#39;</span>lat<span class="pl-pds">&#39;</span></span> ] ) ,</td>
      </tr>
      <tr>
        <td id="L472" class="blob-num js-line-number" data-line-number="472"></td>
        <td id="LC472" class="blob-code blob-code-inner js-file-line"> <span class="pl-c1">float</span> ( client [ <span class="pl-s"><span class="pl-pds">&#39;</span>lon<span class="pl-pds">&#39;</span></span> ] ) ] ,</td>
      </tr>
      <tr>
        <td id="L473" class="blob-num js-line-number" data-line-number="473"></td>
        <td id="LC473" class="blob-code blob-code-inner js-file-line"> [ <span class="pl-c1">float</span> ( <span class="pl-c1">II</span> . get ( <span class="pl-s"><span class="pl-pds">&#39;</span>lat<span class="pl-pds">&#39;</span></span> ) ) ,</td>
      </tr>
      <tr>
        <td id="L474" class="blob-num js-line-number" data-line-number="474"></td>
        <td id="LC474" class="blob-code blob-code-inner js-file-line"> <span class="pl-c1">float</span> ( <span class="pl-c1">II</span> . get ( <span class="pl-s"><span class="pl-pds">&#39;</span>lon<span class="pl-pds">&#39;</span></span> ) ) ] )</td>
      </tr>
      <tr>
        <td id="L475" class="blob-num js-line-number" data-line-number="475"></td>
        <td id="LC475" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">II</span> [ <span class="pl-s"><span class="pl-pds">&#39;</span>d<span class="pl-pds">&#39;</span></span> ] <span class="pl-k">=</span> <span class="pl-c1">OOO00O</span></td>
      </tr>
      <tr>
        <td id="L476" class="blob-num js-line-number" data-line-number="476"></td>
        <td id="LC476" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">OOO00O</span> <span class="pl-k">not</span> <span class="pl-k">in</span> Oo0OO :</td>
      </tr>
      <tr>
        <td id="L477" class="blob-num js-line-number" data-line-number="477"></td>
        <td id="LC477" class="blob-code blob-code-inner js-file-line">     Oo0OO [ <span class="pl-c1">OOO00O</span> ] <span class="pl-k">=</span> [ <span class="pl-c1">II</span> ]</td>
      </tr>
      <tr>
        <td id="L478" class="blob-num js-line-number" data-line-number="478"></td>
        <td id="LC478" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span> :</td>
      </tr>
      <tr>
        <td id="L479" class="blob-num js-line-number" data-line-number="479"></td>
        <td id="LC479" class="blob-code blob-code-inner js-file-line">     Oo0OO [ <span class="pl-c1">OOO00O</span> ] . append ( <span class="pl-c1">II</span> )</td>
      </tr>
      <tr>
        <td id="L480" class="blob-num js-line-number" data-line-number="480"></td>
        <td id="LC480" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">del</span> oooOo0OOOoo0</td>
      </tr>
      <tr>
        <td id="L481" class="blob-num js-line-number" data-line-number="481"></td>
        <td id="LC481" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">del</span> iiI11ii1I1</td>
      </tr>
      <tr>
        <td id="L482" class="blob-num js-line-number" data-line-number="482"></td>
        <td id="LC482" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">del</span> Ooo0OOoOoO0</td>
      </tr>
      <tr>
        <td id="L483" class="blob-num js-line-number" data-line-number="483"></td>
        <td id="LC483" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">except</span> I1II1III11iii :</td>
      </tr>
      <tr>
        <td id="L484" class="blob-num js-line-number" data-line-number="484"></td>
        <td id="LC484" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L485" class="blob-num js-line-number" data-line-number="485"></td>
        <td id="LC485" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">93</span> <span class="pl-k">-</span> <span class="pl-c1">93</span>: Oo0oO0ooo <span class="pl-k">*</span> OoooooooOO <span class="pl-k">+</span> O0OOo</td>
      </tr>
      <tr>
        <td id="L486" class="blob-num js-line-number" data-line-number="486"></td>
        <td id="LC486" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">33</span> <span class="pl-k">-</span> <span class="pl-c1">33</span>: O0 <span class="pl-k">*</span> o0oOOo0O0Ooo <span class="pl-k">-</span> ooO00oOoo <span class="pl-k">%</span> ooO00oOoo</td>
      </tr>
      <tr>
        <td id="L487" class="blob-num js-line-number" data-line-number="487"></td>
        <td id="LC487" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> Oo0OO :</td>
      </tr>
      <tr>
        <td id="L488" class="blob-num js-line-number" data-line-number="488"></td>
        <td id="LC488" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L489" class="blob-num js-line-number" data-line-number="489"></td>
        <td id="LC489" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">18</span> <span class="pl-k">-</span> <span class="pl-c1">18</span>: ooO00oOoo <span class="pl-k">/</span> Oo0Ooo <span class="pl-k">*</span> ooO00oOoo <span class="pl-k">+</span> ooO00oOoo <span class="pl-k">*</span> i11iIiiIii <span class="pl-k">*</span> I1ii11iIi11i</td>
      </tr>
      <tr>
        <td id="L490" class="blob-num js-line-number" data-line-number="490"></td>
        <td id="LC490" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-k">not</span> Oo0OO :</td>
      </tr>
      <tr>
        <td id="L491" class="blob-num js-line-number" data-line-number="491"></td>
        <td id="LC491" class="blob-code blob-code-inner js-file-line">  Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Failed to retrieve list of speedtest.net servers<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L492" class="blob-num js-line-number" data-line-number="492"></td>
        <td id="LC492" class="blob-code blob-code-inner js-file-line">  sys . <span class="pl-c1">exit</span> ( <span class="pl-c1">1</span> )</td>
      </tr>
      <tr>
        <td id="L493" class="blob-num js-line-number" data-line-number="493"></td>
        <td id="LC493" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">11</span> <span class="pl-k">-</span> <span class="pl-c1">11</span>: O0OOo <span class="pl-k">/</span> OoOoOO00 <span class="pl-k">-</span> Oo0oO0ooo <span class="pl-k">*</span> OoooooooOO <span class="pl-k">+</span> OoooooooOO . OoOoOO00</td>
      </tr>
      <tr>
        <td id="L494" class="blob-num js-line-number" data-line-number="494"></td>
        <td id="LC494" class="blob-code blob-code-inner js-file-line"> i1I1i111Ii <span class="pl-k">=</span> [ ]</td>
      </tr>
      <tr>
        <td id="L495" class="blob-num js-line-number" data-line-number="495"></td>
        <td id="LC495" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">for</span> <span class="pl-c1">OOO00O</span> <span class="pl-k">in</span> <span class="pl-c1">sorted</span> ( Oo0OO . keys ( ) ) :</td>
      </tr>
      <tr>
        <td id="L496" class="blob-num js-line-number" data-line-number="496"></td>
        <td id="LC496" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">for</span> ooo <span class="pl-k">in</span> Oo0OO [ <span class="pl-c1">OOO00O</span> ] :</td>
      </tr>
      <tr>
        <td id="L497" class="blob-num js-line-number" data-line-number="497"></td>
        <td id="LC497" class="blob-code blob-code-inner js-file-line">   i1I1i111Ii . append ( ooo )</td>
      </tr>
      <tr>
        <td id="L498" class="blob-num js-line-number" data-line-number="498"></td>
        <td id="LC498" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">len</span> ( i1I1i111Ii ) <span class="pl-k">==</span> <span class="pl-c1">5</span> <span class="pl-k">and</span> <span class="pl-k">not</span> <span class="pl-c1">all</span> :</td>
      </tr>
      <tr>
        <td id="L499" class="blob-num js-line-number" data-line-number="499"></td>
        <td id="LC499" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L500" class="blob-num js-line-number" data-line-number="500"></td>
        <td id="LC500" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">else</span> :</td>
      </tr>
      <tr>
        <td id="L501" class="blob-num js-line-number" data-line-number="501"></td>
        <td id="LC501" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L502" class="blob-num js-line-number" data-line-number="502"></td>
        <td id="LC502" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L503" class="blob-num js-line-number" data-line-number="503"></td>
        <td id="LC503" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">27</span> <span class="pl-k">-</span> <span class="pl-c1">27</span>: O0OOo <span class="pl-k">%</span> I1IiiI</td>
      </tr>
      <tr>
        <td id="L504" class="blob-num js-line-number" data-line-number="504"></td>
        <td id="LC504" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">del</span> Oo0OO</td>
      </tr>
      <tr>
        <td id="L505" class="blob-num js-line-number" data-line-number="505"></td>
        <td id="LC505" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">return</span> i1I1i111Ii</td>
      </tr>
      <tr>
        <td id="L506" class="blob-num js-line-number" data-line-number="506"></td>
        <td id="LC506" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">73</span> <span class="pl-k">-</span> <span class="pl-c1">73</span>: Oo0ooO0oo0oO</td>
      </tr>
      <tr>
        <td id="L507" class="blob-num js-line-number" data-line-number="507"></td>
        <td id="LC507" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">70</span> <span class="pl-k">-</span> <span class="pl-c1">70</span>: iIii1I11I1II1</td>
      </tr>
      <tr>
        <td id="L508" class="blob-num js-line-number" data-line-number="508"></td>
        <td id="LC508" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">i11ii1iI</span> ( <span class="pl-smi">servers</span> ) :</td>
      </tr>
      <tr>
        <td id="L509" class="blob-num js-line-number" data-line-number="509"></td>
        <td id="LC509" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">22</span> <span class="pl-k">-</span> <span class="pl-c1">22</span>: OoooooooOO</td>
      </tr>
      <tr>
        <td id="L510" class="blob-num js-line-number" data-line-number="510"></td>
        <td id="LC510" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">75</span> <span class="pl-k">-</span> <span class="pl-c1">75</span>: o0oOOo0O0Ooo <span class="pl-k">+</span> o0oOOo0O0Ooo <span class="pl-k">+</span> i1IIi <span class="pl-k">-</span> i1IIi</td>
      </tr>
      <tr>
        <td id="L511" class="blob-num js-line-number" data-line-number="511"></td>
        <td id="LC511" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">76</span> <span class="pl-k">-</span> <span class="pl-c1">76</span>: OoO0O00 . O0 <span class="pl-k">%</span> O0 <span class="pl-k">-</span> o0oOOo0O0Ooo <span class="pl-k">-</span> iIii1I11I1II1 <span class="pl-k">-</span> I1IiiI</td>
      </tr>
      <tr>
        <td id="L512" class="blob-num js-line-number" data-line-number="512"></td>
        <td id="LC512" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">53</span> <span class="pl-k">-</span> <span class="pl-c1">53</span>: i1IIi</td>
      </tr>
      <tr>
        <td id="L513" class="blob-num js-line-number" data-line-number="513"></td>
        <td id="LC513" class="blob-code blob-code-inner js-file-line"> o0OOOoO0 <span class="pl-k">=</span> { }</td>
      </tr>
      <tr>
        <td id="L514" class="blob-num js-line-number" data-line-number="514"></td>
        <td id="LC514" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">for</span> oOo0OOoO0 <span class="pl-k">in</span> servers :</td>
      </tr>
      <tr>
        <td id="L515" class="blob-num js-line-number" data-line-number="515"></td>
        <td id="LC515" class="blob-code blob-code-inner js-file-line">  o0OoOo00o0o <span class="pl-k">=</span> [ ]</td>
      </tr>
      <tr>
        <td id="L516" class="blob-num js-line-number" data-line-number="516"></td>
        <td id="LC516" class="blob-code blob-code-inner js-file-line">  O0OooOo0o <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/latency.txt<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> os . path . dirname ( oOo0OOoO0 [ <span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span> ] )</td>
      </tr>
      <tr>
        <td id="L517" class="blob-num js-line-number" data-line-number="517"></td>
        <td id="LC517" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">I1II1I11I1I</span> <span class="pl-k">=</span> urlparse ( O0OooOo0o )</td>
      </tr>
      <tr>
        <td id="L518" class="blob-num js-line-number" data-line-number="518"></td>
        <td id="LC518" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">for</span> <span class="pl-c1">OOOO</span> <span class="pl-k">in</span> <span class="pl-c1">range</span> ( <span class="pl-c1">0</span> , <span class="pl-c1">3</span> ) :</td>
      </tr>
      <tr>
        <td id="L519" class="blob-num js-line-number" data-line-number="519"></td>
        <td id="LC519" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L520" class="blob-num js-line-number" data-line-number="520"></td>
        <td id="LC520" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">I1II1I11I1I</span> [ <span class="pl-c1">0</span> ] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>https<span class="pl-pds">&#39;</span></span> :</td>
      </tr>
      <tr>
        <td id="L521" class="blob-num js-line-number" data-line-number="521"></td>
        <td id="LC521" class="blob-code blob-code-inner js-file-line">     OoOO0o <span class="pl-k">=</span> HTTPSConnection ( <span class="pl-c1">I1II1I11I1I</span> [ <span class="pl-c1">1</span> ] )</td>
      </tr>
      <tr>
        <td id="L522" class="blob-num js-line-number" data-line-number="522"></td>
        <td id="LC522" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span> :</td>
      </tr>
      <tr>
        <td id="L523" class="blob-num js-line-number" data-line-number="523"></td>
        <td id="LC523" class="blob-code blob-code-inner js-file-line">     OoOO0o <span class="pl-k">=</span> HTTPConnection ( <span class="pl-c1">I1II1I11I1I</span> [ <span class="pl-c1">1</span> ] )</td>
      </tr>
      <tr>
        <td id="L524" class="blob-num js-line-number" data-line-number="524"></td>
        <td id="LC524" class="blob-code blob-code-inner js-file-line">    i1II1 <span class="pl-k">=</span> { <span class="pl-s"><span class="pl-pds">&#39;</span>User-Agent<span class="pl-pds">&#39;</span></span> : iII111ii }</td>
      </tr>
      <tr>
        <td id="L525" class="blob-num js-line-number" data-line-number="525"></td>
        <td id="LC525" class="blob-code blob-code-inner js-file-line">    II111iiiI1Ii <span class="pl-k">=</span> timeit . default_timer ( )</td>
      </tr>
      <tr>
        <td id="L526" class="blob-num js-line-number" data-line-number="526"></td>
        <td id="LC526" class="blob-code blob-code-inner js-file-line">    OoOO0o . request ( <span class="pl-s"><span class="pl-pds">&quot;</span>GET<span class="pl-pds">&quot;</span></span> , <span class="pl-c1">I1II1I11I1I</span> [ <span class="pl-c1">2</span> ] , <span class="pl-v">headers</span> <span class="pl-k">=</span> i1II1 )</td>
      </tr>
      <tr>
        <td id="L527" class="blob-num js-line-number" data-line-number="527"></td>
        <td id="LC527" class="blob-code blob-code-inner js-file-line">    i11i1 <span class="pl-k">=</span> OoOO0o . getresponse ( )</td>
      </tr>
      <tr>
        <td id="L528" class="blob-num js-line-number" data-line-number="528"></td>
        <td id="LC528" class="blob-code blob-code-inner js-file-line">    IiiiiI1i1Iii <span class="pl-k">=</span> ( timeit . default_timer ( ) <span class="pl-k">-</span> II111iiiI1Ii )</td>
      </tr>
      <tr>
        <td id="L529" class="blob-num js-line-number" data-line-number="529"></td>
        <td id="LC529" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">except</span> ( HTTPError , URLError , socket . error ) :</td>
      </tr>
      <tr>
        <td id="L530" class="blob-num js-line-number" data-line-number="530"></td>
        <td id="LC530" class="blob-code blob-code-inner js-file-line">    o0OoOo00o0o . append ( <span class="pl-c1">3600</span> )</td>
      </tr>
      <tr>
        <td id="L531" class="blob-num js-line-number" data-line-number="531"></td>
        <td id="LC531" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L532" class="blob-num js-line-number" data-line-number="532"></td>
        <td id="LC532" class="blob-code blob-code-inner js-file-line">   oo00oO0o <span class="pl-k">=</span> i11i1 . read ( <span class="pl-c1">9</span> )</td>
      </tr>
      <tr>
        <td id="L533" class="blob-num js-line-number" data-line-number="533"></td>
        <td id="LC533" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">int</span> ( i11i1 . status ) <span class="pl-k">==</span> <span class="pl-c1">200</span> <span class="pl-k">and</span> oo00oO0o <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>test=test<span class="pl-pds">&#39;</span></span> . encode ( ) :</td>
      </tr>
      <tr>
        <td id="L534" class="blob-num js-line-number" data-line-number="534"></td>
        <td id="LC534" class="blob-code blob-code-inner js-file-line">    o0OoOo00o0o . append ( IiiiiI1i1Iii )</td>
      </tr>
      <tr>
        <td id="L535" class="blob-num js-line-number" data-line-number="535"></td>
        <td id="LC535" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">else</span> :</td>
      </tr>
      <tr>
        <td id="L536" class="blob-num js-line-number" data-line-number="536"></td>
        <td id="LC536" class="blob-code blob-code-inner js-file-line">    o0OoOo00o0o . append ( <span class="pl-c1">3600</span> )</td>
      </tr>
      <tr>
        <td id="L537" class="blob-num js-line-number" data-line-number="537"></td>
        <td id="LC537" class="blob-code blob-code-inner js-file-line">   OoOO0o . close ( )</td>
      </tr>
      <tr>
        <td id="L538" class="blob-num js-line-number" data-line-number="538"></td>
        <td id="LC538" class="blob-code blob-code-inner js-file-line">  iiii111II <span class="pl-k">=</span> <span class="pl-c1">round</span> ( ( <span class="pl-c1">sum</span> ( o0OoOo00o0o ) <span class="pl-k">/</span> <span class="pl-c1">6</span> ) <span class="pl-k">*</span> <span class="pl-c1">1000</span> , <span class="pl-c1">3</span> )</td>
      </tr>
      <tr>
        <td id="L539" class="blob-num js-line-number" data-line-number="539"></td>
        <td id="LC539" class="blob-code blob-code-inner js-file-line">  o0OOOoO0 [ iiii111II ] <span class="pl-k">=</span> oOo0OOoO0</td>
      </tr>
      <tr>
        <td id="L540" class="blob-num js-line-number" data-line-number="540"></td>
        <td id="LC540" class="blob-code blob-code-inner js-file-line"> I11iIiI1I1i11 <span class="pl-k">=</span> <span class="pl-c1">sorted</span> ( o0OOOoO0 . keys ( ) ) [ <span class="pl-c1">0</span> ]</td>
      </tr>
      <tr>
        <td id="L541" class="blob-num js-line-number" data-line-number="541"></td>
        <td id="LC541" class="blob-code blob-code-inner js-file-line"> OOoooO00o0oo0 <span class="pl-k">=</span> o0OOOoO0 [ I11iIiI1I1i11 ]</td>
      </tr>
      <tr>
        <td id="L542" class="blob-num js-line-number" data-line-number="542"></td>
        <td id="LC542" class="blob-code blob-code-inner js-file-line"> OOoooO00o0oo0 [ <span class="pl-s"><span class="pl-pds">&#39;</span>latency<span class="pl-pds">&#39;</span></span> ] <span class="pl-k">=</span> I11iIiI1I1i11</td>
      </tr>
      <tr>
        <td id="L543" class="blob-num js-line-number" data-line-number="543"></td>
        <td id="LC543" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">61</span> <span class="pl-k">-</span> <span class="pl-c1">61</span>: o00ooo0 <span class="pl-k">/</span> I1ii11iIi11i <span class="pl-k">%</span> Oo0oO0ooo <span class="pl-k">+</span> O0OOo <span class="pl-k">/</span> ooO00oOoo . O0OOo</td>
      </tr>
      <tr>
        <td id="L544" class="blob-num js-line-number" data-line-number="544"></td>
        <td id="LC544" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">return</span> OOoooO00o0oo0</td>
      </tr>
      <tr>
        <td id="L545" class="blob-num js-line-number" data-line-number="545"></td>
        <td id="LC545" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">12</span> <span class="pl-k">-</span> <span class="pl-c1">12</span>: i1IIi <span class="pl-k">+</span> i1IIi <span class="pl-k">-</span> I1ii11iIi11i <span class="pl-k">*</span> Oo0Ooo <span class="pl-k">%</span> Oo0Ooo <span class="pl-k">-</span> II111iiii</td>
      </tr>
      <tr>
        <td id="L546" class="blob-num js-line-number" data-line-number="546"></td>
        <td id="LC546" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">52</span> <span class="pl-k">-</span> <span class="pl-c1">52</span>: O0OOo . o00 <span class="pl-k">+</span> ooO00oOoo</td>
      </tr>
      <tr>
        <td id="L547" class="blob-num js-line-number" data-line-number="547"></td>
        <td id="LC547" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">iiii1IIi</span> ( <span class="pl-smi">signum</span> , <span class="pl-smi">frame</span> ) :</td>
      </tr>
      <tr>
        <td id="L548" class="blob-num js-line-number" data-line-number="548"></td>
        <td id="LC548" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">33</span> <span class="pl-k">-</span> <span class="pl-c1">33</span>: OoOoOO00 <span class="pl-k">*</span> Oo0ooO0oo0oO <span class="pl-k">-</span> II111iiii</td>
      </tr>
      <tr>
        <td id="L549" class="blob-num js-line-number" data-line-number="549"></td>
        <td id="LC549" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">83</span> <span class="pl-k">-</span> <span class="pl-c1">83</span>: OoOoOO00 <span class="pl-k">-</span> o00ooo0 <span class="pl-k">/</span> I1i1iI1i <span class="pl-k">/</span> ooO00oOoo <span class="pl-k">+</span> o0OO0 <span class="pl-k">-</span> O0</td>
      </tr>
      <tr>
        <td id="L550" class="blob-num js-line-number" data-line-number="550"></td>
        <td id="LC550" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">4</span> <span class="pl-k">-</span> <span class="pl-c1">4</span>: Oo0ooO0oo0oO <span class="pl-k">*</span> OoO0O00 <span class="pl-k">%</span> i1IIi <span class="pl-k">*</span> i11iIiiIii <span class="pl-k">%</span> Oo0Ooo <span class="pl-k">-</span> o0OO0</td>
      </tr>
      <tr>
        <td id="L551" class="blob-num js-line-number" data-line-number="551"></td>
        <td id="LC551" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">67</span> <span class="pl-k">-</span> <span class="pl-c1">67</span>: OoOoOO00 <span class="pl-k">+</span> I1ii11iIi11i . o0oOOo0O0Ooo . II111iiii</td>
      </tr>
      <tr>
        <td id="L552" class="blob-num js-line-number" data-line-number="552"></td>
        <td id="LC552" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">global</span> ii11iIi1I</td>
      </tr>
      <tr>
        <td id="L553" class="blob-num js-line-number" data-line-number="553"></td>
        <td id="LC553" class="blob-code blob-code-inner js-file-line"> ii11iIi1I . <span class="pl-c1">set</span> ( )</td>
      </tr>
      <tr>
        <td id="L554" class="blob-num js-line-number" data-line-number="554"></td>
        <td id="LC554" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">raise</span> <span class="pl-c1">SystemExit</span> ( <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span>Cancelling...<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L555" class="blob-num js-line-number" data-line-number="555"></td>
        <td id="LC555" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">98</span> <span class="pl-k">-</span> <span class="pl-c1">98</span>: o00</td>
      </tr>
      <tr>
        <td id="L556" class="blob-num js-line-number" data-line-number="556"></td>
        <td id="LC556" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">68</span> <span class="pl-k">-</span> <span class="pl-c1">68</span>: iIii1I11I1II1 <span class="pl-k">*</span> iIii1I11I1II1 . o0oOOo0O0Ooo <span class="pl-k">/</span> II111iiii <span class="pl-k">%</span> Oo0Ooo</td>
      </tr>
      <tr>
        <td id="L557" class="blob-num js-line-number" data-line-number="557"></td>
        <td id="LC557" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">38</span> <span class="pl-k">-</span> <span class="pl-c1">38</span>: O0OOo <span class="pl-k">-</span> Oo0ooO0oo0oO <span class="pl-k">/</span> o00</td>
      </tr>
      <tr>
        <td id="L558" class="blob-num js-line-number" data-line-number="558"></td>
        <td id="LC558" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">66</span> <span class="pl-k">-</span> <span class="pl-c1">66</span>: O0 <span class="pl-k">%</span> I1ii11iIi11i <span class="pl-k">+</span> i11iIiiIii . OoOoOO00 <span class="pl-k">/</span> o00ooo0 <span class="pl-k">+</span> I1ii11iIi11i</td>
      </tr>
      <tr>
        <td id="L559" class="blob-num js-line-number" data-line-number="559"></td>
        <td id="LC559" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">86</span> <span class="pl-k">-</span> <span class="pl-c1">86</span>: o0oOOo0O0Ooo</td>
      </tr>
      <tr>
        <td id="L560" class="blob-num js-line-number" data-line-number="560"></td>
        <td id="LC560" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">5</span> <span class="pl-k">-</span> <span class="pl-c1">5</span>: Oo0oO0ooo <span class="pl-k">*</span> OoOoOO00</td>
      </tr>
      <tr>
        <td id="L561" class="blob-num js-line-number" data-line-number="561"></td>
        <td id="LC561" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">i1Ii1i1I11Iii</span> ( <span class="pl-smi">list</span> <span class="pl-k">=</span> <span class="pl-c1">False</span> , <span class="pl-smi">mini</span> <span class="pl-k">=</span> <span class="pl-c1">None</span> , <span class="pl-smi">server</span> <span class="pl-k">=</span> <span class="pl-c1">None</span> , <span class="pl-smi">share</span> <span class="pl-k">=</span> <span class="pl-c1">False</span> , <span class="pl-smi">simple</span> <span class="pl-k">=</span> <span class="pl-c1">False</span> , <span class="pl-smi">src</span> <span class="pl-k">=</span> <span class="pl-c1">None</span> , <span class="pl-smi">timeout</span> <span class="pl-k">=</span> <span class="pl-c1">10</span> , <span class="pl-smi">units</span> <span class="pl-k">=</span> ( <span class="pl-s"><span class="pl-pds">&#39;</span>bit<span class="pl-pds">&#39;</span></span> , <span class="pl-c1">8</span> ) , <span class="pl-smi">version</span> <span class="pl-k">=</span> <span class="pl-c1">False</span> ) :</td>
      </tr>
      <tr>
        <td id="L562" class="blob-num js-line-number" data-line-number="562"></td>
        <td id="LC562" class="blob-code blob-code-inner js-file-line"> I1i1i1 <span class="pl-k">=</span> xbmcgui . DialogProgress ( )</td>
      </tr>
      <tr>
        <td id="L563" class="blob-num js-line-number" data-line-number="563"></td>
        <td id="LC563" class="blob-code blob-code-inner js-file-line"> OoO0O00O0oo0O <span class="pl-k">=</span> [ <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span> , <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span> , <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span> ]</td>
      </tr>
      <tr>
        <td id="L564" class="blob-num js-line-number" data-line-number="564"></td>
        <td id="LC564" class="blob-code blob-code-inner js-file-line"> I1i1i1 . create ( Iii1ii1II11i <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span> - Ookla speedtest.net<span class="pl-pds">&#39;</span></span> , OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] )</td>
      </tr>
      <tr>
        <td id="L565" class="blob-num js-line-number" data-line-number="565"></td>
        <td id="LC565" class="blob-code blob-code-inner js-file-line"> I1i1i1 . update ( <span class="pl-c1">0</span> , OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] )</td>
      </tr>
      <tr>
        <td id="L566" class="blob-num js-line-number" data-line-number="566"></td>
        <td id="LC566" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">36</span> <span class="pl-k">-</span> <span class="pl-c1">36</span>: Oo0ooO0oo0oO <span class="pl-k">+</span> O0 <span class="pl-k">-</span> o00ooo0 <span class="pl-k">-</span> O0 <span class="pl-k">%</span> I1i1iI1i . o0OO0</td>
      </tr>
      <tr>
        <td id="L567" class="blob-num js-line-number" data-line-number="567"></td>
        <td id="LC567" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">74</span> <span class="pl-k">-</span> <span class="pl-c1">74</span>: i11iIiiIii . I1IiiI</td>
      </tr>
      <tr>
        <td id="L568" class="blob-num js-line-number" data-line-number="568"></td>
        <td id="LC568" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">36</span> <span class="pl-k">-</span> <span class="pl-c1">36</span>: OoooooooOO . OoO0O00</td>
      </tr>
      <tr>
        <td id="L569" class="blob-num js-line-number" data-line-number="569"></td>
        <td id="LC569" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">global</span> ii11iIi1I , i1iIIi1</td>
      </tr>
      <tr>
        <td id="L570" class="blob-num js-line-number" data-line-number="570"></td>
        <td id="LC570" class="blob-code blob-code-inner js-file-line"> ii11iIi1I <span class="pl-k">=</span> threading . Event ( )</td>
      </tr>
      <tr>
        <td id="L571" class="blob-num js-line-number" data-line-number="571"></td>
        <td id="LC571" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">56</span> <span class="pl-k">-</span> <span class="pl-c1">56</span>: Oo0Ooo . I1ii11iIi11i . I1IiiI</td>
      </tr>
      <tr>
        <td id="L572" class="blob-num js-line-number" data-line-number="572"></td>
        <td id="LC572" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">39</span> <span class="pl-k">-</span> <span class="pl-c1">39</span>: O0 <span class="pl-k">+</span> ooO00oOoo</td>
      </tr>
      <tr>
        <td id="L573" class="blob-num js-line-number" data-line-number="573"></td>
        <td id="LC573" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">91</span> <span class="pl-k">-</span> <span class="pl-c1">91</span>: OoooooooOO <span class="pl-k">-</span> iIii1I11I1II1 <span class="pl-k">+</span> OoOoOO00 <span class="pl-k">/</span> OoO0O00 . OoOoOO00 <span class="pl-k">+</span> O0</td>
      </tr>
      <tr>
        <td id="L574" class="blob-num js-line-number" data-line-number="574"></td>
        <td id="LC574" class="blob-code blob-code-inner js-file-line"> iIiii1iI1 <span class="pl-k">=</span> (</td>
      </tr>
      <tr>
        <td id="L575" class="blob-num js-line-number" data-line-number="575"></td>
        <td id="LC575" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>Command line interface for testing internet bandwidth using <span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L576" class="blob-num js-line-number" data-line-number="576"></td>
        <td id="LC576" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>speedtest.net.<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L577" class="blob-num js-line-number" data-line-number="577"></td>
        <td id="LC577" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>------------------------------------------------------------<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L578" class="blob-num js-line-number" data-line-number="578"></td>
        <td id="LC578" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>--------------<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L579" class="blob-num js-line-number" data-line-number="579"></td>
        <td id="LC579" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>https://github.com/sivel/speedtest-cli<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L580" class="blob-num js-line-number" data-line-number="580"></td>
        <td id="LC580" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">33</span> <span class="pl-k">-</span> <span class="pl-c1">33</span>: Oo0oO0ooo <span class="pl-k">%</span> iIii1I11I1II1 <span class="pl-k">*</span> I1IiiI</td>
      </tr>
      <tr>
        <td id="L581" class="blob-num js-line-number" data-line-number="581"></td>
        <td id="LC581" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">95</span> <span class="pl-k">-</span> <span class="pl-c1">95</span>: O0OOo <span class="pl-k">/</span> O0OOo</td>
      </tr>
      <tr>
        <td id="L582" class="blob-num js-line-number" data-line-number="582"></td>
        <td id="LC582" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">30</span> <span class="pl-k">-</span> <span class="pl-c1">30</span>: I1ii11iIi11i <span class="pl-k">+</span> Oo0Ooo <span class="pl-k">/</span> Oo0Ooo <span class="pl-k">%</span> I1ii11iIi11i . I1ii11iIi11i</td>
      </tr>
      <tr>
        <td id="L583" class="blob-num js-line-number" data-line-number="583"></td>
        <td id="LC583" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> version :</td>
      </tr>
      <tr>
        <td id="L584" class="blob-num js-line-number" data-line-number="584"></td>
        <td id="LC584" class="blob-code blob-code-inner js-file-line">  version ( )</td>
      </tr>
      <tr>
        <td id="L585" class="blob-num js-line-number" data-line-number="585"></td>
        <td id="LC585" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">55</span> <span class="pl-k">-</span> <span class="pl-c1">55</span>: O0OOo <span class="pl-k">-</span> I1i1iI1i <span class="pl-k">+</span> II111iiii <span class="pl-k">+</span> o00 <span class="pl-k">%</span> o00ooo0</td>
      </tr>
      <tr>
        <td id="L586" class="blob-num js-line-number" data-line-number="586"></td>
        <td id="LC586" class="blob-code blob-code-inner js-file-line"> socket . setdefaulttimeout ( timeout )</td>
      </tr>
      <tr>
        <td id="L587" class="blob-num js-line-number" data-line-number="587"></td>
        <td id="LC587" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">41</span> <span class="pl-k">-</span> <span class="pl-c1">41</span>: i1IIi <span class="pl-k">-</span> I1i1iI1i <span class="pl-k">-</span> o00ooo0</td>
      </tr>
      <tr>
        <td id="L588" class="blob-num js-line-number" data-line-number="588"></td>
        <td id="LC588" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">8</span> <span class="pl-k">-</span> <span class="pl-c1">8</span>: OoO0O00 <span class="pl-k">+</span> ooO00oOoo <span class="pl-k">-</span> o0oOOo0O0Ooo <span class="pl-k">%</span> Oo0Ooo <span class="pl-k">%</span> o0oOOo0O0Ooo <span class="pl-k">*</span> o0OO0</td>
      </tr>
      <tr>
        <td id="L589" class="blob-num js-line-number" data-line-number="589"></td>
        <td id="LC589" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> src :</td>
      </tr>
      <tr>
        <td id="L590" class="blob-num js-line-number" data-line-number="590"></td>
        <td id="LC590" class="blob-code blob-code-inner js-file-line">  i1iIIi1 <span class="pl-k">=</span> src</td>
      </tr>
      <tr>
        <td id="L591" class="blob-num js-line-number" data-line-number="591"></td>
        <td id="LC591" class="blob-code blob-code-inner js-file-line">  socket . socket <span class="pl-k">=</span> <span class="pl-c1">II1III</span></td>
      </tr>
      <tr>
        <td id="L592" class="blob-num js-line-number" data-line-number="592"></td>
        <td id="LC592" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">9</span> <span class="pl-k">-</span> <span class="pl-c1">9</span>: Oo0Ooo <span class="pl-k">-</span> i11iIiiIii <span class="pl-k">-</span> Oo0ooO0oo0oO <span class="pl-k">*</span> o00ooo0 <span class="pl-k">+</span> O0OOo</td>
      </tr>
      <tr>
        <td id="L593" class="blob-num js-line-number" data-line-number="593"></td>
        <td id="LC593" class="blob-code blob-code-inner js-file-line"> OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Recupero configurazione da speedtest.net...<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L594" class="blob-num js-line-number" data-line-number="594"></td>
        <td id="LC594" class="blob-code blob-code-inner js-file-line"> I1i1i1 . update ( <span class="pl-c1">10</span> , OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] )</td>
      </tr>
      <tr>
        <td id="L595" class="blob-num js-line-number" data-line-number="595"></td>
        <td id="LC595" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-k">not</span> simple :</td>
      </tr>
      <tr>
        <td id="L596" class="blob-num js-line-number" data-line-number="596"></td>
        <td id="LC596" class="blob-code blob-code-inner js-file-line">  Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Recupero configurazione da speedtest.net...<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L597" class="blob-num js-line-number" data-line-number="597"></td>
        <td id="LC597" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L598" class="blob-num js-line-number" data-line-number="598"></td>
        <td id="LC598" class="blob-code blob-code-inner js-file-line">  OOoO <span class="pl-k">=</span> O0oO ( )</td>
      </tr>
      <tr>
        <td id="L599" class="blob-num js-line-number" data-line-number="599"></td>
        <td id="LC599" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">except</span> URLError :</td>
      </tr>
      <tr>
        <td id="L600" class="blob-num js-line-number" data-line-number="600"></td>
        <td id="LC600" class="blob-code blob-code-inner js-file-line">  I1i1i1 . close ( )</td>
      </tr>
      <tr>
        <td id="L601" class="blob-num js-line-number" data-line-number="601"></td>
        <td id="LC601" class="blob-code blob-code-inner js-file-line">  Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Cannot retrieve speedtest configuration<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L602" class="blob-num js-line-number" data-line-number="602"></td>
        <td id="LC602" class="blob-code blob-code-inner js-file-line">  sys . <span class="pl-c1">exit</span> ( <span class="pl-c1">1</span> )</td>
      </tr>
      <tr>
        <td id="L603" class="blob-num js-line-number" data-line-number="603"></td>
        <td id="LC603" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">44</span> <span class="pl-k">-</span> <span class="pl-c1">44</span>: II111iiii</td>
      </tr>
      <tr>
        <td id="L604" class="blob-num js-line-number" data-line-number="604"></td>
        <td id="LC604" class="blob-code blob-code-inner js-file-line"> OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Recupero la lista dei server speedtest.net...<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L605" class="blob-num js-line-number" data-line-number="605"></td>
        <td id="LC605" class="blob-code blob-code-inner js-file-line"> I1i1i1 . update ( <span class="pl-c1">15</span> , OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] )</td>
      </tr>
      <tr>
        <td id="L606" class="blob-num js-line-number" data-line-number="606"></td>
        <td id="LC606" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-k">not</span> simple :</td>
      </tr>
      <tr>
        <td id="L607" class="blob-num js-line-number" data-line-number="607"></td>
        <td id="LC607" class="blob-code blob-code-inner js-file-line">  Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Recupero la lista dei server speedtest.net...<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L608" class="blob-num js-line-number" data-line-number="608"></td>
        <td id="LC608" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">list</span> <span class="pl-k">or</span> server :</td>
      </tr>
      <tr>
        <td id="L609" class="blob-num js-line-number" data-line-number="609"></td>
        <td id="LC609" class="blob-code blob-code-inner js-file-line">  Oo0OO <span class="pl-k">=</span> oO00oOOoooO ( OOoO [ <span class="pl-s"><span class="pl-pds">&#39;</span>client<span class="pl-pds">&#39;</span></span> ] , <span class="pl-c1">True</span> )</td>
      </tr>
      <tr>
        <td id="L610" class="blob-num js-line-number" data-line-number="610"></td>
        <td id="LC610" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">list</span> :</td>
      </tr>
      <tr>
        <td id="L611" class="blob-num js-line-number" data-line-number="611"></td>
        <td id="LC611" class="blob-code blob-code-inner js-file-line">   <span class="pl-c1">OOOO0OOO</span> <span class="pl-k">=</span> [ ]</td>
      </tr>
      <tr>
        <td id="L612" class="blob-num js-line-number" data-line-number="612"></td>
        <td id="LC612" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">for</span> server <span class="pl-k">in</span> Oo0OO :</td>
      </tr>
      <tr>
        <td id="L613" class="blob-num js-line-number" data-line-number="613"></td>
        <td id="LC613" class="blob-code blob-code-inner js-file-line">    i1i1ii <span class="pl-k">=</span> ( <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%(id)4s</span>) <span class="pl-c1">%(sponsor)s</span> (<span class="pl-c1">%(name)s</span>, <span class="pl-c1">%(country)s</span>) <span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L614" class="blob-num js-line-number" data-line-number="614"></td>
        <td id="LC614" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>[<span class="pl-c1">%(d)0.2f</span> km]<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> server )</td>
      </tr>
      <tr>
        <td id="L615" class="blob-num js-line-number" data-line-number="615"></td>
        <td id="LC615" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">OOOO0OOO</span> . append ( i1i1ii )</td>
      </tr>
      <tr>
        <td id="L616" class="blob-num js-line-number" data-line-number="616"></td>
        <td id="LC616" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">46</span> <span class="pl-k">-</span> <span class="pl-c1">46</span>: OoOoOO00 <span class="pl-k">+</span> OoO0O00</td>
      </tr>
      <tr>
        <td id="L617" class="blob-num js-line-number" data-line-number="617"></td>
        <td id="LC617" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">70</span> <span class="pl-k">-</span> <span class="pl-c1">70</span>: o00 <span class="pl-k">/</span> iIii1I11I1II1</td>
      </tr>
      <tr>
        <td id="L618" class="blob-num js-line-number" data-line-number="618"></td>
        <td id="LC618" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">85</span> <span class="pl-k">-</span> <span class="pl-c1">85</span>: OoooooooOO <span class="pl-k">%</span> i1IIi <span class="pl-k">*</span> OoooooooOO <span class="pl-k">/</span> I1ii11iIi11i</td>
      </tr>
      <tr>
        <td id="L619" class="blob-num js-line-number" data-line-number="619"></td>
        <td id="LC619" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L620" class="blob-num js-line-number" data-line-number="620"></td>
        <td id="LC620" class="blob-code blob-code-inner js-file-line">    <span class="pl-v">unicode</span> ( )</td>
      </tr>
      <tr>
        <td id="L621" class="blob-num js-line-number" data-line-number="621"></td>
        <td id="LC621" class="blob-code blob-code-inner js-file-line">    Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span> . join ( <span class="pl-c1">OOOO0OOO</span> ) . encode ( <span class="pl-s"><span class="pl-pds">&#39;</span>utf-8<span class="pl-pds">&#39;</span></span> , <span class="pl-s"><span class="pl-pds">&#39;</span>ignore<span class="pl-pds">&#39;</span></span> ) )</td>
      </tr>
      <tr>
        <td id="L622" class="blob-num js-line-number" data-line-number="622"></td>
        <td id="LC622" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">except</span> <span class="pl-c1">NameError</span> :</td>
      </tr>
      <tr>
        <td id="L623" class="blob-num js-line-number" data-line-number="623"></td>
        <td id="LC623" class="blob-code blob-code-inner js-file-line">    Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span> . join ( <span class="pl-c1">OOOO0OOO</span> ) )</td>
      </tr>
      <tr>
        <td id="L624" class="blob-num js-line-number" data-line-number="624"></td>
        <td id="LC624" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">except</span> <span class="pl-c1">IOError</span> :</td>
      </tr>
      <tr>
        <td id="L625" class="blob-num js-line-number" data-line-number="625"></td>
        <td id="LC625" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L626" class="blob-num js-line-number" data-line-number="626"></td>
        <td id="LC626" class="blob-code blob-code-inner js-file-line">   sys . <span class="pl-c1">exit</span> ( <span class="pl-c1">0</span> )</td>
      </tr>
      <tr>
        <td id="L627" class="blob-num js-line-number" data-line-number="627"></td>
        <td id="LC627" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">else</span> :</td>
      </tr>
      <tr>
        <td id="L628" class="blob-num js-line-number" data-line-number="628"></td>
        <td id="LC628" class="blob-code blob-code-inner js-file-line">  Oo0OO <span class="pl-k">=</span> oO00oOOoooO ( OOoO [ <span class="pl-s"><span class="pl-pds">&#39;</span>client<span class="pl-pds">&#39;</span></span> ] )</td>
      </tr>
      <tr>
        <td id="L629" class="blob-num js-line-number" data-line-number="629"></td>
        <td id="LC629" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">96</span> <span class="pl-k">-</span> <span class="pl-c1">96</span>: OoooooooOO <span class="pl-k">+</span> o0OO0</td>
      </tr>
      <tr>
        <td id="L630" class="blob-num js-line-number" data-line-number="630"></td>
        <td id="LC630" class="blob-code blob-code-inner js-file-line"> OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Fornitore servizio internet --&gt; <span class="pl-c1">%(isp)s</span> (<span class="pl-c1">%(ip)s</span>)<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> OOoO [ <span class="pl-s"><span class="pl-pds">&#39;</span>client<span class="pl-pds">&#39;</span></span> ]</td>
      </tr>
      <tr>
        <td id="L631" class="blob-num js-line-number" data-line-number="631"></td>
        <td id="LC631" class="blob-code blob-code-inner js-file-line"> I1i1i1 . update ( <span class="pl-c1">25</span> , OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] )</td>
      </tr>
      <tr>
        <td id="L632" class="blob-num js-line-number" data-line-number="632"></td>
        <td id="LC632" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-k">not</span> simple :</td>
      </tr>
      <tr>
        <td id="L633" class="blob-num js-line-number" data-line-number="633"></td>
        <td id="LC633" class="blob-code blob-code-inner js-file-line">  Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Fornitore servizio internet <span class="pl-c1">%(isp)s</span> (<span class="pl-c1">%(ip)s</span>)...<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> OOoO [ <span class="pl-s"><span class="pl-pds">&#39;</span>client<span class="pl-pds">&#39;</span></span> ] )</td>
      </tr>
      <tr>
        <td id="L634" class="blob-num js-line-number" data-line-number="634"></td>
        <td id="LC634" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">44</span> <span class="pl-k">-</span> <span class="pl-c1">44</span>: o0OO0</td>
      </tr>
      <tr>
        <td id="L635" class="blob-num js-line-number" data-line-number="635"></td>
        <td id="LC635" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> server :</td>
      </tr>
      <tr>
        <td id="L636" class="blob-num js-line-number" data-line-number="636"></td>
        <td id="LC636" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L637" class="blob-num js-line-number" data-line-number="637"></td>
        <td id="LC637" class="blob-code blob-code-inner js-file-line">   OOoooO00o0oo0 <span class="pl-k">=</span> i11ii1iI ( <span class="pl-c1">filter</span> ( <span class="pl-k">lambda</span> <span class="pl-smi">I1i11i</span> : I1i11i [ <span class="pl-s"><span class="pl-pds">&#39;</span>id<span class="pl-pds">&#39;</span></span> ] <span class="pl-k">==</span> server ,</td>
      </tr>
      <tr>
        <td id="L638" class="blob-num js-line-number" data-line-number="638"></td>
        <td id="LC638" class="blob-code blob-code-inner js-file-line"> Oo0OO ) )</td>
      </tr>
      <tr>
        <td id="L639" class="blob-num js-line-number" data-line-number="639"></td>
        <td id="LC639" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">except</span> <span class="pl-c1">IndexError</span> :</td>
      </tr>
      <tr>
        <td id="L640" class="blob-num js-line-number" data-line-number="640"></td>
        <td id="LC640" class="blob-code blob-code-inner js-file-line">   I1i1i1 . close ( )</td>
      </tr>
      <tr>
        <td id="L641" class="blob-num js-line-number" data-line-number="641"></td>
        <td id="LC641" class="blob-code blob-code-inner js-file-line">   Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Invalid server ID<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L642" class="blob-num js-line-number" data-line-number="642"></td>
        <td id="LC642" class="blob-code blob-code-inner js-file-line">   sys . <span class="pl-c1">exit</span> ( <span class="pl-c1">1</span> )</td>
      </tr>
      <tr>
        <td id="L643" class="blob-num js-line-number" data-line-number="643"></td>
        <td id="LC643" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">elif</span> mini :</td>
      </tr>
      <tr>
        <td id="L644" class="blob-num js-line-number" data-line-number="644"></td>
        <td id="LC644" class="blob-code blob-code-inner js-file-line">  IiIi , <span class="pl-c1">OOOOO0O00</span> <span class="pl-k">=</span> os . path . splitext ( mini )</td>
      </tr>
      <tr>
        <td id="L645" class="blob-num js-line-number" data-line-number="645"></td>
        <td id="LC645" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">OOOOO0O00</span> :</td>
      </tr>
      <tr>
        <td id="L646" class="blob-num js-line-number" data-line-number="646"></td>
        <td id="LC646" class="blob-code blob-code-inner js-file-line">   O0OooOo0o <span class="pl-k">=</span> os . path . dirname ( mini )</td>
      </tr>
      <tr>
        <td id="L647" class="blob-num js-line-number" data-line-number="647"></td>
        <td id="LC647" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">else</span> :</td>
      </tr>
      <tr>
        <td id="L648" class="blob-num js-line-number" data-line-number="648"></td>
        <td id="LC648" class="blob-code blob-code-inner js-file-line">   O0OooOo0o <span class="pl-k">=</span> mini</td>
      </tr>
      <tr>
        <td id="L649" class="blob-num js-line-number" data-line-number="649"></td>
        <td id="LC649" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">I1II1I11I1I</span> <span class="pl-k">=</span> urlparse ( O0OooOo0o )</td>
      </tr>
      <tr>
        <td id="L650" class="blob-num js-line-number" data-line-number="650"></td>
        <td id="LC650" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L651" class="blob-num js-line-number" data-line-number="651"></td>
        <td id="LC651" class="blob-code blob-code-inner js-file-line">   iIIiIi1iIII1 <span class="pl-k">=</span> O0oOO0 ( mini )</td>
      </tr>
      <tr>
        <td id="L652" class="blob-num js-line-number" data-line-number="652"></td>
        <td id="LC652" class="blob-code blob-code-inner js-file-line">   OooOOOOo <span class="pl-k">=</span> urlopen ( iIIiIi1iIII1 )</td>
      </tr>
      <tr>
        <td id="L653" class="blob-num js-line-number" data-line-number="653"></td>
        <td id="LC653" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">except</span> :</td>
      </tr>
      <tr>
        <td id="L654" class="blob-num js-line-number" data-line-number="654"></td>
        <td id="LC654" class="blob-code blob-code-inner js-file-line">   Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Invalid Speedtest Mini URL<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L655" class="blob-num js-line-number" data-line-number="655"></td>
        <td id="LC655" class="blob-code blob-code-inner js-file-line">   sys . <span class="pl-c1">exit</span> ( <span class="pl-c1">1</span> )</td>
      </tr>
      <tr>
        <td id="L656" class="blob-num js-line-number" data-line-number="656"></td>
        <td id="LC656" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">else</span> :</td>
      </tr>
      <tr>
        <td id="L657" class="blob-num js-line-number" data-line-number="657"></td>
        <td id="LC657" class="blob-code blob-code-inner js-file-line">   oo00oO0o <span class="pl-k">=</span> OooOOOOo . read ( )</td>
      </tr>
      <tr>
        <td id="L658" class="blob-num js-line-number" data-line-number="658"></td>
        <td id="LC658" class="blob-code blob-code-inner js-file-line">   OooOOOOo . close ( )</td>
      </tr>
      <tr>
        <td id="L659" class="blob-num js-line-number" data-line-number="659"></td>
        <td id="LC659" class="blob-code blob-code-inner js-file-line">  Iii <span class="pl-k">=</span> re . findall ( <span class="pl-s"><span class="pl-pds">&#39;</span>upload_extension: &quot;([^&quot;]+)&quot;<span class="pl-pds">&#39;</span></span> , oo00oO0o . decode ( ) )</td>
      </tr>
      <tr>
        <td id="L660" class="blob-num js-line-number" data-line-number="660"></td>
        <td id="LC660" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-k">not</span> Iii :</td>
      </tr>
      <tr>
        <td id="L661" class="blob-num js-line-number" data-line-number="661"></td>
        <td id="LC661" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">for</span> <span class="pl-c1">OOOOO0O00</span> <span class="pl-k">in</span> [ <span class="pl-s"><span class="pl-pds">&#39;</span>php<span class="pl-pds">&#39;</span></span> , <span class="pl-s"><span class="pl-pds">&#39;</span>asp<span class="pl-pds">&#39;</span></span> , <span class="pl-s"><span class="pl-pds">&#39;</span>aspx<span class="pl-pds">&#39;</span></span> , <span class="pl-s"><span class="pl-pds">&#39;</span>jsp<span class="pl-pds">&#39;</span></span> ] :</td>
      </tr>
      <tr>
        <td id="L662" class="blob-num js-line-number" data-line-number="662"></td>
        <td id="LC662" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L663" class="blob-num js-line-number" data-line-number="663"></td>
        <td id="LC663" class="blob-code blob-code-inner js-file-line">     iIIiIi1iIII1 <span class="pl-k">=</span> O0oOO0 ( <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/speedtest/upload.<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span></td>
      </tr>
      <tr>
        <td id="L664" class="blob-num js-line-number" data-line-number="664"></td>
        <td id="LC664" class="blob-code blob-code-inner js-file-line"> ( mini , <span class="pl-c1">OOOOO0O00</span> ) )</td>
      </tr>
      <tr>
        <td id="L665" class="blob-num js-line-number" data-line-number="665"></td>
        <td id="LC665" class="blob-code blob-code-inner js-file-line">     OooOOOOo <span class="pl-k">=</span> urlopen ( iIIiIi1iIII1 )</td>
      </tr>
      <tr>
        <td id="L666" class="blob-num js-line-number" data-line-number="666"></td>
        <td id="LC666" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">except</span> :</td>
      </tr>
      <tr>
        <td id="L667" class="blob-num js-line-number" data-line-number="667"></td>
        <td id="LC667" class="blob-code blob-code-inner js-file-line">     <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L668" class="blob-num js-line-number" data-line-number="668"></td>
        <td id="LC668" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span> :</td>
      </tr>
      <tr>
        <td id="L669" class="blob-num js-line-number" data-line-number="669"></td>
        <td id="LC669" class="blob-code blob-code-inner js-file-line">     I1IiiiiI <span class="pl-k">=</span> OooOOOOo . read ( ) . strip ( )</td>
      </tr>
      <tr>
        <td id="L670" class="blob-num js-line-number" data-line-number="670"></td>
        <td id="LC670" class="blob-code blob-code-inner js-file-line">     <span class="pl-k">if</span> ( OooOOOOo . code <span class="pl-k">==</span> <span class="pl-c1">200</span> <span class="pl-k">and</span></td>
      </tr>
      <tr>
        <td id="L671" class="blob-num js-line-number" data-line-number="671"></td>
        <td id="LC671" class="blob-code blob-code-inner js-file-line"> <span class="pl-c1">len</span> ( I1IiiiiI . splitlines ( ) ) <span class="pl-k">==</span> <span class="pl-c1">1</span> <span class="pl-k">and</span></td>
      </tr>
      <tr>
        <td id="L672" class="blob-num js-line-number" data-line-number="672"></td>
        <td id="LC672" class="blob-code blob-code-inner js-file-line"> re . match ( <span class="pl-s"><span class="pl-pds">&#39;</span>size=[0-9]<span class="pl-pds">&#39;</span></span> , I1IiiiiI ) ) :</td>
      </tr>
      <tr>
        <td id="L673" class="blob-num js-line-number" data-line-number="673"></td>
        <td id="LC673" class="blob-code blob-code-inner js-file-line">      Iii <span class="pl-k">=</span> [ <span class="pl-c1">OOOOO0O00</span> ]</td>
      </tr>
      <tr>
        <td id="L674" class="blob-num js-line-number" data-line-number="674"></td>
        <td id="LC674" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L675" class="blob-num js-line-number" data-line-number="675"></td>
        <td id="LC675" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">I1II1I11I1I</span> <span class="pl-k">or</span> <span class="pl-k">not</span> Iii :</td>
      </tr>
      <tr>
        <td id="L676" class="blob-num js-line-number" data-line-number="676"></td>
        <td id="LC676" class="blob-code blob-code-inner js-file-line">   Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Please provide the full URL of your Speedtest Mini server<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L677" class="blob-num js-line-number" data-line-number="677"></td>
        <td id="LC677" class="blob-code blob-code-inner js-file-line">   sys . <span class="pl-c1">exit</span> ( <span class="pl-c1">1</span> )</td>
      </tr>
      <tr>
        <td id="L678" class="blob-num js-line-number" data-line-number="678"></td>
        <td id="LC678" class="blob-code blob-code-inner js-file-line">  Oo0OO <span class="pl-k">=</span> [ {</td>
      </tr>
      <tr>
        <td id="L679" class="blob-num js-line-number" data-line-number="679"></td>
        <td id="LC679" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>sponsor<span class="pl-pds">&#39;</span></span> : <span class="pl-s"><span class="pl-pds">&#39;</span>Speedtest Mini<span class="pl-pds">&#39;</span></span> ,</td>
      </tr>
      <tr>
        <td id="L680" class="blob-num js-line-number" data-line-number="680"></td>
        <td id="LC680" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">I1II1I11I1I</span> [ <span class="pl-c1">1</span> ] ,</td>
      </tr>
      <tr>
        <td id="L681" class="blob-num js-line-number" data-line-number="681"></td>
        <td id="LC681" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>d<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">0</span> ,</td>
      </tr>
      <tr>
        <td id="L682" class="blob-num js-line-number" data-line-number="682"></td>
        <td id="LC682" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span> : <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/speedtest/upload.<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> ( O0OooOo0o . rstrip ( <span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span> ) , Iii [ <span class="pl-c1">0</span> ] ) ,</td>
      </tr>
      <tr>
        <td id="L683" class="blob-num js-line-number" data-line-number="683"></td>
        <td id="LC683" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>latency<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">0</span> ,</td>
      </tr>
      <tr>
        <td id="L684" class="blob-num js-line-number" data-line-number="684"></td>
        <td id="LC684" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>id<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L685" class="blob-num js-line-number" data-line-number="685"></td>
        <td id="LC685" class="blob-code blob-code-inner js-file-line"> } ]</td>
      </tr>
      <tr>
        <td id="L686" class="blob-num js-line-number" data-line-number="686"></td>
        <td id="LC686" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L687" class="blob-num js-line-number" data-line-number="687"></td>
        <td id="LC687" class="blob-code blob-code-inner js-file-line">   OOoooO00o0oo0 <span class="pl-k">=</span> i11ii1iI ( Oo0OO )</td>
      </tr>
      <tr>
        <td id="L688" class="blob-num js-line-number" data-line-number="688"></td>
        <td id="LC688" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">except</span> :</td>
      </tr>
      <tr>
        <td id="L689" class="blob-num js-line-number" data-line-number="689"></td>
        <td id="LC689" class="blob-code blob-code-inner js-file-line">   OOoooO00o0oo0 <span class="pl-k">=</span> Oo0OO [ <span class="pl-c1">0</span> ]</td>
      </tr>
      <tr>
        <td id="L690" class="blob-num js-line-number" data-line-number="690"></td>
        <td id="LC690" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">else</span> :</td>
      </tr>
      <tr>
        <td id="L691" class="blob-num js-line-number" data-line-number="691"></td>
        <td id="LC691" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-k">not</span> simple :</td>
      </tr>
      <tr>
        <td id="L692" class="blob-num js-line-number" data-line-number="692"></td>
        <td id="LC692" class="blob-code blob-code-inner js-file-line">   OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] <span class="pl-k">=</span> OoO0O00O0oo0O [ <span class="pl-c1">1</span> ]</td>
      </tr>
      <tr>
        <td id="L693" class="blob-num js-line-number" data-line-number="693"></td>
        <td id="LC693" class="blob-code blob-code-inner js-file-line">   OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] <span class="pl-k">=</span> OoO0O00O0oo0O [ <span class="pl-c1">2</span> ]</td>
      </tr>
      <tr>
        <td id="L694" class="blob-num js-line-number" data-line-number="694"></td>
        <td id="LC694" class="blob-code blob-code-inner js-file-line">   OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Selecting best server based on latency...<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L695" class="blob-num js-line-number" data-line-number="695"></td>
        <td id="LC695" class="blob-code blob-code-inner js-file-line">   I1i1i1 . update ( <span class="pl-c1">30</span> , OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] )</td>
      </tr>
      <tr>
        <td id="L696" class="blob-num js-line-number" data-line-number="696"></td>
        <td id="LC696" class="blob-code blob-code-inner js-file-line">   Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Selecting best server based on latency...<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L697" class="blob-num js-line-number" data-line-number="697"></td>
        <td id="LC697" class="blob-code blob-code-inner js-file-line">  OOoooO00o0oo0 <span class="pl-k">=</span> i11ii1iI ( Oo0OO )</td>
      </tr>
      <tr>
        <td id="L698" class="blob-num js-line-number" data-line-number="698"></td>
        <td id="LC698" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">31</span> <span class="pl-k">-</span> <span class="pl-c1">31</span>: o0oOOo0O0Ooo <span class="pl-k">%</span> OoO0O00</td>
      </tr>
      <tr>
        <td id="L699" class="blob-num js-line-number" data-line-number="699"></td>
        <td id="LC699" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-k">not</span> simple :</td>
      </tr>
      <tr>
        <td id="L700" class="blob-num js-line-number" data-line-number="700"></td>
        <td id="LC700" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">14</span> <span class="pl-k">-</span> <span class="pl-c1">14</span>: o0OO0 <span class="pl-k">/</span> o0OO0 <span class="pl-k">%</span> O0OOo</td>
      </tr>
      <tr>
        <td id="L701" class="blob-num js-line-number" data-line-number="701"></td>
        <td id="LC701" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">56</span> <span class="pl-k">-</span> <span class="pl-c1">56</span>: I1IiiI . O0 <span class="pl-k">+</span> Oo0Ooo</td>
      </tr>
      <tr>
        <td id="L702" class="blob-num js-line-number" data-line-number="702"></td>
        <td id="LC702" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">1</span> <span class="pl-k">-</span> <span class="pl-c1">1</span>: o00</td>
      </tr>
      <tr>
        <td id="L703" class="blob-num js-line-number" data-line-number="703"></td>
        <td id="LC703" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">try</span> :</td>
      </tr>
      <tr>
        <td id="L704" class="blob-num js-line-number" data-line-number="704"></td>
        <td id="LC704" class="blob-code blob-code-inner js-file-line">   <span class="pl-v">unicode</span> ( )</td>
      </tr>
      <tr>
        <td id="L705" class="blob-num js-line-number" data-line-number="705"></td>
        <td id="LC705" class="blob-code blob-code-inner js-file-line">   OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] <span class="pl-k">=</span> OoO0O00O0oo0O [ <span class="pl-c1">1</span> ]</td>
      </tr>
      <tr>
        <td id="L706" class="blob-num js-line-number" data-line-number="706"></td>
        <td id="LC706" class="blob-code blob-code-inner js-file-line">   OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] <span class="pl-k">=</span> OoO0O00O0oo0O [ <span class="pl-c1">2</span> ]</td>
      </tr>
      <tr>
        <td id="L707" class="blob-num js-line-number" data-line-number="707"></td>
        <td id="LC707" class="blob-code blob-code-inner js-file-line">   OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] <span class="pl-k">=</span> ( <span class="pl-s"><span class="pl-pds">&#39;</span>Hosted by <span class="pl-c1">%(sponsor)s</span> (<span class="pl-c1">%(name)s</span>) [<span class="pl-c1">%(d)0.2f</span> km]: <span class="pl-c1">%(latency)s</span> ms<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> OOoooO00o0oo0 ) . encode ( <span class="pl-s"><span class="pl-pds">&#39;</span>utf-8<span class="pl-pds">&#39;</span></span> , <span class="pl-s"><span class="pl-pds">&#39;</span>ignore<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L708" class="blob-num js-line-number" data-line-number="708"></td>
        <td id="LC708" class="blob-code blob-code-inner js-file-line">   I1i1i1 . update ( <span class="pl-c1">40</span> , OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] )</td>
      </tr>
      <tr>
        <td id="L709" class="blob-num js-line-number" data-line-number="709"></td>
        <td id="LC709" class="blob-code blob-code-inner js-file-line">   Ii11iI1i ( ( <span class="pl-s"><span class="pl-pds">&#39;</span>Hosted by <span class="pl-c1">%(sponsor)s</span> (<span class="pl-c1">%(name)s</span>) [<span class="pl-c1">%(d)0.2f</span> km]: <span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L710" class="blob-num js-line-number" data-line-number="710"></td>
        <td id="LC710" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%(latency)s</span> ms<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> OOoooO00o0oo0 ) . encode ( <span class="pl-s"><span class="pl-pds">&#39;</span>utf-8<span class="pl-pds">&#39;</span></span> , <span class="pl-s"><span class="pl-pds">&#39;</span>ignore<span class="pl-pds">&#39;</span></span> ) )</td>
      </tr>
      <tr>
        <td id="L711" class="blob-num js-line-number" data-line-number="711"></td>
        <td id="LC711" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">except</span> <span class="pl-c1">NameError</span> :</td>
      </tr>
      <tr>
        <td id="L712" class="blob-num js-line-number" data-line-number="712"></td>
        <td id="LC712" class="blob-code blob-code-inner js-file-line">   OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] <span class="pl-k">=</span> OoO0O00O0oo0O [ <span class="pl-c1">1</span> ]</td>
      </tr>
      <tr>
        <td id="L713" class="blob-num js-line-number" data-line-number="713"></td>
        <td id="LC713" class="blob-code blob-code-inner js-file-line">   OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] <span class="pl-k">=</span> OoO0O00O0oo0O [ <span class="pl-c1">2</span> ]</td>
      </tr>
      <tr>
        <td id="L714" class="blob-num js-line-number" data-line-number="714"></td>
        <td id="LC714" class="blob-code blob-code-inner js-file-line">   OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Hosted by <span class="pl-c1">%(sponsor)s</span> (<span class="pl-c1">%(name)s</span>) [<span class="pl-c1">%(d)0.2f</span> km]: <span class="pl-c1">%(latency)s</span> ms<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> OOoooO00o0oo0</td>
      </tr>
      <tr>
        <td id="L715" class="blob-num js-line-number" data-line-number="715"></td>
        <td id="LC715" class="blob-code blob-code-inner js-file-line">   I1i1i1 . update ( <span class="pl-c1">40</span> , OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] )</td>
      </tr>
      <tr>
        <td id="L716" class="blob-num js-line-number" data-line-number="716"></td>
        <td id="LC716" class="blob-code blob-code-inner js-file-line">   Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Hosted by <span class="pl-c1">%(sponsor)s</span> (<span class="pl-c1">%(name)s</span>) [<span class="pl-c1">%(d)0.2f</span> km]: <span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L717" class="blob-num js-line-number" data-line-number="717"></td>
        <td id="LC717" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%(latency)s</span> ms<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> OOoooO00o0oo0 )</td>
      </tr>
      <tr>
        <td id="L718" class="blob-num js-line-number" data-line-number="718"></td>
        <td id="LC718" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">else</span> :</td>
      </tr>
      <tr>
        <td id="L719" class="blob-num js-line-number" data-line-number="719"></td>
        <td id="LC719" class="blob-code blob-code-inner js-file-line">  OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] <span class="pl-k">=</span> OoO0O00O0oo0O [ <span class="pl-c1">1</span> ]</td>
      </tr>
      <tr>
        <td id="L720" class="blob-num js-line-number" data-line-number="720"></td>
        <td id="LC720" class="blob-code blob-code-inner js-file-line">  OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] <span class="pl-k">=</span> OoO0O00O0oo0O [ <span class="pl-c1">2</span> ]</td>
      </tr>
      <tr>
        <td id="L721" class="blob-num js-line-number" data-line-number="721"></td>
        <td id="LC721" class="blob-code blob-code-inner js-file-line">  OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Ping: <span class="pl-c1">%(latency)s</span> ms<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> OOoooO00o0oo0</td>
      </tr>
      <tr>
        <td id="L722" class="blob-num js-line-number" data-line-number="722"></td>
        <td id="LC722" class="blob-code blob-code-inner js-file-line">  I1i1i1 . update ( <span class="pl-c1">40</span> , OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] )</td>
      </tr>
      <tr>
        <td id="L723" class="blob-num js-line-number" data-line-number="723"></td>
        <td id="LC723" class="blob-code blob-code-inner js-file-line">  Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Ping: <span class="pl-c1">%(latency)s</span> ms<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> OOoooO00o0oo0 )</td>
      </tr>
      <tr>
        <td id="L724" class="blob-num js-line-number" data-line-number="724"></td>
        <td id="LC724" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">97</span> <span class="pl-k">-</span> <span class="pl-c1">97</span>: Oo0ooO0oo0oO <span class="pl-k">+</span> o00 <span class="pl-k">+</span> O0 <span class="pl-k">+</span> i11iIiiIii</td>
      </tr>
      <tr>
        <td id="L725" class="blob-num js-line-number" data-line-number="725"></td>
        <td id="LC725" class="blob-code blob-code-inner js-file-line"> oOoO0 <span class="pl-k">=</span> [ <span class="pl-c1">350</span> , <span class="pl-c1">500</span> , <span class="pl-c1">750</span> , <span class="pl-c1">1000</span> , <span class="pl-c1">1500</span> , <span class="pl-c1">2000</span> , <span class="pl-c1">2500</span> , <span class="pl-c1">3000</span> , <span class="pl-c1">3500</span> , <span class="pl-c1">4000</span> ]</td>
      </tr>
      <tr>
        <td id="L726" class="blob-num js-line-number" data-line-number="726"></td>
        <td id="LC726" class="blob-code blob-code-inner js-file-line"> iI1111iiii <span class="pl-k">=</span> [ ]</td>
      </tr>
      <tr>
        <td id="L727" class="blob-num js-line-number" data-line-number="727"></td>
        <td id="LC727" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">for</span> OOo0oO00ooO00 <span class="pl-k">in</span> oOoO0 :</td>
      </tr>
      <tr>
        <td id="L728" class="blob-num js-line-number" data-line-number="728"></td>
        <td id="LC728" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">for</span> <span class="pl-c1">OOOO</span> <span class="pl-k">in</span> <span class="pl-c1">range</span> ( <span class="pl-c1">0</span> , <span class="pl-c1">4</span> ) :</td>
      </tr>
      <tr>
        <td id="L729" class="blob-num js-line-number" data-line-number="729"></td>
        <td id="LC729" class="blob-code blob-code-inner js-file-line">   iI1111iiii . append ( <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>/random<span class="pl-c1">%s</span>x<span class="pl-c1">%s</span>.jpg<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span></td>
      </tr>
      <tr>
        <td id="L730" class="blob-num js-line-number" data-line-number="730"></td>
        <td id="LC730" class="blob-code blob-code-inner js-file-line"> ( os . path . dirname ( OOoooO00o0oo0 [ <span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span> ] ) , OOo0oO00ooO00 , OOo0oO00ooO00 ) )</td>
      </tr>
      <tr>
        <td id="L731" class="blob-num js-line-number" data-line-number="731"></td>
        <td id="LC731" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">77</span> <span class="pl-k">-</span> <span class="pl-c1">77</span>: iIii1I11I1II1 . o00 <span class="pl-k">%</span> o00 <span class="pl-k">+</span> i11iIiiIii</td>
      </tr>
      <tr>
        <td id="L732" class="blob-num js-line-number" data-line-number="732"></td>
        <td id="LC732" class="blob-code blob-code-inner js-file-line"> OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] <span class="pl-k">=</span> OoO0O00O0oo0O [ <span class="pl-c1">1</span> ]</td>
      </tr>
      <tr>
        <td id="L733" class="blob-num js-line-number" data-line-number="733"></td>
        <td id="LC733" class="blob-code blob-code-inner js-file-line"> OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] <span class="pl-k">=</span> OoO0O00O0oo0O [ <span class="pl-c1">2</span> ]</td>
      </tr>
      <tr>
        <td id="L734" class="blob-num js-line-number" data-line-number="734"></td>
        <td id="LC734" class="blob-code blob-code-inner js-file-line"> OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Testando le prestazioni in download...<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L735" class="blob-num js-line-number" data-line-number="735"></td>
        <td id="LC735" class="blob-code blob-code-inner js-file-line"> I1i1i1 . update ( <span class="pl-c1">50</span> , OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] )</td>
      </tr>
      <tr>
        <td id="L736" class="blob-num js-line-number" data-line-number="736"></td>
        <td id="LC736" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-k">not</span> simple :</td>
      </tr>
      <tr>
        <td id="L737" class="blob-num js-line-number" data-line-number="737"></td>
        <td id="LC737" class="blob-code blob-code-inner js-file-line">  Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Testando le prestazioni in download...<span class="pl-pds">&#39;</span></span> , <span class="pl-v">end</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L738" class="blob-num js-line-number" data-line-number="738"></td>
        <td id="LC738" class="blob-code blob-code-inner js-file-line"> Oo00o0OO0O00o <span class="pl-k">=</span> i1iI11i1ii11 ( iI1111iiii , simple )</td>
      </tr>
      <tr>
        <td id="L739" class="blob-num js-line-number" data-line-number="739"></td>
        <td id="LC739" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-k">not</span> simple :</td>
      </tr>
      <tr>
        <td id="L740" class="blob-num js-line-number" data-line-number="740"></td>
        <td id="LC740" class="blob-code blob-code-inner js-file-line">  Ii11iI1i ( )</td>
      </tr>
      <tr>
        <td id="L741" class="blob-num js-line-number" data-line-number="741"></td>
        <td id="LC741" class="blob-code blob-code-inner js-file-line"> OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] <span class="pl-k">=</span> OoO0O00O0oo0O [ <span class="pl-c1">1</span> ]</td>
      </tr>
      <tr>
        <td id="L742" class="blob-num js-line-number" data-line-number="742"></td>
        <td id="LC742" class="blob-code blob-code-inner js-file-line"> OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] <span class="pl-k">=</span> OoO0O00O0oo0O [ <span class="pl-c1">2</span> ]</td>
      </tr>
      <tr>
        <td id="L743" class="blob-num js-line-number" data-line-number="743"></td>
        <td id="LC743" class="blob-code blob-code-inner js-file-line"> OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Download: <span class="pl-c1">%0.2f</span> M<span class="pl-c1">%s</span>/s<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> ( ( Oo00o0OO0O00o <span class="pl-k">/</span> <span class="pl-c1">1000</span> <span class="pl-k">/</span> <span class="pl-c1">1000</span> ) <span class="pl-k">*</span> units [ <span class="pl-c1">1</span> ] , units [ <span class="pl-c1">0</span> ] )</td>
      </tr>
      <tr>
        <td id="L744" class="blob-num js-line-number" data-line-number="744"></td>
        <td id="LC744" class="blob-code blob-code-inner js-file-line"> I1i1i1 . update ( <span class="pl-c1">70</span> , OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] )</td>
      </tr>
      <tr>
        <td id="L745" class="blob-num js-line-number" data-line-number="745"></td>
        <td id="LC745" class="blob-code blob-code-inner js-file-line"> Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Download: <span class="pl-c1">%0.2f</span> M<span class="pl-c1">%s</span>/s<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span></td>
      </tr>
      <tr>
        <td id="L746" class="blob-num js-line-number" data-line-number="746"></td>
        <td id="LC746" class="blob-code blob-code-inner js-file-line"> ( ( Oo00o0OO0O00o <span class="pl-k">/</span> <span class="pl-c1">1000</span> <span class="pl-k">/</span> <span class="pl-c1">1000</span> ) <span class="pl-k">*</span> units [ <span class="pl-c1">1</span> ] , units [ <span class="pl-c1">0</span> ] ) )</td>
      </tr>
      <tr>
        <td id="L747" class="blob-num js-line-number" data-line-number="747"></td>
        <td id="LC747" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">82</span> <span class="pl-k">-</span> <span class="pl-c1">82</span>: I1i1iI1i <span class="pl-k">+</span> OoooooooOO <span class="pl-k">-</span> i1IIi . i1IIi</td>
      </tr>
      <tr>
        <td id="L748" class="blob-num js-line-number" data-line-number="748"></td>
        <td id="LC748" class="blob-code blob-code-inner js-file-line"> iIi1i <span class="pl-k">=</span> [ <span class="pl-c1">int</span> ( <span class="pl-c1">.25</span> <span class="pl-k">*</span> <span class="pl-c1">1000</span> <span class="pl-k">*</span> <span class="pl-c1">1000</span> ) , <span class="pl-c1">int</span> ( <span class="pl-c1">.5</span> <span class="pl-k">*</span> <span class="pl-c1">1000</span> <span class="pl-k">*</span> <span class="pl-c1">1000</span> ) ]</td>
      </tr>
      <tr>
        <td id="L749" class="blob-num js-line-number" data-line-number="749"></td>
        <td id="LC749" class="blob-code blob-code-inner js-file-line"> oOoO0 <span class="pl-k">=</span> [ ]</td>
      </tr>
      <tr>
        <td id="L750" class="blob-num js-line-number" data-line-number="750"></td>
        <td id="LC750" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">for</span> OOo0oO00ooO00 <span class="pl-k">in</span> iIi1i :</td>
      </tr>
      <tr>
        <td id="L751" class="blob-num js-line-number" data-line-number="751"></td>
        <td id="LC751" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">for</span> <span class="pl-c1">OOOO</span> <span class="pl-k">in</span> <span class="pl-c1">range</span> ( <span class="pl-c1">0</span> , <span class="pl-c1">25</span> ) :</td>
      </tr>
      <tr>
        <td id="L752" class="blob-num js-line-number" data-line-number="752"></td>
        <td id="LC752" class="blob-code blob-code-inner js-file-line">   oOoO0 . append ( OOo0oO00ooO00 )</td>
      </tr>
      <tr>
        <td id="L753" class="blob-num js-line-number" data-line-number="753"></td>
        <td id="LC753" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">27</span> <span class="pl-k">-</span> <span class="pl-c1">27</span>: Oo0ooO0oo0oO <span class="pl-k">*</span> O0OOo . ooO00oOoo <span class="pl-k">%</span> Oo0oO0ooo <span class="pl-k">*</span> Oo0oO0ooo . i1IIi</td>
      </tr>
      <tr>
        <td id="L754" class="blob-num js-line-number" data-line-number="754"></td>
        <td id="LC754" class="blob-code blob-code-inner js-file-line"> OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] <span class="pl-k">=</span> OoO0O00O0oo0O [ <span class="pl-c1">1</span> ]</td>
      </tr>
      <tr>
        <td id="L755" class="blob-num js-line-number" data-line-number="755"></td>
        <td id="LC755" class="blob-code blob-code-inner js-file-line"> OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] <span class="pl-k">=</span> OoO0O00O0oo0O [ <span class="pl-c1">2</span> ]</td>
      </tr>
      <tr>
        <td id="L756" class="blob-num js-line-number" data-line-number="756"></td>
        <td id="LC756" class="blob-code blob-code-inner js-file-line"> OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Testando le prestazioni in upload...<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L757" class="blob-num js-line-number" data-line-number="757"></td>
        <td id="LC757" class="blob-code blob-code-inner js-file-line"> I1i1i1 . update ( <span class="pl-c1">80</span> , OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] )</td>
      </tr>
      <tr>
        <td id="L758" class="blob-num js-line-number" data-line-number="758"></td>
        <td id="LC758" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-k">not</span> simple :</td>
      </tr>
      <tr>
        <td id="L759" class="blob-num js-line-number" data-line-number="759"></td>
        <td id="LC759" class="blob-code blob-code-inner js-file-line">  Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Testando le prestazioni in upload...<span class="pl-pds">&#39;</span></span> , <span class="pl-v">end</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L760" class="blob-num js-line-number" data-line-number="760"></td>
        <td id="LC760" class="blob-code blob-code-inner js-file-line"> O0OOoOOO0oO <span class="pl-k">=</span> oO0OOOO0 ( OOoooO00o0oo0 [ <span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span> ] , oOoO0 , simple )</td>
      </tr>
      <tr>
        <td id="L761" class="blob-num js-line-number" data-line-number="761"></td>
        <td id="LC761" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-k">not</span> simple :</td>
      </tr>
      <tr>
        <td id="L762" class="blob-num js-line-number" data-line-number="762"></td>
        <td id="LC762" class="blob-code blob-code-inner js-file-line">  Ii11iI1i ( )</td>
      </tr>
      <tr>
        <td id="L763" class="blob-num js-line-number" data-line-number="763"></td>
        <td id="LC763" class="blob-code blob-code-inner js-file-line"> OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] <span class="pl-k">=</span> OoO0O00O0oo0O [ <span class="pl-c1">1</span> ]</td>
      </tr>
      <tr>
        <td id="L764" class="blob-num js-line-number" data-line-number="764"></td>
        <td id="LC764" class="blob-code blob-code-inner js-file-line"> OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] <span class="pl-k">=</span> OoO0O00O0oo0O [ <span class="pl-c1">2</span> ]</td>
      </tr>
      <tr>
        <td id="L765" class="blob-num js-line-number" data-line-number="765"></td>
        <td id="LC765" class="blob-code blob-code-inner js-file-line"> OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Upload: <span class="pl-c1">%0.2f</span> M<span class="pl-c1">%s</span>/s<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> ( ( O0OOoOOO0oO <span class="pl-k">/</span> <span class="pl-c1">1000</span> <span class="pl-k">/</span> <span class="pl-c1">1000</span> ) <span class="pl-k">*</span> units [ <span class="pl-c1">1</span> ] , units [ <span class="pl-c1">0</span> ] )</td>
      </tr>
      <tr>
        <td id="L766" class="blob-num js-line-number" data-line-number="766"></td>
        <td id="LC766" class="blob-code blob-code-inner js-file-line"> I1i1i1 . update ( <span class="pl-c1">99</span> , OoO0O00O0oo0O [ <span class="pl-c1">0</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">1</span> ] , OoO0O00O0oo0O [ <span class="pl-c1">2</span> ] )</td>
      </tr>
      <tr>
        <td id="L767" class="blob-num js-line-number" data-line-number="767"></td>
        <td id="LC767" class="blob-code blob-code-inner js-file-line"> Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Upload: <span class="pl-c1">%0.2f</span> M<span class="pl-c1">%s</span>/s<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span></td>
      </tr>
      <tr>
        <td id="L768" class="blob-num js-line-number" data-line-number="768"></td>
        <td id="LC768" class="blob-code blob-code-inner js-file-line"> ( ( O0OOoOOO0oO <span class="pl-k">/</span> <span class="pl-c1">1000</span> <span class="pl-k">/</span> <span class="pl-c1">1000</span> ) <span class="pl-k">*</span> units [ <span class="pl-c1">1</span> ] , units [ <span class="pl-c1">0</span> ] ) )</td>
      </tr>
      <tr>
        <td id="L769" class="blob-num js-line-number" data-line-number="769"></td>
        <td id="LC769" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">28</span> <span class="pl-k">-</span> <span class="pl-c1">28</span>: O0OOo <span class="pl-k">+</span> i11iIiiIii <span class="pl-k">/</span> I1i1iI1i <span class="pl-k">%</span> OoOoOO00 <span class="pl-k">%</span> Oo0Ooo <span class="pl-k">-</span> O0</td>
      </tr>
      <tr>
        <td id="L770" class="blob-num js-line-number" data-line-number="770"></td>
        <td id="LC770" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> share <span class="pl-k">and</span> mini :</td>
      </tr>
      <tr>
        <td id="L771" class="blob-num js-line-number" data-line-number="771"></td>
        <td id="LC771" class="blob-code blob-code-inner js-file-line">  Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Cannot generate a speedtest.net share results image while <span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L772" class="blob-num js-line-number" data-line-number="772"></td>
        <td id="LC772" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>testing against a Speedtest Mini server<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L773" class="blob-num js-line-number" data-line-number="773"></td>
        <td id="LC773" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">elif</span> share :</td>
      </tr>
      <tr>
        <td id="L774" class="blob-num js-line-number" data-line-number="774"></td>
        <td id="LC774" class="blob-code blob-code-inner js-file-line">  ooo0OOO <span class="pl-k">=</span> <span class="pl-c1">int</span> ( <span class="pl-c1">round</span> ( ( Oo00o0OO0O00o <span class="pl-k">/</span> <span class="pl-c1">1000</span> ) <span class="pl-k">*</span> <span class="pl-c1">8</span> , <span class="pl-c1">0</span> ) )</td>
      </tr>
      <tr>
        <td id="L775" class="blob-num js-line-number" data-line-number="775"></td>
        <td id="LC775" class="blob-code blob-code-inner js-file-line">  iii1Ii1Ii1 <span class="pl-k">=</span> <span class="pl-c1">int</span> ( <span class="pl-c1">round</span> ( OOoooO00o0oo0 [ <span class="pl-s"><span class="pl-pds">&#39;</span>latency<span class="pl-pds">&#39;</span></span> ] , <span class="pl-c1">0</span> ) )</td>
      </tr>
      <tr>
        <td id="L776" class="blob-num js-line-number" data-line-number="776"></td>
        <td id="LC776" class="blob-code blob-code-inner js-file-line">  IIi <span class="pl-k">=</span> <span class="pl-c1">int</span> ( <span class="pl-c1">round</span> ( ( O0OOoOOO0oO <span class="pl-k">/</span> <span class="pl-c1">1000</span> ) <span class="pl-k">*</span> <span class="pl-c1">8</span> , <span class="pl-c1">0</span> ) )</td>
      </tr>
      <tr>
        <td id="L777" class="blob-num js-line-number" data-line-number="777"></td>
        <td id="LC777" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">94</span> <span class="pl-k">-</span> <span class="pl-c1">94</span>: II111iiii <span class="pl-k">-</span> Oo0Ooo</td>
      </tr>
      <tr>
        <td id="L778" class="blob-num js-line-number" data-line-number="778"></td>
        <td id="LC778" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">91</span> <span class="pl-k">-</span> <span class="pl-c1">91</span>: Oo0Ooo</td>
      </tr>
      <tr>
        <td id="L779" class="blob-num js-line-number" data-line-number="779"></td>
        <td id="LC779" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">31</span> <span class="pl-k">-</span> <span class="pl-c1">31</span>: Oo0ooO0oo0oO <span class="pl-k">/</span> i11iIiiIii <span class="pl-k">%</span> iIii1I11I1II1 <span class="pl-k">+</span> Oo0ooO0oo0oO <span class="pl-k">/</span> i11iIiiIii</td>
      </tr>
      <tr>
        <td id="L780" class="blob-num js-line-number" data-line-number="780"></td>
        <td id="LC780" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">70</span> <span class="pl-k">-</span> <span class="pl-c1">70</span>: OoO0O00 <span class="pl-k">*</span> O0 . I1i1iI1i <span class="pl-k">+</span> I1IiiI . Oo0oO0ooo</td>
      </tr>
      <tr>
        <td id="L781" class="blob-num js-line-number" data-line-number="781"></td>
        <td id="LC781" class="blob-code blob-code-inner js-file-line">  Ii1iIiII1Ii <span class="pl-k">=</span> [</td>
      </tr>
      <tr>
        <td id="L782" class="blob-num js-line-number" data-line-number="782"></td>
        <td id="LC782" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>download=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> ooo0OOO ,</td>
      </tr>
      <tr>
        <td id="L783" class="blob-num js-line-number" data-line-number="783"></td>
        <td id="LC783" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>ping=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> iii1Ii1Ii1 ,</td>
      </tr>
      <tr>
        <td id="L784" class="blob-num js-line-number" data-line-number="784"></td>
        <td id="LC784" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>upload=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> IIi ,</td>
      </tr>
      <tr>
        <td id="L785" class="blob-num js-line-number" data-line-number="785"></td>
        <td id="LC785" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>promo=<span class="pl-pds">&#39;</span></span> ,</td>
      </tr>
      <tr>
        <td id="L786" class="blob-num js-line-number" data-line-number="786"></td>
        <td id="LC786" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>startmode=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> <span class="pl-s"><span class="pl-pds">&#39;</span>pingselect<span class="pl-pds">&#39;</span></span> ,</td>
      </tr>
      <tr>
        <td id="L787" class="blob-num js-line-number" data-line-number="787"></td>
        <td id="LC787" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>recommendedserverid=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> OOoooO00o0oo0 [ <span class="pl-s"><span class="pl-pds">&#39;</span>id<span class="pl-pds">&#39;</span></span> ] ,</td>
      </tr>
      <tr>
        <td id="L788" class="blob-num js-line-number" data-line-number="788"></td>
        <td id="LC788" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>accuracy=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> <span class="pl-c1">1</span> ,</td>
      </tr>
      <tr>
        <td id="L789" class="blob-num js-line-number" data-line-number="789"></td>
        <td id="LC789" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>serverid=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> OOoooO00o0oo0 [ <span class="pl-s"><span class="pl-pds">&#39;</span>id<span class="pl-pds">&#39;</span></span> ] ,</td>
      </tr>
      <tr>
        <td id="L790" class="blob-num js-line-number" data-line-number="790"></td>
        <td id="LC790" class="blob-code blob-code-inner js-file-line"> <span class="pl-s"><span class="pl-pds">&#39;</span>hash=<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> md5 ( ( <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>-<span class="pl-c1">%s</span>-<span class="pl-c1">%s</span>-<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span></td>
      </tr>
      <tr>
        <td id="L791" class="blob-num js-line-number" data-line-number="791"></td>
        <td id="LC791" class="blob-code blob-code-inner js-file-line"> ( iii1Ii1Ii1 , IIi , ooo0OOO , <span class="pl-s"><span class="pl-pds">&#39;</span>297aae72<span class="pl-pds">&#39;</span></span> ) )</td>
      </tr>
      <tr>
        <td id="L792" class="blob-num js-line-number" data-line-number="792"></td>
        <td id="LC792" class="blob-code blob-code-inner js-file-line"> . encode ( ) ) . hexdigest ( ) ]</td>
      </tr>
      <tr>
        <td id="L793" class="blob-num js-line-number" data-line-number="793"></td>
        <td id="LC793" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">42</span> <span class="pl-k">-</span> <span class="pl-c1">42</span>: O0 <span class="pl-k">*</span> o00ooo0 . Oo0Ooo <span class="pl-k">-</span> I1IiiI <span class="pl-k">*</span> iIii1I11I1II1</td>
      </tr>
      <tr>
        <td id="L794" class="blob-num js-line-number" data-line-number="794"></td>
        <td id="LC794" class="blob-code blob-code-inner js-file-line">  i1II1 <span class="pl-k">=</span> { <span class="pl-s"><span class="pl-pds">&#39;</span>Referer<span class="pl-pds">&#39;</span></span> : <span class="pl-s"><span class="pl-pds">&#39;</span>https://c.speedtest.net/flash/speedtest.swf<span class="pl-pds">&#39;</span></span> }</td>
      </tr>
      <tr>
        <td id="L795" class="blob-num js-line-number" data-line-number="795"></td>
        <td id="LC795" class="blob-code blob-code-inner js-file-line">  iIIiIi1iIII1 <span class="pl-k">=</span> O0oOO0 ( <span class="pl-s"><span class="pl-pds">&#39;</span>https://www.speedtest.net/api/api.php<span class="pl-pds">&#39;</span></span> ,</td>
      </tr>
      <tr>
        <td id="L796" class="blob-num js-line-number" data-line-number="796"></td>
        <td id="LC796" class="blob-code blob-code-inner js-file-line"> <span class="pl-v">data</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>&amp;<span class="pl-pds">&#39;</span></span> . join ( Ii1iIiII1Ii ) . encode ( ) ,</td>
      </tr>
      <tr>
        <td id="L797" class="blob-num js-line-number" data-line-number="797"></td>
        <td id="LC797" class="blob-code blob-code-inner js-file-line"> <span class="pl-v">headers</span> <span class="pl-k">=</span> i1II1 )</td>
      </tr>
      <tr>
        <td id="L798" class="blob-num js-line-number" data-line-number="798"></td>
        <td id="LC798" class="blob-code blob-code-inner js-file-line">  OooOOOOo <span class="pl-k">=</span> Ii1i ( iIIiIi1iIII1 )</td>
      </tr>
      <tr>
        <td id="L799" class="blob-num js-line-number" data-line-number="799"></td>
        <td id="LC799" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> OooOOOOo <span class="pl-k">is</span> <span class="pl-c1">False</span> :</td>
      </tr>
      <tr>
        <td id="L800" class="blob-num js-line-number" data-line-number="800"></td>
        <td id="LC800" class="blob-code blob-code-inner js-file-line">   Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Could not submit results to speedtest.net<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L801" class="blob-num js-line-number" data-line-number="801"></td>
        <td id="LC801" class="blob-code blob-code-inner js-file-line">   sys . <span class="pl-c1">exit</span> ( <span class="pl-c1">1</span> )</td>
      </tr>
      <tr>
        <td id="L802" class="blob-num js-line-number" data-line-number="802"></td>
        <td id="LC802" class="blob-code blob-code-inner js-file-line">  iII111Ii <span class="pl-k">=</span> OooOOOOo . read ( )</td>
      </tr>
      <tr>
        <td id="L803" class="blob-num js-line-number" data-line-number="803"></td>
        <td id="LC803" class="blob-code blob-code-inner js-file-line">  Ooo00OoOOO <span class="pl-k">=</span> OooOOOOo . code</td>
      </tr>
      <tr>
        <td id="L804" class="blob-num js-line-number" data-line-number="804"></td>
        <td id="LC804" class="blob-code blob-code-inner js-file-line">  OooOOOOo . close ( )</td>
      </tr>
      <tr>
        <td id="L805" class="blob-num js-line-number" data-line-number="805"></td>
        <td id="LC805" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">98</span> <span class="pl-k">-</span> <span class="pl-c1">98</span>: iIii1I11I1II1 <span class="pl-k">*</span> I1ii11iIi11i <span class="pl-k">*</span> Oo0ooO0oo0oO <span class="pl-k">+</span> O0OOo <span class="pl-k">%</span> i11iIiiIii <span class="pl-k">%</span> O0</td>
      </tr>
      <tr>
        <td id="L806" class="blob-num js-line-number" data-line-number="806"></td>
        <td id="LC806" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">int</span> ( Ooo00OoOOO ) <span class="pl-k">!=</span> <span class="pl-c1">200</span> :</td>
      </tr>
      <tr>
        <td id="L807" class="blob-num js-line-number" data-line-number="807"></td>
        <td id="LC807" class="blob-code blob-code-inner js-file-line">   Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Could not submit results to speedtest.net<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L808" class="blob-num js-line-number" data-line-number="808"></td>
        <td id="LC808" class="blob-code blob-code-inner js-file-line">   sys . <span class="pl-c1">exit</span> ( <span class="pl-c1">1</span> )</td>
      </tr>
      <tr>
        <td id="L809" class="blob-num js-line-number" data-line-number="809"></td>
        <td id="LC809" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">27</span> <span class="pl-k">-</span> <span class="pl-c1">27</span>: O0</td>
      </tr>
      <tr>
        <td id="L810" class="blob-num js-line-number" data-line-number="810"></td>
        <td id="LC810" class="blob-code blob-code-inner js-file-line">  OOO0oOOoo <span class="pl-k">=</span> parse_qs ( iII111Ii . decode ( ) )</td>
      </tr>
      <tr>
        <td id="L811" class="blob-num js-line-number" data-line-number="811"></td>
        <td id="LC811" class="blob-code blob-code-inner js-file-line">  oOOO00o000o <span class="pl-k">=</span> OOO0oOOoo . get ( <span class="pl-s"><span class="pl-pds">&#39;</span>resultid<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L812" class="blob-num js-line-number" data-line-number="812"></td>
        <td id="LC812" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-k">not</span> oOOO00o000o <span class="pl-k">or</span> <span class="pl-c1">len</span> ( oOOO00o000o ) <span class="pl-k">!=</span> <span class="pl-c1">1</span> :</td>
      </tr>
      <tr>
        <td id="L813" class="blob-num js-line-number" data-line-number="813"></td>
        <td id="LC813" class="blob-code blob-code-inner js-file-line">   Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Could not submit results to speedtest.net<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L814" class="blob-num js-line-number" data-line-number="814"></td>
        <td id="LC814" class="blob-code blob-code-inner js-file-line">   sys . <span class="pl-c1">exit</span> ( <span class="pl-c1">1</span> )</td>
      </tr>
      <tr>
        <td id="L815" class="blob-num js-line-number" data-line-number="815"></td>
        <td id="LC815" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">9</span> <span class="pl-k">-</span> <span class="pl-c1">9</span>: o0OO0 <span class="pl-k">+</span> I1i1iI1i <span class="pl-k">/</span> I1i1iI1i</td>
      </tr>
      <tr>
        <td id="L816" class="blob-num js-line-number" data-line-number="816"></td>
        <td id="LC816" class="blob-code blob-code-inner js-file-line">  Ii11iI1i ( <span class="pl-s"><span class="pl-pds">&#39;</span>Share results: https://www.speedtest.net/result/<span class="pl-c1">%s</span>.png<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span></td>
      </tr>
      <tr>
        <td id="L817" class="blob-num js-line-number" data-line-number="817"></td>
        <td id="LC817" class="blob-code blob-code-inner js-file-line"> oOOO00o000o [ <span class="pl-c1">0</span> ] )</td>
      </tr>
      <tr>
        <td id="L818" class="blob-num js-line-number" data-line-number="818"></td>
        <td id="LC818" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">global</span> oo00o0Oo0oo</td>
      </tr>
      <tr>
        <td id="L819" class="blob-num js-line-number" data-line-number="819"></td>
        <td id="LC819" class="blob-code blob-code-inner js-file-line">  oo00o0Oo0oo <span class="pl-k">=</span> oOOO00o000o [ <span class="pl-c1">0</span> ]</td>
      </tr>
      <tr>
        <td id="L820" class="blob-num js-line-number" data-line-number="820"></td>
        <td id="LC820" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">import</span> time</td>
      </tr>
      <tr>
        <td id="L821" class="blob-num js-line-number" data-line-number="821"></td>
        <td id="LC821" class="blob-code blob-code-inner js-file-line">  time . sleep ( <span class="pl-c1">2</span> )</td>
      </tr>
      <tr>
        <td id="L822" class="blob-num js-line-number" data-line-number="822"></td>
        <td id="LC822" class="blob-code blob-code-inner js-file-line">  I1i1i1 . close ( )</td>
      </tr>
      <tr>
        <td id="L823" class="blob-num js-line-number" data-line-number="823"></td>
        <td id="LC823" class="blob-code blob-code-inner js-file-line">  Ii1I11ii1i <span class="pl-k">=</span> O0iIiIIIIIii ( )</td>
      </tr>
      <tr>
        <td id="L824" class="blob-num js-line-number" data-line-number="824"></td>
        <td id="LC824" class="blob-code blob-code-inner js-file-line">  Ii1I11ii1i . doModal ( )</td>
      </tr>
      <tr>
        <td id="L825" class="blob-num js-line-number" data-line-number="825"></td>
        <td id="LC825" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">del</span> Ii1I11ii1i</td>
      </tr>
      <tr>
        <td id="L826" class="blob-num js-line-number" data-line-number="826"></td>
        <td id="LC826" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">58</span> <span class="pl-k">-</span> <span class="pl-c1">58</span>: o0oOOo0O0Ooo <span class="pl-k">/</span> Oo0oO0ooo . OoOoOO00 <span class="pl-k">/</span> OoooooooOO <span class="pl-k">+</span> ooO00oOoo</td>
      </tr>
      <tr>
        <td id="L827" class="blob-num js-line-number" data-line-number="827"></td>
        <td id="LC827" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">86</span> <span class="pl-k">-</span> <span class="pl-c1">86</span>: I1i1iI1i <span class="pl-k">*</span> I1IiiI <span class="pl-k">+</span> I1i1iI1i <span class="pl-k">+</span> II111iiii</td>
      </tr>
      <tr>
        <td id="L828" class="blob-num js-line-number" data-line-number="828"></td>
        <td id="LC828" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">8</span> <span class="pl-k">-</span> <span class="pl-c1">8</span>: ooO00oOoo <span class="pl-k">-</span> o00 <span class="pl-k">/</span> O0OOo</td>
      </tr>
      <tr>
        <td id="L829" class="blob-num js-line-number" data-line-number="829"></td>
        <td id="LC829" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">O0iIiIIIIIii</span> ( <span class="pl-e">xbmcgui</span> . <span class="pl-e">WindowDialog</span> ) :</td>
      </tr>
      <tr>
        <td id="L830" class="blob-num js-line-number" data-line-number="830"></td>
        <td id="LC830" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">def</span> <span class="pl-c1">__init__</span> ( <span class="pl-smi"><span class="pl-smi">self</span></span> ) :</td>
      </tr>
      <tr>
        <td id="L831" class="blob-num js-line-number" data-line-number="831"></td>
        <td id="LC831" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">self</span> . imgControl <span class="pl-k">=</span> xbmcgui . ControlImage ( <span class="pl-c1">340</span> , <span class="pl-c1">210</span> , <span class="pl-c1">600</span> , <span class="pl-c1">270</span> , <span class="pl-s"><span class="pl-pds">&#39;</span>https://www.speedtest.net/result/<span class="pl-c1">%s</span>.png<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> oo00o0Oo0oo )</td>
      </tr>
      <tr>
        <td id="L832" class="blob-num js-line-number" data-line-number="832"></td>
        <td id="LC832" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">self</span> . addControl ( <span class="pl-c1">self</span> . imgControl )</td>
      </tr>
      <tr>
        <td id="L833" class="blob-num js-line-number" data-line-number="833"></td>
        <td id="LC833" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> self . button0 = xbmcgui . ControlButton ( int ( 340 + 505 ) , int ( 210 + 206 ) , 120 , 80 , &quot;Chiudi&quot; )</span></td>
      </tr>
      <tr>
        <td id="L834" class="blob-num js-line-number" data-line-number="834"></td>
        <td id="LC834" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> self . addControl ( self . button0 )</span></td>
      </tr>
      <tr>
        <td id="L835" class="blob-num js-line-number" data-line-number="835"></td>
        <td id="LC835" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> self . setFocus ( self . button0 )</span></td>
      </tr>
      <tr>
        <td id="L836" class="blob-num js-line-number" data-line-number="836"></td>
        <td id="LC836" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">96</span> <span class="pl-k">-</span> <span class="pl-c1">96</span>: OoOoOO00</td>
      </tr>
      <tr>
        <td id="L837" class="blob-num js-line-number" data-line-number="837"></td>
        <td id="LC837" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">def</span> <span class="pl-en">onAction</span> ( <span class="pl-smi"><span class="pl-smi">self</span></span> , <span class="pl-smi">action</span> ) :</td>
      </tr>
      <tr>
        <td id="L838" class="blob-num js-line-number" data-line-number="838"></td>
        <td id="LC838" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> action <span class="pl-k">==</span> II1Iiii1111i <span class="pl-k">or</span> action <span class="pl-k">==</span> i1IIi11111i :</td>
      </tr>
      <tr>
        <td id="L839" class="blob-num js-line-number" data-line-number="839"></td>
        <td id="LC839" class="blob-code blob-code-inner js-file-line">   <span class="pl-c1">self</span> . saveClose ( )</td>
      </tr>
      <tr>
        <td id="L840" class="blob-num js-line-number" data-line-number="840"></td>
        <td id="LC840" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">29</span> <span class="pl-k">-</span> <span class="pl-c1">29</span>: I1ii11iIi11i <span class="pl-k">/</span> i1IIi . I1IiiI <span class="pl-k">-</span> OoOoOO00 <span class="pl-k">-</span> OoOoOO00 <span class="pl-k">-</span> o00ooo0</td>
      </tr>
      <tr>
        <td id="L841" class="blob-num js-line-number" data-line-number="841"></td>
        <td id="LC841" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">def</span> <span class="pl-en">onControl</span> ( <span class="pl-smi"><span class="pl-smi">self</span></span> , <span class="pl-smi">control</span> ) :</td>
      </tr>
      <tr>
        <td id="L842" class="blob-num js-line-number" data-line-number="842"></td>
        <td id="LC842" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> control <span class="pl-k">==</span> <span class="pl-c1">self</span> . button0 :</td>
      </tr>
      <tr>
        <td id="L843" class="blob-num js-line-number" data-line-number="843"></td>
        <td id="LC843" class="blob-code blob-code-inner js-file-line">   <span class="pl-c1">self</span> . saveClose ( )</td>
      </tr>
      <tr>
        <td id="L844" class="blob-num js-line-number" data-line-number="844"></td>
        <td id="LC844" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">20</span> <span class="pl-k">-</span> <span class="pl-c1">20</span>: i1IIi <span class="pl-k">%</span> OoO0O00 . I1IiiI <span class="pl-k">/</span> Oo0oO0ooo <span class="pl-k">*</span> i11iIiiIii <span class="pl-k">*</span> Oo0ooO0oo0oO</td>
      </tr>
      <tr>
        <td id="L845" class="blob-num js-line-number" data-line-number="845"></td>
        <td id="LC845" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">def</span> <span class="pl-en">saveClose</span> ( <span class="pl-smi"><span class="pl-smi">self</span></span> ) :</td>
      </tr>
      <tr>
        <td id="L846" class="blob-num js-line-number" data-line-number="846"></td>
        <td id="LC846" class="blob-code blob-code-inner js-file-line">  OOo <span class="pl-k">=</span> xbmcgui . Dialog ( )</td>
      </tr>
      <tr>
        <td id="L847" class="blob-num js-line-number" data-line-number="847"></td>
        <td id="LC847" class="blob-code blob-code-inner js-file-line">  i1i11I1I1iii1 <span class="pl-k">=</span> OOo . yesno ( <span class="pl-s"><span class="pl-pds">&quot;</span>Salva risultato<span class="pl-pds">&quot;</span></span> , <span class="pl-s"><span class="pl-pds">&quot;</span>Vuoi salvare il risultato di questo speedtest?<span class="pl-pds">&quot;</span></span> , <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span> , <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L848" class="blob-num js-line-number" data-line-number="848"></td>
        <td id="LC848" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> i1i11I1I1iii1 :</td>
      </tr>
      <tr>
        <td id="L849" class="blob-num js-line-number" data-line-number="849"></td>
        <td id="LC849" class="blob-code blob-code-inner js-file-line">   <span class="pl-c1">self</span> . location <span class="pl-k">=</span> OOo . browse ( <span class="pl-c1">3</span> , <span class="pl-s"><span class="pl-pds">&#39;</span>Dove vuoi salvare il risultato?<span class="pl-pds">&#39;</span></span> , <span class="pl-s"><span class="pl-pds">&#39;</span>files<span class="pl-pds">&#39;</span></span> , <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span> , <span class="pl-c1">False</span> , <span class="pl-c1">False</span> , <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L850" class="blob-num js-line-number" data-line-number="850"></td>
        <td id="LC850" class="blob-code blob-code-inner js-file-line">   <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>self.location<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L851" class="blob-num js-line-number" data-line-number="851"></td>
        <td id="LC851" class="blob-code blob-code-inner js-file-line">   <span class="pl-c1">print</span> <span class="pl-c1">self</span> . location</td>
      </tr>
      <tr>
        <td id="L852" class="blob-num js-line-number" data-line-number="852"></td>
        <td id="LC852" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">import</span> urllib</td>
      </tr>
      <tr>
        <td id="L853" class="blob-num js-line-number" data-line-number="853"></td>
        <td id="LC853" class="blob-code blob-code-inner js-file-line">   I1iii11 <span class="pl-k">=</span> urllib . URLopener ( )</td>
      </tr>
      <tr>
        <td id="L854" class="blob-num js-line-number" data-line-number="854"></td>
        <td id="LC854" class="blob-code blob-code-inner js-file-line">   I1iii11 . retrieve ( <span class="pl-s"><span class="pl-pds">&#39;</span>https://www.speedtest.net/result/<span class="pl-c1">%s</span>.png<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> oo00o0Oo0oo , <span class="pl-c1">self</span> . location <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>.png<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> oo00o0Oo0oo )</td>
      </tr>
      <tr>
        <td id="L855" class="blob-num js-line-number" data-line-number="855"></td>
        <td id="LC855" class="blob-code blob-code-inner js-file-line">   OOo . ok ( <span class="pl-s"><span class="pl-pds">&quot;</span>Risultato salvato!<span class="pl-pds">&quot;</span></span> , <span class="pl-s"><span class="pl-pds">&quot;</span>&#39;<span class="pl-c1">%s</span>.png&#39;<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> oo00o0Oo0oo <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> salvato in &#39;<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">self</span> . location <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>&#39;<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L856" class="blob-num js-line-number" data-line-number="856"></td>
        <td id="LC856" class="blob-code blob-code-inner js-file-line">  OOo . ok ( <span class="pl-s"><span class="pl-pds">&quot;</span>Terminato!<span class="pl-pds">&quot;</span></span> , <span class="pl-s"><span class="pl-pds">&quot;</span>Speedtest terminato!<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L857" class="blob-num js-line-number" data-line-number="857"></td>
        <td id="LC857" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">self</span> . close ( )</td>
      </tr>
      <tr>
        <td id="L858" class="blob-num js-line-number" data-line-number="858"></td>
        <td id="LC858" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">74</span> <span class="pl-k">-</span> <span class="pl-c1">74</span>: O0 <span class="pl-k">/</span> i1IIi</td>
      </tr>
      <tr>
        <td id="L859" class="blob-num js-line-number" data-line-number="859"></td>
        <td id="LC859" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">78</span> <span class="pl-k">-</span> <span class="pl-c1">78</span>: OoooooooOO . OoO0O00 <span class="pl-k">+</span> O0OOo <span class="pl-k">-</span> i1IIi</td>
      </tr>
      <tr>
        <td id="L860" class="blob-num js-line-number" data-line-number="860"></td>
        <td id="LC860" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">ii1O0</span> ( <span class="pl-e">xbmcgui</span> . <span class="pl-e">WindowDialog</span> ) :</td>
      </tr>
      <tr>
        <td id="L861" class="blob-num js-line-number" data-line-number="861"></td>
        <td id="LC861" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">def</span> <span class="pl-c1">__init__</span> ( <span class="pl-smi"><span class="pl-smi">self</span></span> ) :</td>
      </tr>
      <tr>
        <td id="L862" class="blob-num js-line-number" data-line-number="862"></td>
        <td id="LC862" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">self</span> . imgControl <span class="pl-k">=</span> xbmcgui . ControlImage ( <span class="pl-c1">340</span> , <span class="pl-c1">210</span> , <span class="pl-c1">600</span> , <span class="pl-c1">270</span> , <span class="pl-s"><span class="pl-pds">&#39;</span>https://www.speedtest.net/result/4670696458.png<span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L863" class="blob-num js-line-number" data-line-number="863"></td>
        <td id="LC863" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">self</span> . addControl ( <span class="pl-c1">self</span> . imgControl )</td>
      </tr>
      <tr>
        <td id="L864" class="blob-num js-line-number" data-line-number="864"></td>
        <td id="LC864" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">self</span> . button0 <span class="pl-k">=</span> xbmcgui . ControlButton ( <span class="pl-c1">int</span> ( <span class="pl-c1">340</span> <span class="pl-k">+</span> <span class="pl-c1">505</span> ) , <span class="pl-c1">int</span> ( <span class="pl-c1">210</span> <span class="pl-k">+</span> <span class="pl-c1">206</span> ) , <span class="pl-c1">80</span> , <span class="pl-c1">50</span> , <span class="pl-s"><span class="pl-pds">&quot;</span>[B]Close[/B]<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L865" class="blob-num js-line-number" data-line-number="865"></td>
        <td id="LC865" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">self</span> . addControl ( <span class="pl-c1">self</span> . button0 )</td>
      </tr>
      <tr>
        <td id="L866" class="blob-num js-line-number" data-line-number="866"></td>
        <td id="LC866" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">self</span> . setFocus ( <span class="pl-c1">self</span> . button0 )</td>
      </tr>
      <tr>
        <td id="L867" class="blob-num js-line-number" data-line-number="867"></td>
        <td id="LC867" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">33</span> <span class="pl-k">-</span> <span class="pl-c1">33</span>: i1IIi</td>
      </tr>
      <tr>
        <td id="L868" class="blob-num js-line-number" data-line-number="868"></td>
        <td id="LC868" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">def</span> <span class="pl-en">onAction</span> ( <span class="pl-smi"><span class="pl-smi">self</span></span> , <span class="pl-smi">action</span> ) :</td>
      </tr>
      <tr>
        <td id="L869" class="blob-num js-line-number" data-line-number="869"></td>
        <td id="LC869" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> action <span class="pl-k">==</span> II1Iiii1111i <span class="pl-k">or</span> action <span class="pl-k">==</span> i1IIi11111i :</td>
      </tr>
      <tr>
        <td id="L870" class="blob-num js-line-number" data-line-number="870"></td>
        <td id="LC870" class="blob-code blob-code-inner js-file-line">   <span class="pl-c1">self</span> . saveClose ( )</td>
      </tr>
      <tr>
        <td id="L871" class="blob-num js-line-number" data-line-number="871"></td>
        <td id="LC871" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">36</span> <span class="pl-k">-</span> <span class="pl-c1">36</span>: II111iiii <span class="pl-k">%</span> i11iIiiIii <span class="pl-k">*</span> OoOoOO00 <span class="pl-k">+</span> I1i1iI1i</td>
      </tr>
      <tr>
        <td id="L872" class="blob-num js-line-number" data-line-number="872"></td>
        <td id="LC872" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">def</span> <span class="pl-en">onControl</span> ( <span class="pl-smi"><span class="pl-smi">self</span></span> , <span class="pl-smi">control</span> ) :</td>
      </tr>
      <tr>
        <td id="L873" class="blob-num js-line-number" data-line-number="873"></td>
        <td id="LC873" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> control <span class="pl-k">==</span> <span class="pl-c1">self</span> . button0 :</td>
      </tr>
      <tr>
        <td id="L874" class="blob-num js-line-number" data-line-number="874"></td>
        <td id="LC874" class="blob-code blob-code-inner js-file-line">   <span class="pl-c1">self</span> . saveClose ( )</td>
      </tr>
      <tr>
        <td id="L875" class="blob-num js-line-number" data-line-number="875"></td>
        <td id="LC875" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">if</span> <span class="pl-c1">25</span> <span class="pl-k">-</span> <span class="pl-c1">25</span>: iIii1I11I1II1 <span class="pl-k">%</span> o00 . O0OOo</td>
      </tr>
      <tr>
        <td id="L876" class="blob-num js-line-number" data-line-number="876"></td>
        <td id="LC876" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">def</span> <span class="pl-en">saveClose</span> ( <span class="pl-smi"><span class="pl-smi">self</span></span> ) :</td>
      </tr>
      <tr>
        <td id="L877" class="blob-num js-line-number" data-line-number="877"></td>
        <td id="LC877" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">14</span> <span class="pl-k">-</span> <span class="pl-c1">14</span>: o0OO0 <span class="pl-k">+</span> I1ii11iIi11i <span class="pl-k">-</span> o00 <span class="pl-k">/</span> O0 . ooO00oOoo</td>
      </tr>
      <tr>
        <td id="L878" class="blob-num js-line-number" data-line-number="878"></td>
        <td id="LC878" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">45</span> <span class="pl-k">-</span> <span class="pl-c1">45</span>: ooO00oOoo</td>
      </tr>
      <tr>
        <td id="L879" class="blob-num js-line-number" data-line-number="879"></td>
        <td id="LC879" class="blob-code blob-code-inner js-file-line">  OOo <span class="pl-k">=</span> xbmcgui . Dialog ( )</td>
      </tr>
      <tr>
        <td id="L880" class="blob-num js-line-number" data-line-number="880"></td>
        <td id="LC880" class="blob-code blob-code-inner js-file-line">  i1i11I1I1iii1 <span class="pl-k">=</span> OOo . yesno ( <span class="pl-s"><span class="pl-pds">&quot;</span>Save Result<span class="pl-pds">&quot;</span></span> , <span class="pl-s"><span class="pl-pds">&quot;</span>Would you like to save a copy of this speed test?<span class="pl-pds">&quot;</span></span> , <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span> , <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L881" class="blob-num js-line-number" data-line-number="881"></td>
        <td id="LC881" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> i1i11I1I1iii1 :</td>
      </tr>
      <tr>
        <td id="L882" class="blob-num js-line-number" data-line-number="882"></td>
        <td id="LC882" class="blob-code blob-code-inner js-file-line">   <span class="pl-c1">self</span> . location <span class="pl-k">=</span> OOo . browse ( <span class="pl-c1">3</span> , <span class="pl-s"><span class="pl-pds">&#39;</span>Where would you like to save the result?<span class="pl-pds">&#39;</span></span> , <span class="pl-s"><span class="pl-pds">&#39;</span>files<span class="pl-pds">&#39;</span></span> , <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span> , <span class="pl-c1">False</span> , <span class="pl-c1">False</span> , <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span> )</td>
      </tr>
      <tr>
        <td id="L883" class="blob-num js-line-number" data-line-number="883"></td>
        <td id="LC883" class="blob-code blob-code-inner js-file-line">   <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>self.location<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L884" class="blob-num js-line-number" data-line-number="884"></td>
        <td id="LC884" class="blob-code blob-code-inner js-file-line">   <span class="pl-c1">print</span> <span class="pl-c1">self</span> . location</td>
      </tr>
      <tr>
        <td id="L885" class="blob-num js-line-number" data-line-number="885"></td>
        <td id="LC885" class="blob-code blob-code-inner js-file-line">   <span class="pl-k">import</span> urllib</td>
      </tr>
      <tr>
        <td id="L886" class="blob-num js-line-number" data-line-number="886"></td>
        <td id="LC886" class="blob-code blob-code-inner js-file-line">   I1iii11 <span class="pl-k">=</span> urllib . URLopener ( )</td>
      </tr>
      <tr>
        <td id="L887" class="blob-num js-line-number" data-line-number="887"></td>
        <td id="LC887" class="blob-code blob-code-inner js-file-line">   I1iii11 . retrieve ( <span class="pl-s"><span class="pl-pds">&#39;</span>https://www.speedtest.net/result/4670696458.png<span class="pl-pds">&#39;</span></span> , <span class="pl-c1">self</span> . location <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>4670696458.png<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L888" class="blob-num js-line-number" data-line-number="888"></td>
        <td id="LC888" class="blob-code blob-code-inner js-file-line">   OOo . ok ( <span class="pl-s"><span class="pl-pds">&quot;</span>Result Saved!<span class="pl-pds">&quot;</span></span> , <span class="pl-s"><span class="pl-pds">&quot;</span>&#39;4670696458.png&#39;<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> was saved to &#39;<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">self</span> . location <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>&#39;<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L889" class="blob-num js-line-number" data-line-number="889"></td>
        <td id="LC889" class="blob-code blob-code-inner js-file-line">  OOo . ok ( <span class="pl-s"><span class="pl-pds">&quot;</span>Result Saved!<span class="pl-pds">&quot;</span></span> ,  )</td>
      </tr>
      <tr>
        <td id="L890" class="blob-num js-line-number" data-line-number="890"></td>
        <td id="LC890" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">self</span> . close ( )</td>
      </tr>
      <tr>
        <td id="L891" class="blob-num js-line-number" data-line-number="891"></td>
        <td id="LC891" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">83</span> <span class="pl-k">-</span> <span class="pl-c1">83</span>: OoOoOO00 . OoooooooOO</td>
      </tr>
      <tr>
        <td id="L892" class="blob-num js-line-number" data-line-number="892"></td>
        <td id="LC892" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">58</span> <span class="pl-k">-</span> <span class="pl-c1">58</span>: i11iIiiIii <span class="pl-k">+</span> OoooooooOO <span class="pl-k">%</span> OoooooooOO <span class="pl-k">/</span> Oo0oO0ooo <span class="pl-k">/</span> i11iIiiIii</td>
      </tr>
      <tr>
        <td id="L893" class="blob-num js-line-number" data-line-number="893"></td>
        <td id="LC893" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>__main__<span class="pl-pds">&#39;</span></span> :</td>
      </tr>
      <tr>
        <td id="L894" class="blob-num js-line-number" data-line-number="894"></td>
        <td id="LC894" class="blob-code blob-code-inner js-file-line"> i1Ii1i1I11Iii ( <span class="pl-v">share</span> <span class="pl-k">=</span> <span class="pl-c1">True</span> , <span class="pl-v">simple</span> <span class="pl-k">=</span> <span class="pl-c1">True</span> )</td>
      </tr>
      <tr>
        <td id="L895" class="blob-num js-line-number" data-line-number="895"></td>
        <td id="LC895" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">62</span> <span class="pl-k">-</span> <span class="pl-c1">62</span>: OoO0O00 <span class="pl-k">/</span> I1ii11iIi11i</td>
      </tr>
      <tr>
        <td id="L896" class="blob-num js-line-number" data-line-number="896"></td>
        <td id="LC896" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">7</span> <span class="pl-k">-</span> <span class="pl-c1">7</span>: OoooooooOO . Oo0oO0ooo</td>
      </tr>
      <tr>
        <td id="L897" class="blob-num js-line-number" data-line-number="897"></td>
        <td id="LC897" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">53</span> <span class="pl-k">-</span> <span class="pl-c1">53</span>: o00ooo0 <span class="pl-k">%</span> o00ooo0 <span class="pl-k">*</span> o0oOOo0O0Ooo <span class="pl-k">+</span> OoOoOO00</td>
      </tr>
      <tr>
        <td id="L898" class="blob-num js-line-number" data-line-number="898"></td>
        <td id="LC898" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> <span class="pl-c1">92</span> <span class="pl-k">-</span> <span class="pl-c1">92</span>: OoooooooOO <span class="pl-k">+</span> i1IIi <span class="pl-k">/</span> o00ooo0 <span class="pl-k">*</span> O0</td>
      </tr>
      <tr>
        <td id="L899" class="blob-num js-line-number" data-line-number="899"></td>
        <td id="LC899" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> dd678faae9ac167bc83abf78e5cb2f3f0688d3a3</span></td>
      </tr>
</table>

  <details class="details-reset details-overlay BlobToolbar position-absolute js-file-line-actions dropdown d-none" aria-hidden="true">
    <summary class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1" aria-label="Inline file action toolbar">
      <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 13 16" version="1.1" width="13" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zm5 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zM13 7.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/></svg>
    </summary>
    <details-menu>
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2">
        <li><clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-lines" style="cursor:pointer;" data-original-text="Copy lines">Copy lines</clipboard-copy></li>
        <li><clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;" data-original-text="Copy permalink">Copy permalink</clipboard-copy></li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" role="menuitem" href="/FusionwareIT/script.speedtest/blame/80fe817b4a6be4134b109476bcc782db228b477f/default.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" role="menuitem" href="/FusionwareIT/script.speedtest/issues/new">Open new issue</a></li>
      </ul>
    </details-menu>
  </details>

  </div>

    </div>

  

  <details class="details-reset details-overlay details-overlay-dark">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>


  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

        
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2018 <span title="0.16172s from unicorn-5844f8669f-nq8gc">GitHub</span>, Inc.</li>
        <li class="mr-3"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3"><a href="/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li class="mr-3"><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3"><a href="https://blog.github.com" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    
    <script crossorigin="anonymous" integrity="sha512-092+yG9tBLtacCexwGKGjTtkuRfZo0YUa8VrsiKW+Zh/nyA2j7MvftFLeoIor9CGQ9uDFYNIcbFDbbTPw7tV3Q==" type="application/javascript" src="https://assets-cdn.github.com/assets/frameworks-176ef037f2b2ddbb94c6810c7bce4ec9.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-7B0eg/R5PL/dlNG+bHCysBLGVVm7GlnXXMppGKvIdTDISxAVuMDqbRd3Xp1MCE61ePFFWbROn+Ym2NSKYt0n7A==" type="application/javascript" src="https://assets-cdn.github.com/assets/github-1d7545c663040df39896fe9d26aae303.js"></script>
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
  </div>
</div>

  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark" open>
    <summary aria-haspopup="dialog" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

<div id="hovercard-aria-description" class="sr-only">
  Press h to open a hovercard with more details.
</div>


  </body>
</html>

