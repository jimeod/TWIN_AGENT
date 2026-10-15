"""Styling constants for the digital twin Gradio app.

Estética: glassmorphism pastel (vidrio esmerilado sobre un degradado
lavanda -> menta), botones en forma de píldora y tarjetas con tinte pastel.
"""

GOLD = "#f2b872"    
BLUE = "#9cc9e8"    
PURPLE = "#b9a8ee"  
GREEN = "#b9e3b0"  

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* ============================================================
   Tokens — modo claro (por defecto, como la referencia)
   ============================================================ */
:root {
  --twin-text: #14141a;
  --twin-muted: #6b7084;

  --twin-glass: rgba(255, 255, 255, 0.50);
  --twin-glass-strong: rgba(255, 255, 255, 0.78);
  --twin-glass-border: rgba(255, 255, 255, 0.85);
  --twin-line: rgba(20, 20, 40, 0.10);
  --twin-shadow: 0 24px 70px rgba(88, 98, 168, 0.20);
  --twin-shadow-soft: 0 6px 20px rgba(88, 98, 168, 0.12);

  --twin-ink-bg: #0b0b0f;      /* botón primario / burbuja del usuario */
  --twin-ink-fg: #ffffff;

  --twin-green:  rgba(212, 238, 198, 0.80);
  --twin-blue:   rgba(197, 224, 243, 0.82);
  --twin-purple: rgba(220, 212, 247, 0.85);
  --twin-orange: rgba(251, 225, 196, 0.85);

  --twin-bg-1: #c4ccee;
  --twin-bg-2: #cde7ea;
  --twin-blob-a: #d3d0f7;
  --twin-blob-b: #c3e9d9;
  --twin-blob-c: #9aa7ee;
}

/* ============================================================
   Tokens — modo oscuro (Gradio agrega .dark al <body>)
   ============================================================ */
body.dark {
  --twin-text: #ececf3;
  --twin-muted: #9a9db2;

  --twin-glass: rgba(34, 36, 58, 0.55);
  --twin-glass-strong: rgba(46, 48, 74, 0.75);
  --twin-glass-border: rgba(255, 255, 255, 0.12);
  --twin-line: rgba(255, 255, 255, 0.10);
  --twin-shadow: 0 24px 70px rgba(0, 0, 0, 0.45);
  --twin-shadow-soft: 0 6px 20px rgba(0, 0, 0, 0.30);

  --twin-ink-bg: #ffffff;
  --twin-ink-fg: #0b0b0f;

  --twin-green:  rgba(90, 130, 100, 0.40);
  --twin-blue:   rgba(80, 125, 160, 0.42);
  --twin-purple: rgba(125, 105, 190, 0.42);
  --twin-orange: rgba(190, 135, 80, 0.40);

  --twin-bg-1: #171a33;
  --twin-bg-2: #12262b;
  --twin-blob-a: #3a2f72;
  --twin-blob-b: #1f4a4a;
  --twin-blob-c: #2c3a8c;
}

footer, .built-with, .show-api, .api-docs { display: none !important; }

/* ============================================================
   Fondo: degradado lavanda -> menta con manchas de color
   ============================================================ */
html, body {
  min-height: 100%;
  background:
    radial-gradient(700px 520px at 12% 8%,  var(--twin-blob-a) 0%, transparent 65%),
    radial-gradient(640px 520px at 92% 30%, var(--twin-blob-c) 0%, transparent 70%),
    radial-gradient(760px 600px at 78% 100%, var(--twin-blob-b) 0%, transparent 65%),
    linear-gradient(135deg, var(--twin-bg-1), var(--twin-bg-2)) !important;
  background-attachment: fixed !important;
}
gradio-app { background: transparent !important; }

/* ============================================================
   Ventana de vidrio
   ============================================================ */
.gradio-container {
  background: var(--twin-glass) !important;
  -webkit-backdrop-filter: blur(26px) saturate(140%);
  backdrop-filter: blur(26px) saturate(140%);
  border: 1px solid var(--twin-glass-border) !important;
  border-radius: 28px !important;
  box-shadow: var(--twin-shadow) !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
  width: calc(100% - 32px) !important;
  max-width: 880px !important;
  min-width: 0 !important;
  margin: 40px auto !important;
  padding: 28px 28px 32px !important;
}
.gradio-container .main, .gradio-container .contain, .gradio-container .wrap {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
  background: transparent !important;
}
.gradio-container * { min-width: 0; }

/* ============================================================
   Título
   ============================================================ */
.gradio-container h1 {
  color: var(--twin-text) !important;
  font-size: 28px !important;
  font-weight: 700 !important;
  letter-spacing: -0.02em !important;
  text-align: left !important;
  margin: 2px 0 6px !important;
  display: flex;
  align-items: center;
  gap: 12px;
}
.gradio-container h1::before {
  content: "";
  flex: 0 0 auto;
  width: 24px;
  height: 24px;
  border-radius: 8px;
  background: var(--twin-ink-bg);
  box-shadow: inset 0 0 0 6px var(--twin-ink-bg), inset 0 0 0 9px var(--twin-ink-fg);
}
.gradio-container p, .gradio-container .prose { color: var(--twin-muted) !important; }

