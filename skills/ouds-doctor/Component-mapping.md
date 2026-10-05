---
name: ouds-doctor-component-mapping
description: OUDS components (published keys) and the correspondence of older Orange libraries (One-i, ODS Web / Android / iOS) with OUDS, used by OUDS Doctor to flag non-OUDS and detached components and propose the OUDS replacement.
version: 0.2.0
updated: 2026-10-04
status: draft — to be validated by the OUDS team
---

# OUDS component mapping

Components are identified by their **published component key** (the key an instance points to in any file).
- An instance of an OUDS component still attached to the OUDS library is OK as is: nothing inside it is checked.
- A detached frame keeps the key of the component it came from (`detachedInfo`): flagged, with that component.
- An instance from an older library is flagged; when the table gives an OUDS component, it is proposed with the property correspondence.

Match: **same** · **close** (options differ) · **partial** · **check** (to confirm) · **none** (no OUDS equivalent yet) · **later** (put aside: Headers / Footers being built, native components).

## OUDS components ([OUDS Lib] Components library)

| Component | Key | Status | Variant properties |
|---|---|---|---|
| Accordion list item | `20f527bc8561b29ac1ccb7257ec8f8e92de4f33e` | EA v1.0 | Size:Small/Default; Alignment:Center/Top; State:Enabled/Hover/Focus/Pressed/Disabled/Skeleton; Expanded; Reverse |
| Accordion card item | `7fec7f66ad0c7f4dad94149facacb6fdd8b3b629` | EA v1.0 | Size; Alignment; State; Expanded; Outlined; Rounded corner; Reverse |
| Accordion Q&A | `7f21f76fb4d10ac1d5b959860fb51f5810acb4b5` | EA v1.0 | State; Expanded; Reverse |
| Assistant button | `6b4d8843b009087cedb4de2e0b60d3cbeee54308` | EA v1.1 | Layout:Text + icon/Icon only; Size:Default/Small; State; Rounded corner |
| Assistant icon | `932734c2165741e6fee849d3be8ceaab544af721` | EA v1.0 | State |
| Inline alert | `5c8ea9a59f2fc98fa14d45c105893a42fcb00ae1` | LIVE v1.0 | State:Enabled/Skeleton; Status:Neutral/Accent/Negative/Positive/Info/Warning |
| Alert message | `506707b6311231662528570fef8f442ec48d1ea5` | DEV v1.1.1 / EA v1.2.0 | State; Action layout:None/Trailing/Bottom; Status; Close button; Rounded corner |
| Alert banner | `81d91bfbe9332af25b826a8e265dcc83bf0173cd` | EA v1.0 | Layout:Start/Center |
| Toast | `f45947abac8df620be49d9d5b67ea2cb0bfdd43d` | EA v1.0 | Alignement:Center/Top; State:Enabled/Loading; Action layout; Status; Close button; Rounded corner |
| iOS 26/Tab bar/Tab Bar - iPhone | `6f6b6ddb5fe7b053915a2604d05e7353715ffd7c` | LIVE v1.0 | Separate Search; Minimized; Tabs:2/3/4/5 |
| iOS 26/Tab bar/Tab Bar - iPad | `1a0f478c3fb6bb00acfa1ffee263667511fc05e3` | LIVE v1.0 |  |
| iOS 18/Tab bar/Tab Bar - iPad | `3143fe0decfdd1f51acad98ef198e089a20dfb2a` | LIVE v1.0 | Selected Tab:1-8 |
| iOS 18/Tab bar/Tab Bar - iPhone (Compact Size Class) | `4dfb83b62d64f656e84a5989e224688a93f63298` | LIVE v1.0 | Selected:1-5 |
| iOS 18/Tab bar/Tab Bar - iPhone (Regular Size Class) | `d7e29cc8465c862350bd1d1aae453fa9bf8510ca` | LIVE v1.0 | Selected:1-5 |
| iOS 26/Navigation bar/Toolbar - Top - iPad | `7a4aad1d3564563ed86c5fe50c4180233a8729cb` | LIVE v1.1 | Style; Tab Bar |
| iOS 26/Navigation bar/Toolbar - Top - Sheet | `699aee162b6da4b3d1d8b0084577d88bd0b0f06f` | LIVE v1.1 | Style |
| iOS 26/Navigation bar/Toolbar - Top - iPhone | `ca3ca00bde42849e690493538820a31c105da2fa` | LIVE v1.1 | Style:Default/Compact Large/Large Title/Title 2 Line/Title 2 Line Left |
| iOS 18/Navigation bar/Navigation Bar - iPhone (Compact Size Class) | `f8616d25dba2b374a815fd84a2a1c9c62246b23e` | LIVE v1.1 | Style:Default/Default Modal/Default Modal Stack/Large/Large Modal/Large Modal Stack |
| iOS 18/Navigation bar/Navigation Bar - iPad - Multitasking (Compact Size Class) | `d8cea96c7c781b4cf2aede0ebf39fe35d5098031` | LIVE v1.1 | Style:Default/Large |
| iOS 18/Navigation bar/Navigation Bar - iPad (Regular Size Class) | `38585a87ba611eb41bbf1b6f533dbc99aa10cb08` | LIVE v1.1 | Style; Show Tab bar; Show Home title |
| iOS 26/System bar/Status bar and Menu bar- iPad | `2b7f9cb769ffe7b4806218af14656180655db5fa` | LIVE v1.0 | Type |
| iOS 26/System bar/Status bar - iPhone | `47e14c71556961c4d811f437898e5cc5e09558bc` | LIVE v1.0 | Size |
| iOS 18/System bar/Status Bar - iPhone | `22d39141af27068c9c45237a3e2d421f844b8d9b` | LIVE v1.0 | Background |
| iOS 18/System bar/Status Bar - iPad | `100e61f42fdc9a2ae62517b6f4030bb0dc707534` | LIVE v1.0 | Background; Device |
| iOS 26/System bar/Home Indicator | `247580df254e7520a2da689984c275e5203eda44` | LIVE v1.0 | Device; Orientation |
| iOS 18/System bar/Home Indicator | `eff60dd96ea80d9139da030f9401f982f4ba5ab3` | LIVE v1.0 | Device; Orientation |
| iOS 26/Toolbar/Toolbar - Bottom | `70fb3e2588cbefd8464361e6456bf30f74758eaa` | LIVE v1.0 | Type |
| iOS 18/Toolbar/Toolbar - iPhone | `0df80bb8d037dc334402451234582c75daf065ea` | LIVE v1.0 | Type:Icon/Text; Buttons:2-5 |
| iOS 18/Toolbar/Toolbar - iPad | `45111e709c229bd7c89c31a842020121bbbcb8b3` | LIVE v1.0 | Type; Buttons |
| Material 3/Navigation bar/Navigation Bar: Horizontal items | `1abc062a0f78ad1044b0fde986f7e2ab926c98f8` | LIVE v1.0 | Selected |
| Material 3/Navigation bar/Navigation Bar: Vertical items | `34ebaaf31ff0d5c50e1d1db8a73620fa357f3fbc` | LIVE v1.0 | Selected |
| Material 3/Navigation bar/XR Navigation bar | `1a77acbe3827364a9a54736b0226bdb878df83c9` | LIVE v1.0 | Segments |
| Material 2/Bottom navigation bar | `1ef3c4efa212c8fb131cb6a43ca770d6bfd2e508` | LIVE v1.0 | Selected |
| Material 3/App bar/App bar | `4946c237a3a4afaad98726b66f04ad5e1c2c332b` | LIVE v1.0 | Configuration:Small-centered/Small-image/Search/Small/Medium/Large; Show Background |
| Material 3/App bar/XR App bar | `fb3d6e3e6ba744dd2f10ab71a2878e8fb2deca44` | LIVE v1.0 | Elevation; Configuration |
| Material 3/App bar/Search/Search view full-screen | `7d592abc8954a41399f125a3051ff691ccaa01df` | LIVE v1.0 |  |
| Material 3/App bar/Search/Search view modal | `0156055ec4f5ad5587c6caa4d3d2ac72a11eab50` | LIVE v1.0 |  |
| Material 3/App bar/Search/Search bar | `6d4367eb47d090ddf2c60ff02afd0bb117ee9beb` | LIVE v1.0 | State; Show avatar |
| Material 2/Top app bar | `a8c0affca1fa82a4126fd8d9850624b88289b155` | LIVE v1.0 | Context; Elevation |
| Material 3/System bar/Status bar | `ea5448f1b64b437381f882eb1e0d159f7fe6b38a` | LIVE v1.0 |  |
| Material 2/System bar/Status bar | `0c1c02bcdebfd7e4543937d7e52a524bc082b6ee` | LIVE v1.0 |  |
| Material 3/System bar/Navigation bar: System | `ed1ecb6738a691399441370c38cb447496e02634` | LIVE v1.0 |  |
| Material 2/System bar/System navigation bar | `5d5e91b96f32a1631f6d529de7007ea880f6de22` | LIVE v1.0 | Navigation |
| Material 3/Toolbar/Toolbar: Icon button | `9840ffd48c0d6eb29ae8abbba283dea9b33c8905` | LIVE v1.0 | Configuration; Orientation |
| Material 3/Toolbar/Toolbar: Icon button toggleable | `4182e58b07784aadd61430b6f6063dcd0d46026a` | LIVE v1.0 | Configuration; Orientation |
| Material 3/Toolbar/Toolbar: Button toggleable | `af1bb9d32c0002cc5c9c79c8842ad7589330490e` | LIVE v1.0 | Configuration |
| Material 2/Bottom app bar | `f850c3fc6a9b0e0cd62e2ca5b5eb188e2a39fa9b` | LIVE v1.0 | Version |
| Badge | `998cdefb107bd31a2ad0dc714d3252502c8983fc` | LIVE v1.2 | Status:Neutral/Accent/Positive/Info/Warning/Negative; Size:Xsmall/Small/Medium/Large; State:Enabled/Disabled |
| Badge count | `3035eb38e3425416099eceee96428e83ac6d5c75` | LIVE v1.2 | Status; Size:Medium/Large; State |
| Badge icon | `b76db2425f7e14396ce2692c2d7cef6c78bdd7e1` | LIVE v1.3 | Status; Size:Xsmall/Small/Medium/Large; State |
| Breadcrumb | `f2656ab46d1104d25d7c6f96691b120ed11baf81` | LIVE v1.1 / EA v1.2 | Drilldown:N+1/N+2/N+3/N+4 |
| Bubble | `5b391a0bc20ba0be66e1be3812e5ac5abd9edb4b` | DRAFT |  |
| Bullet list | `e904cfb339cb94d7e2ecb113f945f2d2d310a172` | LIVE v1.1 | Type:Unordered/Ordered/Bare; Text style:Body Large/Body Medium; Nested level:0/1/2; Bold; Skeleton |
| Button | `4616cd237e834c1d101f7e2d603b1196e22168e0` | LIVE v3.2 / DEV v3.3 / EA v3.4 | Appearance:Default/Strong/Brand/Minimal/Negative; Layout:Text only/Text + icon/Icon only; Size:Default/Small; State:Enabled/Hover/Focus/Pressed/Loading/Disabled/Skeleton; Rounded corner |
| Expand button | `8ade9dd01e68221a7b51d5a03a02e7c5985a891b` | DEV v3.2 / EA v3.3 | Appearance:Default/Strong/Brand/Minimal; State; Expanded; Icon only; Rounded corner |
| Navigation button | `2aede5b36a45cbc1075a89b50646813e09e73069` | DEV v3.2 / EA v3.4 | Appearance:Default/Strong/Brand/Minimal; Layout:Next/Previous; State; Icon only; Rounded corner |
| Button - On colored bg | `9d38320f41279f60039ece671436cd50f08d6425` | LIVE v3.2 / EA v3.4 | Appearance:Default/Strong/Minimal; Layout; State; Rounded corner |
| Navigation button - On colored bg | `f59a642f076af8df0f61fe38eb46a651e2b2c2fc` | DEV v3.2 / EA v3.4 | Appearance; Layout:Next/Previous; State; Icon only; Rounded corner |
| Social button | `e06e193a79fc5500663dcfec96345bf2ce378a98` | EA v1.0 | Appearance:Strong/Minimal; Size; State |
| Checkbox | `ea338697133122a7d34438b7b9d4a5a1d2912f9e` | LIVE v2.4 | State:Enabled/Hover/Focus/Pressed/Read only/Disabled/Skeleton; Selection status:Unselected/Selected/Indeterminate; Error |
| Checkbox item | `97b1af5c3b0bb33d4d475c647b73a1878f6e9aba` | LIVE v2.4 | State; Selection status; Error; Reverse |
| Filter chip | `c78b4065ab408717070ff0c5b837daf1fe6c9a6b` | LIVE v1.4 / EA v1.5 | Layout:Text only/Text + Icon/Icon only; Selected; State |
| Suggestion chip | `1c2d8d0a48cdcc17917b712dd369546a61cfedc4` | LIVE v1.4 / EA v1.5 | Layout:Text only/Text + icon/Icon only; State |
| Filter chip expand | `696f52ec183458b99a893a08ef7fe28ae2047ec8` | EA v1.5 | Selected; Expanded; State |
| Divider | `97df65d19cfc1a82123f2f733b7ee2192a8a0517` | LIVE v1.0 | Orientation:Horizontal/Vertical |
| Link | `e252f380dd2aeaa5480cd14caedb6abce2dc03f9` | LIVE v2.2 / EA v2.4 | Layout:Next/Previous/Text only/Text + icon/Visited; Size:Default/Small; Density:Default/Compact; State |
| Link - On colored bg | `ed25f76782737dfc98383fd6ede007b90a13c9e6` | LIVE v2.2 / EA v2.4 | Layout; Size; Density; State |
| Expand link | `4b8049b206e3e650f4d7b0f6de7bae00c8a7941f` | DEV v2.5 / EA v2.5 | Size; Density; State; Expanded; Reverse |
| Expand link - On colored bg | `0aea6daa38c82740c6c043d233920f354b7c1b52` | DEV v2.5 / EA v2.5 | Size; Density; State; Expanded; Reverse |
| Static card item | `5622f51feead0df6fe3220c7cd6f01c8ddf716ec` | DEV v1.0 / EA v1.2 | Size; Alignment; State; Outlined; Rounded corner |
| Static list item | `900d63347f03bf67a962fdd36bf0e7b47debab6f` | DEV v1.0 / EA v1.2 | Size; Alignment; State |
| Navigation list item | `a690c5aaaedd054b01239d5366cf1fb0232b019f` | DEV v1.0 / EA v1.2 | Size; Alignment; State; Layout:Next/Previous |
| Navigation card item | `11a362db1f2d44ad6b1bb28ebbacca089ae7ef23` | DEV v1.0 / EA v1.2 | Size; Alignment; State; Layout; Outlined; Rounded corner |
| Modal dialog | `5b2475bb713d16034cb1b95597424966e53a06ee` | EA v1.0 | Size:Default/Small; Fixed height; Sticky action; Rounded corner |
| Fullscreen dialog | `ca6f0a147433b64ccf07126ce0362d6eeb01c437` | EA v1.0 | Sticky action |
| Backdrop | `9e4b6c47ca1005f9669690b50ac43bba9b00cbbb` | EA v1.0 | Blurred |
| Password input | `6814654f183957dde9dc962bcc8e38a33d80aa63` | LIVE v1.3 / EA v1.3.1 | Input status:Empty/Empty (Placeholder)/Filled; State; Outlined; Rounded corner; Error; Leading icon; Hidden password |
| PIN code input | `6ac1f8729dbc3a0b338104ea0408a4ea40303159` | DEV v1.4 | Length:4/6/8; Outlined; Rounded corner; Error |
| Phone number input | `f04d75f1f79a2adf38de9967c6c086850e53b606` | EA v1.3.1 | Input status; State; Outlined; Rounded corner; Error; Leading icon; Country selector |
| Linear progress indicator | `5d16fb5d2f4f3c7a7cc40be6b64cc7a25c2bf920` | DEV v1.1 | Progress type:Indeterminate/Determinate |
| Circular progress indicator | `70b749264f76fb8dbdd746423896fead5ad02aa0` | DEV v1.2 | Progress type:Indeterminate/Determinate |
| Quantity input | `6fe91b222498e69896fe57161cf8df2a119463d9` | EA v1.3.1 | Actions placement:Trailing/Split; Input status; State |
| Radio button | `5bf03a643607b160de3ca09cc382f8957feebab7` | LIVE v1.4 | State; Selected; Error |
| Radio button item | `75ad0e109874c9c0a88ba1628ab5ab2d0a2d741c` | LIVE v1.4 | State; Selected; Error; Outlined; Reverse |
| Select input | `88df4bc648f4ab21b921c41ca876450abc10f40a` | DEV v1.3 / EA v1.3.1 | Input status:Empty/Filled; State; Outlined; Rounded corner |
| Side sheet | `fecef6b7582132d7517ccf44d62c926cf147cbf9` | EA v1.0 | Size; Placement:Start/End; Sticky action |
| Tag | `b3bb1a621c089f968f0fcb8b5120f3cd0e9573d2` | LIVE v1.5 | Appearance:Muted/Emphasized; Status; Layout:Text only/Text + Bullet/Text + Icon; Size:Default/Small; State; Rounded corner |
| Input tag | `d81fb090c5f52f9e39726da242ebf2522df18f16` | LIVE v1.2 | State |
| Categorical tag | `d9a3e91a4cea407c077ec7153f89259627dc4564` | EA v1.0 | Category:1-5; Layout; Size; State; Rounded corner |
| Skeleton | `4649d35b6a29ecc1d075534036c797a46ce0c507` | LIVE v1.0 | Security margin |
| Switch | `2ee7abc83c95b75ebac37cb0c31d440becb18715` | LIVE v1.5 | State; Selected |
| Switch item | `f4b5f4559a798e651bda21eb96816fbc93caed11` | LIVE v1.5 | State; Selected; Error; Reverse |
| Text area | `be2b4798d601cd9e69ed4fc251dea31164fc6f01` | DEV v1.2 / EA v1.2.1 | Input status; State; Outlined; Rounded corner; Error |
| Text input | `da7d9af1f73f1bba110f73639c0aee74884a0039` | LIVE v1.4 / EA v1.4.1 | Input status; State; Outlined; Rounded corner; Error; Leading icon; Trailing action |
| Display | `6c02c8478e551702c21c7eeee8d36b9ad5508f05` | DEV v1.0 | Size:Large/Medium/Small |
| Heading | `510be83a075eaa6e81d0edd670271c56b3f14230` | DEV v1.1 | Size:Xlarge/Large/Medium/Small |
| Body | `67c713e4f78a5d71beb7ec6ede2d31266be4b309` | DEV v1.0 | Size:Large/Medium/Small; Weight:Default/Moderate/Strong |
| Label | `fa318f62cf05dd9e2d87061e36d7f3a5cd462d9f` | DEV v1.0 | Size:Xlarge/Large/Medium/Small; Weight |
| Code | `5b095ce0d87e15865127c08327231d34ad70ca07` | DEV v1.0 |  |
| Line tabs | `fd68dec05a41b962afd5fcc718c525630e428e14` | Review | Layout; Distribution; Skeleton |

