Progress indicators can use different statuses depending on the meaning of the process they represent. Status colors should communicate the nature of the operation, not its completion percentage.

&nbsp;

### Non-functional
Non-functional statuses are used for standard progress indication without conveying any semantic feedback. They simply communicate that a process is running or progressing.

**`Neutral`** Default status used when progress has no specific semantic meaning. Suitable for generic loading, processing, synchronization, or background tasks where only the completion progress needs to be communicated.

**`Accent`** Used to highlight primary or brand-related actions. Recommended for user-initiated operations such as uploads, downloads, installations, onboarding, or other key experiences where reinforcing the brand identity is appropriate.

&nbsp;

### Functional
Functional statuses communicate additional semantic meaning about the operation being performed. They should only be used when the process itself represents a meaningful system state.

⚠️ Functional statuses must not be communicated by colour alone.

When Positive, Info, Warning or Negative is used, the same meaning must be available through visible text in the parent context and through an accessible status description.

The progress indicator colour communicates the nature of the process, while the text explains the actual state.

**`Negative`** Indicates progress related to an error, recovery, cancellation, or failure. Use only when the progress itself communicates a negative operation, such as rolling back changes, removing content, or recovering from an error.

**`Positive`** Indicates successful progress or a process leading to a successful outcome. Use for confirmation, completed validations, successful synchronization, or other positive system operations.

**`Info`** Indicates informational or system-related processes. Use for background synchronization, data retrieval, initialization, or informational operations that are neither positive nor negative.

**`Warning`** Indicates progress related to an operation that requires user attention or should be monitored. Use when the process involves caution, validation, or potentially disruptive actions.
