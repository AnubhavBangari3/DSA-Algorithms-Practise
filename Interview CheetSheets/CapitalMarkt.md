# SWIFT / Financial Messaging (Interview Notes)

## What is SWIFT?
SWIFT (Society for Worldwide Interbank Financial Telecommunication) is a global messaging network used by banks and financial institutions to exchange secure and standardized financial messages.

> **Important:** SWIFT only sends messages. It does **not** transfer money or securities. :contentReference[oaicite:0]{index=0}

---

# ISO 15022

## What is it?
ISO 15022 is the older SWIFT messaging standard.

- Uses MT (Message Type) messages.
- Widely used in securities and payments.
- Messages are fixed-format and field-based.

## Examples
- MT103
- MT202
- MT540
- MT548

## Interview Answer
> ISO 15022 is the traditional SWIFT messaging standard that uses MT messages for payments and securities processing.

---

# ISO 20022

## What is it?
ISO 20022 is the newer financial messaging standard.

- XML-based
- More structured
- Supports richer business data
- Replacing many ISO 15022 messages

## Example
- sese.030

## Interview Answer
> ISO 20022 is the next-generation financial messaging standard that provides richer and more structured data than ISO 15022.

---

# SWIFT Message Exchange

## What is it?
It is the process of exchanging financial messages between institutions.

Typical Flow:

Bank A
↓
SWIFT Network
↓
Bank B

Messages exchanged include:
- Payment messages
- Settlement messages
- Confirmation messages
- Status updates

## Interview Answer
> SWIFT Message Exchange is the secure communication process through which banks exchange standardized financial messages.

---

# Settlement Messages

## What are they?
Settlement messages are used during securities settlement.

They instruct:
- Buy securities
- Sell securities
- Receive securities
- Deliver securities
- Settlement status

Most common:
- MT540–MT548

---

# Corporate Action Processing

## What is it?

Corporate actions are events initiated by a company that affect investors.

Examples:
- Dividend
- Bonus Issue
- Stock Split
- Rights Issue
- Merger

Banks exchange SWIFT messages to notify and process these events.

## Interview Answer
> Corporate Action Processing is the handling of events like dividends, stock splits, and mergers using standardized SWIFT messages.

---

# MT530

## Purpose
Settlement Instruction Request

## Used For
Request settlement instructions before settlement.

## Simple Example
A custodian requests settlement details before processing a trade.

## Interview Answer
> MT530 is used to request settlement instructions for a securities transaction.

---

# MT540

## Purpose
Receive Free

## Meaning
Receive securities without payment.

## Example
Free transfer of shares between accounts.

## Money Movement?
❌ No

## Interview Answer
> MT540 is used to receive securities without any cash payment.

---

# MT541

## Purpose
Receive Against Payment (RAP)

## Meaning
Receive securities after making payment.

## Example
Buying shares from another institution.

## Money Movement?
✅ Yes

## Interview Answer
> MT541 is used when securities are received only after payment is made.

---

# MT542

## Purpose
Deliver Free

## Meaning
Deliver securities without payment.

## Example
Gift transfer or internal transfer.

## Money Movement?
❌ No

## Interview Answer
> MT542 delivers securities without exchanging cash.

---

# MT543

## Purpose
Deliver Against Payment (DAP)

## Meaning
Deliver securities after receiving payment.

## Example
Selling securities.

## Money Movement?
✅ Yes

## Interview Answer
> MT543 delivers securities only after payment is received.

---

# MT544

## Purpose
Receive Free Confirmation

## Meaning
Confirms free receipt of securities.

## Interview Answer
> MT544 confirms that securities were successfully received without payment.

---

# MT545

## Purpose
Receive Against Payment Confirmation

## Meaning
Confirms receipt after payment.

## Interview Answer
> MT545 confirms successful receipt of securities against payment.

---

# MT546

## Purpose
Deliver Free Confirmation

## Meaning
Confirms free delivery of securities.

## Interview Answer
> MT546 confirms successful delivery of securities without payment.

---

# MT547

## Purpose
Deliver Against Payment Confirmation

## Meaning
Confirms delivery after payment.

## Interview Answer
> MT547 confirms successful delivery of securities against payment.

---

# MT548

## Purpose
Settlement Status and Processing Advice

## Meaning
Provides settlement status.

## Common Status
- Pending
- Matched
- Settled
- Failed
- Cancelled

## Interview Answer
> MT548 provides the current status of a settlement instruction.

---

# MT596

## Purpose
Statement of Fees

## Meaning
Communicates settlement-related charges and fees.

## Example
Custody fees
Settlement fees

## Interview Answer
> MT596 communicates charges or fees associated with settlement processing.

---

# MT598

## Purpose
Free Format Message

## Meaning
Used for manual communication between institutions.

## Example
Additional settlement instructions
Operational queries
Clarifications

## Interview Answer
> MT598 is a free-format SWIFT message used for operational communication.

---

# MT103

## Purpose
Single Customer Credit Transfer

## Meaning
Transfers money from one customer to another.

## Example
Customer sends ₹1,00,000 internationally.

## Used In
Payments

## Interview Answer
> MT103 is used for international customer-to-customer fund transfers.

---

# MT202

## Purpose
Bank-to-Bank Transfer

## Meaning
Transfers funds between financial institutions.

## Example
Settlement between correspondent banks.

## Used In
Interbank payments

## Interview Answer
> MT202 is used for transferring funds between banks.

---

# ISO 20022 - sese.030

## Purpose
Securities Settlement Transaction Status Advice

## Replaces
MT548 (in many implementations)

## Used For
- Pending
- Matched
- Settled
- Failed
- Cancelled

## Interview Answer
> sese.030 is the ISO 20022 message used to communicate securities settlement status.

---

# Quick MT540–MT548 Summary

| Message | Meaning | Payment? |
|----------|---------|----------|
| MT540 | Receive Free | ❌ |
| MT541 | Receive Against Payment | ✅ |
| MT542 | Deliver Free | ❌ |
| MT543 | Deliver Against Payment | ✅ |
| MT544 | Confirmation - Receive Free | ❌ |
| MT545 | Confirmation - Receive Against Payment | ✅ |
| MT546 | Confirmation - Deliver Free | ❌ |
| MT547 | Confirmation - Deliver Against Payment | ✅ |
| MT548 | Settlement Status | Depends |

---

# ISO 15022 vs ISO 20022

| ISO 15022 | ISO 20022 |
|------------|------------|
| MT Messages | XML Messages |
| Older Standard | New Standard |
| Less Data | Rich Data |
| Field Based | Structured XML |
| Widely Used | Future Standard |

---

# Payment vs Securities Messages

## Payment Messages
- MT103
- MT202

Used for transferring money.

---

## Securities Messages
- MT530
- MT540
- MT541
- MT542
- MT543
- MT544
- MT545
- MT546
- MT547
- MT548
- sese.030

Used for securities settlement.

---

# Interview Tip

If the interviewer asks:

**"Which SWIFT messages have you worked on?"**

You can answer:

> In TCS BaNCS, I worked primarily with securities settlement messages such as MT540–MT548, MT530, MT596, MT598, and payment messages like MT103 and MT202. I also have knowledge of ISO 20022 messages like sese.030 used for settlement status processing. :contentReference[oaicite:1]{index=1}