## One-i → OUDS

| Older component | Older keys | OUDS component | Match | Properties / note |
|---|---|---|---|---|
| Accordion | `5d899a0a7d912922de9d210df50b92b751fa8f29` | Accordion list item | close | Folded=True → Expanded=False; Size Standard/Large → Default; Pressed-Touch → Pressed; Background Black → dark mode |
| Badge | `1c40f9b2c698bdb95082bfe34624a284693e1102` | Badge count | check | One-i Badge (Small/Medium/Large) shows a number? → Badge count (Medium/Large); a dot → Badge |
| App Banner | `2ed5ed657a7fb7e2e6e4b944c758cf6f51791b8c` |  | none |  |
| Banner: Smart | `d3e7c04028dfa2b288ff17f679a91c78189e64d8` |  | none |  |
| Bottom sheet | `49d0822b1850ada3715f5acc5dee18d08da5567a` |  | none | OUDS has Side sheet only |
| Breadcrumb | `7df1e5043ca1781ff4201f7395ae05b828a963f6` | Breadcrumb | same | Level N+2/N+3/N+4 → Drilldown N+2/N+3/N+4; N+5 has no OUDS value |
| Bullet list | `fffa7b2a6b8454129036cb99b8eb542325b6d2bd` | Bullet list | close | Version Bullet-point → Type Unordered; Tick → check; Boldness Bold → Bold=True |
| Button | `08cead59bab30ea942a354659aa159087e89b99e` | Button | check | Version Full → Appearance Strong?, Outline → Default?; Pressed-Touch → Pressed; dark / coloured Background → Button - On colored bg |
| Card: Action | `9e5255018d5af33d52e5a2b196a0a1a62c87a442` | Navigation card item | partial |  |
| Card: Select | `4c9461fc7cfee10325b869dcebeedb117ecd39fc` |  | check | selectable card: no OUDS equivalent? |
| Card: Divider | `bf1c17a206aa62ea132c6210829763795f176924` |  | none |  |
| Carousel | `86822e0121f65c9c453c365ce3e40796a7ee1eb9` |  | none |  |
| Product carousel | `d0fb914dd0a830ad52d7f6a0ce9e7ee6bd804460` |  | none |  |
| Bubbles: Message | `a714d26984ab35b7f79573bc68067096ae1e6fa7` | Bubble | close | OUDS Bubble is DRAFT |
| Bubbles: Picture | `f74358bfcee1ba320bd47253c9a8cc4e2ef78bf6` | Bubble | close | OUDS Bubble is DRAFT |
| Chat feed | `53348cf292fcb8fd4bf41c54303bb357835c4407` |  | none |  |
| Chatbot text input (Compact, Regular) | `0d9ef369270b8d3363dadc0eb9e79090bb98a25e` |  | none |  |
| Chatbot text input (Full page integrated) | `90b2d61fbce70093effcef4e209ddde45fb44a55` |  | none |  |
| Chatbot text input (Window) | `a3453e31c27e69caf96cb9525a36fa8829da2f92` |  | none |  |
| FAB - Extra small - Small - Compact - Regular | `ab031f7a8a2826be963f258576608ac89cc55081` | Assistant button | check | chatbot floating button → AI Assistant button (EA)? |
| FAB - Medium - Large - Extra large - XX large | `a88609bf4b6ca7d3819814991292508bc6a53b17` | Assistant button | check |  |
| Quick replies (Redirect to "Chip") | `915aa0604a82a831478626bc697f3f2dc267285c` | Suggestion chip | same |  |
| Checkbox | `1c9c92e742801edf0910caaad64978fde8e1a647` | Checkbox | same | Selection Selected/Not selected/Undetermined → Selection status Selected/Unselected/Indeterminate; Pressed-Touch → Pressed |
| Checkbox list | `423e27718aede999342c770cf34d9c8075b251ef` | Checkbox item | same | Version Left action → Reverse=False, Right action → Reverse=True (check); Selected True/False → Selected/Unselected |
| Chip: Filter | `6f5747629cb8ae2d73c83fa8c58174c64770a10e` | Filter chip | same | Version Text only/Text + Icon/Icon only → Layout |
| Chip: Suggestion | `95113974d8101ed7668684a57817aa3077bcf396` | Suggestion chip | same | Version → Layout; Pressed-Touch → Pressed |
| Chip: Input | `30c3ee707e0c77892f01331ff51834e455868c43` | Input tag | close | Pressed-Touch → Pressed-Touch |
| Color picker |  |  | none |  |
| Content push: Music | `c8ca407ca17773e9b813637810d7594063df7441` |  | none |  |
| Content push: News | `5d74e79902f5532e9fb086340af87f9ce3944163` |  | none |  |
| Content push: Option | `994ee732abfe7e3751dac7511c316fcc18c1d94b` |  | none |  |
| Content push: VOD ranking | `6496a99e88d3fce0b5aab4907ee0625d78f2093d` |  | none |  |
| Content push: VOD-Book | `a11d8d48d2bd0c403ec0d162f4022c4191051c17` |  | none |  |
| Date picker | `08447d438e0a3ae83ef7c6498ec96830d6e4bdfd` |  | none |  |
| Date time picker: Fixed hours | `4173988f7dd2e9e0e0d030aace77a5da3cbba550` |  | none |  |
| Date time picker: Time slots | `ef35954f29d2664a4865452e9577e6aec0de18d7` |  | none |  |
| Divider: 1px (Horizontal) | `1e17c5cb665b979240ea9504e8c2f76d0b97b839` | Divider | same | Orientation=Horizontal; Color → OUDS border tokens (check) |
| Divider: 1px (Vertical) | `3bb9cad91ca4b4c9efc960d49d382e1dc243abc2` | Divider | same | Orientation=Vertical |
| Divider: 15px | `08700b844cb597268e95682976a61d8a87d03bcd` |  | check | section separator: no OUDS equivalent? |
| Dropdown: Select | `09be3fbf9c5be115ddbde1d62c16315dd8605f18` | Select input | close |  |
| Dropdown: Menu | `7f6dd76685a49f94b77415bad23ff4c0b39b4d09` |  | none |  |
| Dropdown: Search | `c1dd8c86033e35826ce5ccde6b038eace0a56522` |  | none |  |
| Dropdown: Loading | `11087a7c0536218a75188a0fd4f53c9a60cce92c` |  | none |  |
| Editorial push | `ab68372f9f16178c512c602505cd61c54aedb7bb` |  | none |  |
| Family avatar | `0c7f01cb1352f13037ffbb7622a633af4f5df676` |  | none |  |
| File Selector | `6c13b150ab2ec9c27dd085d85f1a67bb14b41612` |  | none |  |
| Filter Bar | `0a206050685096f637986a6744cfc0dd7913d0cc` |  | none |  |
| Filter chips bar | `029fd62cb124548af931e6459b918cde3e593e01` | Filter chip | partial | a row of Filter chips |
| Footer | `0a27b17aa5db425f1bd04787cb4abefc5e6c7bb0` |  | later | OUDS Header / Footer being built (Ben, 2026-10-03) |
| Header: Assistance | `192754a9fb9a675ce84e7d11acf89402f66c0dcc` |  | later | OUDS Header / Footer being built (Ben, 2026-10-03) |
| Header: Espace client | `f992a71408687c6b9d87e53f5cdef3309af0abcf` |  | later | OUDS Header / Footer being built (Ben, 2026-10-03) |
| Header: Standard | `6690fa8c402bfe76f79dd4469813385c107c370c` |  | later | OUDS Header / Footer being built (Ben, 2026-10-03) |
| Header: Top level only | `59e357628ebd0d6887aed81de3d6bb533e06933a` |  | later | OUDS Header / Footer being built (Ben, 2026-10-03) |
| In-line alert | `f9942e58863cec1dcf77558a4fa7ab3c8a51e631` | Inline alert | same | Size Standard/Small/Full width → no OUDS size |
| In-line suggestion | `ddb36fc21bd332e035b444a76d168d41dd4a6771` |  | none |  |
| In-page alert | `97b882f9e3f93822864b5b85fd05b2258f9fc0c6` | Alert message | close | Display Page/Modal |
| Legal notice | `5a14f49a50916e77e7bf35dd316ce80d047503d7` |  | none |  |
| Link | `ecd01cff9199cae970a3d787db9edbb462a20c10` | Link | same | Version Next/Back/Text/Icon → Layout Next/Previous/Text only/Text + icon; Folded/Unfolded → Expand link (Expanded False/True); Size Standard → Default; dark Background → Link - On colored bg |
| List item: Standard | `5525954809d05baf20e810d27f011b1ead109987` | Navigation list item | close | Right content Navigation only → Navigation list item; Feedback / Notification → Static list item |
| List item: Chronological order | `aec3f3d19af31d2219ecf8c5f3cc62df815f484e` | Static list item | partial |  |
| List item: Price and document restitution | `bb945cc2ad78a1f28695b6170725d24fdaf7931a` | Static list item | partial |  |
| List item: Status restitution | `8303a6fa22b1ac4af0c4c3543694e41413c0e185` | Static list item | partial |  |
| List item: Network quality | `e45d4ab8ffc21558945f97cab8dbdcd6326c9899` | Static list item | partial |  |
| Loading indicator: Circular | `5bed85e81f45cb273026aed11473c6ab5f421726` | Circular progress indicator | same | Version Determinate/Indeterminate → Progress type |
| Loading indicator: Linear | `9040c3017bd0f87b07265bc812e4fa0782984e2c` | Linear progress indicator | same | Version → Progress type |
| Loading page | `a6666000c3a06b4637fcdc093632321ac9a5356d` |  | none |  |
| Map | `dabb6029ae69f162f4082a1957e42b8a556f72d6` |  | none |  |
| Pin | `25eb51641812b9bbd3ecbea775daced7d0623ad7` |  | none |  |
| Pin group | `4e37f200af32bdff7b269039e7b0e8ecf6656c1a` |  | none |  |
| Pin-search | `3fc386032eb951b1923ea2ace524a7ba3223aec9` |  | none |  |
| Modal dialog | `76e8ca80f08b86fb4cd8e8fb13f61637dbd8c7d4` | Modal dialog | same | Grid → Size Default/Small |
| Bottom navigation bar (Android) | `dbc1e72a67a5c2482ebee7f1a13650a55cdce8db` | Material 3/Navigation bar/Navigation Bar: Horizontal items | close | OS Android → Material 2/Bottom navigation bar; Material You → Material 3 Navigation Bar; Active tab → Selected |
| Top app bar (Android) | `7caf28b0be90e320c4dca99c290db4631863c05d` | Material 3/App bar/App bar | close | OS Android → Material 2/Top app bar; Material You → Material 3 App bar |
| Navigation bar (iOS) | `067489f47556166c8a756111c794891c7b572b84` | iOS 18/Navigation bar/Navigation Bar - iPhone (Compact Size Class) | check | iOS 18 or iOS 26 version?; iPadOS → iPad versions |
| Tab bar (iOS) | `2fcb678748c0d9a660e4a66264479c86042e9414` | iOS 18/Tab bar/Tab Bar - iPhone (Compact Size Class) | check | iOS 18 or iOS 26 version?; Active tab → Selected |
| Onboarding | `8ffe8d8e3c618ba78f1b9fc2b33764b5a07c63cd` |  | none |  |
| Page indicator | `399f8601149dc711041acda28051e93a9c4420a9` |  | none |  |
| Pagination: Compact | `dfb81556d983d633c6f886651c79dd8c8377814d` |  | none |  |
| Pagination: Standard | `7581bb9028bd5c195b56d53c42d2cd575e4c31fc` |  | none |  |
| Price | `ac9ba769400a4df397c52dac1a9e854860ef0eb4` |  | none |  |
| Progress indicator: Step bar | `c3fb4ef2b571fecac2faaed480cc1e09e1369302` |  | none |  |
| Promotional code | `13a3b98fe713421239b47e1d9c94496e9c7fcb9c` |  | none |  |
| Rating | `73b034ed94cfddd2e7be07dff02ad7e580b183ae` |  | none |  |
| Slider | `45fce126b14a1ce617e0f46cbaa3869ede65afdf` |  | none |  |
| Step | `afbd5b19468d28f7b651dea812a30f8612a7f457` |  | none |  |
| Timeline | `96e552b99d8a98aa9c21fef61473ee5017b04f95` |  | none |  |
| Tooltip | `a206f4086551f8465ca64564d3545a5880dd14b8` |  | none |  |
| Tooltip: Onboarding | `d35ed05f87b32d2698898c494e4a044d33f7a3d7` |  | none |  |
| Context reminder | `f4b44613edd5638e1ed77601bf3c839d9667db47` |  | none |  |
| Text input: Search | `60d02ef6f992e22f6c60506204d7017a5a20e6ec` |  | none |  |
| Text input: Machine Readable Zone | `d7a9381b47515fcf0f2bd8efcf02977094feaaa6` |  | none |  |
| Slot component (Black background) | `6ea78a60804887b69a8c02ffd463105787d54c32` |  | none |  |
| Slot component (White background) | `b70a0c2ea3d11ec18c16f8518b4fb4f24deb2ced` |  | none |  |
| Progress indicator: Linear bar | `15afab9ca779e749eb570aae6e9aaa49ea13acb0` `21bed74bd7eb011c5c2a3658611a137e9d776a9a` | Linear progress indicator | close | Steps number Know/Unknow → Progress type Determinate/Indeterminate |
| Radio button | `9566d87293dc226d12347d948211d5af9ec1a218` | Radio button | same | Pressed-Touch → Pressed |
| Radio button list: Standard | `f8c9e71b276042b618347751bca7dcef5ca4c5af` | Radio button item | same | Version Right action → Reverse=True (check) |
| Radio button list: Highlight | `ef8c0966ff68acfa211b0eec183af3f6c5486081` | Radio button item | close | Outlined=True? |
| Radio button list: Price and document selection | `88522c052fd27fe784bffefdd74da23aed55ab80` | Radio button item | partial |  |
| Side sheet | `1fa58b91f570280e739f107005bf17ced4e3ee28` | Side sheet | same |  |
| Skeleton screen | `1d114e293fd1f233111fb8c3615bce91cc339bab` `51453a4cb0c08e62b718f29ca79d2b5d922cd4db` | Skeleton | same | Security margin With/Without → True/False |
| Switch | `8a78104b5aed7dd1bb9246972173084c1c3f129e` | Switch | same | Toggled → Selected; Pressed-Touch → Pressed |
| Switch list | `a12c8c63e7d77cf3b3e9d11b3e4f86cd6af8186f` | Switch item | same | Version Left action → Reverse=True? (OUDS Switch item has the switch at the end); Toggled → Selected; Disabled=True → State Disabled |
| Tabs: Equal distribution | `fbf4abbfa4764d78f96348ee7f0b13ba6f5b0d03` | Line tabs | check | OUDS Tabs still in review; Distribution Justified |
| Tabs: Unequal distribution | `cd9cdbccb2719ebc6d4586602111891f2c5ad3bc` | Line tabs | check | Distribution Left aligned |
| Tag: Status | `f7c1c1c6e533ef6cabbd9762423f365312801942` | Tag | close | Context Positive/Negative/Warning/Information → Status Positive/Negative/Warning/Info; Disabled → State Disabled; Reminder / Used → check; Size Standard → Default |
| Tag: Commercial | `738bd9bb8f9d39fcaec4ef5039222d4e7a4969a2` | Tag | check | Commercial/Subscription → Status Accent?; Unavailable → Disabled?; Information → Info |
| Text area | `001e148f37b010da6e246e10b7c0c65b508cc5d9` | Text area | same | Filled → Input status Filled; Active → Focus; Error → Error=True |
| Text input: Standard | `a4ddaacf7e5fbd5cd68a1b5a39204a97f6187241` | Text input | same | Context Phone number → Phone number input; Active → Focus; Error → Error=True; Filled → Input status |
| Text input: Select | `c61b1d5d56b71bd32e63c84017be48c2593a3267` | Select input | same |  |
| Toast | `403f04210bef07d06148a5a61003e80d9652b4c8` | Toast | same | Action → Action layout |
| 1.Heading 1 | `ae14f501f444f2a7ef07394f4991bbd78ac42455` | Heading | check | Heading 1 → Size Xlarge? (or Display) |
| 2.Heading 2 | `33c0951cab737febc01ae7495707f16d5e064b7d` | Heading | check | → Size Large? |
| 3.Heading 3 | `44a5ce9453ea46396d90b30bc85bf212a7f3ea5d` | Heading | check | → Size Medium? |
| 4.Heading 4 | `072d478f4979bec2a9a2bede41e7c51a79007fec` | Heading | check | → Size Small? |
| 5.Body 1 | `4d38e24545355c9656670e3a5b1350ceac24c880` | Body | check | → Size Large?; 75 Bold → Weight Strong, 55 Roman → Default |
| 6.Body 2 | `d443b1dacf25e9038d7f8a3fc702ac5c01cd3493` | Body | check | → Size Medium? |
| 7.Caption | `96b8d24d974c8e0694f1823046a199ff58372b69` | Label | check | → Label Small or Body Small? |
| 8.Price | `1563eafddb262bb3231d0d472aea5b48db3e6df4` |  | none |  |
| Android/Status bar | `4ce1baf92ad3506cbebe87bde77a2af94379badc` | Material 2/System bar/Status bar | close |  |
| Android/Navigation Bar | `acf6a99833373c4d1e69fd3f057a8ba48c011afe` | Material 2/System bar/System navigation bar | close |  |
| Apple/Status bar | `1ce7553eac630658e6ff07f0c04b379b19eee003` | iOS 18/System bar/Status Bar - iPhone | close |  |
| Apple/Home indicator | `e27b7b5849967c4334dcb9d52989de4796bac37f` | iOS 18/System bar/Home Indicator | close |  |
| Apple/Toolbar | `ca87bb7d3a24b9d39898df84c0948e840848eeaf` | iOS 18/Toolbar/Toolbar - iPhone | close |  |
| Flag (≈250 country flags) | see note |  | same | same country code in the OUDS Flag page (match by name, e.g. "fr" → "fr") |
| Icon (≈410 icons) | see note |  | check | icons live in the OUDS icon libraries ([OUDS Lib] Orange Solaris icons / Themed icons): match by name? |

