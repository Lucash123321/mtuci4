function getCanvasFingerprint() {
    var canvas = document.createElement('canvas');
    var ctx = canvas.getContext('2d');
    ctx.textBaseline = "top";
    ctx.font = "14px 'Arial'";
    ctx.fillText('test', 2, 2);
    return canvas.toDataURL();
}

function getWebGLFingerprint() {
    var canvas = document.createElement('canvas');
    var gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
    if (!gl) return null;

    var debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
    if (debugInfo) {
        return gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL);
    }
    return null;
}

function getFingerprint() {
    var canvasFingerprint = getCanvasFingerprint();
    var webglFingerprint = getWebGLFingerprint();
    return { canvas: canvasFingerprint, webgl: webglFingerprint };
}

document.addEventListener("DOMContentLoaded", () => {
    console.log(getFingerprint());
})
