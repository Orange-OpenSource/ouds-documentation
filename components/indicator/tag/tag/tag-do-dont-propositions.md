# Tag — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([tag.md](tag.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ To display short informational labels such as categories, statuses, or keywords

✅ When content needs to be quickly grouped or identified without interaction

✅ As a visual marker in lists, cards, or filter contexts

✅ When information should be always visible and easy to scan

## Status — do & don't

✅ **Do:** Use semantic colors consistently—green for success, yellow for warning, red for error, and blue for information  
❌ **Don't:** Mix semantic color meanings or use warning colors for positive statuses

✅ **Do:** Always pair functional tags with their dedicated functional icons to reinforce meaning  
❌ **Don't:** Use decorative or unrelated icons with functional status tags

✅ **Do:** Reserve functional tags for system feedback and use neutral/accent for categorization  
❌ **Don't:** Overuse functional colors for non-status information, diluting their semantic value

✅ **Do:** Ensure status colors meet WCAG AA contrast requirements (4.5:1 for text)  
❌ **Don't:** Rely solely on color to convey status—always include text labels and icons

✅ **Do:** Use neutral tags as the default when no specific status needs to be communicated  
❌ **Don't:** Apply accent or functional styling to generic labels that don't warrant attention

## Appearance — do & don't

✅ **Do:** Use emphasized tags for primary status information that requires immediate attention  
❌ **Don't:** Use emphasized appearance for all tags, as it reduces the impact of important ones

✅ **Do:** Apply muted tags for secondary or supplementary information that shouldn't dominate the view  
❌ **Don't:** Use muted tags for critical statuses like errors or warnings that need visibility

✅ **Do:** Create visual hierarchy by combining muted and emphasized tags within the same context  
❌ **Don't:** Mix appearance styles inconsistently without a clear information hierarchy rationale

✅ **Do:** Consider the background surface when choosing appearance to ensure adequate contrast  
❌ **Don't:** Place muted tags on backgrounds where they become difficult to read or distinguish

✅ **Do:** Use emphasized tags sparingly to maintain their visual impact and draw focus effectively  
❌ **Don't:** Default to emphasized appearance when muted would suffice for the content's importance

## Layouts — do & don't

✅ **Do:** Use text-only tags for simple categorization where additional visual cues aren't needed  
❌ **Don't:** Add icons or bullets to tags when they provide no additional meaningful information

✅ **Do:** Use the bullet layout to indicate presence, online status, or activity states  
❌ **Don't:** Use bullets for general categorization where they add no semantic value

✅ **Do:** Choose icons that clearly reinforce the tag's meaning and are universally understood  
❌ **Don't:** Use ambiguous or decorative icons that don't enhance comprehension

✅ **Do:** Maintain consistent layout choices across similar tag types within the same interface  
❌ **Don't:** Randomly alternate between layouts for tags serving the same purpose

✅ **Do:** Position icons before the text label to follow natural left-to-right reading patterns  
❌ **Don't:** Place icons after text or in inconsistent positions across tag instances

## Rounded corner — do & don't

✅ **Do:** Use rounded (pill-shaped) tags for consumer-facing interfaces where approachability matters  
❌ **Don't:** Mix rounded and square tags inconsistently within the same interface context

✅ **Do:** Apply square-cornered tags in formal business contexts like promotions, offers, or legal notices  
❌ **Don't:** Use square tags in casual or consumer applications where rounded shapes fit better

✅ **Do:** Maintain consistent shape choices across all tags within a single product or feature area  
❌ **Don't:** Alternate shapes based on personal preference rather than established design rationale

✅ **Do:** Consider the overall design language when selecting tag shape to ensure visual harmony  
❌ **Don't:** Choose tag shapes that conflict with the established border-radius patterns in your UI

✅ **Do:** Use shape as a secondary differentiator alongside color and content for tag categorization  
❌ **Don't:** Rely solely on shape to distinguish between different tag types or meanings

## Size — do & don't

✅ **Do:** Use default size tags for standalone displays where visibility and readability are priorities  
❌ **Don't:** Use default size tags in dense data tables where they compete with primary content

✅ **Do:** Apply small tags in tables, lists, and compact layouts to maintain visual balance  
❌ **Don't:** Use small tags when they become difficult to read or interact with on mobile devices

✅ **Do:** Maintain consistent sizing within the same component or layout context  
❌ **Don't:** Mix default and small sizes arbitrarily within the same view or data grouping

✅ **Do:** Consider touch target requirements—small tags should still meet minimum accessibility standards  
❌ **Don't:** Reduce tag size below readable thresholds even in space-constrained environments

✅ **Do:** Choose tag size based on the information density and importance of surrounding content  
❌ **Don't:** Default to small size without considering the tag's visibility needs in context
