'use strict'

window.addEventListener('DOMContentLoaded', onLoad)

function onLoad () {
  // Show loading spinner immediately because the search cache will be building for some time
  createSpinner()

  // Add ui events
  document.getElementById('search_full').addEventListener('keyup', searchFullHandler)

  document.querySelectorAll('input[id^=enable_list_]').forEach(function (e) {
    if (document.location.pathname.indexOf('all.html') === -1 && e.classList.contains('notloaded')) {
      e.addEventListener('change', openAll)
    } else {
      e.addEventListener('change', searchFullHandler)
    }
  })

  document.getElementById('enable_more_columns').addEventListener('change', toggleMoreColums)
  document.querySelectorAll('#emoji_table tr').forEach(tr => tr.addEventListener('click', trClick))
  document.addEventListener('selectionchange', onSelectionChange)
  document.documentElement.addEventListener('click', closeModalOutsideClick)

  // Fix table header height, otherwise the two table headers (position:sticky) may overlap
  const rowHeight = document.querySelector('#emoji_table .listheader').clientHeight + 'px'
  document.querySelectorAll('#emoji_table .header>*').forEach(e => (e.style.height = rowHeight))

  // Parse url
  if (document.location.search.indexOf('enableList=enable_list_') !== -1) {
    const m = document.location.search.match(/enableList=(\w+)/)
    if (m) {
      document.getElementById(m[1]).checked = true
    }
  }
  if (document.location.search.indexOf('query=') !== -1) {
    const m = document.location.search.match(/query=([^=#&]+)/)
    if (m) {
      document.getElementById('search_full').value = decodeURIComponent(m[1])
    }
  }

  // Update table (and build search cache)
  toggleMoreColums()
  searchFullHandler().then(hideSpinner)
}

function openAll () {
  // Open all.html with parameters
  this.checked = false
  let params = `enableList=${this.id}`
  if (document.getElementById('search_full').value) {
    params += `&query=${encodeURIComponent(document.getElementById('search_full').value)}`
  }
  document.location.href = `all.html?${params}`
}

function onSelectionChange (e) {
  // If the selected text is in a .copiable element, copy the whole textContent to the clipboard
  const selection = document.getSelection()
  if (selection.toString().length === 0) {
    return
  }
  if (selection.anchorNode != null) {
    let node = null
    if ('classList' in selection.anchorNode && selection.anchorNode.classList.contains('copiable')) {
      node = selection.anchorNode
    } else if (selection.anchorNode.parentNode && 'classList' in selection.anchorNode.parentNode && selection.anchorNode.parentNode.classList.contains('copiable')) {
      node = selection.anchorNode.parentNode
    }
    if (node) {
      selection.removeAllRanges()
      const range = document.createRange()
      range.selectNode(node)
      selection.addRange(range)
      navigator.clipboard.writeText(node.textContent)
      node.classList.add('copied')
      window.setTimeout(() => node.classList.add('copiedfadeout'), 100)
      window.setTimeout(() => { node.classList.remove('copied'); node.classList.remove('copiedfadeout') }, 2000)
    }
  }
}

function closeModalOutsideClick (ev) {
  if (document.querySelector('.modal').style.display === 'none') {
    return
  }
  let node = ev.target
  while (node && node !== document.body) {
    if ('classList' in node && node.classList.contains('modal')) {
      return
    }
    node = node.parentNode
  }
  closeModal()
}

function closeModal () {
  document.querySelector('.modal').style.display = 'none'
}

function examplePythonCode (fName, stringArg, argN) {
  const s = `emoji.<span style="color:#6f42c1">${fName}</span>(<span style="color:#032f62">${JSON.stringify(stringArg)}</span>`
  if (argN) {
    return `${s}, ${argN.replace(/=(\w*)/g, '<span style="color:#005cc5">=$1</span>').replace(/("\w+")/g, '<span style="color:#032f62">$1</span>')})`
  }
  return `${s})`
}

function trClick () {
  const tr = this
  if (tr.className.indexOf('listheader') !== -1) {
    // list header click

  } else if (tr.className.indexOf('header') !== -1) {
    // top header click

  } else {
    // emoji row click
    const selection = document.getSelection()
    if (selection && !selection.isCollapsed) {
      // User is selecting text in the row -> don't open the modal
      return
    }
    loadMoreColumns()
    const tds = tr.querySelectorAll('td')
    const emoji = tds[0].textContent
    const name = tds[1].textContent
    const unicode = tds[2].textContent
    const charName = tds[3].textContent
    const xml = tds[4].textContent
    // find language code
    let listheader = tr.previousElementSibling
    while (listheader && listheader.className.indexOf('listheader') === -1) {
      listheader = listheader.previousElementSibling
    }
    const modal = document.querySelector('.modal')

    modal.querySelector('.emoji').textContent = emoji
    modal.querySelector('.name').textContent = name
    modal.querySelector('.unicode').textContent = unicode
    modal.querySelector('.charname').textContent = charName
    modal.querySelector('.xml').textContent = xml
    modal.querySelector('.example .emojize').innerHTML = examplePythonCode('emojize', name, listheader.dataset.languageArg)
    modal.querySelector('.example .demojize').innerHTML = examplePythonCode('demojize', emoji, listheader.dataset.languageArg)

    window.setTimeout(function () {
      modal.style.display = 'block'
    }, 100)
  }
}

let moreColumnsLoaded = false
function loadMoreColumns () {
  if (!moreColumnsLoaded) {
    // Fill missing columns in table
    document.querySelectorAll('#emoji_table tr>td:nth-child(3)').forEach(function (td) {
      const tdU32 = td.parentNode.appendChild(document.createElement('td'))
      tdU32.textContent = xmlFromPython32(td.textContent)
    })
    moreColumnsLoaded = true
  }
}

function xmlFromPython32 (s) {
  return s.trim().split('\\').slice(1).map(c => `&#${parseInt(c.substring(1), 16)};`).join('')
}

function toggleMoreColums () {
  if (document.getElementById('enable_more_columns').checked) {
    loadMoreColumns()
    document.getElementById('emoji_table').classList.add('allcolumns')
  } else {
    document.getElementById('emoji_table').classList.remove('allcolumns')
  }
}

function wordsInText (words, text) {
  let matches = 0
  for (const word of words) {
    matches += (text.indexOf(word) !== -1)
  }
  return matches === words.length
}

let searchTimeOut = null
let lastSearchParameters = null
let enabledLists = {}
function searchFullHandler () {
  return new Promise(function downloadCrossSiteImage (resolve) {
    window.clearTimeout(searchTimeOut)
    const query = document.getElementById('search_full').value
    searchTimeOut = window.setTimeout(() => searchFull(query, resolve), 500)
  })
}

let searchCache = null
function buildSearchCache () {
  searchCache = []
  document.querySelectorAll('#emoji_table tr').forEach(function (tr, i) {
    if (tr.className.indexOf('header') === -1) {
      searchCache.push({
        tr: tr,
        text: tr.textContent.toLowerCase(),
        list: tr.className
      })
    }
  })
}

function createSpinner () {
  if (document.querySelector('.spinnerholder .roundspinner')) {
    document.querySelector('.spinnerholder').style.display = 'inline-block'
    return
  }

  const spinnerHolder = document.createElement('div')
  spinnerHolder.classList.add('spinnerholder')
  const spinner = spinnerHolder.appendChild(document.createElement('div'))
  spinner.classList.add('roundspinner')

  const oldSpinnerHolder = document.querySelector('.spinnerholder')
  oldSpinnerHolder.parentNode.replaceChild(spinnerHolder, oldSpinnerHolder)
}

function hideSpinner () {
  if (document.querySelector('.spinnerholder')) {
    document.querySelector('.spinnerholder').style.display = 'none'
  }
}

function searchFull (query, onDoneCallback) {
  // Full text search in the table
  searchTimeOut = null

  createSpinner()

  if (searchCache == null) {
    buildSearchCache()
  }
  const searchWords = query.toLowerCase().split(/\s+/)

  enabledLists = {}

  const table = document.getElementById('emoji_table')

  document.querySelectorAll('input[id^=enable_list_]').forEach(function (e) {
    if (e.checked) {
      enabledLists[e.dataset.name] = true
      const tr = table.querySelector(`tr.listheader.${e.dataset.name}`)
      if (tr) {
        tr.style.display = ''
      }
    } else {
      const tr = table.querySelector(`tr.listheader.${e.dataset.name}`)
      if (tr) {
        tr.style.display = 'none'
      }
    }
  })

  if (lastSearchParameters === query + '#' + Object.keys(enabledLists).join(',')) {
    hideSpinner()
    if (onDoneCallback) {
      onDoneCallback()
    }
    return
  }

  const tableHolder = document.getElementById('emoji_table_holder')
  const fragment = document.createDocumentFragment()
  fragment.appendChild(table)

  table.querySelectorAll('tr.empty').forEach(e => e.remove())

  const onDone = function () {
    if (tableHolder.firstElementChild) {
      tableHolder.replaceChild(fragment, tableHolder.firstElementChild)
    } else {
      tableHolder.appendChild(fragment)
    }
    lastSearchParameters = query + '#' + Object.keys(enabledLists).join(',')
    hideSpinner()
    if (onDoneCallback) {
      onDoneCallback()
    }
  }

  window.setTimeout(() => searchFullWorker(searchWords, 0, 0, 4000, onDone))
}

function searchFullWorker (searchWords, startIndex, hiddenNodesCounter, batchSize, cb) {
  const endIndex = Math.min(startIndex + batchSize, searchCache.length)
  const emptyTr = document.createElement('tr')
  emptyTr.classList.add('empty')
  for (let i = startIndex; i < endIndex; i++) {
    const entry = searchCache[i]
    if (!(entry.list in enabledLists)) {
      entry.tr.style.display = 'none'
    } else if (!searchWords.length || wordsInText(searchWords, entry.text)) {
      entry.tr.style.display = ''
      if (hiddenNodesCounter > 0 && hiddenNodesCounter % 2 === 1) {
        // Insert an empty node to correct the odd/even css behaviour
        entry.tr.parentNode.insertBefore(emptyTr.cloneNode(false), entry.tr)
        hiddenNodesCounter = 0
      }
    } else {
      entry.tr.style.display = 'none'
      hiddenNodesCounter++
    }
  }

  if (endIndex < searchCache.length - 1) {
    window.setTimeout(() => searchFullWorker(searchWords, endIndex, hiddenNodesCounter, batchSize, cb))
  } else if (cb) {
    cb()
  }
}
