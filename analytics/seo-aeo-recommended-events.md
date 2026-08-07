# Recommended conversion-event plan

No analytics script is active in the repository, so this implementation does not add third-party tracking. Connect these events to an approved consent-aware analytics setup when one is selected.

| Event | Trigger | Useful parameters |
| --- | --- | --- |
| `book_discovery_call_click` | Click on the Calendly discovery-call link | `page_path`, `cta_location`, `service` |
| `field_manual_start` | Focus or first interaction with the Field Manual form | `page_path` |
| `field_manual_submit` | Successful Field Manual form submission | `page_path`, `lead_magnet` |
| `service_page_view` | View a service page | `service` |
| `service_related_content_click` | Click on a related resource from a service page | `service`, `destination` |

Respect the existing cookie-consent choices before loading analytics or sending non-essential events. Do not send form values, email addresses, message text, or other personal data as event parameters.