## ODS Web → OUDS

| Older component | Older keys | OUDS component | Match | Properties / note |
|---|---|---|---|---|
| Accordion | `be929155dd5ce148913fc88ead06f06e03bada7e` | Accordion list item | close | Closed/Open → Expanded False/True; Hover/Focus → State |
| Alerts | `dd1b7b4c9ae2dae699c9e80e1c2a7c8c19bfa568` | Alert message | close | Variants Desktop and Tablet/Mobile → Alert message, Inline → Inline alert, Toast → Toast; State Success/Information/Warning/Error → Status Positive/Info/Warning/Negative |
| Buttons | `a2a0a0d3f358259c40db828423a8df8ed968551a` | Button | close | Emphasis High → Strong, Medium → Default, Low → Minimal, Negative → Negative, Positive → none; Size Large/Medium → Default, Small → Small; State Default → Enabled |
| Cards | `bf5048783e3d6c19286df58194c7a7915fae3bbe` | Static card item | partial | Fill Outlined → Outlined=True |
| Carousel Navigation | `74f4c789af7cb7e123a57966120eb96446ee7ca4` | Navigation button | close | Direction Left/Right → Layout Previous/Next; Icon only=True |
| Checkbox | `fa3fb78818927435a32f382ca74f7e7b1eea19aa` | Checkbox | same | States Unselected/Selected/Intermediate → Selection status Unselected/Selected/Indeterminate; Focus / Disabled → State; Error → Error=True |
| Colour Picker | `0687f500d9a883312726eb46619b8ad8c357a5e0` |  | none |  |
| Country Code Selector (TextField/Top Box) | `407875e90d7d75560747fba462d3b9734bece9d4` | Phone number input | close | Country selector=True |
| Data Tables/Cell Text 1 Line | `90634e1eb85b27117e29b786d691eb0cf1149c67` |  | none |  |
| Data Tables/Cell Text 2 Lines | `797b9ba3a9b33cb5a0e198672e2bb201e978809b` |  | none |  |
| Data Tables/Cell Text 3 Lines | `eae3ea5c7e506939f31e9f18bc803e38b482129c` |  | none |  |
| Data Tables/Column Heading | `2745270cecca64cbb97d0158528c90e6f4c5718c` |  | none |  |
| Data Tables/Column Filter | `a8b2e64d4a285ef11c211b179c406c4cc8ffba91` |  | none |  |
| Data Tables/Checkbox Cell | `d4ae3ee78873ba93da59eb489c48e0106e341cfa` |  | none |  |
| Data Tables/Icon Cell | `38bb815fe4c0eac5f4c370facf25fc22514aaae6` |  | none |  |
| Data Tables/Image Cell | `151a0aaa7ed57539a476f6335f11700dc8e43314` |  | none |  |
| Data Tables/More Button Cell | `ec7790a2e8e565f9765b3133bbced351b256bb6c` |  | none |  |
| Data Tables/Arrow Cell | `9efec85f9ebf0474a4cd6b769f993fd9d4827864` |  | none |  |
| Date Picker | `a6aa6059b8c2a1f1ccb981f514d694c14271a7b1` |  | none |  |
| File input | `1243c135d7062bce45cafba980b0d9e374773152` |  | none |  |
| Global Menu | `45a67ed2467d7a93c0ecba3ceafd162f7dbf9d54` |  | none |  |
| Global Search | `875295ffe33d971cb6c10f737bee88b31b96c20e` |  | none |  |
| Local Header/Title Bar | `c750c3fa1aa89b66df76558e98ff7584dd9a1651` |  | none |  |
| Local Header/Navigation | `2139afbdba6eab8a6aae787edcbcdb787cd67e0b` |  | none |  |
| Pagination | `dd5701187b0d895f780615c9b21b3c8a0a1a0d99` |  | none |  |
| Pagination Dots | `d034b63ce15da2773602c6f1ddbc534cdc339817` |  | none |  |
| Popovers | `9267401535fb22bc94a63437966b9ad89f4d7749` |  | none |  |
| Rating Star | `04a80d9ed99a6e3dec4037dd8ffa437872064a52` |  | none |  |
| Side Navigation | `df6cf368ab0867cf8ec8badd9be53251788aaede` `97f784fc2a847cbf354241690024b9e54088b106` |  | none |  |
| Slider | `44b80a462a115e117bd4d1145b488f9623f36865` |  | none |  |
| Split Buttons | `1eadc40e90b605da02d3d5e0da56d63ff51e8372` |  | none |  |
| Stepped Process | `3d853cfe119f3e955369b586e99b39cdf1c54e63` |  | none |  |
| Stickers | `e4f162c08229656df8bd8259620865770fbeba1d` |  | none |  |
| Story Button | `0e40ab05d6eadd5dda4c262c5bd139e23758a351` |  | none |  |
| Time Picker | `2f5a286f6248b9bda1cf6172ce05bce67d994880` |  | none |  |
| Toggle Buttons | `e9317c4d2df5e63593408d360453de745e757cdc` |  | none |  |
| Tooltip | `f076f5fcc43c092035d6966e806731d85e461f47` |  | none |  |
| Footers | `f0ded844550b0c02da321b41c7e9484bfdf4959b` |  | later | OUDS Header / Footer being built (Ben, 2026-10-03) |
| Global Header/Supra Bar | `7d5c5b901bc854a04b458e3806a79297d74b90c4` |  | later | OUDS Header / Footer being built (Ben, 2026-10-03) |
| Global Header/Navigation Bar | `ea1c33cb6adfa790e597fd99293a85dc6d724e5e` |  | later | OUDS Header / Footer being built (Ben, 2026-10-03) |
| Global Header/Title Bar | `a105970f1700745236b81e69b510bafbd2173d49` |  | later | OUDS Header / Footer being built (Ben, 2026-10-03) |
| Dropdown List | `3bfd69fca99fef33b09e49fb270a6a10e4ead2ae` | Select input | close | Closed/Open → State Enabled/Expanded |
| Icon Button | `b759e940124c65e4bf3364bd1f3d278fe4cb46c3` | Button | close | Layout=Icon only; Styles Outline → Default, No Outline → Minimal; Size Large/Medium → Default, Small → Small |
| List Group | `65fe19aa78a69e4e84f9ca483a45a79484e96fdd` | Static list item | partial |  |
| Local Header/Breadcrumb | `725a8c6b3a635c1aa2719f3d2d540aa7d5994bdd` | Breadcrumb | close |  |
| Modals | `ff6b0491d416d0ebd777fc60fff7c671f13715ac` | Modal dialog | same | Mob Portrait → Small?, Large → Default |
| Pagination Buttons | `e031b958a873d6306ad6beae2759cc54fb2208db` | Navigation button | close | Styles Previous/Next → Layout; Back to Top → none |
| Placeholder | `c738deed89195bf31a91f5da7ad50aaac1c537d3` | Skeleton | close |  |
| Progress Indicators/Spinner | `0f2c8507bce629caf61740490293c7376f332e38` | Circular progress indicator | same |  |
| Progress Indicators/Progress Bar | `4cac9e15ead593e81385ba42b8f30f5f712c2ec8` | Linear progress indicator | same |  |
| Quantity Selector | `10d22e3ac3f2ef360ddf002bf3e65636dd09b374` | Quantity input | same |  |
| Radio Button | `a3f2477af931ab45e3df30f7b6efdf53c00daffe` | Radio button | same | Unselected/Selected → Selected False/True; Focus/Disabled → State; Error → Error=True |
| Social Buttons | `0195d89dd4bec02f9eee10974b006c5306597819` | Social button | same | OUDS Social button is EA |
| Spacers | `e72116cd8e7ed81bfe1abb9ec45f518a965d40b3` |  | none | use OUDS space tokens instead |
| Tabs | `301cf4dfbdb8bcfff848d47bb1130a4e24c53875` | Line tabs | check | OUDS Tabs still in review |
| Tags | `0266346ed6f85e952d88ab9ebf06fe6230cb0a11` | Input tag | check | With Remove Icon → Input tag; Selected states → Filter chip; plain → Tag |
| TextField/Standard | `26c0841db02fc2f74c1ce9ac189c100c9f6bf6b5` | Text input | same | Size Multiple Lines → Text area; Error → Error=True; Active Filled → Input status Filled |
| TextLink | `cb286c58b6483fba1fb0684b2f3738437f230c6b` | Link | same | Size Large/Medium → Default, Small → Small |
| Toggle Switches | `2af584d6832b26b20b2ffc534a183ed048d04c4f` | Switch | same | On/Off → Selected True/False; Disabled / Focus → State |

