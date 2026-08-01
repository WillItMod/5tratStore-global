/* Independent 5tratStore defaults for the upstream Node-RED runtime. */
module.exports = {
    uiPort: process.env.PORT || 1880,
    uiHost: "0.0.0.0",
    flowFile: "flows.json",
    credentialSecret: process.env.NODE_RED_CREDENTIAL_SECRET,
    editorTheme: {
        projects: {
            enabled: false
        }
    },
    diagnostics: {
        enabled: false,
        ui: false
    },
    runtimeState: {
        enabled: false,
        ui: false
    },
    logging: {
        console: {
            level: "info",
            metrics: false,
            audit: false
        }
    }
};
