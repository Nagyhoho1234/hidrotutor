import { useState, useEffect, useRef, useCallback } from 'react';
import { getConceptGraph } from '../api/client';

// Part color palette — 6 parts for the hidroinformatics book
const PART_COLORS = [
  '#3b82f6', // I  — blue (Foundations)
  '#10b981', // II — green (Terrain Analysis)
  '#14b8a6', // III — teal (Watershed Delineation)
  '#ef4444', // IV — red (Flood Hazard)
  '#92400e', // V  — brown (Groundwater)
  '#8b5cf6', // VI — purple (AI and the Future)
];

function getPartIndex(chapterNum) {
  if (chapterNum <= 4) return 0;   // Part I: Ch 1-4
  if (chapterNum <= 8) return 1;   // Part II: Ch 5-8
  if (chapterNum <= 12) return 2;  // Part III: Ch 9-12
  if (chapterNum <= 17) return 3;  // Part IV: Ch 13-17
  if (chapterNum <= 21) return 4;  // Part V: Ch 18-21
  return 5;                        // Part VI: Ch 22-25
}

// Simple layered layout: assign Y by topological depth, X spread within each layer
function layoutNodes(nodes, edges) {
  const keys = Object.keys(nodes).sort((a, b) => Number(a) - Number(b));

  // Build adjacency for depth calculation
  const inDeg = {};
  const children = {};
  keys.forEach((k) => { inDeg[k] = 0; children[k] = []; });
  edges.forEach((e) => {
    if (inDeg[e.to] !== undefined) inDeg[e.to]++;
    if (children[e.from]) children[e.from].push(e.to);
  });

  // BFS to assign depth (longest path from roots)
  const depth = {};
  keys.forEach((k) => { depth[k] = 0; });
  let changed = true;
  while (changed) {
    changed = false;
    edges.forEach((e) => {
      const nd = depth[e.from] + 1;
      if (nd > depth[e.to]) {
        depth[e.to] = nd;
        changed = true;
      }
    });
  }

  // Group by depth
  const layers = {};
  keys.forEach((k) => {
    const d = depth[k];
    if (!layers[d]) layers[d] = [];
    layers[d].push(k);
  });

  const maxDepth = Math.max(...Object.values(depth));
  const layerCount = maxDepth + 1;

  // Compute positions
  const positions = {};
  const paddingX = 80;
  const paddingY = 60;
  const layerHeight = 100;
  const svgHeight = layerCount * layerHeight + paddingY * 2;

  // Find widest layer for scaling
  const maxWidth = Math.max(...Object.values(layers).map((l) => l.length));
  const nodeSpacing = 110;
  const svgWidth = Math.max(maxWidth * nodeSpacing + paddingX * 2, 900);

  Object.entries(layers).forEach(([d, nodeKeys]) => {
    const y = paddingY + Number(d) * layerHeight;
    const totalW = (nodeKeys.length - 1) * nodeSpacing;
    const startX = (svgWidth - totalW) / 2;
    nodeKeys.forEach((k, i) => {
      positions[k] = { x: startX + i * nodeSpacing, y };
    });
  });

  return { positions, svgWidth, svgHeight };
}