## ODS Android → OUDS

| Older component | Older keys | OUDS component | Match | Properties / note |
|---|---|---|---|---|
| App bar: tops | `ac5ac8cc555d23087a21038adf71eba665550f39` `997cbe5477b04e0ca7cc7961c0552474b80d1695` | Material 2/Top app bar | close | Style Search → Material 3/App bar/Search/Search bar |
| App bar: bottoms | `de6dd2f91a671b255268776a7fa4c4d7f1e866fe` `4622921e114652e30d9f81490bac1833ffb59e7f` | Material 2/Bottom app bar | same |  |
| System bar | `e26e4ca8b911fde7f385c1b1fad0d5ab424b050b` `8c3deb24cf545535d9ee271fbfff5c74f690f1b1` | Material 2/System bar/Status bar | close |  |
| Backdrop | `d29a78a47840d8691f7c0222ed3288abbf535c9e` | Backdrop | check | Material backdrop vs OUDS modal backdrop: same idea? |
| Banner | `ca998fb7e17b923ae382a30750fd815c98df3487` `bf7eb732b00927081913c94e06ab1e5503807f90` | Alert message | check |  |
| Buttons | `8c34bc5720c71b6a1ea2b35039a7a5d824a629de` `23d5b90b4e71fa7d981db98f6487e986022190a7` `f43d2fa3db0c876d259fedaf6d2650b45063c4dd` | Button | close | Type High Emphasis → Strong, Medium → Default, Low → Minimal, Neutral → Default?, Functional Negative → Negative, Functional Positive → none; also ≈60 single components named "Buttons/<Emphasis>/…" (same rule, matched by name) |
| FAB | `3d6ed9da77e30678b293a594146ed3d438b43914` `a28c15cdb44d4d4d7974976739e2290539d88a16` |  | none |  |
| Cards | `763ba7a2da56232c3e9bd8624a0f3923aa7d105f` `c74a447d05ccbdb84e7261541864478950cf9bdf` | Static card item | partial |  |
| Checkbox | `3b480e23350b0009aa779219eb99ea1214f127f9` `3971a048f55552cf3df6c91b3569e64e3c06061a` | Checkbox | same | Selected On/Off → Selected/Unselected; Focused/Hover/Pressed/Disabled → State |
| Chips | `29fd9f6e15b18e8229da7daaceb5ae799e780663` `e2871accec33c432af06e3f3cde83fc23d634294` | Filter chip | close | Style Filter/Choice → Filter chip, Action → Suggestion chip, Input → Input tag |
| Dialog | `d3dcaaa90113c1307179bececd11f40f2ed1193b` `d4a44e12137806d0f1212260fab5ba579fe70cb0` | Modal dialog | close |  |
| Image lists | `70fbf32897e3b4cf06239f4f5f633d6b0c48ffe2` `a472d1269c849c7d6d790efdeb39ef7427a1379a` |  | none |  |
| List | `0b7255c5a55af1caf843f8949168d95f143451e9` `150a5154590f5d2839b8ab1e58b10e8962165f90` | Static list item | close |  |
| Divider | `3fe314e9e31c7f7a79729fb150f3ba8678ef4b4b` | Divider | same |  |
| Menu | `46e13ed6909202ddb03d634586304b43ba47a32e` `a9d912f1dae5aea3d8bf60335ef48554c54867e8` |  | none |  |
| Bottom nav | `6d40a046ad6cdd76f888e9cc241463d143f0d068` `8cb7cbde297a1b2a71903de985f740fb108cd15e` | Material 2/Bottom navigation bar | same | tabs 3/4/5 |
| Nav drawer | `1200ee57847a5aedb1780c523357bac196d099d7` `131ef6befe07458bb96b99a99474cbbbb36868ce` |  | none |  |
| Page control | `4b10d1a66c702cc2ec63efbf2eb2e713c5c1aeb3` `95de66d594714323ca217e7cd0125dc2c7ae5a6e` |  | none |  |
| Radio button | `424c856d3c7ceb1371f2d9ecce65bbcddb04fac4` `be8d263724633405e472655c2dda22e69fa4ad50` | Radio button | same | Selected On/Off → True/False |
| Progress bar | `71f05192ee490721e62a9e81eeb2ac9d4c631fab` `ac0ce48454f11a9e1020fec59dfb39f9487e65ce` | Linear progress indicator | close | Style Circular → Circular progress indicator, Linear → Linear progress indicator |
| Sheets | `7aa106359eb4d33f50c17f38da11fa5b300cc2f0` `e9e2262278360bb69564a8a7b791470deade2d9c` | Side sheet | partial | Style Side → Side sheet; Bottom → none |
| Slider | `87b047646dd173451cba51240a4abbb6597d80a1` `4a39bab5e28cfcfc14b8f96142b8b17f9ac05a88` |  | none |  |
| Switch | `3ea1f36278593289e3dacd2fe7578e2914f11cc0` `26e79587d24cbab7a3980c34b898d44dfcff9700` | Switch | same | Selected On/Off → True/False |
| Tabs | `0ec489ff14c34618294bf093617ea6f582aa7632` `d05c28ffe1ba2ea38099165570550acdc4d59502` | Line tabs | check | OUDS Tabs still in review |
| Text field | `82ce7c7801352eb559b80c0f31e5f866c8b796b7` `96f7b0661e71e0cf4cd316f53628832f68c3ba66` `937a6aca7bed63d9baf5b57258f5a010cf2589ea` | Text input | same | Alert → Error=True; Focused → Focus; Inactive / Disabled → Disabled |
| Snackbar | `08ebdf6a4160d6e92618881505140436416c4d6a` `99d3c0c4d2956ad85a119729b7a47375fa81b3a7` | Toast | close |  |
| Tooltips | `98ff69659e6d354e2ee5863f935d1eb9be609246` `c371a8c51ad4169adb7eea2b069c9193ad0003d6` |  | none |  |

