import * as vscode from 'vscode';
import axios from 'axios';

export function activate(context: vscode.ExtensionContext) {
    // Ikkada ippudu context.extensionUri error rakunda pass avthundi
    const provider = new RAGChatProvider(context.extensionUri);
    context.subscriptions.push(
        vscode.window.registerWebviewViewProvider('ragChatSidebar', provider)
    );
}

class RAGChatProvider implements vscode.WebviewViewProvider {
    // Ee constructor ni add cheyandi
    constructor(private readonly _extensionUri: vscode.Uri) {}

    public resolveWebviewView(webviewView: vscode.WebviewView) {
        webviewView.webview.options = { 
            enableScripts: true,
            localResourceRoots: [this._extensionUri] 
        };

        webviewView.webview.html = this._getHtmlForWebview();

        webviewView.webview.onDidReceiveMessage(async (data) => {
            if (data.type === 'askAI') {
                try {
                    const response = await axios.get('http://127.0.0.1:8000/ask', {
                        params: { query: data.value }
                    });
                    webviewView.webview.postMessage({ type: 'addResponse', value: response.data.answer });
                } catch (error) {
                    webviewView.webview.postMessage({ type: 'addResponse', value: "Error: Backend unreachable." });
                }
            }
        });
    }

    private _getHtmlForWebview() {
        // Mee patha HTML logic ikkada unchandi
        return `
            <!DOCTYPE html>
            <html>
            <style>
                body { font-family: sans-serif; padding: 10px; color: white; background: #1e1e1e; }
                #chat { height: 300px; overflow-y: auto; border: 1px solid #333; margin-bottom: 10px; padding: 5px; }
                input { width: 75%; padding: 5px; background: #333; color: white; border: none; }
                button { width: 20%; padding: 5px; cursor: pointer; background: #007acc; color: white; border: none; }
                .msg { margin: 5px 0; padding: 5px; border-radius: 4px; }
                .user { background: #0e639c; text-align: right; }
                .ai { background: #333; text-align: left; }
            </style>
            <body>
                <h3>RAG AI Assistant</h3>
                <div id="chat"></div>
                <input type="text" id="inp" placeholder="Ask about code...">
                <button onclick="send()">Ask</button>
                <script>
                    const vscode = acquireVsCodeApi();
                    function send() {
                        const val = document.getElementById('inp').value;
                        document.getElementById('chat').innerHTML += '<div class="msg user">' + val + '</div>';
                        vscode.postMessage({ type: 'askAI', value: val });
                        document.getElementById('inp').value = '';
                    }
                    window.addEventListener('message', event => {
                        const message = event.data;
                        if (message.type === 'addResponse') {
                            document.getElementById('chat').innerHTML += '<div class="msg ai">' + message.value + '</div>';
                        }
                    });
                </script>
            </body>
            </html>
        `;
    }
}