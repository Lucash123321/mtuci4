function getCanvasFingerprint() {
    let canvas = document.createElement('canvas');
    let ctx = canvas.getContext('2d');
    ctx.textBaseline = "top";
    ctx.font = "14px 'Arial'";
    ctx.fillText('test', 2, 2);
    return canvas.toDataURL();
}

function getWebGLFingerprint() {
    let canvas = document.createElement('canvas');
    let gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
    if (!gl) return null;

    let debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
    if (debugInfo) {
        return gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL);
    }
    return null;
}
function getCSRFToken() {
    const csrfToken = document.cookie.match(/csrftoken=([^;]+)/);
    return csrfToken ? csrfToken[1] : null;
}

document.addEventListener("DOMContentLoaded", () => {
    const url = document.querySelector(".lmao").dataset.getUrl;
    const csrfToken = getCSRFToken();

    const formData = new FormData();
    let canvas = getCanvasFingerprint();
    let webgl = getWebGLFingerprint();

    formData.append('canvas', canvas);
    formData.append('webgl', webgl);

    fetch(url, {
        method: "POST",
        headers: {
            "X-CSRFToken": csrfToken,
        },
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
            // console.log(data);
        })
        .catch((error) => console.error(error));
    
})