/* ============================================================
   Superficies base
   ============================================================ */
.block, .form {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

/* Ocultar la etiqueta del chatbot */
.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container {
  display: none !important;
}

/* ============================================================
   Panel del chat (vidrio interior)
   ============================================================ */
.chatbot, .chatbot.block {
  background: var(--twin-glass) !important;
  -webkit-backdrop-filter: blur(14px);
  backdrop-filter: blur(14px);
  border: 1px solid var(--twin-glass-border) !important;
  border-radius: 22px !important;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.5) !important;
  min-height: 460px !important;
  overflow: hidden;
}
.chatbot .placeholder, .chatbot .placeholder * { color: var(--twin-muted) !important; }

/* ============================================================
   Mensajes
   ============================================================ */
.message-row,
.message-row > div,
.message-row .role,
.message-wrap, .bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  border: 0 !important;
  border-radius: 18px !important;
  box-shadow: none !important;
  padding: 10px 14px !important;
  font-size: 14px !important;
  line-height: 1.55 !important;
}

/* Usuario: píldora negra, como el botón "Sign up" */
.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble {
  background: var(--twin-ink-bg) !important;
  color: var(--twin-ink-fg) !important;
  border-bottom-right-radius: 6px !important;
}

/* Twin: vidrio claro con borde sutil */
.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble {
  background: var(--twin-glass-strong) !important;
  color: var(--twin-text) !important;
  border: 1px solid var(--twin-glass-border) !important;
  border-bottom-left-radius: 6px !important;
  box-shadow: var(--twin-shadow-soft) !important;
}

/* Evitar doble borde/radio en burbujas anidadas */
.message-row.bot-row .message .message,
.message-row.bot-row .message .bubble,
.message-row.bot-row .message .message-bubble,
.message-row.bot-row .bubble .message,
.message-row.bot-row .bubble .bubble,
.message-row.bot-row .bubble .message-bubble,
.message-row.bot-row .message-bubble .message,
.message-row.bot-row .message-bubble .bubble,
.message-row.bot-row .message-bubble .message-bubble,
.message-row[data-role="assistant"] .message .message,
.message-row[data-role="assistant"] .message .bubble,
.message-row[data-role="assistant"] .message .message-bubble,
.message-row[data-role="assistant"] .bubble .message,
.message-row[data-role="assistant"] .bubble .bubble,
.message-row[data-role="assistant"] .bubble .message-bubble,
.message-row[data-role="assistant"] .message-bubble .message,
.message-row[data-role="assistant"] .message-bubble .bubble,
.message-row[data-role="assistant"] .message-bubble .message-bubble {
  border: 0 !important;
  box-shadow: none !important;
  padding: 0 !important;
}

/* Párrafos con tamaño uniforme */
.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p,
.message-row .prose p {
  font-size: 14px !important;
  line-height: 1.55 !important;
  margin: 0 0 8px !important;
  color: inherit !important;
}
.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child,
.message-row .prose p:last-child { margin-bottom: 0 !important; }

/* Limpiar fondos internos heredados */
.message-row .message *,
.message-row .message-bubble *,
.message-row .bubble * {
  background: transparent !important;
  border-color: transparent !important;
  box-shadow: none !important;
  color: inherit !important;
}
.message-row .message a,
.message-row .message-bubble a {
  color: inherit !important;
  text-decoration: underline;
  text-underline-offset: 2px;
}

/* ============================================================
   Campo de texto
   ============================================================ */
.input-row,
.gr-input-row,
.chat-input-row,
form[class*="input"] { align-items: stretch !important; gap: 10px !important; }

textarea, input[type="text"] {
  background: var(--twin-glass-strong) !important;
  border: 1px solid var(--twin-glass-border) !important;
  border-radius: 18px !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 14px !important;
  padding: 13px 16px !important;
  line-height: 1.4 !important;
  min-height: 48px !important;
  box-shadow: var(--twin-shadow-soft) !important;
}
textarea:focus, input[type="text"]:focus {
  border-color: var(--twin-ink-bg) !important;
  outline: none !important;
  box-shadow: 0 0 0 3px rgba(117, 105, 220, 0.25) !important;
}
textarea::placeholder, input::placeholder { color: var(--twin-muted) !important; }

/* ============================================================
   Botones: píldoras
   ============================================================ */