## ODS iOS → OUDS

| Older component | Older keys | OUDS component | Match | Properties / note |
|---|---|---|---|---|
| Alerts iOS / Actions | `923bc29c1670faa7fcc0cf9b56d34cde87dba408` `4e0a068a57f8a2a9e059cb865e52e16bc1fae2a0` |  | later | native components put aside (Ben, 2026-10-03) |
| Banner | `6c34911568fa336319f2fd5f5260242412577346` `f54759d3e1f250a4bb79198fa9be478a65a8048b` | Alert message | check |  |
| Search bar | `6fd52d274550729a7baeb3e3f1caf4ac1093c2a1` `7ac439051c9f172930db8de2634c06b6e53c4ac7` |  | none |  |
| Navigation Bars | `03dc2bf671be73f8e73c57cf8a5b6a2080a34ed9` `2db400ba40639fcdf5a771dc6b814e357cf311ab` | iOS 18/Navigation bar/Navigation Bar - iPhone (Compact Size Class) | check | iOS 18 or iOS 26?; Title Large → Style Large |
| Control bars / elements | `643cf41b985226663add0f9dc69ac3dd12ffe886` `2957dde5f2a873214f6d3ccc35d78e68071836b7` | iOS 18/Navigation bar/Navigation Bar - iPhone (Compact Size Class) | partial |  |
| Status bar | `f7913e2b3dca766fbba1b85d925f9ddd9b3806c7` `a89c3c1655a167381641e8362367e46fb138825d` | iOS 18/System bar/Status Bar - iPhone | same |  |
| Bars - tab | `24e6a5b5b9d77310b57c31d40f7db8f2911e1139` `0caaa6a0f62499ff8f191c1d22a20acb7b1cfd6e` | iOS 18/Tab bar/Tab Bar - iPhone (Compact Size Class) | check | iOS 18 or iOS 26? |
| Icon button | `1bdb15ed926011fc22e1c21ecd067cab27720fa4` `9bb904f0fe5676859d460e2f38bbbea889c8fd67` | Button | close | Layout=Icon only; Emphasis Lowest → Minimal, Neutral → Default |
| Button | `d1e901df812d7a77745435aeb4d9319c71de69ca` | Button | close | Emphasis High → Strong, Medium → Default, Low/Lowest → Minimal, Negative → Negative, Neutral → Default?, Positive → none; State Default → Enabled |
| Buttons iOS / Apple Pay | `eb75d351a2a4498ec9fda58da3f3093bc79f7ebb` `6c1d4b851684738b9cab7ce814eb38044ddf5478` |  | later | native components put aside (Ben, 2026-10-03) |
| Buttons iOS / Add to Siri | `036b43438dddff27e8a7b81b91410605f2d2dd28` `af41a069b92f1094ba774bc0810f8b1891e88a36` |  | later | native components put aside (Ben, 2026-10-03) |
| Toolbar | `43e639e082033d6c69aca0d707c5af524bcab6fb` `c7512b73c8d8f87eeadd8d4c44392359f7206787` | iOS 18/Toolbar/Toolbar - iPhone | same | Glyphs/Labels → Type Icon/Text |
| Cards (Vertical / Horizontal) | `3d2d20dedcc19eea788725f31067efb7107bb36c` `bd2ac1defcc6c971e2b98c9e9b233a928b0b264b` `f88889196e0fb2d2a8a0dd7ee8aa19392af420c3` `23c78d4ae540b15a13611407ccc72bf9f5705f6e` `64f3a918ad739d911a31a608e601ff3ca84c6210` `dbee08a9b9e89cdf7e6089e0d827628cee94a3e8` `e126da8fb95ac10be47387de3b0834b5b42abdc0` | Static card item | partial | plus ≈20 single card components named "Vertical - …/Horizontal/…" (matched by name) |
| Input Chip | `193f21fab10666fe055777b2af42c832dcb4bcf5` `40e2b007792b7ade734158c687de1a3d074ca9a9` | Input tag | close |  |
| Filter Chip | `9a1acccbc326d85a50a120defbac12ca21179fdc` `46cb552394c285d3b42da798816c8166edafdf78` | Filter chip | same | Selected → Selected=True |
| Choice Chip | `02bd5906e8e1646d6f8039f350c1bb423c584950` `664b369899ecd2e918d7e2c8efb46311ed128e2a` | Filter chip | close |  |
| Action Chip | `20d61f472ca3da792fe38c6b253116c7c2fee256` `a23300eb7237cd6893ad8fe0dcf8c085705af484` | Suggestion chip | close |  |
| Lists | `3853e603a98dc45eb593d286583bc38b41088964` `97e4b1942bff67a8a99b123b30628ed938891cf4` | Navigation list item | close | with Disclosure → Navigation list item; without → Static list item |
| Lists / Action slider | `2b47b30031ff4888764776b7ec4f89888a9a25cd` `2e5df661e145d5fcfbf69a7b491f9c68ae8505a4` |  | none |  |
| Sections / indexes | `d9c36b626e3fffc0e05a1a665bf03be4586ce528` `1f42a5e8a27a2c1c43673af1673a2b76531b2a15` `a7138a8f98e9271cf2d270d613a00bc7e483cb02` `cca2077f446683f843c42a8a509d58aeb05c3c09` `29fa4ad5571ed5a376d280251a4e5b1e86c0c843` `87b1985a1153141c84aeae989d0014e1b59e0aff` |  | none |  |
| Media / Players | `56d1bc3db07564f50b13cff018d9ff6d445b7935` `545e3b4d6be25cddeaf7f72e08ad543b22314108` |  | none |  |
| Pagination / Dots | `22ea30f2845cd7ac1978c19e477835c1463bcf62` `ae635796a38def6074a2b376195f49befbc8f59a` |  | none |  |
| Picker | `99932abea1ae7fccfc60a10c13261312c39a79c0` `8f3eb7b954333bcc59ec4894036a5b5134c84163` `3f0157576202680ca9dafeb94b9022b1cda57bf3` `e5092ce73611634e44dacdba778ed8d227f37e71` |  | none |  |
| Pin_Pad | `f5d648ae35059f8462abe861294908d4ff1b087f` `55a9ceca054587cfb87733414fdaec19fca58904` |  | none |  |
| Transaction | `697f163d9c770c47542d7213146bc16137c55089` `02ce119d9228f8e240216fdc0215a3b8b71a1160` |  | none |  |
| Alerts iOS / Sheet: Actions | `3061bd218a47cf92cc2261e50b8e36821347ad2d` `589061a279eed6a4e2d75af987076aaea7f9af2a` |  | none |  |
| Bottom Sheets | `df4eb2af8f5093518de7196b2c9f0c745a9be4fe` `67857521625bbfcd538887c1a035d9e285a3ea00` |  | none |  |
| Sliders / custom | `cc9381354dca620fc05a9ca12d9693227c18b22b` `071d6cbc14f84e35e4ba6b0c3078a723076fca46` |  | none |  |
| Edit / edit options | `556062d4e706b999d71c5883a5c0af04700a033b` `b0eae0efeab18f824c133fb7fd900f9c6ef17cae` |  | none |  |
| Pin Input Dots | `d05e681f20c5794c8ddc74da1448caba296862f6` `a9b2affaea461bb10869ed0fd04fb580a9ae41df` `aa5cbba5ae3cdfa74cdad24cc779644b1112205d` `5292cb1c1c703aef4983934caa78d5c6246be060` | PIN code input | close | entry 4 → Length 4 |
| Activity indicator | `4f925f52523366777ba2c7d828397fef6b12bfcb` `573414a831b848e8dbefedccaf7f3f47efd6e0a2` | Circular progress indicator | same |  |
| Progress Bar | `8dec7a72d9f919be09666f2b6fe4e48c5f086b14` `2c1b5edd602450afe578f42551aa778e19bd7e4f` | Linear progress indicator | same |  |
| Segmented Control / Tabs | `982c1add2e3d8833178571dfa20b83f109550ff6` `2ed17287b4737d284bc9dcc2c58938c39cf5ac16` |  | check | OUDS Pill tabs (in review)? |
| Edit / text field | `c5a0b6aeed057773bcbda3438e6967ad5e75c204` `58fe4bc319e07945d56b30bb98c24acc48245f2b` | Text input | same |  |
