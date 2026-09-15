# Zeus Permission Model

The Zeus permission model is designed to provide useful automation while maintaining human control over actions that could affect the system.

Zeus should not have unrestricted access to the host system simply because the underlying AI model can generate commands.

## Permission Levels

Zeus will use multiple levels of authorization depending on the potential impact of an action.

### Level 0 — No System Access

The AI can:

* Answer questions
* Analyze information provided by the user
* Generate text
* Explain commands
* Provide recommendations

No system action is performed.

### Level 1 — Safe Automatic Actions

Low-risk actions may be performed automatically.

Examples include:

* Reading non-sensitive system information
* Checking service status
* Checking disk space
* Checking network status
* Analyzing existing logs
* Running predefined diagnostic checks

Zeus should report the result after completing the action.

### Level 2 — Controlled Actions

Actions with a greater potential impact may be permitted when they fall within an explicitly configured set of approved operations.

Examples may include:

* Restarting an approved service
* Running a predefined maintenance task
* Updating a controlled configuration
* Performing an authorized defensive scan

Zeus should log these operations and report what was performed.

### Level 3 — Explicit User Approval

Actions that could significantly modify the system should require confirmation before execution.

Examples include:

* Installing or removing software
* Changing firewall rules
* Modifying important system configuration
* Changing user permissions
* Stopping critical services
* Making significant network changes

Zeus should explain the intended action before requesting approval.

### Level 4 — Restricted or Prohibited Actions

Certain operations should be blocked or restricted regardless of the AI's request.

Examples include:

* Actions outside the authorized environment
* Attempts to bypass Zeus's security controls
* Destructive operations without appropriate authorization
* Access to protected credentials or secrets
* Operations that violate the project's security boundaries

## Permission Flow

The planned permission architecture is:

```text
User Request
     ↓
Zeus
     ↓
Determine Intended Action
     ↓
Risk / Permission Check
     ↓
┌───────────────┬────────────────┬─────────────────┐
│ Safe          │ Approval       │ Restricted      │
│ Automatic     │ Required       │ / Blocked       │
└───────┬───────┴───────┬────────┴────────┬────────┘
        ↓               ↓                 ↓
     Execute         Ask User           Refuse
        ↓               ↓
      Log            Execute if
                     Approved
```

## Principle of Least Privilege

Zeus should receive only the permissions necessary for the task it is performing.

For example, a tool that only needs to inspect logs should not automatically receive permission to modify system files.

Permissions should be granted to individual tools or capabilities rather than treating the entire AI as trusted.

## Logging

System actions performed by Zeus should eventually be recorded.

Logs should provide enough information to determine:

* What action was requested
* What tool was used
* What permission level applied
* Whether approval was required
* Whether the user approved the action
* What result was produced

Logging will help with troubleshooting, auditing, and detecting unexpected behavior.

## Emergency Shutdown

Future versions of Zeus should include a mechanism to immediately disable automated system actions.

The shutdown mechanism should remain available independently of the AI's normal decision-making process.

## Future Development

The permission system will evolve as Zeus gains additional capabilities.

Future components may include:

* Tool-specific permissions
* Command allowlists
* Command validation
* Sandboxed execution
* Filesystem restrictions
* Resource limits
* Approval prompts
* Action logging
* Emergency shutdown
* Separate permissions for the cybersecurity lab environment

The goal is to make Zeus increasingly capable without giving the AI unrestricted control over the system.