export default function ConceptMap({ onChapterOpen }) {
  const [graph, setGraph] = useState(null);
  const [loading, setLoading] = useState(true);
  const [tooltip, setTooltip] = useState(null);
  const [hoveredNode, setHoveredNode] = useState(null);
  const svgRef = useRef(null);
  const containerRef = useRef(null);

  useEffect(() => {
    setLoading(true);
    getConceptGraph()
      .then(setGraph)
      .catch(() => setGraph(null))
      .finally(() => setLoading(false));
  }, []);

  const handleNodeClick = useCallback((chapterNum) => {
    if (onChapterOpen) onChapterOpen(chapterNum);
  }, [onChapterOpen]);

  if (loading) {
    return (
      <div className="h-full flex items-center justify-center text-gray-500 dark:text-gray-400">
        Loading concept map...
      </div>
    );
  }

  if (!graph) {
    return (
      <div className="h-full flex items-center justify-center text-gray-500 dark:text-gray-400">
        Failed to load concept graph.
      </div>
    );
  }

  // Group concepts by chapter — one node per chapter on the map
  const rawNodes = graph.nodes;
  const rawEdges = graph.edges;

  // Build chapter-level nodes: one node per unique chapter number
  const chapterNodes = {};
  const conceptToChapter = {}; // concept key -> chapter key
  Object.entries(rawNodes).forEach(([key, node]) => {
    const chKey = `ch${node.chapter_num}`;
    conceptToChapter[key] = chKey;
    if (!chapterNodes[chKey]) {
      chapterNodes[chKey] = {
        name: `Ch ${node.chapter_num}`,
        chapter_num: node.chapter_num,
        concepts: [],
      };
    }
    chapterNodes[chKey].concepts.push(node.name);
  });

  // Build chapter-level edges (deduplicated)
  const edgeSet = new Set();
  const chapterEdges = [];
  rawEdges.forEach((e) => {
    const from = conceptToChapter[e.from];
    const to = conceptToChapter[e.to];
    if (from && to && from !== to) {
      const ek = `${from}-${to}`;
      if (!edgeSet.has(ek)) {
        edgeSet.add(ek);
        chapterEdges.push({ from, to });
      }
    }
  });

  const nodes = chapterNodes;
  const edges = chapterEdges;
  const { positions, svgWidth, svgHeight } = layoutNodes(nodes, edges);

  // Build set of connected edges for hover highlighting
  const connectedEdges = new Set();
  const connectedNodes = new Set();
  if (hoveredNode) {
    connectedNodes.add(hoveredNode);
    edges.forEach((e) => {
      if (e.from === hoveredNode || e.to === hoveredNode) {
        connectedEdges.add(`${e.from}-${e.to}`);
        connectedNodes.add(e.from);
        connectedNodes.add(e.to);
      }
    });
  }

  const nodeRadius = 22;
  const markerId = 'arrow';

  // Part legend — English labels for our 6 parts
  const partNames = [
    'I. Foundations',
    'II. Terrain Analysis',
    'III. Watershed Delineation',
    'IV. Flood Hazard',
    'V. Groundwater',
    'VI. AI & Future',
  ];

  return (
    <div ref={containerRef} className="h-full flex flex-col">
      {/* Legend */}
      <div className="flex flex-wrap gap-3 px-4 py-2 border-b border-gray-200 dark:border-gray-700 text-xs text-gray-500 dark:text-gray-400">
        {partNames.map((name, i) => (
          <span key={i} className="flex items-center gap-1">
            <span style={{ display: 'inline-block', width: 10, height: 10, borderRadius: '50%', background: PART_COLORS[i] }} />
            {name}
          </span>
        ))}
        <span className="ml-auto text-gray-400 dark:text-gray-500">
          Click a chapter to open it
        </span>
      </div>

      {/* SVG graph */}
      <div className="flex-1 overflow-auto p-2">
        <svg
          ref={svgRef}
          viewBox={`0 0 ${svgWidth} ${svgHeight}`}
          width={svgWidth}
          height={svgHeight}
          style={{ maxWidth: '100%', height: 'auto', display: 'block', margin: '0 auto' }}
        >
          <defs>
            <marker
              id={markerId}
              viewBox="0 0 10 7"
              refX="10"
              refY="3.5"
              markerWidth="8"
              markerHeight="6"
              orient="auto-start-reverse"
            >
              <polygon points="0 0, 10 3.5, 0 7" fill="#9ca3af" opacity="0.5" />
            </marker>
          </defs>

          {/* Edges */}
          {edges.map((e, i) => {
            const from = positions[e.from];
            const to = positions[e.to];
            if (!from || !to) return null;

            const edgeKey = `${e.from}-${e.to}`;
            const isHighlighted = hoveredNode && connectedEdges.has(edgeKey);
            const isDimmed = hoveredNode && !connectedEdges.has(edgeKey);

            // Shorten line to stop at node circle edge
            const dx = to.x - from.x;
            const dy = to.y - from.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist === 0) return null;
            const ux = dx / dist;
            const uy = dy / dist;
            const x1 = from.x + ux * nodeRadius;
            const y1 = from.y + uy * nodeRadius;
            const x2 = to.x - ux * (nodeRadius + 4);
            const y2 = to.y - uy * (nodeRadius + 4);

            return (
              <line
                key={i}
                x1={x1} y1={y1} x2={x2} y2={y2}
                stroke={isHighlighted ? '#3b82f6' : '#9ca3af'}
                strokeWidth={isHighlighted ? 2 : 1}
                opacity={isDimmed ? 0.15 : isHighlighted ? 0.9 : 0.35}
                markerEnd={`url(#${markerId})`}
              />
            );
          })}

          {/* Nodes */}
          {Object.entries(nodes).map(([key, node]) => {
            const pos = positions[key];
            if (!pos) return null;
            const chNum = node.chapter_num;
            const color = PART_COLORS[getPartIndex(chNum)];
            const isDimmed = hoveredNode && !connectedNodes.has(key);
            const isHovered = hoveredNode === key;

            return (
              <g
                key={key}
                style={{ cursor: 'pointer' }}
                onClick={() => handleNodeClick(chNum)}
                onMouseEnter={(ev) => {
                  setHoveredNode(key);
                  const conceptList = node.concepts ? node.concepts.join(', ') : node.name;
                  setTooltip({ text: `Ch ${chNum}: ${conceptList}`, x: ev.clientX, y: ev.clientY });
                }}
                onMouseMove={(ev) => {
                  setTooltip((prev) => prev ? { ...prev, x: ev.clientX, y: ev.clientY } : null);
                }}
                onMouseLeave={() => { setHoveredNode(null); setTooltip(null); }}
                opacity={isDimmed ? 0.25 : 1}
              >
                <circle
                  cx={pos.x} cy={pos.y} r={nodeRadius}
                  fill={color}
                  stroke={isHovered ? '#1f2937' : 'transparent'}
                  strokeWidth={isHovered ? 2.5 : 0}
                  opacity={0.9}
                />
                <text
                  x={pos.x} y={pos.y + 1}
                  textAnchor="middle"
                  dominantBaseline="central"
                  fill="white"
                  fontSize="13"
                  fontWeight="bold"
                  style={{ pointerEvents: 'none', userSelect: 'none' }}
                >
                  {chNum}
                </text>
              </g>
            );
          })}
        </svg>
      </div>

      {/* Tooltip */}
      {tooltip && (
        <div
          className="fixed z-[9999] px-3 py-1.5 rounded-lg shadow-lg text-xs font-medium pointer-events-none bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 border border-gray-200 dark:border-gray-700"
          style={{
            left: tooltip.x + 12,
            top: tooltip.y - 28,
            boxShadow: '0 4px 16px rgba(0,0,0,0.15)',
            maxWidth: 320,
          }}
        >
          {tooltip.text}
        </div>
      )}
    </div>
  );
}
