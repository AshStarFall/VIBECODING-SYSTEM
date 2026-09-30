# Desktop Applications

- Choose native or web-shell architecture based on OS integration, distribution, performance, update model, and team capability.
- Define supported OS versions, installer/update strategy, code signing, local data location, permissions, and uninstall behavior.
- Treat renderer/web content as untrusted; isolate privileged APIs and validate IPC messages. Do not expose arbitrary filesystem or shell access.
- Protect local secrets appropriately and explain backup/export/deletion behavior. Plan crash reporting with privacy controls.
- Test fresh install, upgrade, rollback/update failure, offline behavior, high-DPI/accessibility, and signed release artifacts.

Examples to evaluate: Tauri, Electron, Wails, .NET, Compose Multiplatform, PyInstaller/Nuitka. Compare bundle size, runtime model, plugin ecosystem, security boundary, signing, and maintenance rather than choosing by trend.