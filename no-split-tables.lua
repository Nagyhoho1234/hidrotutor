-- Pandoc Lua filter: prevent tables from splitting across pages
function Table(tbl)
  return {
    pandoc.RawBlock('latex', '\\begin{minipage}{\\textwidth}'),
    tbl,
    pandoc.RawBlock('latex', '\\end{minipage}')
  }
end