button {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  letter-spacing: 0 !important;
  text-transform: none !important;
  border: 1px solid var(--twin-ink-bg) !important;
  border-radius: 999px !important;
  background: transparent !important;
  color: var(--twin-text) !important;
  padding: 0 20px !important;
  min-height: 46px !important;
  align-self: stretch !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer;
  transition: background 0.15s ease, color 0.15s ease, border-color 0.15s ease, transform 0.15s ease;
}
button:hover { background: var(--twin-glass-strong) !important; }
button:focus-visible { outline: 2px solid #7569dc !important; outline-offset: 2px; }

/* Botón primario (enviar): negro sólido */
button.primary,
button[variant="primary"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary {
  background: var(--twin-ink-bg) !important;
  border: 1px solid var(--twin-ink-bg) !important;
  color: var(--twin-ink-fg) !important;
  min-height: 46px !important;
  align-self: stretch !important;
  padding: 0 18px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}
button.primary:hover,
button.submit:hover,
.submit-button:hover,
button.lg.primary:hover {
  background: var(--twin-ink-bg) !important;
  border-color: var(--twin-ink-bg) !important;
  color: var(--twin-ink-fg) !important;
  transform: translateY(-1px);
}

button.submit svg,
button.submit-button svg,
.submit-button svg,
button.primary svg,
button[variant="primary"] svg {
  width: 18px !important;
  height: 18px !important;
  margin: 0 auto !important;
  display: block !important;
  align-self: center !important;
  color: var(--twin-ink-fg) !important;
  fill: currentColor !important;
  stroke: currentColor !important;
}

/* ============================================================
   Ejemplos: tarjetas de vidrio con tinte pastel
   ============================================================ */
.examples, .examples-holder, [data-testid="examples"] {
  background: transparent !important;
  padding: 0 !important;
  margin-top: 16px !important;
}
.examples table, .examples-table { background: transparent !important; border: 0 !important; }

.examples button, .example, .examples td button, [data-testid="examples"] button {
  background: var(--twin-glass-strong) !important;
  border: 1px solid var(--twin-glass-border) !important;
  border-radius: 18px !important;
  box-shadow: var(--twin-shadow-soft) !important;
  color: var(--twin-text) !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  line-height: 1.4 !important;
  padding: 14px 16px !important;
  text-align: left !important;
  min-height: 0 !important;
  align-self: auto !important;
  display: inline-block !important;
}
.examples button:nth-of-type(4n+1), [data-testid="examples"] button:nth-of-type(4n+1) { background: var(--twin-green)  !important; }
.examples button:nth-of-type(4n+2), [data-testid="examples"] button:nth-of-type(4n+2) { background: var(--twin-blue)   !important; }
.examples button:nth-of-type(4n+3), [data-testid="examples"] button:nth-of-type(4n+3) { background: var(--twin-purple) !important; }
.examples button:nth-of-type(4n+4), [data-testid="examples"] button:nth-of-type(4n+4) { background: var(--twin-orange) !important; }

.examples button:hover, .example:hover, [data-testid="examples"] button:hover {
  border-color: var(--twin-ink-bg) !important;
  transform: translateY(-2px);
}

/* ============================================================
   Iconos (limpiar, reintentar, copiar)
   ============================================================ */
.icon-button, .chatbot .icon-button {
  color: var(--twin-muted) !important;
  background: transparent !important;
  border: 0 !important;
  border-radius: 999px !important;
  min-height: 0 !important;
  align-self: auto !important;
  padding: 6px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}
.icon-button:hover, .chatbot .icon-button:hover {
  color: var(--twin-text) !important;
  background: var(--twin-glass-strong) !important;
}

/* ============================================================
   Scrollbar y selección
   ============================================================ */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(120, 125, 170, 0.35); border-radius: 999px; }
::-webkit-scrollbar-thumb:hover { background: rgba(120, 125, 170, 0.55); }

::selection { background: var(--twin-purple); color: #14141a; }

/* ============================================================
   Móvil
   ============================================================ */
@media (max-width: 640px) {
  .gradio-container {
    width: calc(100% - 16px) !important;
    margin: 8px auto !important;
    padding: 18px 14px 22px !important;
    border-radius: 22px !important;
  }
  .gradio-container h1 { font-size: 22px !important; }
  .chatbot, .chatbot.block { min-height: 380px !important; border-radius: 18px !important; }
}
"""

JS = """
() => {
  document.title = 'Digital Twin';

  const focusInput = () => {
    const areas = document.querySelectorAll('textarea');
    if (areas.length) areas[areas.length - 1].focus();
  };
  setTimeout(focusInput, 300);

  // Re-focus the message field whenever Gradio re-enables it
  // (i.e. after the assistant finishes responding).
  const watchTextarea = (area) => {
    if (area.dataset.twinWatched) return;
    area.dataset.twinWatched = '1';
    let wasDisabled = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, { attributes: true, attributeFilter: ['disabled', 'readonly'] });
  };

  const scan = () => document.querySelectorAll('textarea').forEach(watchTextarea);
  setTimeout(scan, 500);
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
}
"""