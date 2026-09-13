var html = new ActiveXObject('htmlfile');
html.write('<meta http-equiv="x-ua-compatible" content="IE=edge" />');
try {
    var fso = new ActiveXObject('Scripting.FileSystemObject');
    var ts = fso.OpenTextFile('app.js', 1);
    var code = ts.ReadAll();
    ts.Close();
    
    html.parentWindow.execScript(code, 'JavaScript');
    WScript.Echo('Parsed successfully.');
} catch (e) {
    WScript.Echo('Error: ' + e.description);
}
