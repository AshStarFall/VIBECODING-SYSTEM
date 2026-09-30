# Android and Mobile

- Clarify supported OS/device range, offline behavior, permissions, distribution channel, accessibility, and data synchronization.
- For Android, prefer the existing Kotlin/Compose architecture when present; define navigation, state ownership, persistence, network boundaries, and dependency injection consistently.
- Request platform permissions in context and handle denial/revocation. Minimize sensitive local data and protect exported components/deep links.
- Plan lifecycle, process death, connectivity changes, background limits, localization, and screen-size behavior.
- Test unit and integration behavior plus representative emulator/device flows. Verify install, upgrade, offline/error paths, accessibility, and release signing.
- For store release, verify current target API, policy, data-safety declarations, and signing requirements using official console documentation.

Candidate references include Android's Now in Android, Compose samples, Retrofit/OkHttp, Room, Coil, OWASP MASVS/MASTG, and platform testing docs. Check versions and licenses before selection.