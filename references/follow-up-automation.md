# Follow-Up Automation

Do not create recurring tasks or push notifications unless the user explicitly confirms:

- ASIN list
- Marketplace
- Frequency
- Push channel
- Output format
- Storage location

## Supported Automation Designs

1. Manual review:
   - User provides current data.
   - Compare with the last snapshot.
   - Return a follow-up report in chat.

2. Codex reminder:
   - Wake the task on a schedule.
   - Ask the user to provide or authorize fresh data.
   - Summarize changes.

3. Feishu push:
   - Use only after user confirms bot/chat target.
   - Send short alerts, not full reports.
   - Store full report only after confirmation.

4. GitHub Actions cron:
   - Use if the skill repo contains scripts and allowed credentials.
   - Commit generated snapshots or reports only after the user approves the repository workflow.

## Alert Threshold Examples

- BSR improvement or decline above 30%.
- Monthly units growth above 30%.
- Review velocity change above 30%.
- Coupon/effective price change above 10%.
- New large keyword ad rank or lost major natural rank.
- New suspected offsite signal.
- New promotion or sudden end of promotion.

Thresholds are defaults. Adjust by category volatility.
