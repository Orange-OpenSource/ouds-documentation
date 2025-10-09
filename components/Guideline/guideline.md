# Guideline
## Intro
The text area is a multi-line input field that allows users to enter and edit larger amounts of free-form text. It adapts its height to the content and provides visual feedback across multiple states.

## What is It?
A text area is a form component designed for collecting longer textual input from users, such as comments, descriptions, or messages. It supports label, placeholder, helper text, error messaging, and optional helper links.

## Anatomy
Part | Description | Optional
--- | --- | ---
Label | Identifies the purpose of the input field | Optional
Input field | The editable multi-line text box where users type content | Required
Placeholder | Hint text displayed when the field is empty | Optional
Helper text | Guidance or instructions displayed below the input | Optional
Error message | Validation feedback replacing helper text when an error occurs | Optional
Helper link | Actionable text link providing access to additional resources | Optional
Character count | Displays remaining or exceeded character limit | Optional

## Key Features
- **Adaptive height**: Expands from 3 lines to 10 lines as content grows, then activates internal scroll
- **State feedback**: Visual indicators for enabled, hover, focus, loading, read-only, disabled, skeleton, and error states
- **Flexible styling**: Supports outlined and filled variants, with optional rounded corners for brand contexts
- **Comprehensive validation**: Displays error messages, replaces helper text, and indicates character limit violations
- **Accessibility-first**: Proper semantic markup, keyboard navigation, and screen reader support

## When to Use
- Collect long-form user input such as feedback, reviews, or descriptions
- Provide space for multi-paragraph or formatted text entry
- Allow users to compose messages, comments, or notes
- Enable content editing where more than a single line is needed

## When Not to Use
- For short, single-line inputsâ€"use a text input component instead
- When input must follow a strict formatâ€"use constrained fields like date pickers or dropdowns
- For numeric data entryâ€"use number input or stepper components
- When space is extremely limited and multi-line input is not practical

## Common Patterns
**Form feedback**  
Text areas are commonly used in feedback forms, surveys, or support tickets where users provide detailed explanations, comments, or descriptions.

**Content creation**  
In content management systems or social platforms, text areas enable users to compose posts, articles, or bios that require multiple lines and paragraphs.

**Communication interfaces**  
Messaging applications, email clients, and chat interfaces use text areas for composing messages where users need space to express thoughts clearly.